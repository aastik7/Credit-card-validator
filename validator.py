sum_odd_digits = 0
sum_even_digits = 0 
total = 0

#Step 1
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]
print(card_number)

#Step 2

for x in card_number[::2]:
    sum_odd_digits += x