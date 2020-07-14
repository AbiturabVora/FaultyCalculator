def main():
    print("\nWelcome to Casio Calculator")
    num1 = int(input("Enter a number = "))
    num2 = int(input("Enter 2nd number = "))
    operator = input("Select your Operator + - * / \n")
    if num1==56 and num2==9 and operator== "+" :
        print(77)
    elif num1==45 and num2==3 and operator=="*":
        print(555)
    elif num1==56 and num2==6 and operator=="/":
        print(4)
    elif operator=="+":
        print("sum =",num1+num2)
    elif operator == "*":
        print("mul =", num1 * num2)
    elif operator == "/":
        print("div =", num1 / num2)
    elif operator == "-":
        print("sub =", num1 - num2)

while True:
    main()
    if input("Repeat the  program?(Y/N)").strip().upper()!="Y":
        break
print("Thanks for using Calulator")



