# A currency converter takes two inputs from the user: an amount
# and an exchange rate. It multiplies them to get the converted
# value. Bad input should not crash the program.
#
# Your job: prompt for both values, run the conversion, and handle
# any bad input gracefully.

def currency_converter():
    """Converts currency for the user."""
    message = '\nPlease provide use with your current currency, desired currency,'
    message += ' the value of your current currency, and the exchange rate,'
    message += ' and we will convert the value for you.'
    print(message)

    current_currency = input('\nWhat currency do you currently hold? ')
    current_amount = input('How much of this currency do you hold? ')
    desired_currency = input('What currency do you wish to convert this to? ')
    exchange_rate = input('Please provide the exchange rate: ')

    try:
        desired_amount = int(current_amount) * float(exchange_rate)
    except ValueError:
        message = '\nPlease make sure you only enter integers for the Current'
        message += ' Amount and the Exchange Rate. Do not enter symbols, i.e.,'
        message += ' $.'
        print(message)
    else:
        message = f'\n{current_amount} of {current_currency} is worth'
        message += f' {desired_amount} of {desired_currency}.'
        print(message)

currency_converter()