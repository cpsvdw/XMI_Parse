arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
arr2 = [1, 33, 4, 56, 2, 55, 4, 56, 66, 5]

set_1 = set(arr1)
set_2 = set(arr2)

def sim2():
    similarity = len(set_1.intersection(set_2)) / len(set_1) * 100
    print(f'The similarity is: {similarity}%')
