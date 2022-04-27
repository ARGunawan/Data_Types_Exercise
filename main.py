# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_half = two_digit_number[0]
second_half = two_digit_number[1]

#Because the above are still strings you convert them into integers
addition = int(first_half) + int(second_half)

print(addition)
