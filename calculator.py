def sum(x,y):
    return(x+y)
def substract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y !=0:
        return x /y
    else:
        return "error ! Divison by zero"

print("Select Operator:")
print(" 1. sum ")
print(" 2. substract")
print(" 3. multiply ")
print(" 4. divide")


number = input("enter the choice : 1/2/3/4/5 :")


num1=int(input("Enter the first value:"))
num2 = int(input("Ente the second value:"))
if number == "1":
        print(f"{num1}+{num2}={sum(num1 , num2)}")
elif number == "2":
        print(f"{num1}-{num2}={substract(num1,num2)}")
elif number=="3":
        print(f"{num1}*{num2}={multiply(num1,num2)}")
elif number=="4":
        print(f"{num1}?{num2}={divide(num1,num2)}")
else:
        print("invalid number")

    
    
 


