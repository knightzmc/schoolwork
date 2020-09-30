def get_amount():
    try:
        return int(input('How much would you like to withdraw?\n'))
    except ValueError:
        print("That doesn't look like a number")
        return get_amount()


def validate_amount(amount) -> bool:
    if amount % 10 != 0:
        print('You can only withdraw a multiple of £10.')
        return False
    if 10 < amount > 200:
        print('You can only withdraw between £10 and £200. Sorry for any inconvenience caused.')
        return False
    return True


def get_note_distributions(amount):
    notes20 = amount // 20
    notes10 = (amount % 20) // 10
    return notes10, notes20


def run():
    print('Welcome to Python Bank ATM. Please input how much you would like to withdraw.')

    amount = get_amount()
    if not validate_amount(amount):
        return

    notes10, notes20 = get_note_distributions(amount)

    print('Collect your money:')
    if notes20 > 0:
        print(f'      >> £20 Notes: {notes20}')
    if notes10 > 0:
        print(f'      >> £10 Notes: {notes10}')
    print('Thank you for using Python Bank')
    print('Have a nice day')


if __name__ == '__main__':
    while True:
        run()
