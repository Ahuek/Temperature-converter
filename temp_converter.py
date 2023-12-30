def c_f(c):
    farenheit=(c* 9/5) + 32 
    return farenheit
def f_c(f):
    celsius=(f-32) * 5/9 
    return Celsius

choice=input('input f to convert to fahrenheit and c to convert to convert to celsius')


if choice=='f':
    celsius_input=float(input('Enter value in celsius'))
    result1=c_f(celsius_input)
    print('your converted value is',result1)
if choice=='c':
    farenheit_input=float(input('Enter value in farenheit'))
    result2=f_c(farenheit_input)
    print('your converted value is',result2)


