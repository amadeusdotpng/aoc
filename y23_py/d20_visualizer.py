with open('d20.in') as f:
    inp = [line.split(' -> ') for line in f.read().strip().splitlines()]

modules = {}
mapping = {}
for module, dests in inp:
    dests = dests.split(', ')
    name = module if module == 'broadcast' else module[1:]
    modules[name] = module
    mapping[module] = dests


print('flowchart LR')
for module in modules.values():
    for dest in mapping[module]:
        if dest not in modules:
            print(f'\t{module} --> {dest}')
            continue
        print(f'\t{module} --> {modules[dest]}')

