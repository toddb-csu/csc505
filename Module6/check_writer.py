# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 6: Critical Thinking Assignment
#
# This Python program will write a formatted check string
# based on the numeric dollar amount by the user
#
# Prompt the user to enter a dollar amount that they want to print to a check.
# Verify the amount is a valid number and the number is at least .01 or 1 cent
def get_amount():
    user_input = input("Enter the dollar amount that you would like printed on a check: $")
    try:
        amount = float(user_input)
    except ValueError:
        print(f"Sorry, {user_input} is not a valid dollar amount.")
    else:
        # We don't want to print a check for an amount less than 1 cent.
        if amount < .01:
            print(f"Sorry, {user_input} must be 1 cent or more to write a check.")
        else:
            return amount
    return 0.0


# Split the amount into dollars and cents.
# I considered subtracting dollars from amount and multiplying by 100,
# but this sometimes causes a rounding issue such as 4.17 - 4 = 0.1699997
# I don't want to round in case someone enters 4.169 and we should drop
# the 9 as we do not support fractions of a cent.
def split_amount(amount):
    dollars = int(amount)
    str_amount = str(amount)
    cents = int(str_amount.split('.')[1])
    return dollars, cents


# Convert numbers to words using the dictionary num_to_word and recursion.
def convert_numbers_to_words(num):
    num_to_word = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    if num == 0:
        return 'zero'
    elif num < 20:
        return num_to_word[num]
    elif num < 100:
        words = num_to_word[int(num/10) * 10]
        if num % 10 > 0:
            words += '-' + num_to_word[num % 10]
        return words
    elif num < 1000:
        words = num_to_word[int(num/100)] + ' hundred'
        if num % 100 > 0:
            words += ' ' + convert_numbers_to_words(num % 100)
        return words
    elif num < 1000000:
        words = convert_numbers_to_words(int(num/1000)) + ' thousand'
        if num % 1000 > 0:
            words += ' ' + convert_numbers_to_words(num % 1000)
        return words
    else:
        return ''


# Return the formatted string that will be printed on the check
# Putting this in a method allows us to be able to abstract this functionality
# if we want to expand on it later for a variety of formats.
def get_formatted_check_amount(str_dollars, cents):
    return f"{str_dollars} and {cents:02}/100 dollars"


# Our main method that starts everything.
if __name__ == '__main__':
    user_amount = get_amount()
    int_dollars, int_cents = split_amount(user_amount)
    dollar_words = convert_numbers_to_words(int_dollars)
    if dollar_words == '':
        print(f"Sorry, but we cannot write a check for this amount: ${user_amount}")
    else:
        print(get_formatted_check_amount(dollar_words, int_cents))
