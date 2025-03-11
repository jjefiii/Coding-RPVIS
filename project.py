c = float(input("Enter the temperature in Celsius: "))
f = (c - 32) * 5 / 9
f = round(f, 1)
k = 273.5 + ((f - 32.0) * (5.0/9.0))
k = round(k, 1)
print(f"The temperature in Fahrenheit is {f} and in Kelvin is {k}.")