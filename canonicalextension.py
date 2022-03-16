from itertools import permutations
from inputs import worlds, dict_worldsandprob, all_the_successors, access, all_basic_conditionals



atoms_bac = list(permutations(worlds))


def multiplyList(myList) :
     
    # Multiply elements of myList one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     



def list_prob(lst):
    prob_list = []
    for i in lst:
        if lst.index(i) == 0:
            prob_list.append(float(dict_worldsandprob[i]))
        if lst.index(i) != 0:
            prec = []
            prob_elements_denom = []
            for h in lst:
                if lst.index(h) < lst.index(i):
                    prec.append(h)
            for j in lst:
                if j not in prec:
                    prob_elements_denom.append(dict_worldsandprob[j])
            #print(prob_elements_denom)
            prob_list.append(float(dict_worldsandprob[i]/sum(prob_elements_denom)))
    return multiplyList(prob_list)



result = {}

for i in atoms_bac:
    result[i]=list_prob(i)


print('This is the probability distribution on the atoms of the BAC: ')
print(result)


def atoms_below(tup):
    big_truthmakers = []
    big_falsemakers = []
    for i in atoms_bac:
        small_truthmakers = []
        small_falsemakers = []
        for j in i:
            if j in tup[1]:
                small_truthmakers.append(j)
            else:
                small_falsemakers.append(j)
        if small_truthmakers[0] in tup[0]:
            big_truthmakers.append(i)
        else:
            big_falsemakers.append(i)
    #print(big_truthmakers)
    return big_truthmakers


def box(lst):
    Box = []
    for i in atoms_bac:
        if ((len(access(list(i))[1]) > 0) and ([x for x in atoms_below(lst) if x in access(list(i))[1]] == access(list(i))[1])):
            Box.append(i)
        if len(access(list(i))[1]) == 0:
            Box.append(i)
    return Box


def belief(counter):
    result = []
    for i in box(counter):
        result.append(list_prob(i))
    return sum(result)




