data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]

def flatten(data):
    st = []
    print(data)
    for ind, lst in enumerate(data):
        if type(lst) == type(data):
            data += flatten(lst)
            
            print(data)
        # else:
            # data += flatten(lst)
    for ind, lst in enumerate(data):
        if type(lst) == type(data):
            data.remove(data[ind])
    # data.append(int(st))
    
    # print(data)
    return data

flatten(data)
print(f'itogo: {data}')
# c=[]
# a=[1,3,6]
# b=[2,4,8]
# # a.insert(2,b)
# c=a+b
# print(c)
