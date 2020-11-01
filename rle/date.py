from datetime import date

dob = input('Please input your date of birth in the format YYYY-MM-DD\n')

date_of_birth = date.fromisoformat(dob)
now = date.today()

diff = now - date_of_birth
print(f'You are {diff.days} days old')
