# in foll. self is the actual object point which I have created
# init is a function

class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y

p = Point(3 , 5)
print(p.x)
print(p.y)


#Output
# 3
# 5
