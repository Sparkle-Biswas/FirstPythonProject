#
# CS 177 - Project3.py
# Sparkle Biswas - 0031907121
# Ruhani Sansoya - 0027811803
# Following CS 177 Coding Standards and Guidelines
# This program is an enhancement of the game you created in Project 2
# We were required to add three compulsary features:
# 1) The HINT button. We created a hint button on the control panel which would only be functional went
#       the game panel is open. Once you click on the hint button, it will eliminate three random characters
#       but it will cost them two guesses as 2 Polygons from the Block P will fall.
# 2) The second feature is that at the end of each game, display an Entry box object in the GAME PANEL Graphics
#       window along with a label to prompt the user to enter their name. The player’s game statistics
#       (name, number of rounds and final score) should be added to the scores.txt datafile. The initial
#       file is provided with the Project 3 assignment on Blackboard and your program must support the file
#       in that format. No changes to the format of the scores.txt datafile are allowed.
# 3) The third feature we had to add was the high scores window. We modified the CONTROL PANEL Graphics window
#       to include a new Rectangle labeled HIGH SCORES. A click on this control opens a new Graphics window that
#       displays the top 7 scores from the scores.txt file in a “scrolling” animation.  When the HIGH SCORES
#       Graphics window is opened, it stays open until it is clicked.
#
# We were required to create three Custom Creative Features:
# 1) The first feature we created were the four themes. We made four buttons on the control panel. These buttons
#       are used to buy the theme as well as apply the themes to the game panel. A certain number of boilerbucks
#       (game currency) are mentioned on these buttons(ex: 100 BOILERBUCKS) and once you have the particular amount of boilerbucks
#       you can click on the button to buy it. You have to click on the bought theme button again to apply the theme to
#       the game panel. You can only use one theme for each round.You can apply the theme even in the middle of the round.
#       Even after losing a game you retain  the themes you have bought.
#       Each theme changes the background color of the game panel as well as the letter circles and golden rectangles 
#       after being clicked.if statements check for clicks on the theme button, allowing the player to buy only if they have enough
#       boilerbucks and allowing the application of the theme only if the game panel is open and none of the other themes have been
#       applied for that round.We have created graphics like icicles, fish, grass, clouds, etc. using for loops.
#       We have made winning and losing animations using loops and decision statments. Some animations include,icicles falling 
#       one by one,fish swimming across the window, balloons floating and poping, clouds moving and a sun moving into the screen,etc.
#       
# 2) The second feature we created is the boilerbucks.They can be considered the game's currency. 
#       We made a BOILERBUCKS button at the bottom of the control panel.The player starts with 50 boilerbucks. The player can
#       bet 5 boilerbucks in each round by clicking on the BOILERBUCKS button. This button can be clicked at the beginning of a
#       a round or during the game play however, you cannot click on the button after you have won/lost the round. If you win the
#       round after you bet 5 boilerbucks you win 10 X (length of the word) boilerbucks. Ex: If the secret word is HOME you can win
#       40 boilerbucks. You also win 2 boilerbucks after winning every round(even without betting) so that you don't run out of
#       boilerbucks. You will retain your boilerbucks even after you lose an entire game. You have to remember to click on the
#       BOILERBUCKS button for every round, you can click on it even after you have started guessing. This feature includes decision
#       statements to check for clicks. The amount of boilerbucks you currently have is shown on the BOILERBUCKS button and contiously
#       updated after winning and betting.
#
# 3) The third feature we made is the 'WHAT ARE BOILERBUCKS?' button on the control panel. On clicking this button it will open a new window.
#       This window gives instructions on how to use boilerbucks and is user-interactive. It asks the user to click on the window and
#       buttons to learn how to use the boilerbucks and how to spend them. There is a CLOSE button on the window at all times which can be
#       clicked anytime to close this window. This window also closes with all the other windows when the QUIT button on the control
#       panel is clicked. This feature uses decision statements to check for clicks on the window and accordingly draws and undraws graphic
#       objects. We suggest that the player click on this button before playing the game to get a better idea of how boilerbucks work.
              


 
# importing the required libraries
from graphics import *
from random import *
from math import *
from time import sleep

# define function to explain and demonstrate use of boilerbucks
def what_boiler():
        # Create a gold window
        win4 = GraphWin('BOILERBUCKS!',300,300)
        win4.setBackground('gold')
        # set default boilerbucks to 50
        boiler_count = 50
        # create a black button to close the window at any time
        close = Rectangle(Point(250,5),Point(290,25))
        close.setFill('black')
        close_text = Text (Point(270,15),'CLOSE')
        close_text.setFill('white')
        close_text.setSize(8)
        close_text.setStyle('bold')
        # display detailed instructions on what are boilerbucks and how they can be used
        top_sent = Text(Point(150,15),'INSTRUCTIONS:')
        # user should be able to click in the window at anytime to continue with instructions
        click_cont = Text(Point(126,15),'CLICK ANYWHERE TO SEE AN EXAMPLE!!')
        click_cont.setSize(9)
        click_cont.setFill('red')
        click_cont.setStyle('bold')
        top_sent.setSize(10)
        top_sent.setStyle('bold')
        click_cont.draw(win4)
        # create 3 rectangles to organize instructions
        white1 = Rectangle(Point(5,30),Point(295,95))
        white2 = Rectangle(Point(5,100),Point(295,187))
        white3 = Rectangle(Point(5,193),Point(295,295))
        white1.setFill('black')
        white2.setFill('black')
        white3.setFill('black')
        white1.draw(win4)
        white2.draw(win4)
        white3.draw(win4)
        line1 = Text(Point(150,45),'Boilerbucks lets you buy 4 themes:')
        line2a = Text(Point(75,75),'Winter(100 boilerbucks)'+'\n'+'Party(140 boilerbucks)')
        line2b = Text(Point(215,75),'Underwater(100 boilerbucks)'+'\n'+'sky(140 boilerbucks)')
        line3 = Text (Point(150,145),'Player starts with 50 boilerbucks. They can bet 5 '+'\n'+'boilerbucks at the beginning of and during a round. They'+'\n'+'cannot bet boilerbucks after the game is won. After betting,'+'\n'+'if they guess the word correctly, they earn'+'\n'+'10x(length of word) boilerbucks. Even without betting'+'\n'+'the player can win 2 boilerbucks for winning a round.')
        line4 = Text (Point(150,243),'Once you have enough boilerbucks to buy a theme you'+'\n'+'can click on the theme button and buy it. After buying a'+'\n'+'theme you can click on the theme button again to apply the'+'\n'+'theme to your game panel. Make sure your game'+'\n'+'panel is open. You will retain the themes you have'+'\n'+'bought and the boilerbucks you have earned even after'+'\n'+'losing a game. You will lose them once you click in quit')
        line2a.setSize(8)
        line2b.setSize(8)
        line3.setSize(8)
        line4.setSize(8)
        line1.setFill('white')
        line2a.setFill('white')
        line2b.setFill('white')
        line3.setFill('white')
        line4.setFill('white')
        line1.draw(win4)
        line2a.draw(win4)
        line2b.draw(win4)
        line3.draw(win4)
        line4.draw(win4)
        close.draw(win4)
        close_text.draw(win4)
        # display an example black boilerbucks button on the next page of window
        sent1 = Text(Point(150,40),'CLICK on the ''BOILERBUCKS'' button'+'\n'+'to bet 5 boilerbucks')
        sent1.setSize(8)
        sent1a = Text(Point(150,58),'(The button in the control panel should be used for the actual game)')
        sent1a.setSize(7)
        boiler1 = Rectangle(Point(80,64),Point(220,104))
        boiler1_text = Text(Point(150,74),'BOILERBUCKS')
        boiler1_num = Text(Point(150,94),boiler_count)
        boiler1_text.setSize(9)
        boiler1.setFill('black')
        boiler1.setOutline('gold')
        boiler1_text.setStyle('bold')
        boiler1_text.setFill('gold')
        boiler1_num.setFill('gold')
        boiler1_num.setStyle('bold')
        # HITMAN is the example word
        # The length of the word x 10 will determine how many boilerbucks will be added upon a bet
        sent2 = Text(Point(150,123),'EXAMPLE : Let the secret word be:'+'\n'+'HITMAN (6 characters)')
        sent3 = Text(Point(150,160),'If you guess the word correctly you'+'\n'+'win 10x6 boilerbucks.You win additional'+'\n'+'2 boilerbucks for winning a round. CLICK to win!') 
        sent2.setSize(8)
        sent3.setSize(8)
        # instruction to explain what to do with boilerbucks
        sent4 = Text(Point(150,200),'You have enough boilerbucks to buy a theme'+'\n'+'CLICK on the theme button to buy it:')
        sent4.setSize(8)
        # winter theme is worth 100 boilerbucks
        # create a light blue button to display once the locked grey button is unlocked
        winter1 = Rectangle(Point(80,220),Point(220,250))
        winter1_grey = Rectangle(Point(80,220),Point(220,250))
        winter1.setFill('light blue')
        winter1_grey.setFill('light grey')
        winter1_text = Text (Point(150,235),"WINTER")
        winter1_grey_text = Text (Point(150,235),"100 BOILERBUCKS")
        winter1_text.setSize(10)
        winter1_grey_text.setSize(8)
        winter1_text.setTextColor('white')
        # user must click on the theme button every round to use the theme when it is unlocked
        sent5 = Text(Point(150,275),'Remember to click on the theme button again'+'\n'+'to apply the theme to your game panel'+'\n'+'CLICK on CLOSE button to exit.')
        sent5.setSize(8)
        return win4,click_cont, white1, white2, white3, line1, line2a,line2b, line3, line4, sent1,sent1a,boiler1,boiler1_text, boiler1_num, boiler_count,sent2,sent3,sent4,sent5,winter1,winter1_grey,winter1_text,winter1_grey_text,top_sent

