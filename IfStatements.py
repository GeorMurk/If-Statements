#!/usr/bin/python

#!Creating If Statements

is_female = True

if is_female:
    print("You are a Female")

#! "Or" condition
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a Male or tall or both")
else:
    print("You are neither a Male nor tall or both")

#! "And" condition
is_animal = True
is_huge = False

if is_animal and is_huge:
    print("It is a huge animal!!!")
else:
    print("It is either not huge or an animal or both")

#! using elseif (elif)
is_smart = True
is_cute = False

if is_smart and is_cute:
    print("It is smart and cute")
elif is_smart and not (is_cute):
    print("It is not smart at all")
elif not (is_smart) and is_cute:
    print("It is not cute")
elif not (is_smart) and not (is_cute):
    print("It is neither smart nor cute")

#! using comparision
def max_number(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3

result = (max_number(959, 5132, 23))
print(result)


#!Go Ahead and test it out!!!!
