a=['stone','paper','scissor']
import random
score=0
f=100
e=input('''Please choose one of the following options:-
            1.SELF PLAY
            2.AUTOPLAY ''')
if e=='1' :
    while 5==5:             
        b=input("(please write in small letters) .....stone, paper, scissor!!!! ")
        print("You chosed ",b)    
        c=random.choice(a)
        print("I chosed ",c)
        if b == c :
            print("Tie..........")
        elif c == 'stone' :
            if b == 'scissor' :
                print("You lose")
            elif b == 'paper' :
                print("You win")
                score+=1
        elif c == 'scissor' :
            if b == 'paper' :
                print("You lose")
            elif b == 'stone' :
                print("You win")
                score+=1

        elif c == 'paper' :
            if b == 'stone' :
                print("You lose")
            elif b == 'scissor' :
                print("You win")
                score+=1

        if score>=f:
            print("Your have won",score,"times!!")
            d=input("you still wanna play(y/n)")
            f+=100
            if d=="y":
                print("ok")
            else:
                break

elif e=='2' :
    while 5==5:             
        b=random.choice(a)
        print("You chosed (autoplay.) ",b)    
        c=random.choice(a)
        print("I chosed ",c)
        if b == c :
            print("Tie..........")
        elif c == 'stone' :
            if b == 'scissor' :
                print("You lose")
            elif b == 'paper' :
                print("You win")
                score+=1
        elif c == 'scissor' :
            if b == 'paper' :
                print("You lose")
            elif b == 'stone' :
                print("You win")
                score+=1

        elif c == 'paper' :
            if b == 'stone' :
                print("You lose")
            elif b == 'scissor' :
                print("You win")
                score+=1

        if score>=f:
            print("Your have won",score,"times!!")
            d=input("you still wanna play(y/n)")
            f+=100
            if d=="y":
                print("ok")
            else:
                break

else:
    z=9
