import numpy as np
decryption_key = 811589153
input = [int(line.strip())*decryption_key for line in open(0).readlines()]
# Index list, this is what will be moved around
L = [i for i in range(len(input))]                     
D = {}

# Create dictionary of how the indexes will be moved around
for index, n in enumerate(input):
    D[index] = n
# Iterate through each index in order. Move the indices around in L based on D
for i in range(10):
    for OG_INDEX in D:
        new_index = L.index(OG_INDEX)
        val = D[OG_INDEX]
        to_index = val + new_index
        L = L[:new_index] + L[new_index+1:]
        # print(L)
        if to_index == 0 and val != 0:
            L.insert(len(L), OG_INDEX)
        else:
            L.insert(to_index%(len(L)), OG_INDEX)

new_L = [D[n] for n in L]
# print(new_L)
zero_index = new_L.index(0)
sum = new_L[(zero_index+1000)%len(new_L)] + new_L[(zero_index+2000)%len(new_L)] + new_L[(zero_index+3000)%len(new_L)]
print(sum)


