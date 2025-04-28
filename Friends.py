from Geometry import celsius_to_fahrenheit
from Geometry import fahrenheit_to_celsius
from Geometry import hours_to_seconds
from Geometry import seconds_to_hours
from goida import factorial
from goida import generate_random_number



celsius = 15
fahrenheit = 59
hours = 5
seconds = 18000
number_for_factorial = 5
random_start, random_end = 10, 20

print("\n=== Конвертация температур ===")
print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")

print("\n=== Конвертация времени ===")
print(f"{hours} часа = {hours_to_seconds(hours)} секунд")
print(f"{seconds} секунд = {seconds_to_hours(seconds)} часа")

print("\n=== Математические операции ===")
print(f"Факториал {number_for_factorial} = {factorial(number_for_factorial)}")
print(f"Случайное число от {random_start} до {random_end}: {generate_random_number(random_start, random_end)}")

