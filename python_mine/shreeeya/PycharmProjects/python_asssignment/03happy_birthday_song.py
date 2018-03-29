#03. Happy Birthday Song for a Friend

def yes():
    print("Happy Birthday to",name)
    print("Happy Birthday to You\nMay God Bless You\nCheers!",name)

def no():
    print("Never Mind Then...")

    

name = input("What is your name?\n")

print("So, Is it your birthday today?\n")

ans = input("yes or no?\n")

if(ans == 'yes'):
    yes()

else:
    no()
    

