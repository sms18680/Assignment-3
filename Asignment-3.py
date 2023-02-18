
# Q-1
# write a python function to sum all the numbers in a list
# sample list: (8,2,3,0,7)
# expected output: 20
numbers = [8,2,3,0,7]
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total    
print(sum(numbers))





#Q-2
# write a python program to reverse a string
# sample string:'1234abcd'
#expected output: 'dcba4321.

a=input('enter string')
print(a[-1::-1])

a=input('enter string')
for i in range((len(a)-1,-1-1)):
    print(a[i],end='')










#Q-3
# write a python function that accepts a string and calculate the number of uppercase
# and lower case letter.
# sample string : 'The quick Brow Fox'
#expected output:
# No. of upper case character : 3
# no. of lower case character : 12

str1 = input('enter the string')
LowerC=0
UpperC=0
for character in str1:
    if character.islower():

        LowerC=LowerC+1
    elif character.isupper():
        UpperC=UpperC+1
print('Lower Count:', LowerC)
print('Upper count:', UpperC) 



