from itertools import permutations
from inputs import worlds_number
from inputs import worlds
from inputs import dict_worldsandprob


atoms_bac = list(permutations(worlds))


def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     



def list_prob(lst):
    prob_list = []
    for i in lst:
        if lst.index(i) == 0:
            prob_list.append(dict_worldsandprob[i])
        if lst.index(i) != 0:
            prec = []
            prob_elements_denom = []
            for h in lst:
                if lst.index(h) < lst.index(i):
                    prec.append(h)
            for j in lst:
                if j not in prec:
                    prob_elements_denom.append(dict_worldsandprob[j])
            print(prob_elements_denom)
            prob_list.append(float(dict_worldsandprob[i]/sum(prob_elements_denom)))
    return prob_list

list_prob(atoms_bac[1])

#for i in permutations(worlds):
 #   print(list_prob(i))