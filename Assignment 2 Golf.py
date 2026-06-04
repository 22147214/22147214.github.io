from tkinter import *

#Creating the page for golf leaderboard
root=Tk()
root.title("Crazy golf/golff gwallgof")
root.geometry("820x450")
root.resizable(False,False)
root.configure(background="#e1bbff")

#Creating the commands for buttons
def close():
    quit()



#code for team page
def team():
    team = Toplevel(root)
    team.title("Team golf/Golff Tîm")
    team.geometry("900x550")
    team.configure(background="#e1bbff")
    
    team_heading=Frame(team)
    a_head=Label(team_heading)

    team_heading.grid(row=0,column=2,columnspan=1,padx=10,pady=5)
    team_heading.configure(background="#00ffff")
    Label(team_heading,text="Names are required/mae angen enwau", font=('Arial',18)).grid(row=0,column=3,padx=0,pady=5)

    player_1=Label(team, text="Player/Chwaraewr 1", width=15, height=4)
    player_1.grid(row=1, column=1, padx=0, pady=5)
    player_1.config(bg="#6fa8dc")

    player_2=Label(team, text="Player/Chwaraewr 2", width=15, height=4)
    player_2.grid(row=2, column=1, padx=30, pady=5)
    player_2.config(bg="#ffd966")

    player_3=Label(team, text="Player/Chwaraewr 3", width=15, height=4)
    player_3.grid(row=3, column=1, padx=10, pady=5)
    player_3.config(bg="#cc0000")

    player_4=Label(team, text="Player/Chwaraewr 4", width=15, height=4)
    player_4.grid(row=4, column=1, padx=30, pady=5)
    player_4.config(bg="#6aa84f")

    player_5=Label(team, text="Player/Chwaraewr 5", width=15, height=4)
    player_5.grid(row=5, column=1, padx=10, pady=5)
    player_5.config(bg="#f7acff")

    player_1name=Entry(team,width=15,bg="#6fa8dc")
    player_1name.grid(row=1, column=3, padx=0, pady=5)

    player_2name=Entry(team,width=15,bg="#ffd966")
    player_2name.grid(row=2, column=3, padx=0, pady=5)

    player_3name=Entry(team,width=15,bg="#cc0000")
    player_3name.grid(row=3, column=3, padx=0, pady=5)

    player_4name=Entry(team,width=15,bg="#6aa84f")
    player_4name.grid(row=4, column=3, padx=0, pady=5)

    player_5name=Entry(team,width=15,bg="#f7acff")
    player_5name.grid(row=5, column=3, padx=0, pady=5)

    Go_Golfing=Button(team, text="Go Golfing/Ewch i Golff!", width=20, height=4, command=scoreboard)
    Go_Golfing.grid(row=3, column=4, padx=0, pady=5)
    Go_Golfing.config(bg="#00ffff")

    Exit=Button(team, text="Exit/Ymadael", width=15, height=4, command=close)
    Exit.grid(row=0, column=4, padx=30, pady=5)
    Exit.config(bg="#ff0000")