# define sky() with clouds for the sky theme
def sky(win1):
    # Lose: change background to 'light grey' and change clouds to 'dark grey'
    # win: move clouds out of window and rise a yellow circle into the
    #   window to represent the sun
    # change background to blue for sky
    win1.setBackground('light blue')
    # make cloud 1 with 5 white circles
    cloud1a = Circle(Point(50,140),15)
    cloud1a.draw(win1)
    cloud1a.setFill('white')
    cloud1a.setOutline('white')
    cloud2a = Circle(Point(80,130),20)
    cloud2a.draw(win1)
    cloud2a.setFill('white')
    cloud2a.setOutline('white')
    cloud3a = Circle(Point(70,155),20)
    cloud3a.draw(win1)
    cloud3a.setFill('white')
    cloud3a.setOutline('white')
    cloud4a = Circle(Point(100,160),20)
    cloud4a.draw(win1)
    cloud4a.setFill('white')
    cloud4a.setOutline('white')
    cloud5a = Circle(Point(115,137),20)
    cloud5a.draw(win1)
    cloud5a.setFill('white')
    cloud5a.setOutline('white')
    #make cloud 2 with 5 white circles
    cloud1b = Circle(Point(50-25,140+100),15)
    cloud1b.draw(win1)
    cloud1b.setFill('white')
    cloud1b.setOutline('white')
    cloud2b = Circle(Point(80-25,130+100),20)
    cloud2b.draw(win1)
    cloud2b.setFill('white')
    cloud2b.setOutline('white')
    cloud3b = Circle(Point(70-25,155+100),20)
    cloud3b.draw(win1)
    cloud3b.setFill('white')
    cloud3b.setOutline('white')
    cloud4b = Circle(Point(100-25,160+100),20)
    cloud4b.draw(win1)
    cloud4b.setFill('white')
    cloud4b.setOutline('white')
    cloud5b = Circle(Point(115-25,137+100),20)
    cloud5b.draw(win1)
    cloud5b.setFill('white')
    cloud5b.setOutline('white')
    #make cloud 3 with 5 white circles
    cloud1c = Circle(Point(50+250,140+140),15)
    cloud1c.draw(win1)
    cloud1c.setFill('white')
    cloud1c.setOutline('white')
    cloud2c = Circle(Point(80+250,130+140),20)
    cloud2c.draw(win1)
    cloud2c.setFill('white')
    cloud2c.setOutline('white')
    cloud3c = Circle(Point(70+250,155+140),20)
    cloud3c.draw(win1)
    cloud3c.setFill('white')
    cloud3c.setOutline('white')
    cloud4c = Circle(Point(100+250,160+140),20)
    cloud4c.draw(win1)
    cloud4c.setFill('white')
    cloud4c.setOutline('white')
    cloud5c = Circle(Point(115+250,137+140),20)
    cloud5c.draw(win1)
    cloud5c.setFill('white')
    cloud5c.setOutline('white')
    # create a yellow circle to represent the sun
    sun = Circle(Point(40,430),30)
    sun.setFill('yellow')
    sun.setOutline('yellow')
    sun.draw(win1)
    return cloud1a,cloud2a,cloud3a,cloud4a,cloud5a,cloud1b,cloud2b,cloud3b,cloud4b,cloud5b,cloud1c,cloud2c,cloud3c,cloud4c,cloud5c,sun

# define party() with balloons for the party theme
def party(win1,ice):
# change background to pink
    win1.setBackground('light pink')
    for i in ice:
        i.setFill('light pink')
        i.setOutline('light pink')
# create 5 ballons of different colors
    top1 = Circle(Point(50,130),25)
    top1.draw(win1)
    top1.setFill('red')
    bottom1 = Polygon(Point(50,155),Point(40,165),Point(60,165))
    bottom1.draw(win1)
    bottom1.setFill('red')
    string1 = Line(Point(50,165),Point(50,205))
    string1.draw(win1)
    top2 = Circle(Point(50+55,130+70),25)
    top2.draw(win1)
    top2.setFill('green')
    bottom2 = Polygon(Point(50+55,155+70),Point(40+55,165+70),Point(60+55,165+70))
    bottom2.draw(win1)
    bottom2.setFill('green')
    string2 = Line(Point(50+55,165+70),Point(50+55,205+70))
    string2.draw(win1)
    top3 = Circle(Point(50-20,130+100),25)
    top3.draw(win1)
    top3.setFill('yellow')
    bottom3 = Polygon(Point(50-20,155+100),Point(40-20,165+100),Point(60-20,165+100))
    bottom3.draw(win1)
    bottom3.setFill('yellow')
    string3 = Line(Point(50-20,165+100),Point(50-20,205+100))
    string3.draw(win1)
    top4 = Circle(Point(50+320,130),25)
    top4.draw(win1)
    top4.setFill('light blue')
    bottom4 = Polygon(Point(50+320,155),Point(40+320,165),Point(60+320,165))
    bottom4.draw(win1)
    bottom4.setFill('light blue')
    string4 = Line(Point(50+320,165),Point(50+320,205))
    string4.draw(win1)
    top5 = Circle(Point(50+310,130+120),25)
    top5.draw(win1)
    top5.setFill('purple')
    bottom5 = Polygon(Point(50+310,155+120),Point(40+310,165+120),Point(60+310,165+120))
    bottom5.draw(win1)
    bottom5.setFill('purple')
    string5 = Line(Point(50+310,165+120),Point(50+310,205+120))
    string5.draw(win1)
    # return objects
    return top1,top2,top3,top4,top5,bottom1,bottom2,bottom3,bottom4,bottom5,string1,string2,string3,string4,string5
                
