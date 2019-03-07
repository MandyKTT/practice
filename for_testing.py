#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)


for value in range(1,5):
    print(value)


numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares=[value**2 for value in range(1,11)]
print(squares)

players=['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:" )
for player in players[:3]:
    print(player.title())

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)"""

dimensions=(200,50)
print("Original dimensiona:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)



