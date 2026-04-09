# You're writing a test for a function called get_risk_tier()
# that takes a credit score and returns a tier label like
# "preferred", "standard", or "high-risk".
#
# Name your test function so that if it fails, a teammate
# reading the test report immediately knows what behavior
# broke — without looking at the code.
#
# Write the test function (you can make up a simple version
# of get_risk_tier() to test against). Run it and paste
# the output.

def get_risk_tier(credit_score):
    """Determines an account's risk tier based on their credit score."""
    if credit_score < 0:
        risk_tier = 'unacceptable credit score'
        print(f'You cannot have a negative credit score.')
    elif credit_score < 26:
        risk_tier = 'high-risk'
        print(f"This account falls in the {risk_tier.title()} risk tier.")
    elif credit_score < 76:
        risk_tier = 'standard'
        print(f"This account falls in the {risk_tier.title()} risk tier.")
    elif credit_score < 101:
        risk_tier = 'preferred'
        print(f"This account falls into the {risk_tier.title} risk tier.")
    else:
        risk_tier = 'unacceptable credit score'
        print(f"You cannot have a credit score above 100.")
    return risk_tier