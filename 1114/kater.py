import math
import pprint
import numpy as np

def devg(dgdt1, dgdt2, devt1, devt2):
    return math.sqrt((((dgdt1**2)*(devt1**2))+((dgdt2**2)*(devt2**2)))**(0.5))

def dgdt1(t,L):
    return (-1)*8*((math.pi)**2)*((2*t*(1+(1/(L[0]-L[1]))))**(-2))

def dgdt2(t,L):
    return (-1)*8*((math.pi)**2)*((2*t*(1-(1/(L[0]-L[1]))))**(-2))

def g(T,L):
    return 8*((math.pi)**2)*((((T[0]**2 + T[1]**2))+((T[0]**2 - T[1]**2)/(L[0]-L[1])))**(-1))

def gbar1(gvalue):
    s = 0
    for x in gvalue:
        s += ((x[0])/(x[1]**2))
    return s

def gbar2(gvalue):
    s = 0
    for x in gvalue:
        s += x[1]**(-2)
    return s

def devgbar(gvalue):
    s = 0
    for x in gvalue:
        s += x[1]**(-2)
    return s**(-1)

def gett(T):
    x = 0
    arr = []
    i = 0
    for i in range(len(T)):
        T[i] /= 15
        
    while(x<len(T)):
        nar = T[x:x+3]
        arr.append([round(sum(nar)/3, 3), round(np.array(nar).std(), 4)])
        x += 3
    print(arr)
    return arr
        

#AZM
L = [[.392,.608],[.426,.574],[.456,.544],[.459,.541],[.472,.528]]

T1 = [24.76,24.89,24.91,25.38,25.40,25.35,25.20,25.29,25.23,25.10,25.17,25.13,25.11,25.19,25.23]
T2 = [26.64,26.57,26.67,26.61,26.63,26.57,25.95,25.95,26.01,25.82,25.79,25.84,25.67,25.70,25.63]

t1 = gett(T1)
t2 = gett(T2)

'''t1 = [[1.657, 0.0043],
[1.692, 0.0012],
[1.683, 0.0025],
[1.675, 0.0021],
[1.678, 0.0033]]

t2 = [[1.775, 0.0029],
[1.773, 0.0017],
[1.731, 0.0019],
[1.721, 0.0016],
[1.711, 0.0016]]'''
#ZSP
'''L = [[.505,.495],[.539,.461],[.554,.446],[.563,.437],[.571,.429]]

t1 = [[1.657, 0.0043],
[1.692, 0.0012],
[1.683, 0.0025],
[1.675, 0.0021],
[1.678, 0.0033]]

t2 = [[1.775, 0.0029],
[1.773, 0.0017],
[1.731, 0.0019],
[1.721, 0.0016],
[1.711, 0.0016]]'''

gvalue = []

for i in range(5):
    gvalue.append([round(g([t1[i][0],t2[i][0]],L[i]),2), round(devg(dgdt1(t1[i][0],L[i]), dgdt2(t2[i][0],L[i]), t1[i][1], t2[i][1]),6)])

pprint.pprint(gvalue)

gbar = (round(gbar1(gvalue)/gbar2(gvalue), 2))

print(gbar, round(math.sqrt(devgbar(gvalue)),8))