

from functools import cache


def evaluate(reg, regs, conns):
    def ev(r):
        if r in regs:
            return regs[r]

        op, reg_a, reg_b = conns[r]
        match op:
            case 'AND': return ev(reg_a) & ev(reg_b)
            case 'OR' : return ev(reg_a) | ev(reg_b)
            case 'XOR': return ev(reg_a) ^ ev(reg_b)
    return ev(reg)

def partA(inp: str):
    regs_inp, conns_inp = inp.split('\n\n')
    regs_inp = regs_inp.splitlines()
    conns_inp = conns_inp.splitlines()

    regs = {}
    for reg in regs_inp:
        name, value = reg.split(': ')
        regs[name] = int(value)

    z_outs = []
    conns = {}
    for conn in conns_inp:
        exp, out = conn.split(' -> ')
        reg_a, op, reg_b = exp.split()
        conns[out] = (op, reg_a, reg_b)
        if out[0] == 'z':
            z_outs.append(out)


    out = ''
    for z_out in reversed(sorted(z_outs)):
        res = str(evaluate(z_out, regs, conns))
        out+=res

    return int(out, 2)

# z00 = x00 ^ y00 // HA
# c00 = x00 & y00 

# z01 = c00 ^ wsb
# wsb = y01 ^ x01 
# c01 = wsb & c00 | x01 & y01

# z02 = c01 ^ rjt
# rjt = y02 ^ x02
# c02 = rjt & c01 | x02 & y02

# z03 = c02 ^ nbr
# nbr = y03 ^ x03
# c03 = nbr & c02 | x03 & y03

# z09 = bbp & wwg
# bbp = y09 ^ x09
# wwg = qtk | jnq
# qtk = c08       // assuming
# jnq = x08 & y08
# hnd = wwg ^ bbp

# z16 = ncj | pwk
# mqf = x16 ^ y16 
# pwk = x16 & y16
# ncj = mqf & c15

# z23 = x23 & y23 // something ^ something
# mfr = y23 ^ x23
# bks = mfr ^ scw
# scw = rkp | tgj
# rkp = x22 & y22
# tgj = c22       // assuming

# z37 = ghr ^ tjp
# ghr = mdk | cbd
# tjp = x37 & y37
# nrn = x37 ^ y37
def swap_conns(out_a, out_b, conns):
    new_conns = conns.copy()
    new_conns[out_a], new_conns[out_b] = new_conns[out_b], new_conns[out_a] 
    return new_conns

def partB(inp: str):
    regs_inp, conns_inp = inp.split('\n\n')
    regs_inp = regs_inp.splitlines()
    conns_inp = conns_inp.splitlines()

    x_ins = []
    y_ins = []
    regs = {}
    for reg in regs_inp:
        name, value = reg.split(': ')
        regs[name] = int(value)
        if name[0] == 'x':
            x_ins.append(name)
        if name[0] == 'y':
            y_ins.append(name)


    z_outs = []
    conns = {}
    for conn in conns_inp:
        exp, z_out = conn.split(' -> ')
        reg_a, op, reg_b = exp.split()
        conns[z_out] = (op, reg_a, reg_b)
        if z_out[0] == 'z':
            z_outs.append(z_out)

    conns = swap_conns('z09', 'hnd', conns)
    conns = swap_conns('z16', 'tdv', conns)
    conns = swap_conns('z23', 'bks', conns)
    conns = swap_conns('tjp', 'nrn', conns)
    z_out = ''
    for z in reversed(sorted(z_outs)):
        res = str(evaluate(z, regs, conns))
        z_out += res

    x_ins = ''.join(str(regs[x]) for x in reversed(sorted(x_ins)))
    y_ins = ''.join(str(regs[y]) for y in reversed(sorted(y_ins)))
    x_in, y_in = int(x_ins, 2), int(y_ins, 2)
    correct = int(f'{x_in + y_in:b}', 2)
    z_out = int(z_out, 2)

    assert correct == z_out
    return ','.join(sorted(['z09', 'hnd', 'z16', 'tdv', 'z23', 'bks', 'tjp', 'nrn']))
    '''
    print(f'  {x_ins}')
    print(f'+ {y_ins}')
    print(f'-'*15)
    print(f' {correct} correct')
    print(f' {z_out} incorrect')
    print(f' {''.join(reversed([str(i % 10) for i in range(len(z_out))]))}')
    print(f' {''.join(reversed([str(i // 10) for i in range(len(z_out))]))}')
    '''

if __name__ == '__main__':
    import sys

    infile = sys.argv[1] if len(sys.argv) > 1 else 'd24.in'
    inp = open(infile).read().strip()
    # print(f'A: {partA(inp[::])}')
    print(f'B: {partB(inp[::])}')
