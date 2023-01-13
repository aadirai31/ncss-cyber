from numpy import loadtxt
lines = loadtxt("fusion.txt", delimiter=" ", unpack=False, dtype='str')
print(lines)

for i in lines:
    start = lines[i][0]
    for i in lines:

