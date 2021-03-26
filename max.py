list=[2,4,6,8,9,13,45]
print(max(list))
print(min(list))










num=int(input("Enter a number:"))
mod=num%2
if mod>0:
    print("this is an odd number.")
else:
    print("This is an even number.")



          

def histrogram(items):
    for n in items:
             output= ''
             times =n
             while(times>0):
                     output+='*'
                     times=times-1
             print(output)
histrogram([4,7,3,9])

