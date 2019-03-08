def decimal_Int_to_binary(x):
    """converts a decimal integer to binary"""
    digits = []
    right_most_digit = 0
    isNeg = False
    if x < 0:
        isNeg = True
        x = abs(x)
    if x == 0:
        digits = [0]
    while x > 0:
        right_most_digit = x % 2
        digits.insert(0, right_most_digit)
        x = x // 2
    if isNeg:
        return "-" + "".join(str(i) for i in digits)
    return "".join(str(i) for i in digits)


print(decimal_Int_to_binary(0))
print(decimal_Int_to_binary(1))
print(decimal_Int_to_binary(4))
print(decimal_Int_to_binary(19))
print(decimal_Int_to_binary(-19))

def decimal_Fraction_to_binary(x):
    """converts the fraction part of a decimal to binary"""
    # first find the power of 2 so that x * 2**? will be a whole number
    power = 0
    product = x * (2**power)
    while product % 1 != 0:
        power += 1
        product = x * (2**power)
    print("power is: ", power)
    print("product is: ", product)
    # power found
    # convert product to integer
    product = int(product)
    # convert product to binary repr
    bin_product = int(decimal_Int_to_binary(product))
    print("bin_product is: ", bin_product)
    # now shift the decimal point according to the power
    float_bin_product = bin_product * 10**(-power)
    return float_bin_product

print(decimal_Fraction_to_binary(0.25))
print(decimal_Fraction_to_binary(0.125))
print(decimal_Fraction_to_binary(0.375))
print(decimal_Fraction_to_binary(0.1))
print(decimal_Fraction_to_binary(0.333))




