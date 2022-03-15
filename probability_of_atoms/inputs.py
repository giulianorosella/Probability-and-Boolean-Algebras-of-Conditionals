worlds_number=int(input('Tell me the numbers of atoms of A:'))

worlds = []

worlds_prob = []



for i in range(worlds_number):
        worlds.append((input('Enter atom name: ')))
print('Your initial atoms are:')
print(worlds)


def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 



# Driver program to test above function
print('The atoms of the BAC are: ')
print(permutation(worlds))


for i in worlds:
        worlds_prob.append(float(input('What is the probability of '+str(i)+'? ')))
print(worlds_prob)

dict_worldsandprob = dict(zip(worlds, worlds_prob))

print('The probability of inital atoms are:') 
print(dict_worldsandprob)



