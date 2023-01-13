import math
def my_function(CHP, MHP, CR):
    CV = ((3*MHP-2*CHP)/(3*MHP))*CR

    A = math.sqrt(math.sqrt(16711680/CV))

    CP = (16/A)**4
    NCP = 1 - CP
    return NCP


a = my_function(61, 108, 235)
b = my_function(79, 133, 120)
c = my_function(56, 70, 90)
d = my_function(27, 89, 45)
e = my_function(12, 53, 190)
f = my_function(28, 157, 45)
g = my_function(59, 64, 190)
h = my_function(39, 70, 225)
i = my_function(41, 63, 190)
j = my_function(66, 66, 45)
k = my_function(130, 142, 45)

z = a*b*c*d*e*f*g*h*i*j*k

print(1 - z)

