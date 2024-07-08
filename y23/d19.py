from collections import deque, namedtuple
from typing import Dict, List, Tuple


Workflow = namedtuple('workflow', ['rules', 'otherwise'])
Rule = namedtuple('rule', ['part', 'op', 'rhs', 'result'])
Part = namedtuple('part', ['x', 'm', 'a', 's'])

def evaluate(workflows: Dict[str, Workflow], part: Part) -> bool:
    workflow = workflows['in']
    while True:
        result = None

        for rule in workflow.rules:
            match evaluate_rule(rule, part):
                case 'A': return True
                case 'R': return False
                case None: continue
                case res: result = res; break

        if result:
            workflow = workflows[result]
            continue

        match workflow.otherwise:
            case 'A': return True
            case 'R': return False
            case otherwise: workflow = workflows[otherwise]

def evaluate_rule(rule: Rule, part: Part) -> str | None :
    material = getattr(part, rule.part)
    match rule.op:
        case '>': return rule.result if material > rule.rhs else None
        case '<': return rule.result if material < rule.rhs else None

def partA(input: str):
    workflows, parts = input.split('\n\n')
    workflows, parts = workflows.splitlines(), parts.splitlines()

    # Parse Workflows
    workflows_map = {}
    for workflow in workflows:
        name, rules = workflow.split('{')
        rules_map = []
        rules = rules[:-1].split(',')

        for rule in rules[:-1]:
            condition, result = rule.split(':')

            part = condition[0]
            op = condition[1]
            rhs = int(condition[2:])

            rules_map.append(Rule(part, op, rhs, result))

        workflows_map[name] = Workflow(rules_map, rules[-1])

    # Parse Parts
    parts_list = []
    for part in parts:
        materials = part[1:-1].split(',')

        x = int(materials[0][2:])
        m = int(materials[1][2:])
        a = int(materials[2][2:])
        s = int(materials[3][2:])
        
        parts_list.append(Part(x, m, a, s))

    total = 0
    for part in parts_list:
        if evaluate(workflows_map, part):
            total += part.x + part.m + part.a + part.s

    return total

def partB(input: str):
    workflows, parts = input.split('\n\n')
    workflows, parts = workflows.splitlines(), parts.splitlines()

    # Parse Workflows
    workflows_map = {}
    for workflow in workflows:
        name, rules = workflow.split('{')
        rules_map = []
        rules = rules[:-1].split(',')

        for rule in rules[:-1]:
            condition, result = rule.split(':')

            part = condition[0]
            op = condition[1]
            rhs = int(condition[2:])

            rules_map.append(Rule(part, op, rhs, result))

        workflows_map[name] = Workflow(rules_map, rules[-1])

    accepted = set()
    Q = deque([
        ({'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}, 'in')
    ])

    while Q:
        part, name = Q.pop()
        workflow = workflows_map[name]
        for rule in workflow.rules:
            npart = {k: v for k,v in part.items()}

            if rule.op == '>':
                npart[rule.part] = (rule.rhs+1, npart[rule.part][1])
                part[rule.part] = (part[rule.part][0], rule.rhs)
            else:
                npart[rule.part] = (npart[rule.part][0], rule.rhs-1)
                part[rule.part] = (rule.rhs, part[rule.part][1])

            match rule.result:
                case 'A': accepted.add(npart.values())
                case res if res != 'R': Q.append((npart, res))

        match workflow.otherwise:
            case 'A': accepted.add(part.values())
            case res if res != 'R': Q.append((part, res))

    total = 0
    for part in accepted:
        x, m, a, s = part
        total += (
            (abs(x[0]-x[1]) + 1) *
            (abs(m[0]-m[1]) + 1) * 
            (abs(a[0]-a[1]) + 1) * 
            (abs(s[0]-s[1]) + 1)
        )

    return total

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd19.in'
    inp = open(infile).read().strip()
    print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