#code for scoreboard page
def scoreboard():
    global score1_number1, score1_number2, score1_number3
    global score1_number4, score1_number5, score1_number6
    global score1_number7, score1_number8, score1_number9
    global total_1
    global score2_number1, score2_number2, score2_number3
    global score2_number4, score2_number5, score2_number6
    global score2_number7, score2_number8, score2_number9
    global total_2
    global score3_number1, score3_number2, score3_number3
    global score3_number4, score3_number5, score3_number6
    global score3_number7, score3_number8, score3_number9
    global total_3
    global score4_number1, score4_number2, score4_number3
    global score4_number4, score4_number5, score4_number6
    global score4_number7, score4_number8, score4_number9
    global total_4
    global score5_number1, score5_number2, score5_number3
    global score5_number4, score5_number5, score5_number6
    global score5_number7, score5_number8, score5_number9
    global total_5
    scoreboard = Toplevel(root)
    scoreboard.title("Scoreboard for golf/Sgorfwrdd ar gyfer golff")
    scoreboard.geometry("900x1050")
    scoreboard.configure(background="#e1bbff")
    
    scoreboard_heading=Frame(scoreboard)
    f_head=Label(scoreboard_heading)

    scoreboard_heading.grid(row=0,column=3,columnspan=3,padx=10,pady=5)
    scoreboard_heading.configure(background="#00ffff")
    Label(scoreboard_heading,text="Scoreboard/Sgorfwrdd", font=('Arial',18)).grid(row=0,column=3,padx=0,pady=5)

    player_1=Label(scoreboard, text="Player/Chwaraewr 1", width=15, height=4)
    player_1.grid(row=1, column=2, padx=10, pady=5)
    player_1.config(bg="#6fa8dc")

    player_2=Label(scoreboard, text="Player/Chwaraewr 2", width=15, height=4)
    player_2.grid(row=1, column=3, padx=10, pady=5)
    player_2.config(bg="#ffd966")

    player_3=Label(scoreboard, text="Player/Chwaraewr 3", width=15, height=4)
    player_3.grid(row=1, column=4, padx=10, pady=5)
    player_3.config(bg="#cc0000")

    player_4=Label(scoreboard, text="Player/Chwaraewr 4", width=15, height=4)
    player_4.grid(row=1, column=5, padx=10, pady=5)
    player_4.config(bg="#6aa84f")

    player_5=Label(scoreboard, text="Player/Chwaraewr 5", width=15, height=4)
    player_5.grid(row=1, column=6, padx=10, pady=5)
    player_5.config(bg="#f7acff")

    

    total_score=Label(scoreboard, text="Total score/Cyfanswm sgôr", width=21, height=4)
    total_score.grid(row=11, column=1, padx=0, pady=5)
    total_score.config(bg="#bf4fff")



    hole_1=Label(scoreboard, text="Hole/Twll 1", width=15, height=4)
    hole_1.grid(row=2, column=1, padx=0, pady=5)
    hole_1.config(bg="#ff952d")

    hole_2=Label(scoreboard, text="Hole/Twll 2", width=15, height=4)
    hole_2.grid(row=3, column=1, padx=0, pady=5)
    hole_2.config(bg="#ff952d")

    hole_3=Label(scoreboard, text="Hole/Twll 3", width=15, height=4)
    hole_3.grid(row=4, column=1, padx=0, pady=5)
    hole_3.config(bg="#ff952d")

    hole_4=Label(scoreboard, text="Hole/Twll 4", width=15, height=4)
    hole_4.grid(row=5, column=1, padx=0, pady=5)
    hole_4.config(bg="#ff952d")

    hole_5=Label(scoreboard, text="Hole/Twll 5", width=15, height=4)
    hole_5.grid(row=6, column=1, padx=0, pady=5)
    hole_5.config(bg="#ff952d")

    hole_6=Label(scoreboard, text="Hole/Twll/Twll 6", width=15, height=4)
    hole_6.grid(row=7, column=1, padx=0, pady=5)
    hole_6.config(bg="#ff952d")

    hole_7=Label(scoreboard, text="Hole/Twll 7", width=15, height=4)
    hole_7.grid(row=8, column=1, padx=0, pady=5)
    hole_7.config(bg="#ff952d")

    hole_8=Label(scoreboard, text="Hole/Twll 8", width=15, height=4)
    hole_8.grid(row=9, column=1, padx=0, pady=5)
    hole_8.config(bg="#ff952d")

    hole_9=Label(scoreboard, text="Hole/Twll 9", width=15, height=4)
    hole_9.grid(row=10, column=1, padx=0, pady=5)
    hole_9.config(bg="#ff952d")

    

    score1_number1=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number1.grid(row=2, column=2, padx=0, pady=5)

    score1_number2=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number2.grid(row=3, column=2, padx=0, pady=5)

    score1_number3=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number3.grid(row=4, column=2, padx=0, pady=5)

    score1_number4=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number4.grid(row=5, column=2, padx=0, pady=5)

    score1_number5=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number5.grid(row=6, column=2, padx=0, pady=5)

    score1_number6=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number6.grid(row=7, column=2, padx=0, pady=5)

    score1_number7=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number7.grid(row=8, column=2, padx=0, pady=5)

    score1_number8=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number8.grid(row=9, column=2, padx=0, pady=5)

    score1_number9=Entry(scoreboard,width=15,bg="#6fa8dc")
    score1_number9.grid(row=10, column=2, padx=0, pady=5)



    score2_number1=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number1.grid(row=2, column=3, padx=0, pady=5)

    score2_number2=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number2.grid(row=3, column=3, padx=0, pady=5)

    score2_number3=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number3.grid(row=4, column=3, padx=0, pady=5)

    score2_number4=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number4.grid(row=5, column=3, padx=0, pady=5)

    score2_number5=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number5.grid(row=6, column=3, padx=0, pady=5)

    score2_number6=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number6.grid(row=7, column=3, padx=0, pady=5)

    score2_number7=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number7.grid(row=8, column=3, padx=0, pady=5)

    score2_number8=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number8.grid(row=9, column=3, padx=0, pady=5)

    score2_number9=Entry(scoreboard,width=15,bg="#ffd966")
    score2_number9.grid(row=10, column=3, padx=0, pady=5)

    

    score3_number1=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number1.grid(row=2, column=4, padx=0, pady=5)

    score3_number2=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number2.grid(row=3, column=4, padx=0, pady=5)

    score3_number3=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number3.grid(row=4, column=4, padx=0, pady=5)

    score3_number4=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number4.grid(row=5, column=4, padx=0, pady=5)

    score3_number5=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number5.grid(row=6, column=4, padx=0, pady=5)

    score3_number6=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number6.grid(row=7, column=4, padx=0, pady=5)

    score3_number7=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number7.grid(row=8, column=4, padx=0, pady=5)

    score3_number8=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number8.grid(row=9, column=4, padx=0, pady=5)

    score3_number9=Entry(scoreboard,width=15,bg="#cc0000")
    score3_number9.grid(row=10, column=4, padx=0, pady=5)

    

    score4_number1=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number1.grid(row=2, column=5, padx=0, pady=5)

    score4_number2=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number2.grid(row=3, column=5, padx=0, pady=5)

    score4_number3=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number3.grid(row=4, column=5, padx=0, pady=5)

    score4_number4=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number4.grid(row=5, column=5, padx=0, pady=5)

    score4_number5=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number5.grid(row=6, column=5, padx=0, pady=5)

    score4_number6=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number6.grid(row=7, column=5, padx=0, pady=5)

    score4_number7=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number7.grid(row=8, column=5, padx=0, pady=5)

    score4_number8=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number8.grid(row=9, column=5, padx=0, pady=5)

    score4_number9=Entry(scoreboard,width=15,bg="#6aa84f")
    score4_number9.grid(row=10, column=5, padx=0, pady=5)

    

    score5_number1=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number1.grid(row=2, column=6, padx=0, pady=5)

    score5_number2=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number2.grid(row=3, column=6, padx=0, pady=5)

    score5_number3=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number3.grid(row=4, column=6, padx=0, pady=5)

    score5_number4=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number4.grid(row=5, column=6, padx=0, pady=5)

    score5_number5=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number5.grid(row=6, column=6, padx=0, pady=5)

    score5_number6=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number6.grid(row=7, column=6, padx=0, pady=5)

    score5_number7=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number7.grid(row=8, column=6, padx=0, pady=5)

    score5_number8=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number8.grid(row=9, column=6, padx=0, pady=5)

    score5_number9=Entry(scoreboard,width=15,bg="#f7acff")
    score5_number9.grid(row=10, column=6, padx=0, pady=5)

    

    total_1=Label(scoreboard, width=15, height=4,)
    total_1.grid(row=11, column=2, padx=0, pady=5)
    total_1.config(bg="#bf4fff")

    total_2=Label(scoreboard, width=15, height=4,)
    total_2.grid(row=11, column=3, padx=0, pady=5)
    total_2.config(bg="#bf4fff")

    total_3=Label(scoreboard, width=15, height=4,)
    total_3.grid(row=11, column=4, padx=0, pady=5)
    total_3.config(bg="#bf4fff")

    total_4=Label(scoreboard, width=15, height=4,)
    total_4.grid(row=11, column=5, padx=0, pady=5)
    total_4.config(bg="#bf4fff")

    total_5=Label(scoreboard, width=15, height=4,)
    total_5.grid(row=11, column=6, padx=0, pady=5)
    total_5.config(bg="#bf4fff")

    

    Exit=Button(scoreboard, text="Exit/Ymadael", width=15, height=4, command=close)
    Exit.grid(row=1, column=1, padx=30, pady=5)
    Exit.config(bg="#ff0000")

    calculate_1=Button(scoreboard, text="Calculate/Cyfrifwch", command=total_player1)
    calculate_1.grid(row=12, column=2, pady=10)
    
    calculate_2=Button(scoreboard, text="Calculate/Cyfrifwch", command=total_player2)
    calculate_2.grid(row=12, column=3, pady=10)

    calculate_3=Button(scoreboard, text="Calculate/Cyfrifwch", command=total_player3)
    calculate_3.grid(row=12, column=4, pady=10)

    calculate_4=Button(scoreboard, text="Calculate/Cyfrifwch", command=total_player4)
    calculate_4.grid(row=12, column=5, pady=10)

    calculate_5=Button(scoreboard, text="Calculate/Cyfrifwch", command=total_player5)
    calculate_5.grid(row=12, column=6, pady=10)



