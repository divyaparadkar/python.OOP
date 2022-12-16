#class rectangle

class Rectangle:
    pass
rect1 = Rectangle()
rect2 = Rectangle()

rect1.height = int(input("Enter the height of rect1"))
rect2.height = int(input("Enter the height of rect2"))

rect1.weidth = int(input("Enter the hweidth of rect1"))
rect2.weidth = int (input("Enter the weidth of rect2"))

print(rect1.height * rect2.weidth)
print(rect2.height* rect2.weidth)