# define underwater() theme with fish in background
def underwater(win1):
        # set background to blue to represent water
        win1.setBackground("light blue")
        # create 5 fish of different colors
        body1 = Oval(Point(230,270), Point(280,310))
        body1.draw(win1)
        body1.setFill('orange')
        body1.setOutline('orange')
        fin1 = Polygon(Point(210,270),Point(210,310),Point(240,290))
        fin1.draw(win1)
        fin1.setFill('orange')
        fin1.setOutline('orange')
        dot1 = Circle(Point(265,285),3)
        dot1.draw(win1)
        dot1.setFill('black')
        body2 = Oval(Point(50,100), Point(100,140))
        body2.draw(win1)
        body2.setFill('pink')
        body2.setOutline('pink')
        fin2 = Polygon(Point(30,100),Point(30,140),Point(60,120))
        fin2.draw(win1)
        fin2.setFill('pink')
        fin2.setOutline('pink')
        dot2 = Circle(Point(85,115),3)
        dot2.draw(win1)
        dot2.setFill('black')
        body3 = Oval(Point(340,190), Point(390,230))
        body3.draw(win1)
        body3.setFill('purple')
        body3.setOutline('purple')
        fin3 = Polygon(Point(320,190),Point(320,230),Point(350,210))
        fin3.draw(win1)
        fin3.setFill('purple')
        fin3.setOutline('purple')
        dot3 = Circle(Point(375,205),3)
        dot3.draw(win1)
        dot3.setFill('black')
        body4 = Oval(Point(70,200), Point(120,240))
        body4.draw(win1)
        body4.setFill('light green')
        body4.setOutline('light green')
        fin4 = Polygon(Point(50,200),Point(50,240),Point(80,220))
        fin4.draw(win1)
        fin4.setFill('light green')
        fin4.setOutline('light green')
        dot4 = Circle(Point(105,215),3)
        dot4.draw(win1)
        dot4.setFill('black')
        body1b = Oval(Point(-170,270), Point(-120,310))
        body1b.draw(win1)
        body1b.setFill('orange')
        body1b.setOutline('orange')
        fin1b = Polygon(Point(-190,270),Point(-190,310),Point(-160,290))
        fin1b.draw(win1)
        fin1b.setFill('orange')
        fin1b.setOutline('orange')
        dot1b = Circle(Point(-135,285),3)
        dot1b.draw(win1)
        dot1b.setFill('black')
        body2b = Oval(Point(-350,100), Point(-300,140))
        body2b.draw(win1)
        body2b.setFill('pink')
        body2b.setOutline('pink')
        fin2b = Polygon(Point(-370,100),Point(-370,140),Point(-340,120))
        fin2b.draw(win1)
        fin2b.setFill('pink')
        fin2b.setOutline('pink')
        dot2b = Circle(Point(-315,115),3)
        dot2b.draw(win1)
        dot2b.setFill('black')
        body3b = Oval(Point(-60,190), Point(-10,230))
        body3b.draw(win1)
        body3b.setFill('purple')
        body3b.setOutline('purple')
        fin3b = Polygon(Point(-80,190),Point(-80,230),Point(-50,210))
        fin3b.draw(win1)
        fin3b.setFill('purple')
        fin3b.setOutline('purple')
        dot3b = Circle(Point(-25,205),3)
        dot3b.draw(win1)
        dot3b.setFill('black')
        body4b = Oval(Point(-330,200), Point(-280,240))
        body4b.draw(win1)
        body4b.setFill('light green')
        body4b.setOutline('light green')
        fin4b = Polygon(Point(-350,200),Point(-350,240),Point(-320,220))
        fin4b.draw(win1)
        fin4b.setFill('light green')
        fin4b.setOutline('light green')
        dot4b = Circle(Point(-295,215),3)
        dot4b.draw(win1)
        dot4b.setFill('black')
        # return objects
        return body1,body2,body3,body4,fin1,fin2,fin3,fin4,dot1,dot2,dot3,dot4,body1b,body2b,body3b,body4b,fin1b,fin2b,fin3b,fin4b,dot1b,dot2b,dot3b,dot4b

# define winter() with a snowman and icicles for winter theme
def winter(win1):
# set background to light blue
    win1.setBackground('light blue')
    # create a snowman with a eyes, hat, buttons and carrot nose
    snow1 = Circle(Point(55,270),45)
    snow1.draw(win1)
    snow1.setFill('white')
    snow1.setOutline('white')
    snow2 = Circle(Point(55,200),35)
    snow2.draw(win1)
    snow2.setFill('white')
    snow2.setOutline('white')
    eye1 = Circle(Point(42,190),5)
    eye1.draw(win1)
    eye1.setFill('black')
    eye1 = Circle(Point(70,190),5)
    eye1.draw(win1)
    eye1.setFill('black')
    nose= Polygon(Point(55,210),Point(80,205),Point(55,200))
    nose.draw(win1)
    nose.setFill('orange')
    nose.setOutline('orange')
    buttons = []
    for i in range(0,3*20,20):
        button = Circle(Point(snow1.getCenter().getX(),250+i),5)
        button.draw(win1)
        button.setFill('black')
    hat1 = Line(Point(20,168),Point(90,168))
    hat1.draw(win1)
    hat1.setWidth(10)
    hat1.setFill('brown')
    hat2 = Line(Point(30,150),Point(80,150))
    hat2.draw(win1)
    hat2.setWidth(45)
    hat2.setFill('brown')

# defining bubble_sort() which takes on argument and returns one value
def bubble_sort(data):
# getting the length of the list to be sorted
    n = len(data)
# for loop to make sure there are enough iterations     
    for i in range(n):
# for loop for each iteration            
        for j in range(0, n-1):
# checking if the value before is less than the value after and then switching the positions
#       of all the elements in the list of lists
            if int(data[j][2]) < int(data[j+1][2]) :
                data[j][2], data[j+1][2] = data[j+1][2], data[j][2]
                data[j][1], data[j+1][1] = data[j+1][1], data[j][1]
                data[j][0], data[j+1][0] = data[j+1][0], data[j][0]
# returning the sorted list
    return data

# defining scroll() which takes two arguments and returns nothing
def scroll(text,win3):
        con = True
# while to check if con is true
        while con:
# checking for mouse click 
                p = win3.checkMouse()
# if there is a mouseclick assigning con as false to exit the while loop
                if p != None:
                        con = False
# if no mouse click is detected the text is made to scroll
                else:
                        text.move(0,-10)
                        sleep(0.07)
# once outside the while loop the window is closed
        win3.close()

# define high_score() to create a window that can display the top 7 highscores        
def high_score():
# create window
    win3= GraphWin('High Scores',300,300)
    win3.setBackground('white')
    stats=[]
    line_list=[]
    d =""
    infile1 = open('scores.txt','r')
# creatinga a new file and opening it in write mode
    outfile = open('high_scores.txt','w')
# seperating the data in each line and storing it in stats[]
    for line in infile1:
        line = line.strip('\n')
        data=line.split(',')
        stats.append(data)
    infile1.close()
# sorting stats list by calling bubble_sort()
    stats=bubble_sort(stats)
# for loop to create 200 entries
    for j in range(200):
# writing into the created file
            print('Player        Rounds    Score',file=outfile)
            print('=-'*15,file = outfile)
# only writing the top 7 scores
            for i in range(7):
                print('{:15s}{:3d}{:11d}'.format(stats[i][0],int(stats[i][1]),int(stats[i][2])),file=outfile)
            print('',file = outfile)
    outfile.close()
# creating a single text object with all the contents of the file
    infile2 = open('high_scores.txt','r')
    for line in infile2:
        d = d+line
    text = Text(Point(150,150),d)
    text.setSize(12)
    text.setFace("courier")
    text.draw(win3)
    infile2.close()
# returning the required values
    return text,win3

# defining random(), which takes a string argument and returns two strings and
# one list
def random(window):
    # defining required variables
    len1=0
    rect_list=[]
# opening data file 'words.txt'
    infile=open("words.txt","r")
# Counting the number of lines(words) in the file and storing
# in 'len1'
    for line in infile:
        len1+=1
# closing the data file
    infile.close()
# reopening data file to start reading from the beginning again
    infile=open("words.txt","r")
# choosing a random word
    list1=[]
    r=randint(0,len1+1)
    for i in range(r):
        line=infile.readline()
# determining the length of the selected word
    length= len(line)-1
# Calculating the X coordinate of the first golden rectangle     
    X = (400 - length*50)/2
# creating the golden rectangles and golden letters in the rectangles    
    for i in range(length):
        rect= Rectangle(Point(X,40),Point(X+50,90))
        alphabet= Text(Point(X+25, 65),line[i])
        alphabet.setStyle('bold')
        alphabet.setSize(16)
        list1.append(alphabet)
        rect.setFill('gold')
        rect_list.append(rect)
        X+=50
