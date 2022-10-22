
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "!@#$%^&*"

Use_for = lower_case + upper_case + numbers + symbol
pass_length = 10

password = "".join(random.sample(Use_for, pass_length))
#password = "".join(random.sample(Use_for, length_for_pass))

print("Your password is: "+ password) 
         