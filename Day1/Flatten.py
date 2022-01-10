def flatten(list):
    length = len(list)
    for i in range(length):
        for j in list[0]:
            # append element at last
            list.append(j)
        # delete the sublist    
        del list[0]
    return list 

# passing below 2d list in the function
mylist = [[1], [2, 3], [4, 5, 6, 7]]
flatten_list = flatten(mylist)
print(flatten_list)