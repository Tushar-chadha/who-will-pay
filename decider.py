import random

names_Strin=input('enter names that will be shuffled with a .')
names= names_Strin.split(',')

len_num= len(names) 
#to get the length of names list
print(len_num)

randomChoice= random.randint(0,len_num)

payer=names[randomChoice]
print(payer + " is going to buy the meal today!")