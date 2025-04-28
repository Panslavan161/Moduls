from Geometry import celsius_to_fahrenheit
from Geometry import fahrenheit_to_celsius
from Geometry import hours_to_seconds
from Geometry import seconds_to_hours


celsius = 25
fahrenheit = 77
hours = 2
seconds = 7200

print('°F:', celsius_to_fahrenheit(celsius))
print('°C:', fahrenheit_to_celsius(fahrenheit))
print(hours, 'часа =', hours_to_seconds(hours), 'секунд')
print(seconds, 'секунд =', seconds_to_hours(seconds), 'часа')