def total_player1():

    entries = [
        score1_number1,
        score1_number2,
        score1_number3,
        score1_number4,
        score1_number5,
        score1_number6,
        score1_number7,
        score1_number8,
        score1_number9
    ]

    total = 0

    for entry in entries:
        try:
            total += int(entry.get())
        except:
            total += 0

    total_1.config(text=str(total))

    with open("total.txt", "a") as file:
        file.write(f"Total Player 1 Score: {total}\n")

def total_player2():

    entries = [
        score2_number1,
        score2_number2,
        score2_number3,
        score2_number4,
        score2_number5,
        score2_number6,
        score2_number7,
        score2_number8,
        score2_number9
    ]

    total = 0

    for entry in entries:
        try:
            total += int(entry.get())
        except:
            total += 0

    total_2.config(text=str(total))

    with open("total.txt", "a") as file:
        file.write(f"Total Player 2 Score: {total}\n")

def total_player3():

    entries = [
        score3_number1,
        score3_number2,
        score3_number3,
        score3_number4,
        score3_number5,
        score3_number6,
        score3_number7,
        score3_number8,
        score3_number9
    ]

    total = 0

    for entry in entries:
        try:
            total += int(entry.get())
        except:
            total += 0

    total_3.config(text=str(total))

    with open("total.txt", "a") as file:
        file.write(f"Total Player 3 Score: {total}\n")

    save_scores("Player 3", entries, total)

