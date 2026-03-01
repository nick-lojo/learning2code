# You're building a billing tool for a subscription service.
#
# Starting from 1, print only account numbers that are divisible by 3 up to 30.
# All other account numbers should be skipped.
# Each line should read: "Account #[number] billed."

account_number = 0

while account_number <= 30:
    account_number = account_number + 1
    if account_number % 3 == 0:
        print(f"Account #{account_number} billed.")
    else:
        continue