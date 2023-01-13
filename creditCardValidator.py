card_number = input("enter card number: ")


def even_double_digits(credit_card_number):
    total_sum_of_even_digits = 0
    for i in range(len(credit_card_number) - 2, -1, -2):
        sum_even = int(credit_card_number[i]) * 2
        if sum_even > 9:
            new_sum = sum_even % 10 + sum_even // 10
            total_sum_of_even_digits += new_sum
        else:
            total_sum_of_even_digits += sum_even
    return total_sum_of_even_digits


def odd_digits(credit_card_number):
    total_odd = 0
    for i in range(len(credit_card_number) - 1, -1, -2):
        total_odd += int(credit_card_number[i])
    return total_odd


result_of_digits = odd_digits(card_number) + even_double_digits(card_number)
# if result_of_digits % 10 == 0:
#     print("Card is valid")
# else:
#     print("Card is invalid")


def length_validity(credit_card_number):
    if result_of_digits % 10 == 0 and len(credit_card_number) < 13 or len(credit_card_number) > 16:
        return "Invalid"
    else:
        return "Valid"


def card_prefix(credit_card_number):
    if credit_card_number[0] == "4":
        return "VisaCard"
    elif credit_card_number[0] == "5":
        return "MasterCard"
    elif credit_card_number[0] == "3" and credit_card_number[1] == "7":
        return "American Express Cards"
    elif credit_card_number[0] == "6":
        return "DiscoverCard"
    else:
        return "Invalid"


print("*********************************************")
print("****Card Validity Status: " + length_validity(card_number))
print("****Credit Card Number: " + card_number)
print(f"****Credit Card Digit Length: {+len(card_number)}")
print("****Card Type: " + card_prefix(card_number))
print("*********************************************")

# def print_valid_card():
#     print("Credit Card Validity Status: " + card_validity(card_number))
#     print("Credit Card Type: Valid")
#     print("Credit Card Number: " + card_number)
#     print(f"Credit Card Digit Length {+len(card_number)}")


# def print_is_not_valid():
#     print("Credit Card Validity Status: " + card_validity(card_number))
#     print("Credit Card Type: " + card_validity(card_number))
#     print("Credit Card Number: " + card_number)
#     print(f"Credit Card Digit Length {+len(card_number)}")

# if result_of_digits % 10 == 0 & len(card_number) >= 13 & len(card_number) <= 16:
#     print("Credit Card Validity Status: Valid")
#     print("Credit Card Type: Valid")
#     print("Credit Card Number: " + card_number)
#     print(f"Credit Card Digit Length {+len(card_number)}")
#
# else:
#     print("Credit Card Validity Status: Invalid ")
#     print("Credit Card Type: Invalid")
#     print("Credit Card Number: " + card_number)
#     print(f"Credit Card Digit Length {+len(card_number)}")
