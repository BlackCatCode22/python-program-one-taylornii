# initialize variables
user_name = None
num1 = int(0)
num2 = int(0)
num3 = int(0)
denominator_is_zero = False
first_div_second = float(0)
#
# user enters their name, greet user
user_name = str(input("User name: "))
print("\nHello,", user_name, "\nLet's find the largest of three\n")
#
# make sure input is an integer
while(True):
    try:
        num1 = int(input("Please input first number:"))
        num2 = int(input("Please input second number:"))
        num3 = int(input("Please input third number:"))
        break
    except:
        print("Not a valid input, enter only INTEGERS")
#
# find the largest of three using compounded if
def largest_of_three_compound(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3
#
# find the largest of three using nested if
def largest_of_three_nested(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        if num2 >= num3:
            return num2
        else:
            return num3
#
# find the largest of three chatgpt way aka max()
def largest_of_three_max(num1, num2, num3):
    return max(num1, num2, num3)
#
# make sure divisor(num2) is not zero
if num2 == 0:
    denominator_is_zero = True
else:
    denominator_is_zero = False
#
# find first input divided by second input
if denominator_is_zero == False:
    first_div_second = float(num1/num2)
#
# print: (3)largest of three solutions, quotient solution, and variable types
print("\nlargest of the three...")
print(" using compound if:", largest_of_three_compound(num1, num2, num3))
print(" using nested if:", largest_of_three_nested(num1, num2, num3))
print(" using max function:", largest_of_three_max(num1, num2, num3), "\n")
if denominator_is_zero == False:
    print(num2, "/", num1, " =\n        ", first_div_second)
else:
    print(num1, "/", num2, "=\n   ...cannot divide", num1, "by", num2)
print("\nvariable_name <variable type>")
print("   user_name", type(user_name))
print("   num1",type(num1),"\n   num2", type(num2), "\n   num3", type(num3))
print("   denominator_is_zero", type(denominator_is_zero))
print("   first_div_second", type(first_div_second))