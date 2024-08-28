#Question: Write a for loop to print all numbers from 1 to 10.
#range(start,end,step)

"""for numbers in range(11):
    print(numbers)
"""

"""for numbers in range(2,11):
    print(numbers)
"""

#Question: Write a for loop to calculate the sum of numbers from 1 to 5.
total=0
for i in range(1,6):
    total=total+i # 0+1,1+2,
print(total)


#Question: Write a for loop to print each element of the following list: [10, 20, 30, 40, 50].

l=[10, 20, 30, 40, 50]

for i in l:
    print(i)

l=[10, 20, 30, 40, 50]
l2=[]

for i in l:
    x=i*2
    l2.append(x)
print(l2)


#Question: Write a for loop to print the square of each number from 1 to 5.

for i in range(1,6):
    print(i*i)

#Question: Write a for loop to print the following pattern:
"""
*
**
***
****
*****
"""
"""
1
11
111
1111
"""

for i in range(1,6):
    print("*"*i)


a=10

if a==10:
    if a>7:
        print(a)
    else:
        print("nested if wrong")
else:
    print("wrong")










