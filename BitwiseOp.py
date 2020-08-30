# Binary operators are used to perform bit-level operations on (binary) numbers.

x = 0b1100
y = 0b1010

# and
print (bin(x&y))

# or
print (bin(x|y))

# xor
print (bin(x^y))

# not
print (bin(~x))

# shift 2 bits left 
print (bin(x << 2))

# shift 2 bits right
print (bin(x >> 2))

