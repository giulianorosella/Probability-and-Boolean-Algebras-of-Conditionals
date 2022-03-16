
#A Python program to print all
#permutations using library function
from canonicalextension import atoms_bac, atoms_below, list_prob, box, belief
from inputs import all_basic_conditionals





bc_in_question = (list(input('I want to find the atoms below and the probability of the basic conditional whose consequent is: ')), list(input('and whose antecedent is: ')))

print(bc_in_question)

print('The atoms below are: ')
print(atoms_below(bc_in_question))

print('Its Box is: ')
print(box(bc_in_question))

prob_below = []
for i in atoms_below(bc_in_question):
    prob_below.append(list_prob(i))

print('Its probability is: ')
print(sum(prob_below))

print('Its belief is: ')
print(belief(all_basic_conditionals[2]))



counterfactuals = []
for i in all_basic_conditionals:
    counterfactuals.append(box(i))
    print('The box of ' +str(i)+ ' is: ')
    print(box(i))








#da terminale digitare " cat inputs.txt | python main.py "

  
    

            

    
