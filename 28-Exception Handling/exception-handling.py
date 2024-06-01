a=input("Enter the number:")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i}={int(a)*i}")
except:
    print("Invalid input")

print("End of the program")

try:
    num=int(input("Enter an integer:"))
except:
    print("Number entered is not an integer")