# drawing the the golden letters and rectangles        
    for i in range(length):
        rect_list[i].draw(window)
        list1[i].setTextColor('gold')
        list1[i].draw(window)
# defining placeholder string
    placeholder = "_"*length
# closing the file    
    infile.close()
    word_list=list(line[:-1])
# returning the selected word, the letter list and the placeholder string
    return line[:-1],word_list,list1,placeholder,rect_list

# defining drop() which takes one argument and returns nothing
def drop(polygon):
# changing the color of the polygon and moving it outside the screen
    polygon.setFill('red')
    point = polygon.getPoints()
    dy = - point[3].getY() + 401
    for x in range(10):
        polygon.move(0,dy/10)
# modifying the speed of the moving polygon
        sleep(0.07)
# defining guess() which takes nine arguments 
def guess(c,word,text,placeholder,score,score_num,polygon_list,i,m):
# defining the required variables
    place=list(placeholder)
    str1=""
# checking if the guessed character is in the word
    for x in range(len(word)):
        if (word[x]==c):
            place[x]=c
# changing the color of the letter(guessed character) in the golden rectangle
# to black
            text[x].setTextColor('black')
    str1=str1.join(place)
# checking if the guess is wrong
    if str1==placeholder:
# dropping a polygon since the
        drop(polygon_list[i])
# incrementing m to count one of the 10 tries
        m+=1
# incrementing i so that the next polygon is dropped after a wrong guess
        i+=1
# decrementing score_num as the guess is wrong
        score_num=score_num-1
# updating the score text object 
        score.setText('SCORE:  '+str(score_num))
# palceholder string is assigned the updated string
    placeholder=str1
# Returns updated placeholder string, the score_num, i(keeps track of the number of tries) and m(keeps track of the polygons dropped)
    return placeholder, score_num,i,m
    

# defining create_polygon() which takes one argument(window name) and returns a lisr 
def create_polygon(win1):
# creating 10 white polygons
    poly1= Polygon(Point(110,312),Point(185,312),Point(192,282),Point(117,282))
    poly2= Polygon(Point(125,282),Point(184,282),Point(191,237),Point(132,237))
    poly3 = Polygon(Point(132,237),Point(191,237),Point(198,192),Point(139,192))
    poly4 = Polygon(Point(139,192),Point(198,192),Point(205,147),Point(146,147))
    poly5 = Polygon(Point(146,147),Point(205,147),Point(212,102),Point(153,102))
    poly6 = Polygon(Point(205,147),Point(264,147),Point(271,102),Point(212,102))
    poly7 = Polygon(Point(264,147),Point(323,147),Point(330,102),Point(271,102))
    poly8 = Polygon(Point(257,192),Point(316,192),Point(323,147),Point(264,147))
    poly9 = Polygon(Point(250,237),Point(309,237),Point(316,192),Point(257,192))
    poly10 = Polygon(Point(191,237),Point(250,237),Point(257,192),Point(198,192))
    poly1.setFill('white')
    poly2.setFill('white')
    poly3.setFill('white')
    poly4.setFill('white')
    poly5.setFill('white')
    poly6.setFill('white')
    poly7.setFill('white')
    poly8.setFill('white')
    poly9.setFill('white')
    poly10.setFill('white')
# drawing the white polygons
    poly1.draw(win1)
    poly2.draw(win1)
    poly3.draw(win1)
    poly4.draw(win1)
    poly5.draw(win1)
    poly6.draw(win1)
    poly7.draw(win1)
    poly8.draw(win1)
    poly9.draw(win1)
    poly10.draw(win1)
# creating black polygons
    poly1b= Polygon(Point(110,312),Point(185,312),Point(192,282),Point(117,282))
    poly2b= Polygon(Point(125,282),Point(184,282),Point(191,237),Point(132,237))
    poly3b = Polygon(Point(132,237),Point(191,237),Point(198,192),Point(139,192))
    poly4b = Polygon(Point(139,192),Point(198,192),Point(205,147),Point(146,147))
    poly5b = Polygon(Point(146,147),Point(205,147),Point(212,102),Point(153,102))
    poly6b = Polygon(Point(205,147),Point(264,147),Point(271,102),Point(212,102))
    poly7b = Polygon(Point(264,147),Point(323,147),Point(330,102),Point(271,102))
    poly8b = Polygon(Point(257,192),Point(316,192),Point(323,147),Point(264,147))
    poly9b = Polygon(Point(250,237),Point(309,237),Point(316,192),Point(257,192))
    poly10b = Polygon(Point(191,237),Point(250,237),Point(257,192),Point(198,192))
    poly1b.setFill('black')
    poly2b.setFill('black')
    poly3b.setFill('black')
    poly4b.setFill('black')
    poly5b.setFill('black')
    poly6b.setFill('black')
    poly7b.setFill('black')
    poly8b.setFill('black')
    poly9b.setFill('black')
    poly10b.setFill('black')
# storing the black polygons in list poly_list
    poly_list = [poly1b,poly2b,poly3b,poly4b,poly5b,poly6b,poly7b,poly8b,poly9b,poly10b]
# drawing the black polygons
    poly1b.draw(win1)
    poly2b.draw(win1)
    poly3b.draw(win1)
    poly4b.draw(win1)
    poly5b.draw(win1)
    poly6b.draw(win1)
    poly7b.draw(win1)
    poly8b.draw(win1)
    poly9b.draw(win1)
    poly10b.draw(win1)
# returns poly_list
    return poly_list
    
# defining game_panel() which accepts one argument
def game_panel(score_num):
# creating the game_panel window
    win1= GraphWin('Save the block P',400,400)
    win1.setBackground('gold')
# defining the required variables
    list1=[]
    list2=[]
    list3=[]
    check_list=[]
    check_c_list = []
    hint_list=[]
    random_list=[]
    i=20
    j=20
    k=65
    ice = []
# creating the ice objects in game panel so that they are drawn behind
#       the rectangles
    for a in range(0,400,10):
        tip = randint(20,100)
        triangle = Polygon(Point(a,0),Point(5+a,tip),Point(a+10,0))
        triangle.setFill('gold')
        triangle.setOutline('gold')
        triangle.draw(win1)
        ice.append(triangle)
# creating the score text
    score= Text(Point(200,15),'SCORE:  '+str(score_num))
    poly_list=create_polygon(win1)
# creating and drawing the 26 golden circles 
    for x in range(26):
        if x<13:
            circle=Circle(Point(i,342),15)
            circle.setFill('black')
            circle.draw(win1)
            list1.append(circle)
            i+=30
        else:
            circle=Circle(Point(j,375),15)
            circle.setFill('black')
            circle.draw(win1)
            list1.append(circle)
            j+=30
# creating and drawing 26 letter text objects
# making  two lists, consisting the letter text obejects and letter charactet
    for y in range(26):
        center=list1[y].getCenter()
        letter_text= Text(center,chr(k))
        letter= chr(k)
        list3.append(letter)
        hint_list.append(letter)
        letter_text.setTextColor('white')
        letter_text.setSize(12)
        list2.append(letter_text)
        k+=1
        letter_text.draw(win1)
    score.draw(win1)
# calling random() and assigning the returned values
    word,word_list,text,placeholder,rect_list=random(win1)
    for w in word_list:
        if w in hint_list:
            hint_list.remove(w)
# returning the required values, strings and objects
    return win1, word,len(word),placeholder,text,score,score_num,list1, list2,list3,poly_list, check_list, hint_list,random_list,ice,rect_list,check_c_list

# defining control_panel() which takes no arguments and returns a window variable
def control_panel():
    boiler_num = 50
# creating the control panel window
    win= GraphWin('Welcome to:',400,450)
