
import os
import time
import random
import webbrowser

class The_Guesser:
    points=0
    def __init__(self):
        self.LOWER = 0
    def First_Question():
        while True:
            try:
                print("Albano song in 1982 his name is F......a?\n")
                answer= str(input("Enter your answer: "))
                if answer=="Felicita" or answer =="FELICITA" or answer=="felicita":
                    print("You got the correct answer!!!")
                    os.system('Albano_Felicita.mp3')
                    fh=open('Points.txt','a')
                    fh.write('For the First question you got 1 point\n')
                    fh.close()
                    The_Guesser.points+=1
                    break
                else:
                    print("Wrong answer,try again")
                    break
            except ValueError as var:
                print("Error input,you have to choose from the menu!")
    def Second_Question():
        x=os.system('SecondMusic.m4a')
        while True:
            try:
                print("Do you know the complete name of the singer or the title of this song?\nOne answer will be accepted")
                answer= str(input("Enter your answer: "))
                if answer=="Bob Sinclar" or answer =="World hold on" or answer== "bob sinclar" or answer=="BOB SINCLAR":
                    print("You got the correct answer!!!:)")
                    fh=open('Points.txt','a')
                    fh.write('For the Second question you got 1 point\n')
                    fh.close()
                    The_Guesser.points+=1
                    break
                else:
                    print("Wrong answer,try again")
                    break
            except ValueError as var:
                print("Error input,you have to choose from the menu!")
    def Check():
        while True:
            try:
                print("Do you know the full name of the singer boy?")
                answer= str(input("Enter your answer: "))
                if answer=="Sean Paul" or answer =="sean paul" or answer=="SEAN PAUL":
                    print("Yes is",answer,"bravo!!!!")
                    fh=open('Points.txt','a')
                    fh.write('For the Third question you got 1 point\n')
                    fh.close()
                    The_Guesser.points+=1
                    break
                else:
                    print("Wrong answer,try again")
                    break
            except ValueError as var:
                print("Error input,you have to choose from the menu!")
    def Third_Question():
        x=os.system('Three.mp3')
        while True:
            try:
                print("Do you know the title of this song?\n")
                answer= str(input("Enter your answer: "))
                if answer=="No lie" or answer =="no lie" or answer=="NO LIE":
                    print("You got the title of this song,now i have one more question for you")
                    The_Guesser.Check()
                    break
                else:
                    print("Wrong answer,try again")
                    break
            except ValueError as var:
                print("Error input,you have to choose from the menu!")

    def Random_Songs():
        n= random.randint(0,3)
        print(n)
        music_dir='Random'
        song= os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,song[n]))
        print("Who is the artist of this song?")
        answer=str(input("Enter your answer: "))
        if n==0 and answer=="Bon Jovi" or answer=="bon jovi"or answer=="BON JOVI":
            print("Bravo you got the correct answer!!!")
            fh=open('Points.txt','a')
            fh.write('For the Random question you got 1 point\n')
            fh.close()
            The_Guesser.points+=1
        elif n==1 and answer=="Drake" or answer =="drake" or answer=="DRAKE":
            print("Bravo you got the correct answer!!!")
            fh=open('Points.txt','a')
            fh.write('For the Random question you got 1 point\n')
            fh.close()
            The_Guesser.points+=1
        elif n==2 and answer=="Madcon" or answer=="MADCON"or answer=="madcon":
            print("Bravo you got the correct answer!!!")
            fh=open('Points.txt','a')
            fh.write('For the Random question you got 1 point\n')
            fh.close()
            The_Guesser.points+=1
        elif n==3 and answer=="Michael Jackson" or answer =="Michael"or answer=="michael"or answer =="michael jackson"or answer =="MICHAEL JACKSON":
            print("Bravo you got the correct answer!!!")
            fh=open('Points.txt','a')
            fh.write('For the Random question you got 1 point\n')
            fh.close()
            The_Guesser.points+=1
        else:
            print("Incorrect answer... try again")

    def Bravo():
        return "Bravo you got the correct answer let s continue like that"
    def Fourth_Test_Question():
        print("-------------------------Fourth Question for you!-------------------------")
        print("\nLook the test of ..... song and guess the title👇🏽👇🏽👇🏽\n")
        with open("Test4.txt","r") as file:
            var=file.read()
            print(var)
            file.close()
            pass
        answer=str(input("\nPress your answer: "))
        if answer=="Summer" or answer=="SUMMER" or answer=="summer":
            print("You got one point👏🏼👏🏼👏🏼")
            fh=open('Points.txt','a')
            fh.write('For the part 5 you got all questions correct you got 1 point\n')
            fh.close()
            The_Guesser.points+=1
        else:
            print("Sorry try again:(")
    def Third_Test_Question():
        print("-------------------------Third Question for you!-------------------------")
        print("\nLook the test of ..... song and guess the title👇🏽👇🏽👇🏽\n")
        with open("Test3.txt","r") as file:
            var=file.read()
            print(var)
            file.close()
            pass
        answer=str(input("\nPress your answer: "))
        if answer=="Happy" or answer=="happy" or answer=="HAPPY":
            print(The_Guesser.Bravo())
            The_Guesser.Fourth_Test_Question()
        else:
            print("Sorry try again:(")
    def Second_Test_Question():
        print("-------------------------Second Question for you!-------------------------")
        print("\nLook the test of ..... song and guess the title👇🏽👇🏽👇🏽\n")
        with open("Test2.txt","r") as file:
            var=file.read()
            print(var)
            file.close()
            pass
        answer=str(input("\nPress your answer: "))
        if answer=="Waka Waka" or answer=="WAKA WAKA" or answer=="waka waka":
            print(The_Guesser.Bravo())
            The_Guesser.Third_Test_Question()
        else:
            print("Sorry try again:(")
            
    def First_Test_Question():
        print("-------------------------First Question for you!-------------------------")
        print("Look the test of ..... song and guess the title👇🏽👇🏽👇🏽\n")
        with open("Test1.txt","r") as file:
            var=file.read()
            print(var)
            file.close()
            pass
        answer=str(input("Press your answer: "))
        if answer=="In Italia" or answer=="IN ITALIA" or answer=="in italia"or answer=="in Italia":
            print(The_Guesser.Bravo())
            The_Guesser.Second_Test_Question()
        else:
            print("Sorry try again:(")
            
    def Open_Fileof_Points():
        with open("Points.txt","r") as file:
            var=file.read()
            print(var)
            file.close()
            pass
        print("Total points are: ",The_Guesser.points,"💲💲💲💲💲💲💲💲   ")
        The_Guesser.Are_The_Guesser_Win()

    def EuroVision_Question3():
        print("Witch contry win the EuroVision 2018?")
        print("1.Lithuania\t 2.Albania\t 3.Israel")
        answer=str(input("Press your answer: "))
        if answer=="3":
            print("Yes,Israel won the EuroVision 2018")
            webbrowser.open('https://www.youtube.com/watch?v=84LBjXaeKk4')
            fh=open('Points.txt','a')
            fh.write('For the Euro Vision Questions you got 1 point\n')
            fh.close()
            The_Guesser.points+=1
        else:
            print("Incorrect answer:( try again")
    def EuroVision_Question2():
            print("Witch contry win the EuroVision 2019?")
            print("1.Netherland\t 2.France\t 3.Sweden")
            answer=str(input("Press your answer: "))
            if answer=="1":
                print("Yes,Netherland won the EuroVision 20019")
                webbrowser.open('https://www.youtube.com/watch?v=R3D-r4ogr7s')
                print("-------------------------------------------------------------")
                The_Guesser.EuroVision_Question3()
            else:
                print("Incorrect answer:( try again")
    def EuroVision_Questions():
            print("Witch contry win the EuroVision 2021?")
            print("1.France\t 2.Italy\t 3.Germany")
            answer=str(input("Press your answer: "))
            if answer=="2":
                print("Yes,Italy won the EuroVision 2021")
                webbrowser.open('https://www.youtube.com/watch?v=RVH5dn1cxAQ')
                print("-------------------------------------------------------------")
                The_Guesser.EuroVision_Question2()
            else:
                print("Incorrect answer:( try again")

    def Listen_And_Complete_The_Song_Part3():
         os.system('Queen_We_are_the_Champions_Guess_Worlds.mp3')
         phrase_complete="we are the champions no time for losers because we are the champions of the world"
         while True:
             try:
                 answer= str(input("Enter your answer: "))
                 if answer=="no time for losers" or answer =="NO TIME FOR LOSERS" or answer==phrase_complete or answer==phrase_complete.upper():
                     print("Bravo!!!You got all 3 songs sentence ,you got 1 point!!!")
                     os.system('Queen_We_Are_The_Champions_Complete_Worlds.mp3')
                     fh=open('Points.txt','a')
                     fh.write('For the Listen and Complete the sentence you got 1 point\n')
                     fh.close()
                     The_Guesser.points+=1
                     break
                 else:
                     print("Wrong answer,try again")
                     break
             except ValueError as var:
                 print("Error input,you have to choose from the menu!") 

    def Listen_And_Complete_The_Song_Part2():
         os.system('Luis_Fonsi_Despacito_Guess_The_World.mp3')
         phrase_complete="despacito quiero desnudarte a besos despacito firmo en las paredes de tu laberinto "
         while True:
             try:
                 answer= str(input("Enter your answer: "))
                 if answer=="quiero desnudarte a besos despacito" or answer =="QUIERO DESNUDARTE A BESOS DESPACITO" or answer==phrase_complete or answer==phrase_complete.upper():
                     print("You got the sentence of this song,the next song will be in 20 seconds")
                     os.system('Luis_Fonsi_Despacito_Complete_Worlds.mp3')
                     time.sleep(22)
                     The_Guesser.Listen_And_Complete_The_Song_Part3()
                     break
                 else:
                     print("Wrong answer,try again")
                     break
             except ValueError as var:
                 print("Error input,you have to choose from the menu!") 
    
    def Listen_And_Complete_The_Song():
        print("In this part you will have 3 different songs, you will have to guess the sentence(maximum 5 words) that continue them")
        os.system('Drake_Hotline_Bling_Try_To_Guess_TheWorlds.mp3')
        phrase_complete="late night when you need my love and i know when that hotline bling"
        while True:
            try:
                answer= str(input("Enter your answer: "))
                if answer=="late night when you need" or answer =="LATE NIGHT WHEN YOU NEED" or answer==phrase_complete or answer==phrase_complete.upper():
                    print("You got the sentence of this song,the next song will be in 20 seconds")
                    os.system('Drake_Hotline_Bling_Complete_World.mp3')
                    time.sleep(22)
                    The_Guesser.Listen_And_Complete_The_Song_Part2()
                    break
                else:
                    print("Wrong answer,try again")
                    break
            except ValueError as var:
                print("Error input,you have to choose from the menu!")
    def Are_The_Guesser_Win():
        if The_Guesser.points>=5:
            print("YOU HAVE WIN THE DAVIDE MUSIC QUIZ")
            return True
        else:
            print("YOU HAVE TO GET 5 POINTS FOR WIN THE DAVIDE MUSIC QUIZ")
            return False
                
