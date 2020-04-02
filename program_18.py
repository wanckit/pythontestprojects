item_catalog = {"Blank CD's":7.99,"USB Drivers":12.50, "Keyboard":18.00}

for x in item_catalog:
    print x

def exists_in(A, name):
    result = False
    for y in A:
        if y == name:
            result = True
    return result

print exists_in(item_catalog,"Keyboard")
            
        
        

