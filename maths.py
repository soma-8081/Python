num1=int(input("Enter your first number :"))
num2=int(input("Enter your second number:"))
choice=input("Enter your choice:")
if choice=="+":  
    result=num1+num2
    print(result)
elif choice=="-":
    if num1<num2:
        result=num2-num1
    elif num1==num2:
        result=num2-num1
    elif num1>num2:
        result=num1-num2
    print(result)
elif choice=="*":
    result=num1*num2
    print(result)
elif choice=="/":
    if num1<num2:
        result=num2/num1
    elif num2<num1:
        result=num2/num1
   elif num1==num2:
        result=num1/num2
      
    
    
    

