import tkinter as tk
from tkinter import simpledialog, messagebox

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def temperature_converter():
    root = tk.Tk()
    root.withdraw()

    options = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = simpledialog.askstring("Temperature Converter", f"Convert from ({', '.join(options)}):")
    if from_unit is None:
        return
    to_unit = simpledialog.askstring("Temperature Converter", f"Convert to ({', '.join(options)}):")
    if to_unit is None:
        return
    temp_str = simpledialog.askstring("Temperature Converter", f"Enter temperature in {from_unit}:")
    if temp_str is None:
        return

    try:
        temp = float(temp_str)
        result = None

        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = celsius_to_fahrenheit(temp)
            elif to_unit == "Kelvin":
                result = celsius_to_kelvin(temp)
            elif to_unit == "Celsius":
                result = temp
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = fahrenheit_to_celsius(temp)
            elif to_unit == "Kelvin":
                result = fahrenheit_to_kelvin(temp)
            elif to_unit == "Fahrenheit":
                result = temp
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = kelvin_to_celsius(temp)
            elif to_unit == "Fahrenheit":
                result = kelvin_to_fahrenheit(temp)
            elif to_unit == "Kelvin":
                result = temp

        if result is not None:
            messagebox.showinfo("Result", f"{temp} {from_unit} = {result:.2f} {to_unit}")
        else:
            messagebox.showerror("Error", "Invalid conversion units.")
    except ValueError:
        messagebox.showerror("Error", "Invalid temperature value.")

    root.destroy()

if __name__ == "__main__":
    temperature_converter()