# Your code here
def powerSet(items):
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 3 == 0:
                combo1.append(items[j])
                combo2.append(items[j])
            elif (1 >> j) % 3 == 1:
                combo1.append(items[j])
            else:
                combo2.append(items[j])
        yield (combo1, combo2)
