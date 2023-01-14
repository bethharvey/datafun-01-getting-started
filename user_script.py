"""
Complete the script.
"""
# Domain: Birds
# Part 1
temp_1 = float(input('Enter a temperature in Celsius: '))
temp_2 = float(input('Enter a second temperature in Celsius: '))
temp_3 = float(input('Enter a third temperature in Celsius: '))
print()

# Part 2
temp_sum = round(temp_1 + temp_2 + temp_3, 2)
print(f'The sum of the temperatures is {temp_sum}.')
temp_avg = round(temp_sum / 3, 2)
print(f'The average of the temperatures is {temp_avg}.')
temp_prod = round(temp_1 * temp_2 * temp_3, 2)
print(f'The product of all three temperatures is {temp_prod}.')
temp_min = min(temp_1, temp_2, temp_3)
print(f'The lowest of the three temperatures is {temp_min}.')
temp_max = max(temp_1, temp_2, temp_3)
print(f'The highest of the three temperatures is {temp_max}.')
temp_range = round(temp_max - temp_min, 2)
print(f'The the range of the three temperatures is {temp_range}.')
print()

# Part 3
if temp_3 < 0:
    print('The water in the bird bath is frozen!')

if temp_3 == 0:
    print('The water in the bird bath is freezing!')

if temp_3 > 0:
    print('The water in the bird bath is fine!')