
# A Python program to print all
# permutations using library function
from itertools import permutations
from inputs import worlds_number
from inputs import worlds
from inputs import dict_worldsandprob
from canonicalextension import multiplyList

atoms_bac = permutations(worlds)

for i in worlds:
    print(dict_worldsandprob[i])
    





  
    

            

    
