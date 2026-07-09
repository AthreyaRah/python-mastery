HOT = 85
MILD = 50
COLD = 32


def main():
    celsius_temperatures = [-18, 0, 20, 37, 100,True,"Cold"]
    for temp_in_celsius in celsius_temperatures:
        try: 
            temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)
        except TypeError as e:
            print(f"Error: {e} (input was {temp_in_celsius})")
        else:
            category = temperature_category(temp_in_fahrenheit)
            print(f"{temp_in_celsius}°C is {temp_in_fahrenheit}°F and is {category}")


def celsius_to_fahrenheit(temp_in_celsius):
    if isinstance(temp_in_celsius, bool) or not (isinstance(temp_in_celsius, (int, float))):
        raise TypeError("Invalid input for temperature, a numeric value is expected for temperature")
    else:   
        temp_in_fahrenheit = (temp_in_celsius * 9/5) + 32
        return temp_in_fahrenheit
        

def temperature_category(temp_in_fahrenheit):
    if temp_in_fahrenheit > HOT:
        return "Hot"
    elif MILD <= temp_in_fahrenheit <= HOT:
        return "Mild"
    elif COLD <= temp_in_fahrenheit < MILD:
        return "Cold"
    else:
        return "Freezing"


if __name__ == "__main__":
    main()