# Verifying the conversions using Python code

# Binary to decimal conversion
binary_number = "10110.1011"
decimal_from_binary = int(binary_number.split('.')[0], 2) + sum(
    [int(bit) * (2 ** -(i + 1)) for i, bit in enumerate(binary_number.split('.')[1])]
)

# Hexadecimal to decimal conversion
hex_number = "4BED.C"
decimal_from_hex = int(hex_number.split('.')[0], 16) + sum(
    [int(char, 16) * (16 ** -(i + 1)) for i, char in enumerate(hex_number.split('.')[1])]
)

decimal_from_binary, decimal_from_hex