def total_player4():

    entries = [
        score4_number1,
        score4_number2,
        score4_number3,
        score4_number4,
        score4_number5,
        score4_number6,
        score4_number7,
        score4_number8,
        score4_number9
    ]

    total = 0

    for entry in entries:
        try:
            total += int(entry.get())
        except:
            total += 0

    total_4.config(text=str(total))

    with open("total.txt", "a") as file:
        file.write(f"Total Player 4 Score: {total}\n")

def total_player5():

    entries = [
        score5_number1,
        score5_number2,
        score5_number3,
        score5_number4,
        score5_number5,
        score5_number6,
        score5_number7,
        score5_number8,
        score5_number9
    ]

    total = 0

    for entry in entries:
        try:
            total += int(entry.get())
        except:
            total += 0

    total_5.config(text=str(total))

    with open("total.txt", "a") as file:
        file.write(f"Total Player 5 Score: {total}\n")

#code for score page

def score():
    global score1_number1, score1_number2, score1_number3
    global score1_number4, score1_number5, score1_number6
    global score1_number7, score1_number8, score1_number9
    global totals_1
    score = Toplevel(root)
    score.title("Score for golf/Sgôr ar gyfer golff")
    score.geometry("700x1050")
    score.configure(background="#e1bbff")
    
    score_heading=Frame(score)
    g_head=Label(score_heading)

    score_heading.grid(row=0,column=1,columnspan=2,padx=10,pady=5)
    score_heading.configure(background="#00ffff")
    Label(score_heading,text="Scoreboard/Sgorfwrdd", font=('Arial',18)).grid(row=0,column=3,padx=0,pady=5)

    player_1=Label(score, text="Solo/Unawd", width=15, height=4)
    player_1.grid(row=1, column=2, padx=0, pady=5)
    player_1.config(bg="#21deff")

    total_score=Label(score, text="Total score/Cyfanswm sgôr", width=21, height=4)
    total_score.grid(row=11, column=1, padx=0, pady=5)
    total_score.config(bg="#bf4fff")

    hole_1=Label(score, text="Hole/twll 1", width=15, height=4)
    hole_1.grid(row=2, column=1, padx=0, pady=5)
    hole_1.config(bg="#ff952d")

    hole_2=Label(score, text="Hole/twll 2", width=15, height=4)
    hole_2.grid(row=3, column=1, padx=0, pady=5)
    hole_2.config(bg="#ff952d")

    hole_3=Label(score, text="Hole/twll 3", width=15, height=4)
    hole_3.grid(row=4, column=1, padx=0, pady=5)
    hole_3.config(bg="#ff952d")

    hole_4=Label(score, text="Hole/twll 4", width=15, height=4)
    hole_4.grid(row=5, column=1, padx=0, pady=5)
    hole_4.config(bg="#ff952d")

    hole_5=Label(score, text="Hole/twll 5", width=15, height=4)
    hole_5.grid(row=6, column=1, padx=0, pady=5)
    hole_5.config(bg="#ff952d")

    hole_6=Label(score, text="Hole/twll 6", width=15, height=4)
    hole_6.grid(row=7, column=1, padx=0, pady=5)
    hole_6.config(bg="#ff952d")

    hole_7=Label(score, text="Hole/twll 7", width=15, height=4)
    hole_7.grid(row=8, column=1, padx=0, pady=5)
    hole_7.config(bg="#ff952d")

    hole_8=Label(score, text="Hole/twll 8", width=15, height=4)
    hole_8.grid(row=9, column=1, padx=0, pady=5)
    hole_8.config(bg="#ff952d")

    hole_9=Label(score, text="Hole/twll 9", width=15, height=4)
    hole_9.grid(row=10, column=1, padx=0, pady=5)
    hole_9.config(bg="#ff952d")

    

    score1_number1=Entry(score,width=15,bg="#21deff")
    score1_number1.grid(row=2, column=2, padx=0, pady=5)

    score1_number2=Entry(score,width=15,bg="#21deff")
    score1_number2.grid(row=3, column=2, padx=0, pady=5)

    score1_number3=Entry(score,width=15,bg="#21deff")
    score1_number3.grid(row=4, column=2, padx=0, pady=5)

    score1_number4=Entry(score,width=15,bg="#21deff")
    score1_number4.grid(row=5, column=2, padx=0, pady=5)

    score1_number5=Entry(score,width=15,bg="#21deff")
    score1_number5.grid(row=6, column=2, padx=0, pady=5)

    score1_number6=Entry(score,width=15,bg="#21deff")
    score1_number6.grid(row=7, column=2, padx=0, pady=5)

    score1_number7=Entry(score,width=15,bg="#21deff")
    score1_number7.grid(row=8, column=2, padx=0, pady=5)

    score1_number8=Entry(score,width=15,bg="#21deff")
    score1_number8.grid(row=9, column=2, padx=0, pady=5)

    score1_number9=Entry(score,width=15,bg="#21deff")
    score1_number9.grid(row=10, column=2, padx=0, pady=5)

    totals_1=Label(score, width=15, height=4,)
    totals_1.grid(row=11, column=2, padx=0, pady=5)
    totals_1.config(bg="#bf4fff")

    Exit=Button(score, text="Exit/Ymadael", width=15, height=4, command=close)
    Exit.grid(row=1, column=1, padx=30, pady=5)
    Exit.config(bg="#ff0000")

    calculate_1=Button(score, text="Calculate/Cyfrifwch", command=total_solo)
    calculate_1.grid(row=12, column=2, pady=10)

