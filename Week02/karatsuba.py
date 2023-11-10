#-------------------------------------------Pseudocode----------------------------#

# Multiply_integer( a, b ):
# 	if (n = 1):
# 		return x·y
# 	write a as x·10n/2 + y
# 	write b as v·10n/2 + w



# xy = Multiply_integer(x,y)
# xw = Multiply_integer(x,w)
# yv = Multiply_integer(y,v)
# yw = Multiply_integer(y,w)
# return xv·10n + (xw + yv)·10n/2 + yw 


#-------------------------------------------<<   i   >>----------------------------#

def Multiply_integer(a, b):
    return str(a * b)

#-------------------------------------------<<   ii  >>----------------------------#

def Multiply_string(a, b):
    a = int(a)
    b = int(b)
    return str(a * b)

#-------------------------------------------<<  iii  >>----------------------------#

def Visualize_Karatsuba(a, b):
    a = int(a)
    b = int(b)
    
    result = Karatsuba_Recursive(str(a), str(b))
    print(result)

#-------------------------------------------<<   iv  >>----------------------------#

def Multiply_Recursive(a, b):
    if len(a) == 1 or len(b) == 1:
        return str(int(a) * int(b))
    else:
        m = max(len(a), len(b))
        m2 = m // 2

        a_high = a[:-m2]
        a_low = a[-m2:]

        b_high = b[:-m2]
        b_low = b[-m2:]

        ac = Multiply_Recursive(a_high, b_high)
        bd = Multiply_Recursive(a_low, b_low)
        ad_bc = str(int(Multiply_Recursive(a_high, b_low)) + int(Multiply_Recursive(a_low, b_high)))

        return str(int(ac + '0' * (2 * m2)) + int(ad_bc + '0' * m2) + int(bd))

#-------------------------------------------<<   v   >>----------------------------#

def Karatsuba_Recursive(a, b):
    if len(a) == 1 or len(b) == 1:
        return str(int(a) * int(b))
    else:
        m = max(len(a), len(b))
        m2 = m // 2

        a_high = a[:m2]
        a_low = a[m2:]

        b_high = b[:m2]
        b_low = b[m2:]

        ac = Karatsuba_Recursive(a_high, b_high)
        bd = Karatsuba_Recursive(a_low, b_low)
        ad_bc = str(int(Karatsuba_Recursive(str(int(a_high) + int(a_low)), str(int(b_high) + int(b_low)))) - int(ac) - int(bd))

        return str(int(ac + '0' * (2 * m2)) + int(ad_bc + '0' * m2) + int(bd))
    
#--------------------------------Python Code for Base 2 and 16---------------------#

def Multiply2(x, y):
    if not all(bit in '01' for bit in x) or not all(bit in '01' for bit in y):
        return []  # Invalid input, return empty list
    
    x = int(x, 2)
    y = int(y, 2)
    result = bin(x * y)[2:]  # Convert to binary and remove '0b' prefix
    return result  # Zero-fill to match the expected length

def Multiply16(x, y):
    if not all(c in '0123456789ABCDEF' for c in x) or not all(c in '0123456789ABCDEF' for c in y):
        return []  # Invalid input, return empty list
    
    x = int(x, 16)
    y = int(y, 16)
    result = hex(x * y)[2:]  # Convert to hexadecimal and remove '0x' prefix
    return result.upper()

def validate_input(base, x, y):
    if base == 2:
        if not all(bit in '01' for bit in x) or not all(bit in '01' for bit in y):
            return False
    elif base == 16:
        if not all(c in '0123456789ABCDEF' for c in x) or not all(c in '0123456789ABCDEF' for c in y):
            return False
    else:
        return False
    
    return True

def get_user_input():
    base = int(input("Enter base (2 or 16): "))
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    
    if validate_input(base, x, y):
        return base, x, y
    else:
        print("Invalid input. Please enter valid numbers.")
        return None

def print_result(result):
    if result:
        print("Result:", result)
    else:
        print("Invalid input. Unable to perform multiplication.")
        
# Main code
def main():
    base, x, y = get_user_input()
    
    if base == 2:
        result = Multiply2(x, y)
    elif base == 16:
        result = Multiply16(x, y)
    else:
        result = []
        
    print_result(result)

if __name__ == "__main__":
    main()

