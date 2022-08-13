import math

print("Welcome to the paint can calculator!")
print("Figure how many cans of paint you'll need")
height = int(input("How tall is the wall? "))
width = int(input("How wide is the wall? "))


def calculate_paint_cans(h, w):
    cans_needed = (h * w) / 5
    return cans_needed


answer = math.ceil(calculate_paint_cans(height, width))
print(f"You will need {answer} cans of paint.")
