
#A Python program to print all
#permutations using library function
from canonicalextension import atoms_bac, list_prob


result = {}

for i in range(len(atoms_bac)):
    result[atoms_bac[i]]=list_prob(atoms_bac[i])

print(result)






#da terminale digitare " cat inputs.txt | python main.py "

  
    

            

    
