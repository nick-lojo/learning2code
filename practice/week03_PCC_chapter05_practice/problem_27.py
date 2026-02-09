test_scores = [95, 67, 82, 58, 91, 74]

for score in test_scores:
    if score < 60:
        print(f'Score {score}: F')
    elif score <= 69: #nice
        print(f'Score {score}: D')
    elif score <= 79:
        print(f'Score {score}: C')
    elif score <= 89:
        print(f'Score {score}: B')
    else:
        print(f'Score {score}: A')