from typing import List

def similarity(set_1, set_2, outfile):
    return

def sum_overlap(set_1,set_2):
    j = 0
    i = 0
    sum = 0
    while i < len(set_1) and j < len(set_2):
        min1, max1 = set_1[i]
        min2, max2 = set_2[j]

        if max2 < min1:
            j += 1

        elif min1 <= min2 <= max1 or min1 <= max2 <= max1 or (min2 < min1 and max2 > max1):
            sum += 1
            i += 1

        else:
            i += 1

    return sum

def small_ls(set_1,set_2):
    return sum_overlap(set_1,set_2) / max (len(set_1), len(set_2))

def big_ls(set_1, set_2):
    return (small_ls(set_1,set_2) + small_ls(set_2, set_1)) / 2   

def read_file(filename):
    lists = []
    with open(filename) as f:
        for line in f:
            lists.append(eval(line))

    return lists
    
def main():
    print("Main function")

if __name__ == '__main__':
    main()