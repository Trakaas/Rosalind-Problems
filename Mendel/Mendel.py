#!/usr/bin/env python3
orgs = input().strip().split()

for x in range(0,3):
    orgs[x]=int(orgs[x])

P_rrrr = (orgs[2] / sum(orgs)) * ((orgs[2]-1) / (sum(orgs)-1))
P_RrRr = (orgs[1] / sum(orgs)) * ((orgs[1]-1) / (sum(orgs)-1)) * (1/4)
P_Rrrr = ((orgs[2] / sum(orgs)) * ((orgs[1]) / (sum(orgs)-1))) #+ ((orgs[1] / sum(orgs)) * ((orgs[2]) / (sum(orgs)-1)))

P_R = 1-P_rrrr - P_RrRr - P_Rrrr#*.5

print('{:4f}'.format(P_R))
