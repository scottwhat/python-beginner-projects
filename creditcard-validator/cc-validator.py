




sum_odd_digits = 0
sum_even_digits = 0
total = 0

#step1
card_number = input('Enter number')
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

#step 2, sum all the second digits.
#use the slice and step 2 to get an array of evvery second digit
for x in card_number[::2]:
    sum_odd_digits += int(x)

#step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

#step 4

total = sum_even_digits + sum_even_digits

#step5

if total % 10 == 0:
    print("valid")
else:
    print("invalid")




print(card_number)
