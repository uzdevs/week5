def division(a, b):
    try:
        if type(a) ==str or type(b)==str:
            return int(a)/int(b)
        return a/b
    except ZeroDivisionError as zde:
        # print(zde)
        return f"You can not delete the number to zero"

    except:
        return f"Please check input"
    
    
    

# def division2(a, b):
#     if type(a) ==str or type(b)==str:
#         return int(a)/int(b)
#     return a/b

# Testing your code
print(division(45,90))
print(division(-45,0))
print(division('45',90))
print(division('45','90'))
print(division('45',90))
print(division('john', 'doe'))