# creating the title box,new button, quit button, and themebuttons with boilerbuck price
    title= Rectangle(Point(0,0) , Point(400,30))
    new= Rectangle(Point(30,60) , Point(120,100))
    Quit= Rectangle(Point(280,60) , Point(370,100))
    desp= Rectangle(Point(35,130) , Point(365,250))
    hint= Rectangle(Point(150,320),Point(250,350))
    high_scores= Rectangle(Point(150,65),Point(250,95))
    winter = Rectangle(Point(20,360),Point(120,390))
    underwater = Rectangle(Point(280,360),Point(380,390))
    sky = Rectangle(Point(20,410),Point(120,440))
    party = Rectangle(Point(280,410),Point(380,440))
    winter_grey = Rectangle(Point(20,360),Point(120,390))
    underwater_grey = Rectangle(Point(280,360),Point(380,390))
    sky_grey = Rectangle(Point(20,410),Point(120,440))
    party_grey = Rectangle(Point(280,410),Point(380,440))
    boilerbuck = Rectangle(Point(130,360),Point(270,400))
    what_boilerbuck = Rectangle(Point(130,410),Point(270,440))
    high_scores.setFill('black')
    hint.setFill('black')
    title.setFill('black')
    new.setFill('gold')
    Quit.setFill('black')
    desp.setFill('white')
    winter.setFill('light blue')
    underwater.setFill('light green')
    party.setFill('light pink')
    sky.setFill('white')
    winter_grey.setFill('light grey')
    underwater_grey.setFill('light grey')
    sky_grey.setFill('light grey')
    party_grey.setFill('light grey')
    boilerbuck.setFill('black')
    what_boilerbuck.setFill('gold')
    boilerbuck.setOutline('gold')
# creating the text objects for the title, new button,quit button, click message, and text of themes with prices
    title_text= Text(Point(200,15),'GUESS MASTER 3.0')
    new_text= Text(Point(75,80),'NEW')
    Quit_text= Text(Point(325,80),'QUIT')
    desp_text= Text(Point(200,190),'This is a game where your score is'+'\n'+'based on the number of 4-6 letter'+'\n'+'words you can guess within 10 tries.')
    click_text= Text(Point(200,290),'Click NEW to start a game...')
    hint_text= Text (Point(200,335),'HINT')
    winter_text = Text (Point(70,375),"WINTER")
    underwater_text = Text (Point(330,375),"UNDERWATER")
    sky_text = Text(Point(70,425),"SKY")
    party_text = Text(Point(330,425),'PARTY')
    winter_text = Text (Point(70,375),"WINTER")
    winter_grey_text = Text (Point(70,375),"100 BOILERBUCKS")
    underwater_grey_text = Text (Point(330,375),"120 BOILERBUCKS")
    sky_grey_text = Text(Point(70,425),"160 BOILERBUCKS")
    party_grey_text = Text(Point(330,425),'140 BOILERBUCKS')
    hint_text.setSize(11)
    high_score_text= Text (Point(200,80),'HIGH SCORES')
    boilerbuck_text = Text(Point(200,370),'BOILERBUCKS')
    what_boiler_text = Text(Point(200,425),'WHAT ARE BOILERBUCKS?')
    boiler = Text(Point(200,390),boiler_num)
    high_score_text.setSize(10)
    winter_text.setSize(10)
    underwater_text.setSize(10)
    sky_text.setSize(10)
    party_text.setSize(10)
    title_text.setSize(18)
    new_text.setSize(15)
    Quit_text.setSize(15)
    desp_text.setSize(11)
    click_text.setSize(18)
    boilerbuck_text.setSize(9)
    boiler.setSize(13)
    what_boiler_text.setSize(7)
    winter_grey_text.setSize(8)
    sky_grey_text.setSize(8)
    party_grey_text.setSize(8)
    underwater_grey_text.setSize(8)
    boiler.setStyle('bold')
    title_text.setStyle('bold')
    new_text.setStyle('bold')
    Quit_text.setStyle('bold')
    hint_text.setStyle('bold')
    boilerbuck_text.setStyle('bold')
    high_score_text.setStyle('bold')
    title_text.setTextColor('gold')
    new_text.setTextColor('black')
    Quit_text.setTextColor('gold')
    boilerbuck_text.setTextColor('gold')
    boiler.setTextColor('gold')
    hint_text.setTextColor('white')
    high_score_text.setTextColor('white')
    winter_text.setTextColor('white')
    underwater_text.setTextColor('white')
    party_text.setTextColor('white')
# drawing all the graphic objects
    title.draw(win)
    new.draw(win)
    Quit.draw(win)
    desp.draw(win)
    hint.draw(win)
    high_scores.draw(win)
    winter.draw(win)
    underwater.draw(win)
    sky.draw(win)
    party.draw(win)
    boilerbuck.draw(win)
    what_boilerbuck.draw(win)
    title_text.draw(win)
    new_text.draw(win)
    Quit_text.draw(win)
    desp_text.draw(win)
    click_text.draw(win)
    hint_text.draw(win)
    high_score_text.draw(win)
    winter_text.draw(win)
    underwater_text.draw(win)
    sky_text.draw(win)
    party_text.draw(win)
    boiler.draw(win)
    boilerbuck_text.draw(win)
    winter_grey.draw(win)
    underwater_grey.draw(win)
    party_grey.draw(win)
    sky_grey.draw(win)
    winter_grey_text.draw(win)
    sky_grey_text.draw(win)
    party_grey_text.draw(win)
    underwater_grey_text.draw(win)
    what_boiler_text.draw(win)
# returning the require values
    return win,boiler,boiler_num,winter_grey,underwater_grey, sky_grey, party_grey,winter_grey_text,underwater_grey_text, sky_grey_text, party_grey_text  


# calling the main() 
def main():
# condition to make sure the loop that checks if all ten tries are used up is only entered once
    exit_cond = False
# condition to make sure the loop that checks if game is won is only entered once
    new_cond = True
    cond1= False
    win,boiler,boiler_num,winter_grey,underwater_grey, sky_grey, party_grey,winter_grey_text,underwater_grey_text, sky_grey_text, party_grey_text=control_panel()
# condition to check if quit button is clicked
    condition = True
# condition which checks if new button or any theme is clicked
    new_game_condition= False
    hint_once= False
    boiler_once = False
    winter_once = True
    underwater_once = True
    party_once = True
    sky_once = True
    boiler_check = False
    winter_check = False
    underwater_check = False
    party_check = False
    sky_check = False
    win4_check = False
    m=0
    round_num = 1
    # checks for mouseclicks until condition is false
    while condition:
        p = win.checkMouse()
        if p!=None:
# checks if the user has clicked on quit button
            if p.getX()>=280 and p.getX()<=370 and p.getY()>=60 and p.getY()<=100:
                condition = False
# checks if user has clicked on new button
            if p.getX()>=30 and p.getX()<=120 and p.getY()>=60 and p.getY()<=100:
                cond1= False
# checks is a game_panel is already and closes it
                if new_game_condition:
                    win1.close()
                m = 0
                i=0
                score_num=10
                round_num = 1
                hint_once = True
                boiler_once = True
                winter_check = False
                underwater_check = False
                party_check = False
                sky_check = False
# calling the game_panel() once new button is clicked
                win1,word,length,placeholder,text,score,score_num,circles,letter_text, letter,poly_list,check_list,hint_list,random_list,ice,rect_list,check_c_list= game_panel(score_num)
                print(word)
                new_game_condition= True
# checks if the hint button is clicked
            if p.getX()>=150 and p.getX()<=250 and p.getY()>=320 and p.getY()<=350 and new_game_condition and hint_once:
# checks if there are enough polygons to drop
                if m<9:
# excluding the letters to choose from if they are already clicked
                    for c in check_list:
                        if c in hint_list:
                            hint_list.remove(c)
# for loop to choose 3 random letters
                    for num in range(3):
                        pick = choice(hint_list)
# checks if all the selected letters are different
                        while pick in  random_list:
                            pick = choice(hint_list)
                        random_list.append(pick)
# change the clicked letters to respective background colors for each theme
#       changes the letter circle color to the theme color
                        if winter_check or underwater_check or sky_check:
                                circles[ord(pick)-65].setFill('light blue')
                                letter_text[ord(pick)-65].setTextColor('black')
                        elif party_check:
                                circles[ord(pick)-65].setFill('light pink')
                                letter_text[ord(pick)-65].setTextColor('black')          
                        else:
                                circles[ord(pick)-65].setFill('gold')
                                letter_text[ord(pick)-65].setTextColor('black')
                        check_list.append(pick)
                        check_c_list.append(circles[ord(pick)-65])
