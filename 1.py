def main():
    the_ui()

def the_ui():
    print("==================")
    print("HARVARD ADMISSION")
    print("==================")

def interview(answer):
    ask_qusetions = input("Tell me something about yourself: ")
    if len(ask_qusetions) >= 10:
        print("You're accepted")
    elif len(ask_qusetions) < 10:
        print("You're on the waitlist")
    else:
        print("You're rejected")







