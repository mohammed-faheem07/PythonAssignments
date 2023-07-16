#Task 1: Python program which accepts the radius of a circle from the user and computes area. 
PI = 3.14
rad = float(input("Input the radius of the circle: "))
area = PI*rad*rad
print("The area of the circle with radius",rad ,"is:",area)


#Task 2: Python program to accept a filename from the user and print the extension of that.
filename = input("Input the filename: ")
extension = filename.split(".")
print("The extension of the file is:",extension[-1])