# subtract the score by two and drop two polygons 
                    for num in range(2):
                        drop(poly_list[i])
                        m += 1
                        i += 1
                        score_num = score_num - 1
                        score.setText('SCORE:  '+str(score_num))
# if there are only 1/2 polygons left the hint button will cause them to fall and player loses game
                else:
                    drop(poly_list[m])
                    m += 1
                    i += 1
                    score_num = score_num - 1
                    score.setText('SCORE:  '+str(score_num))
# making hint_once false so that the button can only be pressed once in a round  
                hint_once= False
# checks if the high score button has been clicked       
            if p.getX()>=150 and p.getX()<=250 and p.getY()>=65 and p.getY()<=95:
# calling high_score() and assigning returned values
                text1, win3 = high_score()
# calling the scroll() function
                scroll(text1,win3)
# checks for a click on the BOILERBUCKS button only when player atleast has 5 boilerbucks to bet
#       button can only be clicked onc during a round
            if p.getX()>=130 and p.getX()<=270 and p.getY()>=360 and p.getY()<=400 and new_game_condition and boiler_num>=5 and boiler_once:
# reducing boilerbucks by 5 and updating the value in the text object
                boiler_num = boiler_num - 5
                boiler.setText(boiler_num)
# making sure the button can only be clicked once during a round
                boiler_check = True
                boiler_once = False
# checking if the winter theme button is clicked after been bought
#       the button can only be clicked if the game panel is open and the no other themes have been applied to the game panel for that round
            if p.getX()>=20 and p.getX()<=120 and p.getY()>=360 and p.getY()<=390 and winter_once == False and underwater_check== False and party_check == False and sky_check== False and new_game_condition:
                winter_check = True
                winter(win1)
# applying the theme to the game panel
                for a in ice:
                    a.setFill('white')
                    a.setOutline('light grey')
                for cir in circles:
                        if cir in check_c_list:
                                cir.setFill('light blue')
                for r in rect_list:
                        r.setFill('light blue')
                for t in text:
                        if t.getText() not in check_list:
                                t.setFill('light blue')
# checking for a click on the winter theme button the first time
#       the button can only be clicked when the player has enough boilerbucks to buy the theme 
            if p.getX()>=20 and p.getX()<=120 and p.getY()>=360 and p.getY()<=390 and boiler_num>=100 and winter_once:
                boiler_num= boiler_num - 100
                boiler.setText(boiler_num)
                winter_grey_text.undraw()
                winter_grey.undraw()
                winter_once = False
# buying and applying the underwater theme
            if p.getX()>=280 and p.getX()<=380 and p.getY()>=360 and p.getY()<=390 and underwater_once == False and winter_check == False and party_check == False and sky_check == False and new_game_condition:
                body1,body2,body3,body4,fin1,fin2,fin3,fin4,dot1,dot2,dot3,dot4,body1b,body2b,body3b,body4b,fin1b,fin2b,fin3b,fin4b,dot1b,dot2b,dot3b,dot4b = underwater(win1)
                underwater_check = True
                for a in ice:
                    a.setFill('light blue')
                    a.setOutline('light blue')
                for cir in circles:
                        if cir in check_c_list:
                                cir.setFill('light blue')
                for r in rect_list:
                        r.setFill('light blue')
                for t in text:
                        if t.getText() not in check_list:
                                t.setFill('light blue')
            if p.getX()>=280 and p.getX()<=380 and p.getY()>=360 and p.getY()<=390 and boiler_num>=120 and underwater_once:
                boiler_num= boiler_num - 120
                boiler.setText(boiler_num)
                underwater_grey_text.undraw()
                underwater_grey.undraw()
                underwater_once = False
# buying and applying the party theme
            if p.getX()>=280 and p.getX()<=380 and p.getY()>=410 and p.getY()<=440 and party_once == False and winter_check == False and underwater_check == False and sky_check == False and new_game_condition:
                top1,top2,top3,top4,top5,bottom1,bottom2,bottom3,bottom4,bottom5,string1,string2,string3,string4,string5 = party(win1,ice)
                party_check = True
                for cir in circles:
                        if cir in check_c_list:
                                cir.setFill('light pink')
                for r in rect_list:
                        r.setFill('light pink')
                for t in text:
                        if t.getText() not in check_list:
                                t.setFill('light pink')
            if p.getX()>=280 and p.getX()<=380 and p.getY()>=410 and p.getY()<=440 and boiler_num>=140 and party_once:
                boiler_num= boiler_num - 140
                boiler.setText(boiler_num)
                party_grey_text.undraw()
                party_grey.undraw()
                party_once = False
# buying and applying the sky theme
            if p.getX()>=20 and p.getX()<=120 and p.getY()>=410 and p.getY()<=440 and sky_once == False and winter_check == False and underwater_check == False and party_check==False and new_game_condition:
                cloud1a,cloud2a,cloud3a,cloud4a,cloud5a,cloud1b,cloud2b,cloud3b,cloud4b,cloud5b,cloud1c,cloud2c,cloud3c,cloud4c,cloud5c,sun = sky(win1)
                sky_check = True
                for b in ice:
                    b.setFill('light blue')
                    b.setOutline('light blue')
                for cir in circles:
                        if cir in check_c_list:
                                cir.setFill('light blue')
                for r in rect_list:
                        r.setFill('light blue')
                for t in text:
                        if t.getText() not in check_list:
                                t.setFill('light blue')
            if p.getX()>=20 and p.getX()<=120 and p.getY()>=410 and p.getY()<=440 and boiler_num>=160 and sky_once:
                boiler_num= boiler_num - 160
                boiler.setText(boiler_num)
                sky_grey_text.undraw()
                sky_grey.undraw()
                sky_once = False
# checking for a click on the 'what is boilerbucks' button
            if  p.getX()>=130 and p.getX()<=270 and p.getY()>=410 and p.getY()<=440:
# if there is an existing window open it closes it first
                    if win4_check:
                            win4.close()
# calling the what_boiler() function
                    win4,click_cont, white1, white2, white3, line1, line2a,line2b, line3, line4, sent1,sent1a,boiler1,boiler1_text,boiler1_num, boiler_count,sent2,sent3,sent4,sent5,winter1,winter1_grey,winter1_text,winter1_grey_text,top_sent = what_boiler()
                    win4_check = True
# keeping track of the number of clicks
                    b_count = 1
        if win4_check:
# checking for clicks on the 'what is boilerbucks' window
                p4 = win4.checkMouse()
                if p4 != None:
# checking if the close button is clicked
                        if p4.getX()>= 250 and p4.getX()<=290 and p4.getY()>=5 and p4.getY()<=25:
                                win4.close()
                                win4_check = False
# checking for a second click
                        elif b_count == 1:
# making changes accordingly
                                win4.setBackground('white')
                                click_cont.undraw()
                                white1.undraw()
                                white2.undraw()
                                white3.undraw()
                                line1.undraw()
                                line2a.undraw()
                                line2b.undraw()
                                line3.undraw()
                                line4.undraw()
                                top_sent.draw(win4)
                                sent1.draw(win4)
                                sent1a.draw(win4)
                                boiler1.draw(win4)
                                boiler1_text.draw(win4)
                                boiler1_num.draw(win4)
                                b_count = b_count + 1
# checking for the third click on the boilerbucks button which is only functional in this window
                        elif b_count == 2 and p4.getX()>= 80 and p4.getX()<=220 and p4.getY()>=60 and p4.getY()<=100:
# showing how boilerbucks work
                                boiler_count= boiler_count - 5
                                boiler1_num.setText(boiler_count)
                                sent2.draw(win4)
                                sent3.draw(win4)
                                b_count = b_count + 1
# checking for fourth click to display a example theme button
                        elif b_count == 3:
                                boiler_count= boiler_count + 62
                                boiler1_num.setText(boiler_count)
                                sent4.draw(win4)
                                winter1.draw(win4)
                                winter1_text.draw(win4)
                                winter1_grey.draw(win4)
                                winter1_grey_text.draw(win4)
                                b_count = b_count + 1
