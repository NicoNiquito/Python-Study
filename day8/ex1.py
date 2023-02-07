# Paint calculator
#number of cans = (wall height x wall width) ÷ coverage per can.

import math

def paint_calc(height, width, cover):
    calc = math.ceil((height * width) / cover)
    print(f'A single can of paint can cover {cover} square meters.')
    print(f'For painting a {height}x{width} wall...')
    print(f'You would need {calc} cans of paint.')
 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
