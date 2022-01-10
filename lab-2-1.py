# Yongdong Xi
def double_stuff(lst):
    for index, value in enumerate(lst):
        print(lst[index])
        lst[index] = (2 * value)
        print(lst[index])
    return lst
    


lst1 = [1, 2, 3, 4, 5, 6, 7]
print(double_stuff([1, 2, 3, 4, 5, 6, 7]))


#res = []
    #for x in lst:
        #res.append(x + x)
    #print(res)