def total_solo():

    entries = [
        score1_number1,
        score1_number2,
        score1_number3,
        score1_number4,
        score1_number5,
        score1_number6,
        score1_number7,
        score1_number8,
        score1_number9
    ]

    total = 0

    for entry in entries:
        try:
            total += int(entry.get())
        except:
            total += 0

    totals_1.config(text=str(total))

    with open("total.txt", "a") as file:
        file.write(f"Total Solo Score: {total}\n")



#code for first individual page
def Individual_1():
    Individual_1 = Toplevel(root)
    Individual_1.title("Individual golf/Golff unigol")
    Individual_1.geometry("800x350")
    Individual_1.configure(background="#e1bbff")
    
    Individual1_heading=Frame(Individual_1)
    a_head=Label(Individual1_heading)

    Individual1_heading.grid(row=0,column=2,columnspan=1,padx=10,pady=5)
    Individual1_heading.configure(background="#00ffff")
    Label(Individual1_heading,text="Name is required/Mae angen enw", font=('Arial',18)).grid(row=0,column=3,padx=0,pady=5)

    individual1=Label(Individual_1, text="Individual/Unigol 1", width=15, height=4)
    individual1.grid(row=1, column=1, padx=0, pady=5)
    individual1.config(bg="#f7acff")

    individual1_name=Entry(Individual_1,width=15,bg="#f7acff")
    individual1_name.grid(row=1, column=3, padx=0, pady=5)

    Go_Golfing=Button(Individual_1, text="Go Golfing/Ewch i Golff!", width=20, height=4, command=score)
    Go_Golfing.grid(row=1, column=4, padx=0, pady=5)
    Go_Golfing.config(bg="#00ffff")

    Exit=Button(Individual_1, text="Exit/Ymadael", width=15, height=4, command=close)
    Exit.grid(row=0, column=4, padx=30, pady=5)
    Exit.config(bg="#ff0000")



