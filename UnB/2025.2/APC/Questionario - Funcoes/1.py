def fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit 

def kelvin(celsius):
    kelvin = celsius + 273.15 
    return kelvin

temperatura = int(''.join(filter(str.isdigit, input())))
print(fahrenheit(temperatura))
temperatura = int(''.join(filter(str.isdigit, input())))
print(kelvin(temperatura))