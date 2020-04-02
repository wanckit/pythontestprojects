list1 = [2,4,6,8]
list2 = [2,4,6,8,10]

def listItems(A):
    listSum = 0
    for x in range(0, len(A)):
        listSum = listSum + A[x]
    return listSum

#print listItems(list2) 
