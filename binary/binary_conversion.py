num = int(input("Enter a number: "))
bit = int(input("Enter bit width: "))

# professional string manipulation

# Decimal to Hex
hex_str = ""
temp_num = num

while temp_num > 0:
    remainder = temp_num % 16
    hex_str = "0123456789ABCDEF"[remainder] + hex_str
    temp_num //= 16

print("Hex:", hex_str)

# Decimal to Binary
binary = ""
temp_num = num
for i in range(bit - 1, -1, -1):
    if temp_num & (1 << i):
        binary += "1"
    else:
        binary += "0"

print("Binary:", binary)

# Two's Complement - Invert
inverted = ""
for char in binary:
    if char == "1":
        inverted += "0"
    else:
        inverted += "1"

# Two's Complement -  Add One
result = ""
carry = 1
for i in range(bit - 1, -1, -1):
    bit_val = int(inverted[i])
    total = bit_val + carry
    if total == 0:
        result = "0" + result
        carry = 0
    elif total == 1:
        result = "1" + result
        carry = 0
    elif total == 2:
        result = "0" + result
        carry = 1
    else:
        result = "1" + result
        carry = 1

print("Result:", result)