#code for second individual page
def Individual_2():
    Individual_2 = Toplevel(root)
    Individual_2.title("Individual golf/Golff unigol")
    Individual_2.geometry("800x350")
    Individual_2.configure(background="#e1bbff")
    
    Individual2_heading=Frame(Individual_2)
    Individual2_heading.grid(row=0,column=2,columnspan=1,padx=10,pady=5)
    Individual2_heading.configure(background="#00ffff")

    b_head=Label(Individual2_heading)
    Label(Individual2_heading,text="Name is required/Mae angen enw", font=('Arial',18)).grid(row=0,column=2,padx=0,pady=5)

    individual2=Label(Individual_2, text="Individual/Unigol 2", width=15, height=4)
    individual2.grid(row=1, column=1, padx=0, pady=5)
    individual2.config(bg="#6fa8dc")

    individual2_name=Entry(Individual_2,width=15,bg="#6fa8dc")
    individual2_name.grid(row=1, column=3, padx=0, pady=5)

    Go_Golfing=Button(Individual_2, text="Go Golfing/Ewch i Golff!", width=20, height=4, command=score)
    Go_Golfing.grid(row=1, column=4, padx=0, pady=5)
    Go_Golfing.config(bg="#00ffff")

    Exit=Button(Individual_2, text="Exit/Ymadael", width=15, height=4, command=close)
    Exit.grid(row=0, column=4, padx=30, pady=5)
    Exit.config(bg="#ff0000")



