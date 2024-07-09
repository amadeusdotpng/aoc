from collections import deque
from dataclasses import dataclass
from typing import List, Dict, Tuple
from math import lcm

@dataclass
class FlipFlop:
    state: bool
    dests: List[str]

    def flip(self):
        self.state = not self.state

@dataclass
class Conjunction:
    inputs: Dict[str, bool]
    dests: List[str]

    def remember(self, name: str, power: bool):
        self.inputs[name] = power

@dataclass
class Broadcaster:
    dests: List[str]

type Module = FlipFlop | Conjunction | Broadcaster

@dataclass
class Pulse:
    power: bool
    from_module: str
    dest_module: str

    def __repr__(self):
        return f'{self.from_module} -{'high' if self.power else 'low'}-> {self.dest_module}'

def parse_modules(inp: str) -> Tuple[Dict[str, Module], Dict[str, List[str]]]:
    inp = [line.split(' -> ') for line in inp.splitlines()]
        
    modules: Dict[str, Module] = {}
    inputs: Dict[str, List[str]] = {}
    for module, dests in inp:
        dests = dests.split(', ')

        module_type, module_name = ('B', module) if module == 'broadcaster' else (module[0], module[1:])

        for dest in dests:
            if dest not in inputs:
                inputs[dest] = []

            inputs[dest].append(module_name)

        match module_type:
            case '%': modules[module_name] = FlipFlop(False, dests)
            case '&': modules[module_name] = Conjunction(None, dests)
            case 'B': modules[module_name] = Broadcaster(dests)

    for k, v in modules.items():
        match v:
            case Conjunction(): v.inputs = {name: False for name in inputs[k]}

    return modules, inputs

def press_button(modules: Dict[str, Module], step: int, cycles: Dict[str, int] = None) -> Tuple[int, int]:
    instructions = deque()
    instructions.append(Pulse(False, 'button', 'broadcaster'))

    pulses = [0, 0]
    
    while instructions:
        P: Pulse = instructions.popleft()
        pulses[P.power] += 1

        curr_module = P.dest_module
        if curr_module not in modules:
            continue

        M = modules[curr_module]

        match (M, P.power):
            case (Broadcaster(), power):
                for dest in M.dests:
                    instructions.append(Pulse(power, curr_module, dest))

            case (FlipFlop(), False):
                M.flip()
                for dest in M.dests:
                    instructions.append(Pulse(M.state, curr_module, dest))

            case (Conjunction(), power):
                M.remember(P.from_module, power)
                send_power = False if all(power for power in M.inputs.values()) else True

                if (cycles is not None
                and curr_module in cycles
                and cycles[curr_module] == 0
                and send_power
                ):
                    cycles[curr_module] = step

                for dest in M.dests:
                    instructions.append(Pulse(send_power, curr_module, dest))

    return pulses

def partA(inp: str):
    modules, _ = parse_modules(inp)

    total_lo = 0
    total_hi = 0
    for step in range(1000):
        lo, hi = press_button(modules, step)
        total_lo += lo
        total_hi += hi

    return total_lo * total_hi

def partB(inp: str):
    modules, inputs = parse_modules(inp)

    cycles = {k: 0 for k in inputs[inputs['rx'][0]]}

    step = 0
    while True:
        step += 1
        press_button(modules, step, cycles)

        if all(cycle_length for cycle_length in cycles.values()):
            return lcm(*cycles.values())

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd20.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
