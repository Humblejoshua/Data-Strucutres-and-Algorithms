def linear_search(array,target):
    for i in range(len(array)):
        if array[i] ==target:
            return i
    return -1

data=[2,5,9,1,2]
target=9
result=linear_search(data,target)    


if result!=-1:
    print("the element is at index",result)
else:
    print("element not found")