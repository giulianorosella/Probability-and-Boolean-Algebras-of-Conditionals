
#A Python program to print all
#permutations using library function
from canonicalextension import atoms_bac, list_prob


result = {}

for i in atoms_bac:
    result[i]=list_prob(i)


print('This is the probability distribution on the atoms of the BAC: ')
print(result)






#da terminale digitare " cat inputs.txt | python main.py "

  
    

            

    
