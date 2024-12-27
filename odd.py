#Python program to calculate the sum of all the odd numbers within the given range.
a=int(input("enter the number:"))
sum=0
for x in range(1,a+1):
    if x%2!=0:
        sum+=x
        print(sum)

