'''
Unit converter: Miles and Kilometers
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

def kg_lb():
    kg = float(input('Enter weight in kilograms: '))
    lb = kg * 2.2046226

    print('Weight in pounds: {0}'.format(lb))

def lb_kg():
    lb = float(input('Enter weight in lb: '))
    kg = lb / 2.2046226

    print('Weight in kilograms: {0}'.format(kg))

def cel_fah():
    cel = float(input('Enter temperature in celcius: '))
    fah = cel * 9 / 5 + 32

    print('Temperature in Fahrenheit: {0}'.format(fah))

def fah_cel():
    fah = float(input('Enter temperature in Fahrenheit: '))
    cel = (fah - 32) * 5 / 9

    print('Temperature in Celsius: {0}'.format(cel))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()

    if choice == '2':
        miles_km()

    if choice == '3':
        kg_lb()
    
    if choice == '4':
        lb_kg()
    
    if choice == '5':
        cel_fah()
    
    if choice == '6':
        fah_cel()
