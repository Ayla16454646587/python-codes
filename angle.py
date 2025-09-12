import math
angle_degrees=float(input("Enter the angle in degrees:"))

angle_radians=math.radians(angle_degrees)

sine=math.sin(angle_radians)
consine=math.cos(angle_radians)
tangent=math.tan(angle_radians)

print(f"sin({angle_degrees})={sine}")
print(f"cos({angle_degrees})={consine}")
print(f"tan({angle_degrees})={tangent}")