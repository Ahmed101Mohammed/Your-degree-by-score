try:
    score = float(input('Enter Score: '))
except:
    print('Error: Enter number plz')
    quit()

def computegrade(score):
    if score <= 1 and score >= 0:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
    else: grade = 'Error, plase enter number between 0 and 1'
    return grade

print(computegrade(score))