#code for third individual page
def Individual_3():
    Individual_3 = Toplevel(root)
    Individual_3.title("Individual golf/Golff unigol")
    Individual_3.geometry("800x350")
    Individual_3.configure(background="#e1bbff")
    
    Individual3_heading=Frame(Individual_3)
    Individual3_heading.grid(row=0,column=2,columnspan=1,padx=10,pady=5)
    Individual3_heading.configure(background="#00ffff")

    c_head=Label(Individual3_heading)
    Label(Individual3_heading,text="Name is required/Mae angen enw", font=('Arial',18)).grid(row=0,column=2,padx=0,pady=5)

    individual3=Label(Individual_3, text="Individual/Unigol 3", width=15, height=4)
    individual3.grid(row=1, column=1, padx=0, pady=5)
    individual3.config(bg="#ffd966")

    individual3_name=Entry(Individual_3,width=15,bg="#ffd966")
    individual3_name.grid(row=1, column=3, padx=0, pady=5)

    Go_Golfing=Button(Individual_3, text="Go Golfing/Ewch i Golff!", width=20, height=4, command=score)
    Go_Golfing.grid(row=1, column=4, padx=0, pady=5)
    Go_Golfing.config(bg="#00ffff")

    Exit=Button(Individual_3, text="Exit/Ymadael", width=15, height=4, command=close)
    Exit.grid(row=0, column=4, padx=30, pady=5)
    Exit.config(bg="#ff0000")



#code for forth individual page
def Individual_4():
    Individual_4 = Toplevel(root)
    Individual_4.title("Individual golf/Golff unigol")
    Individual_4.geometry("800x350")
    Individual_4.configure(background="#e1bbff")
    
    Individual4_heading=Frame(Individual_4)
    Individual4_heading.grid(row=0,column=2,columnspan=1,padx=10,pady=5)
    Individual4_heading.configure(background="#00ffff")

    d_head=Label(Individual4_heading)
    Label(Individual4_heading,text="Name is required/Mae angen enw", font=('Arial',18)).grid(row=0,column=2,padx=0,pady=5)

    individual4=Label(Individual_4, text="Individual/Unigol 4", width=15, height=4)
    individual4.grid(row=1, column=1, padx=0, pady=5)
    individual4.config(bg="#cc0000")

    individual4_name=Entry(Individual_4,width=15,bg="#cc0000")
    individual4_name.grid(row=1, column=3, padx=0, pady=5)

    Go_Golfing=Button(Individual_4, text="Go Golfing/Ewch i Golff!", width=20, height=4, command=score)
    Go_Golfing.grid(row=1, column=4, padx=0, pady=5)
    Go_Golfing.config(bg="#00ffff")

    Exit=Button(Individual_4, text="Exit/allanfa", width=15, height=4, command=close)
    Exit.grid(row=0, column=4, padx=30, pady=5)
    Exit.config(bg="#ff0000")



