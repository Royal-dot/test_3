#Python program to calculate the sum of all numbers from 1 to a given number.
n=int(input("enter a number :"))
sum=0
for x in range(1,n+1):
    sum += x
print("sum of numbers from 1 to",n,"is:",sum)
