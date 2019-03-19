def minimum_waste(bottles, potion):
    # sort from greatest to least
    bottles.sort(reverse = True)
    w = float("inf")

    recurse_minimum_waste(w, bottles, potion, bottles[0])



def recurse_minimum_waste(w, bottles, potion, current_bottle):

    # base case
    if potion < current_bottle:

        if w > (current_bottle - potion):
            w = current_bottle - potion
            print('w is now', w)

        return

    # recurse case
    else:
        for i in range(len(bottles)):

            recurse_minimum_waste(w, bottles[i:], potion - bottles[i], bottles[i])
            print('w is now...', w)



minimum_waste([30, 20, 70, 100], 175)