# checking for a fifth click on the the theme button
                        elif b_count == 4 and p4.getX()>= 80 and p4.getX()<=220 and p4.getY()>=230 and p4.getY()<=260:
# showing how to buy and apply the theme button
                                boiler_count= boiler_count - 100
                                boiler1_num.setText(boiler_count)
                                winter1_grey.undraw()
                                winter1_grey_text.undraw()
                                sent5.draw(win4)
                                b_count = b_count + 1
                                   
# checking if game_panel window is open
        if new_game_condition== True:
            p2 = win1.checkMouse()
            if p2!= None:
# checking if the player has lost and if they have clicked on the save button
                if exit_cond==True and p2.getX()>=175 and p2.getX()<=225 and p2.getY()>=235 and p2.getY()<=265 and name.getText()!='':
                    outfile = open('scores.txt','a')
# getting the user's name 
                    name1= name.getText()
                    outfile.write('')
# writing the saved score into 'scores.txt'
                    outfile.write(name1+','+str(round_num)+','+str(score_num)+'\n')
                    win1.close()
                    new_game_condition = False
                    outfile.close()
                    exit_cond = False
                    
                    
# closes the game_panel window, opens a new game_panel and updates the score is the user has one the round
                if new_cond==False:
                    win1.close()
                    win1,word,length,placeholder,text,score,score_num,circles,letter_text, letter,poly_list,check_list,hint_list,random_list,ice,rect_list,check_c_list= game_panel(score_num+10)
                    #print(word)
                    round_num = round_num + 1
                    m=0
                    i=0
# player earns 2 boilerbucks for winning a round
                    boiler_num = boiler_num + 2
                    boiler.setText(boiler_num)
                    new_cond = True
                    hint_once = True
                    boiler_once = True
                    
# for loop to check is the user has clicked on any of the letter circles and made a guess
                for j in range(len(circles)):
                    x= p2.getX()
                    y = p2.getY()
                    center = circles[j].getCenter()
                    radius = circles[j].getRadius()
                    distance = sqrt(((x-center.getX())**2) + ((y-center.getY())**2))
# checking is the user has clicked on any circle and hasn't used up all the 10 tries
                    if distance<=radius and m<10:
                        check= letter[j] in check_list
# checking the character clicked on has already been guessed and if the entire word has been guessed
                        if placeholder!=word and check == False:
# changing the color according to the theme of the circle and letter of the guessed character
                            if winter_check or underwater_check or sky_check:
                                    circles[j].setFill('light blue')
                                    letter_text[j].setTextColor('black')
                            elif party_check:
                                    circles[j].setFill('light pink')
                                    letter_text[j].setTextColor('black')
                            else:
                                    circles[j].setFill('gold')
                                    letter_text[j].setTextColor('black')
# updating the check list preventing the dropping of score if an already guessed character is clicked
                            check_list.append(letter[j])
                            check_c_list.append(circles[j])
# calling the guess()
                            placeholder,score_num,i,m=guess(letter[j], word,text,placeholder,score,score_num,poly_list,i,m)
                    

# checking is 10 tries have been used up
                    if m == 10 and cond1==False:
                        if winter_check:
                            for b in ice:
                                for q in range(10):
                                    b.move(0,600/10)
                                    sleep(0.01)
# displaying the theme animations for losing
                        if underwater_check:
                                win1.setBackground('light grey')
                                for s in ice:
                                        s.setFill('light grey')
                                        s.setOutline('light grey')
                                for r in rect_list:
                                        r.setFill('light grey')
                                for c in check_c_list:
                                        c.setFill('light grey')
                                dx = 400
                                body1.setFill('black')
                                fin1.setFill('black')
                                dot1.setFill('black')
                                body2.setFill('black')
                                fin2.setFill('black')
                                dot2.setFill('black')
                                body3.setFill('black')
                                fin3.setFill('black')
                                dot3.setFill('black')
                                body4.setFill('black')
                                fin4.setFill('black')
                                dot4.setFill('black')
                                body1.setOutline('black')
                                fin1.setOutline('black')
                                dot1.setOutline('black')
                                body2.setOutline('black')
                                fin2.setOutline('black')
                                dot2.setOutline('black')
                                body3.setOutline('black')
                                fin3.setOutline('black')
                                dot3.setOutline('black')
                                body4.setOutline('black')
                                fin4.setOutline('black')
                                dot4.setOutline('black')
                                # the fish swim towards the right
                                for x in range(10):
                                    body1.move(dx/10,0)
                                    fin1.move(dx/10,0)
                                    dot1.move(dx/10,0)
                                    body2.move(dx/10,0)
                                    fin2.move(dx/10,0)
                                    dot2.move(dx/10,0)
                                    body3.move(dx/10,0)
                                    fin3.move(dx/10,0)
                                    dot3.move(dx/10,0)
                                    body4.move(dx/10,0)
                                    fin4.move(dx/10,0)
                                    dot4.move(dx/10,0)
                                    sleep(0.5)
                        # lose in party theme
                        if party_check:
                                # pop the balloons
                                circle_red1 = Circle(Point(50,130),25)
                                circle_red2 = Circle(Point(105,200),25)
                                circle_red3 = Circle(Point(30,230),25)
                                circle_red4 = Circle(Point(370,130),25)
                                circle_red5 = Circle(Point(360,250),25)
                                circle_red1.setFill('red')
                                circle_red2.setFill('red')
                                circle_red3.setFill('red')
                                circle_red4.setFill('red')
                                circle_red5.setFill('red')
                                red_text1 = Text(Point(50,130),'POP!')
                                red_text2 = Text(Point(105,200),'POP!')
                                red_text3 = Text(Point(30,230),'POP!')
                                red_text4 = Text(Point(370,130),'POP!')
                                red_text5 = Text(Point(360,250),'POP!')
                                circle_red1.draw(win1)
                                red_text1.draw(win1)
                                string1.undraw()
                                bottom1.undraw()
                                top1.undraw()
                                circle_red1.move(0,5)
                                red_text1.move(0,5)
                                sleep(0.2)
                                circle_red1.undraw()
                                red_text1.undraw()
                                circle_red2.draw(win1)
                                red_text2.draw(win1)
                                string2.undraw()
                                bottom2.undraw()
                                top2.undraw()
                                circle_red2.move(0,5)
                                red_text2.move(0,5)
                                sleep(0.2)
                                circle_red2.undraw()
                                red_text2.undraw()
                                circle_red3.draw(win1)
                                red_text3.draw(win1)
                                string3.undraw()
                                bottom3.undraw()
                                top3.undraw()
                                circle_red3.move(0,5)
                                red_text3.move(0,5)
                                sleep(0.2)
                                circle_red3.undraw()
                                red_text3.undraw()
                                circle_red4.draw(win1)
                                red_text4.draw(win1)
                                string4.undraw()
                                bottom4.undraw()
                                top4.undraw()
                                circle_red4.move(0,5)
                                red_text4.move(0,5)
                                sleep(0.2)
                                circle_red4.undraw()
                                red_text4.undraw()
                                circle_red5.draw(win1)
                                red_text5.draw(win1)
                                string5.undraw()
                                bottom5.undraw()
                                top5.undraw()
                                circle_red5.move(0,5)
                                red_text5.move(0,5)
                                sleep(0.2)
                                circle_red5.undraw()
                                red_text5.undraw()
                        # lose in sky theme
                        if sky_check:
                                # the sky turns grey
                                win1.setBackground('light grey')
                                for a in ice:
                                        a.setFill('light grey')
                                        a.setOutline('light grey')
                                for b in rect_list:
                                        b.setFill('light grey')
                                for d in check_c_list:
                                        d.setFill('light grey')
                                # the clouds turn grey
                                cloud1a.setFill('grey')
                                cloud2a.setFill('grey')
                                cloud3a.setFill('grey')
                                cloud4a.setFill('grey')
                                cloud5a.setFill('grey')
                                cloud1b.setFill('grey')
                                cloud2b.setFill('grey')
                                cloud3b.setFill('grey')
                                cloud4b.setFill('grey')
                                cloud5b.setFill('grey')
                                cloud1c.setFill('grey')
                                cloud2c.setFill('grey')
                                cloud3c.setFill('grey')
                                cloud4c.setFill('grey')
                                cloud5c.setFill('grey')
                                cloud1a.setOutline('grey')
                                cloud2a.setOutline('grey')
                                cloud3a.setOutline('grey')
                                cloud4a.setOutline('grey')
                                cloud5a.setOutline('grey')
                                cloud1b.setOutline('grey')
                                cloud2b.setOutline('grey')
                                cloud3b.setOutline('grey')
                                cloud4b.setOutline('grey')
                                cloud5b.setOutline('grey')
                                cloud1c.setOutline('grey')
                                cloud2c.setOutline('grey')
                                cloud3c.setOutline('grey')
                                cloud4c.setOutline('grey')
                                cloud5c.setOutline('grey')
                                
