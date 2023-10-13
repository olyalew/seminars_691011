# first task
variant = 7
multiplication = variant + 7

i = [12, 24, 36, 48, 109, 187]
result = list(map(lambda x: x * multiplication, i))

print("First Task Result:", result)

# second task
my_phone_number = [8, 9, 1, 5, 4, 5, 5, 5, 0, 0, 5]
other_phone_number = [8, 9, 1, 6, 3, 1, 6, 6, 5, 6, 5]

result = list(map(lambda x, y: x * y, my_phone_number, other_phone_number))
print("Second Task Result:", result)

# third task
my_phone_number = "89154555005"
variant = 7

number_list = [int(digit) * variant for digit in my_phone_number]

even_numbers = list(filter(lambda x: x % 2 == 0, number_list))
odd_numbers = list(filter(lambda x: x % 2 != 0, number_list))

print("Third Task - Четные числа:", even_numbers)
print("Third Task - Нечетные числа:", odd_numbers)

# fourth task
variant = 7

def integer_divide_and_convert(number, variant):
    return int(number) // variant

def float_divide_and_convert(number, variant):
    return float(number) / variant

my_phone_number = "89154555005"

integer_result = list(map(lambda x: integer_divide_and_convert(x, variant), my_phone_number))
print("Fourth Task - Целочисленное деление и преобразование в числовой формат:", integer_result)

float_result = list(map(lambda x: float_divide_and_convert(x, variant), my_phone_number))
print("Fourth Task - Дробное деление и преобразование в числовой формат:", float_result)
