import copy

# Shallow Copy

list1 = [1, 2, 3, 4, 'a', 'b']
list2 = list1

list2[2] = 5000

# print(list1, list2)
# -----> [1, 2, 5000, 4, 'a', 'b'] [1, 2, 5000, 4, 'a', 'b']

list3 = [1, 2, 3, 4, 'a', 'b']
list4 = list1.copy()

list4[2] = 5000

# print(list3, list4)
# -----> [1, 2, 3, 4, 'a', 'b'] [1, 2, 5000, 4, 'a', 'b']

#################################################
# Deep Copy

list5 = [[1, 2, 3], [4, 5, 6], 7, 'a', 'b']
list6 = list5.copy()

list6[0][1] = 100

print(list5, list6)
# -----> [[1, 100, 3], [4, 5, 6], 7, 'a', 'b'] [[1, 100, 3], [4, 5, 6], 7, 'a', 'b']


list7 = [[1, 2, 3], [4, 5, 6], 7, 'a', 'b']
list8 = copy.deepcopy(list7)

list8[0][1] = 100

# print(list7, list8)
# -----> [[1, 2, 3], [4, 5, 6], 7, 'a', 'b'] [[1, 100, 3], [4, 5, 6], 7, 'a', 'b']
