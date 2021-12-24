'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. Those two number will be the base and height of a triangle. 
The program will then output the area of that triangle. (Reminder: the area of a triangle can be calculated by (base * height)/2 ).

What should appear on the console when this code runs:

Enter the base: 8
Enter the height: 3
The area of the triangle is 12.0

'''

#I prefer functions
def calculateTriangleArea(triangleBase, triangleAlt):
  #triangleBase = int(input("Enter the base: "))
  #triangleAlt = int(input("Enter the height: "))
  triangleArea = (triangleBase * triangleAlt) / 2
  print(triangleArea)
  return triangleArea
calculateTriangleArea(14, 3)




#Simpler code
triangleBase = int(input("Enter the base: "))
triangleAlt = int(input("Enter the height: "))
print((triangleBase * triangleAlt) / 2)
