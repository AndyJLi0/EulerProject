import math

def pythagoreanTriplet():
    for x in range(1, 500):
        for y in range(x+1,500):
            if (x > y):
                break
            z = math.sqrt(x**2 + y**2)
            if (x + y + z == 1000):
                return (x,y,z,x*y*z)
            
print(pythagoreanTriplet())