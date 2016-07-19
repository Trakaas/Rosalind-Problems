<<<<<<< HEAD
#!/usr/bin/env python3
orgs = input().strip().split()

for x in range(0,3):
    orgs[x]=int(orgs[x])

P_rrrr = (orgs[2] / sum(orgs)) * ((orgs[2]-1) / (sum(orgs)-1))
P_RrRr = (orgs[1] / sum(orgs)) * ((orgs[1]-1) / (sum(orgs)-1)) * (1/4)
P_Rrrr = ((orgs[2] / sum(orgs)) * ((orgs[1]) / (sum(orgs)-1))) #+ ((orgs[1] / sum(orgs)) * ((orgs[2]) / (sum(orgs)-1)))

P_R = 1-P_rrrr - P_RrRr - P_Rrrr#*.5

print('{:4f}'.format(P_R))
=======
#!/usr/bin/env python3
orgs = input().strip().split()

for x in range(0,3):
    orgs[x]=int(orgs[x])

P_rrrr = (orgs[2] / sum(orgs)) * ((orgs[2]-1) / (sum(orgs)-1))
P_RrRr = (orgs[1] / sum(orgs)) * ((orgs[1]-1) / (sum(orgs)-1)) * (1/4)
P_Rrrr = ((orgs[2] / sum(orgs)) * ((orgs[1]) / (sum(orgs)-1))) #+ ((orgs[1] / sum(orgs)) * ((orgs[2]) / (sum(orgs)-1)))

P_R = 1-P_rrrr - P_RrRr - P_Rrrr#*.5

print('{:4f}'.format(P_R))
>>>>>>> abfe9e0c9413d6f3f3d7498ab1b806d822fb81f8
