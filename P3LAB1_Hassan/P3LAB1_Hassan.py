#CTI 110
# P3LAB1 
# Hassana
# 10/22/24
# twine does the storytelling 

def main():
    print("Choose Your Own Adventure")
    go_home()

def go_home():
    print("You decide to go home.")
    print("But should you get some food?")
    print("1. Order Chicken 65")
    print("2. Get Desi") 
    print("3. Get Summoned")
    print("4. Get Egged")
    choice = int(input())
    if choice ==1:
        get_chicken_65()
    elif choice ==2:
        get_desi()
    elif choice ==3:
        get_summoned()
    elif choice ==4:
        get_egged()
    
#go to emojipedia
def get_chicken_65():
    print("The chicken is laced with blood that attracts 65 deadly monsters that hunt you")
    print("🎃🎃🎃HOW DID YOU LIKE YOUR TREAT?🎃🎃🎃")

def get_desi():
    print("The desi food will courrupt your mind and will make you transform to a beast at night")
    print("🕯️🕯️🕯️THERE IS NO HAPPY ENDING FOR THE LIKES OF YOU🕯️🕯️🕯️")

def get_summoned():
    print("You get summoned to by a politcal figure and blackmails you into joining his cult")
    print("😈😈😈THE FUN BEGINS!😈😈😈")

def get_egged():
    print("You go on your way home and get egged with acid eggs")
    print("🌚🌚🌚WOMP WOMP WOMP🌚🌚🌚")    
# start the program
main()