def MUSIC_QUIZ():
    print("--------------------------------MUSIC QUIZ --------------------------------")
    print("--------------------------WELCOME TO THE MUSIC QUIZ GAME-------------------------\n0.Exit-Reset the game\n1.First Song Question\n2.Almost 30 seconds to guess the song\n3.Only 7 Seconds of song to guess it\n4.Guess the song in Random Music\n5.There are 4 lyrics from 4 different songs\n6.List the song and complete the word\n7.Euro Vision Questions\n8.Show all points")
    choise = 10
    while  True:
        try:
            if choise == 1:
                print("For the first question is a Italian singer easy to guess the correct answer")
                The_Guesser.First_Question()
                MUSIC_QUIZ()
                break
                print("----------------------------------------------------------------")
            if choise == 2:
                print("For the second question you have almost 30 second to guess this song 🕐  ")
                The_Guesser.Second_Question()
                MUSIC_QUIZ()
                break
            if choise == 3:
                The_Guesser.Third_Question()
                MUSIC_QUIZ()
                break
            if choise ==4:
                The_Guesser.Random_Songs()
                MUSIC_QUIZ()
                break
            if choise ==5:
                print("In this part of the game you have four text questions,if you guess them all,you will receive 1 point!")
                The_Guesser.First_Test_Question()
                MUSIC_QUIZ()
                break
            if choise ==6:
                The_Guesser.Listen_And_Complete_The_Song()
                MUSIC_QUIZ()
                break
            if choise ==7:
                print("In Euro Vision part you will to answer at 3 questions to got 1 point,🎻🎧🎤🎹🎸")
                The_Guesser.EuroVision_Questions()
                MUSIC_QUIZ()
                break
            if choise ==8:
                The_Guesser.Open_Fileof_Points()
                MUSIC_QUIZ()
                break
            elif choise ==0:
                f = open('Points.txt', 'r+')
                f.truncate(0)
                print("Thank for have play the Music quiz")
                The_Guesser.points=0
                break
            choise=int(input("CHOOSE FROM DAVIDE MENU: "))
        except ValueError as var:
            print("Error input,you have to choose from the menu!")


MUSIC_QUIZ()
