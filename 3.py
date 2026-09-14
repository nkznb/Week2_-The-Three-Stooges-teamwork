def the_ui():
    print("====================")
    print("SCORE GRADING SYSTEM")
    print("====================")

def get_grade(score_num):
    if score_num >= 90:
        print("Your grade is A")
    elif score_num >= 80:
        print("Your grade is B")
    elif score_num >= 70:
        print("Your grade is C")
    elif score_num >= 60:
        print("Your grade is D")
    else:
        print("Your grade is F")

def main():
    the_ui()
    score = int(input("Please enter your score: "))
    get_grade(score)

main()