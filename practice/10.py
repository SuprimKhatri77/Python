list = [1,2,3,4,5,6,7,8,7,9,8]

def remove_duplicate_val() :
    for i in list:
        if list.count(i) >= 2:
            print(f"Repated item is: {i}")
remove_duplicate_val()