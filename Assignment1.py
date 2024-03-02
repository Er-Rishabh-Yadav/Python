def average_Of_List( list) :
    sum = 0
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        for i in list:
            sum = sum + i
        return sum / len(list)
    

# initial function 
list = [2,4,7,0,3,5,8,1]
print(average_Of_List(list))