# displaying text to tell the user they have lost and prompting the user to click to exit the game_panel
                        for t in text:
                                t.setFill('black')
                        over_text = Text(Point(200,150),'GAME IS OVER')
                        over_text.setFill('red')
                        over_text.setStyle('bold')
                        over_text.setSize(15)
                        over_text.draw(win1)
                        name= Entry(Point(200,200),10)
                        # user can enter their name upon lose
                        name.setFill('dark grey')
                        save_button = Rectangle(Point(175,235),Point(225,265))
                        save_button.setFill('black')
                        save_button.draw(win1)
                        save_text = Text (Point(200,250),'SAVE')
                        save_text.setFill('white')
                        save_text.draw(win1)
                        name.draw(win1)
                        boiler_once = False
                        cond1= True
                        exit_cond = True
                    # displaying the winning text and promting the user to click on the window to continue to the next round
                    if placeholder == word and new_cond:
                        # win in the underwater theme
                        if underwater_check:
                                # grass grows on the bottom of the windown
                                grass = []
                                dx = 400
                                dx1 = 400
                                for i in range(0,400,15):
                                    end = randint(20,110)
                                    blade = Polygon(Point(i,400),Point(5+i,400-end),Point(i+15,400))
                                    blade.setFill('green')
                                    blade.setOutline('green')
                                    blade.draw(win1)
                                    grass.append(blade)
                                # fish swim towards the right
                                for x in range(10):
                                    body1.move(dx/10,0)
                                    fin1.move(dx/10,0)
                                    dot1.move(dx/10,0)
                                    body2.move(dx/10,0)
                                    fin2.move(dx/10,0)
                                    dot2.move(dx/10,0)
                                    body3.move(dx/10,0)
                                    fin3.move(dx/10,0)
                                    dot3.move(dx/10,0)
                                    body4.move(dx/10,0)
                                    fin4.move(dx/10,0)
                                    dot4.move(dx/10,0)
                                    body1b.move(dx1/10,0)
                                    fin1b.move(dx1/10,0)
                                    dot1b.move(dx1/10,0)
                                    body2b.move(dx1/10,0)
                                    fin2b.move(dx1/10,0)
                                    dot2b.move(dx1/10,0)
                                    body3b.move(dx1/10,0)
                                    fin3b.move(dx1/10,0)
                                    dot3b.move(dx1/10,0)
                                    body4b.move(dx1/10,0)
                                    fin4b.move(dx1/10,0)
                                    dot4b.move(dx1/10,0)
                                    sleep(0.5)
                        # win in the party theme
                        if party_check:
                                dx = 310
                                # create a banner
                                colorList =['red','yellow','green','light blue','purple']
                                for i in range(0,400,40):
                                        banner = Polygon(Point(i,0),Point(20+i,30),Point(i+40,0))
                                        banner.draw(win1)
                                        color = choice(colorList)
                                        banner.setFill(color)
                                # make the balloons float upwards
                                for x in range(10):
                                        top1.move(0,-dx/10)
                                        bottom1.move(0,-dx/10)
                                        string1.move(0,-dx/10)
                                        top2.move(0,-dx/10)
                                        bottom2.move(0,-dx/10)
                                        string2.move(0,-dx/10)
                                        top3.move(0,-dx/10)
                                        bottom3.move(0,-dx/10)
                                        string3.move(0,-dx/10)
                                        top4.move(0,-dx/10)
                                        bottom4.move(0,-dx/10)
                                        string4.move(0,-dx/10)
                                        top5.move(0,-dx/10)
                                        bottom5.move(0,-dx/10)
                                        string5.move(0,-dx/10)
                                        sleep(0.1)
                        # move the clouds out of the screen towards the right with a win
                        if sky_check:
                                ds =300
                                de = 395
                                for s in range(10):
                                        cloud1a.move(ds/10,0)
                                        cloud2a.move(ds/10,0)
                                        cloud3a.move(ds/10,0)
                                        cloud4a.move(ds/10,0)
                                        cloud5a.move(ds/10,0)
                                        cloud1b.move(ds/10,0)
                                        cloud2b.move(ds/10,0)
                                        cloud3b.move(ds/10,0)
                                        cloud4b.move(ds/10,0)
                                        cloud5b.move(ds/10,0)
                                        cloud1c.move(ds/10,0)
                                        cloud2c.move(ds/10,0)
                                        cloud3c.move(ds/10,0)
                                        cloud4c.move(ds/10,0)
                                        cloud5c.move(ds/10,0)
                                        cloud1a.move(ds/10,0)
                                        cloud2a.move(ds/10,0)
                                        cloud3a.move(ds/10,0)
                                        cloud4a.move(ds/10,0)
                                        cloud5a.move(ds/10,0)
                                        cloud1b.move(ds/10,0)
                                        cloud2b.move(ds/10,0)
                                        cloud3b.move(ds/10,0)
                                        cloud4b.move(ds/10,0)
                                        cloud5b.move(ds/10,0)
                                        cloud1c.move(ds/10,0)
                                        cloud2c.move(ds/10,0)
                                        cloud3c.move(ds/10,0)
                                        cloud4c.move(ds/10,0)
                                        cloud5c.move(ds/10,0)
                                        sleep(0.05)
                                for sn in range(10):
                                        sun.move(0,-de/10)
                                        sleep(0.07)
                        # display winning message
                        win1_text = Text(Point(200,215),'YOU WIN - BOILER UP!')
                        win1_text.setFill('grey')
                        win1_text.setStyle('bold')
                        win1_text.setSize(15)
                        win1_text.draw(win1)
                        if boiler_check:
                            boiler_num = boiler_num + (length*10)
                            boiler.setText(boiler_num)
                            boiler_check = False
                        win1_text = Text(Point(200,245),'Click to continue')
                        win1_text.setFill('grey')
                        win1_text.draw(win1)
                        # conditions to continue with a new round
                        new_cond = False
                        # remove applied themes in new round
                        winter_check = False
                        underwater_check =  False
                        party_check = False
                        sky_check = False
# checking is 10 tries have been used up
            if m == 10 and cond1==False:
# displaying text to tell the user they have lost and prompting the user to click to exit the game_panel
                over_text = Text(Point(200,150),'GAME IS OVER')
                over_text.setFill('red')
                over_text.setStyle('bold')
                over_text.setSize(15)
                over_text.draw(win1)
                # display a text box for user to enter their name and save their score upon lose
                name= Entry(Point(200,200),10)
                name.setFill('dark grey')
                save_button = Rectangle(Point(175,235),Point(225,265))
                save_button.setFill('black')
                save_button.draw(win1)
                save_text = Text (Point(200,250),'SAVE')
                save_text.setFill('white')
                save_text.draw(win1)
                name.draw(win1)
                # set conditions for game over
                cond1= True
                exit_cond = True
                winter_check = False
                underwater_check = False
                party_check = False
                sky_check = False

# closing control panel window if the user has clicked in quit button                       
    win.close()
# checking if the game_panel window is open and then closing it as the quit button has been clicked
    if new_game_condition:
        win1.close()
# checking if the what_boiler() window is open and then closing it as the quit button has been clicked
    if win4_check:
            win4.close()
main()


                   
                    

    
    
    



