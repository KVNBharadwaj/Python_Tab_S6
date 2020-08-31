print("Integer Float and Complex Numbers")

print("An integer is a whole number that can be positive or negative and of any length from python3.")

x=10
y=-10
z=123456789

print(x,' ',y,' ',z)

print(" Int is usually base 10. python allows us to write integers in Hexadecimal (base16), Octal (base 8), and Binary (base 2) formats. You can achieve this by adding a prefix to integer.")

print(" Prints binary 187, octal 8, hex 255 ")
print(0b10111011,' ', 0o10,' ', 0xFF)

print(" Boolean is a subtype of integer ")
x=True
print(x)
y=False
print(y)

print(x & y)
print(x or y)

print(" Floating point numbers are fractions ")
x = 10.01
y = -10.01
z = 1.123456

print (x,'  ', y,'  ', z)

print ("scientific notation are supported in python using 'e' or 'E'")

print(42e3)
print(4.2e-3)

print(' max value a float can have is approximately 1.8x10power308. Any number greater than that is indicated as inf (infinity) ')
# max value of a float
print(1.79e308)
print(1.8e308)

print('The minimum value a float can have is approximately 5.0x10power-324. Any number less than that is considered zero')
print(5e-324)
print(5e-325)

print("A complex number is specified as real_part + imaginary_part, where the imaginary part is written with j or J")
print("to extract rean number and imaginary number from complex number x use x.real and x.imag")

x = 2 + 3j
print(x.real)
print(x.imag)

