import pdb
import itertools

def str_permutations(strng):

    arr = []
    perm = ''

    return permutations(strng, arr, perm)

def permutations(strng, arr, perm):

    if len(strng) <= 1:
        perm += strng
        arr.append(perm)
        return
    else:

        for i in range(len(strng)):

            remaining_str = strng[:i] + strng[(i+1):]

            permutations(remaining_str, arr, perm + strng[i])

        return arr

print(str_permutations("xyz"))