#code for fifth individual page
def Individual_5():
    Individual_5 = Toplevel(root)
    Individual_5.title("Individual golf/unigol golff")
    Individual_5.geometry("800x350")
    Individual_5.configure(background="#e1bbff")
    
    Individual5_heading=Frame(Individual_5)
    Individual5_heading.grid(row=0,column=2,columnspan=1,padx=10,pady=5)
    Individual5_heading.configure(background="#00ffff")

    e_head=Label(Individual5_heading)
    Label(Individual5_heading,text="Name is required/mae angen enw", font=('Arial',18)).grid(row=0,column=2,padx=0,pady=5)

    individual5=Label(Individual_5, text="Individual/Unigol 5", width=15, height=4)
    individual5.grid(row=1, column=1, padx=0, pady=5)
    individual5.config(bg="#6aa84f")

    individual5_name=Entry(Individual_5,width=15,bg="#6aa84f")
    individual5_name.grid(row=1, column=3, padx=0, pady=5)

    Go_Golfing=Button(Individual_5, text="Go Golfing/Ewch i Golff!", width=20, height=4, command=score)
    Go_Golfing.grid(row=1, column=4, padx=0, pady=5)
    Go_Golfing.config(bg="#00ffff")

    Exit=Button(Individual_5, text="Exit/Ymadael", width=15, height=4, command=close)
    Exit.grid(row=0, column=4, padx=30, pady=5)
    Exit.config(bg="#ff0000")
    


#Creating the heading and buttons
frame_heading=Frame(root)
form_heading=Label(frame_heading)

frame_heading.grid(row=0,column=2,columnspan=3,padx=10,pady=5)
frame_heading.configure(background="#00ffff")
Label(frame_heading,text="Golfing competition/Cystadleuaeth golff", font=('Arial',18)).grid(row=0,column=3,padx=0,pady=5)

team_1=Button(root, text="Team/Tîm 1", width=15, height=4, command=team)
team_1.grid(row=1, column=1, padx=0, pady=5)
team_1.config(bg="#6fa8dc")

team_2=Button(root, text="Team/Tîm 2", width=15, height=4, command=team)
team_2.grid(row=1, column=2, padx=30, pady=5)
team_2.config(bg="#ffd966")

team_3=Button(root, text="Team/Tîm 3", width=15, height=4, command=team)
team_3.grid(row=1, column=3, padx=10, pady=5)
team_3.config(bg="#cc0000")

team_4=Button(root, text="Team/Tîm 4", width=15, height=4, command=team)
team_4.grid(row=1, column=4, padx=30, pady=5)
team_4.config(bg="#6aa84f")

team_5=Button(root, text="Team/Tîm 5", width=15, height=4, command=team)
team_5.grid(row=1, column=5, padx=10, pady=5)
team_5.config(bg="#f7acff")



individual_1=Button(root, text="Individual/unigol 1", width=15, height=4, command=Individual_1)
individual_1.grid(row=2, column=1, padx=0, pady=20)
individual_1.config(bg="#f7acff")

individual_2=Button(root, text="Individual/unigol 2", width=15, height=4, command=Individual_2)
individual_2.grid(row=2, column=2, padx=30, pady=5)
individual_2.config(bg="#6fa8dc")

individual_3=Button(root, text="Individual/unigol 3", width=15, height=4, command=Individual_3)
individual_3.grid(row=2, column=3, padx=30, pady=5)
individual_3.config(bg="#ffd966")

individual_4=Button(root, text="Individual/unigol 4", width=15, height=4, command=Individual_4)
individual_4.grid(row=2, column=4, padx=30, pady=5)
individual_4.config(bg="#cc0000")

individual_5=Button(root, text="Individual/unigol 5", width=15, height=4, command=Individual_5)
individual_5.grid(row=2, column=5, padx=30, pady=5)
individual_5.config(bg="#6aa84f")

Exit=Button(root, text="Exit/Ymadael", width=20, height=5, command=close)
Exit.grid(row=3, column=3, padx=30, pady=5)
Exit.config(bg="#ff0000")


    
root.mainloop()

