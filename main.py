
#A Python program to print all
#permutations using library function
from canonicalextension import atoms_bac, atoms_below, list_prob

bc_in_question = (list(input('I want to find the atoms below and the probability of the basic conditional whose consequent is: ')), list(input('and whose antecedent is: ')))

print(bc_in_question)

print('The atoms below are: ')
print(atoms_below(bc_in_question))

prob_below = []
for i in atoms_below(bc_in_question):
    prob_below.append(list_prob(i))

print('Its probability is: ')
print(sum(prob_below))



#da terminale digitare " cat inputs.txt | python main.py "

  
    

            

    
