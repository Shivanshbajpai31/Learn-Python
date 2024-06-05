a=int(input("Enter any valyes between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")


while True:
    b=input(int("Enter any value between 5 and 9 :"))
    if a in ('5','6','7','8','9','QUit','quit'):
        break
    else:
        raise ValueError("Value should be between 5 and 9")