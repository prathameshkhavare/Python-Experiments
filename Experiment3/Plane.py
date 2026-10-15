import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def farthest_point(points):
    return max(points, key=lambda p: distance((0, 0), p))

n = int(input("Enter number of points: "))
points = []

for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    points.append((x, y))

print("Points:", points)

if len(points) >= 2:
    print("Enter two points to calculate distance")
    p1_index = int(input("Enter first point number: ")) - 1
    p2_index = int(input("Enter second point number: ")) - 1

    if 0 <= p1_index < n and 0 <= p2_index < n:
        print("Distance:", distance(points[p1_index], points[p2_index]))
    else:
        print("Invalid point number")

if points:
    print("Farthest point from origin:", farthest_point(points))
else:
    print("No points available")