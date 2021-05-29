# Note :- This code is in python programming language :)
#What’s the word?(Naruto characters) 

zz=int(input("Your choice"))
if zz==1:
    a=['Naruto','Sasuke','Sakura','Kakashi',      #K                 #Team 7
   'Lee','TenTen','Neji','Guy',               #O                 #Team _
   'Shikamaru','Choji','Ino','Asuma',         #N                 #Team _
   'Hinata','Akamaru','Shino','Kurenai',      #O                 #Team _
   'Minato','Kushina','Kurama',               #H                 #Naruto's Family
   'Jiraiya','Tsunade','Orochimaaru',         #A                 #Sannin
   'Shizune','Yamato','Sai',                  #Village 
   'Konan','Itachi','Kisame','Sasori','Deidara','Hidan','Kakuzu','Zetsu',#Akatsuki
   'Gaara','Kankuro','Temari','Tobi','Madara','Hashirama','Tobirama','Hiruzen''Konohamaru',#Others......
   'Kabuto','Nagato','Yahiko']
import random
b=random.choice(a)
c=len(b)
d='_'*c

g=list(b)
h=list(d)
print("The word is",d,"It has ",c,"letters")
if b in a[:25]:
    print("Hint:- Ninja from leaf village (Konoha) ")
print("You have 10 chances to guess the word !! ")

e='a'
print('*'*15,"Lets begin",'*'*15)
while h!=g :
    for i in range(10):
        e=str(input("Enter your  guess.(PLEASE ENTER SINGLE WORD AT A TIME) "))
        if e in g:        
            f=g.index(e)
            h[f]=g[f]
            j=g[f+1:c]
            p=len(j)
            o=''
            for j in h :
                o+=j                
            if e in j:
                k=j.index(e)
                h[c-p+k]=g[c-p+k]
                m=''
                for k in h :
                  m+=k
                print("You have guessed ",m)
            else:
                print("You have guessed ",o) 
        else:
            print("WRONG !!")
        if h==g:
            break
    break
if h==g:
    print("You won !! )")
elif h!=g:
    print("You lose (10 chances over)")
if i<7:
    print("Woww, Congrats (Its very rare to win this game in just ",i," becoz I made it (I am python@)")
print("The word was",b)
