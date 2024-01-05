import math

# Prompt the user to enter the radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume and surface area
volume = (4/3) * math.pi * radius**3
surface_area = 4 * math.pi * radius**2

# Display the results
print(f"The volume of the sphere is {volume:.2f} cubic units.")
print(f"The surface area of the sphere is {surface_area:.2f} square units.")