"""
Names: Connor Jones-Hebert
       Joslyn Perez
       Malik Watkins
       Taylor Smith
Assignment: Lab Project | Zanzibar
Date: 28 11 2022
"""
import random as r
import time
import tkinter.font as font
import turtle as t
from functools import partial
from tkinter import *


class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.dice_points = 0
        self.tokens = 20
        self.dice_one = r.randint(1, 6)
        self.dice_two = r.randint(1, 6)
        self.dice_three = r.randint(1, 6)
        self.zanzibar = False
        self.three_of_a_kind = False
        self.one_two_three = False

    def calc_points(self):
        roll = [self.dice_one, self.dice_two, self.dice_three]
        roll.sort()
        if roll == [4, 5, 6]:
            self.zanzibar = True
            self.three_of_a_kind = False
            self.one_two_three = False
            return 5000
        elif roll.count(roll[0]) == 3:
            self.zanzibar = False
            self.three_of_a_kind = True
            self.one_two_three = False
            points_rubric = {1: 4000, 2: 3000, 3: 2000, 4: 1000, 5: 900, 6: 800}
            return points_rubric[roll[0]]
        elif roll == [1, 2, 3]:
            self.zanzibar = False
            self.three_of_a_kind = False
            self.one_two_three = True
            return 700
        else:
            self.zanzibar = False
            self.one_two_three = False
            self.three_of_a_kind = False
            points_rubric = {1: 100, 6: 60, 2: 2, 3: 3, 4: 4, 5: 5}
            points = points_rubric[self.dice_one] + points_rubric[self.dice_two] + points_rubric[self.dice_three]
            return points

    def roll_dice(self):
        self.dice_one = r.randint(1, 6)
        self.dice_two = r.randint(1, 6)
        self.dice_three = r.randint(1, 6)
        self.dice_points = self.calc_points()

    def draw_one(self, x, y):
        t.penup()
        t.setx(x + 39)
        t.sety(y - 44)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

    def draw_two(self, x, y):
        t.penup()
        t.setx(x + 57)
        t.sety(y - 25)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 63)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

    def draw_three(self, x, y):
        t.penup()
        t.setx(x + 57)
        t.sety(y - 25)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 41)
        t.sety(y - 44)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 63)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

    def draw_four(self, x, y):
        t.penup()
        t.setx(x + 57)
        t.sety(y - 25)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.penup()
        t.setx(x + 57)
        t.sety(y - 63)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 63)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 25)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

    def draw_five(self, x, y):
        t.penup()
        t.setx(x + 57)
        t.sety(y - 25)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.penup()
        t.setx(x + 57)
        t.sety(y - 63)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 63)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 25)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 41)
        t.sety(y - 44)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

    def draw_six(self, x, y):
        t.penup()
        t.setx(x + 57)
        t.sety(y - 25)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.penup()
        t.setx(x + 57)
        t.sety(y - 63)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 63)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 25)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 25)
        t.sety(y - 44)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

        t.setx(x + 57)
        t.sety(y - 44)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()

    def draw_outline(self):
        print('----------------------------------')
        print(f"Dice one roll: {self.dice_one}")
        print(f"Dice two roll: {self.dice_two}")
        print(f"Dice three roll: {self.dice_three}")
        print('----------------------------------')

        for i in range(3):
            if i == 0:
                x, y = t.width() // 2 - 140, 0
                if self.dice_one == 1:
                    self.draw_one(x, y)
                elif self.dice_one == 2:
                    self.draw_two(x, y)
                elif self.dice_one == 3:
                    self.draw_three(x, y)
                elif self.dice_one == 4:
                    self.draw_four(x, y)
                elif self.dice_one == 5:
                    self.draw_five(x, y)
                elif self.dice_one == 6:
                    self.draw_six(x, y)
            elif i == 1:
                x, y = t.width() // 2 + 60, 0
                if self.dice_two == 1:
                    self.draw_one(x, y)
                elif self.dice_two == 2:
                    self.draw_two(x, y)
                elif self.dice_two == 3:
                    self.draw_three(x, y)
                elif self.dice_two == 4:
                    self.draw_four(x, y)
                elif self.dice_two == 5:
                    self.draw_five(x, y)
                elif self.dice_two == 6:
                    self.draw_six(x, y)
            else:
                x, y = t.width() // 2 - 40, -140
                if self.dice_three == 1:
                    self.draw_one(x, y)
                elif self.dice_three == 2:
                    self.draw_two(x, y)
                elif self.dice_three == 3:
                    self.draw_three(x, y)
                elif self.dice_three == 4:
                    self.draw_four(x, y)
                elif self.dice_three == 5:
                    self.draw_five(x, y)
                elif self.dice_three == 6:
                    self.draw_six(x, y)

    def adjust_tokens(self, tokens):
        self.tokens += tokens
        if self.tokens < 0:
            self.tokens = 0

    def get_number(self):
        return self.player_number

    def get_points(self):
        return self.dice_points

    def get_tokens(self):
        return self.tokens


def draw_round(player):
    t.setx(0)
    t.sety(370)
    t.write(f'---------- ROUND {round_num} ----------', align='center', font=('Algerian', 40, 'bold'))
    t.sety(300)
    t.write(f'Player {player.get_number()}, it is your turn.', align='center', font=('Algerian', 30, 'normal'))


def draw_die():
    t.setx(t.width() // 2 - 140)
    t.color('black', 'white')
    t.sety(0)
    t.begin_fill()
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.end_fill()

    t.setx(t.width() // 2 + 60)
    t.sety(0)
    t.begin_fill()
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.end_fill()

    t.setx(t.width() // 2 - 40)
    t.color('black', 'white')
    t.sety(-140)
    t.begin_fill()
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.end_fill()


def play_game():
    '''This is the main game loop that is played'''
    screen.bgcolor('#284d8a')
    t.color('black')
    p1 = players[0]
    roll_count = 0

    for i in range(3):
        t.clear()
        draw_round(p1)
        roll_count += 1
        p1.roll_dice()
        draw_die()
        p1.draw_outline()
        if p1.zanzibar:
            t.setx(0)
            t.sety(100)

            t.write('You got: (4, 5, 6) Zanzibar!', align='center', font=('8514oem', 30, 'normal'))

        elif p1.three_of_a_kind:
            t.setx(0)
            t.sety(100)

            t.write(f'You got: {(p1.dice_one, p1.dice_two, p1.dice_three)}', align='center',
                    font=('8514oem', 30, 'normal'))

        elif p1.one_two_three:
            t.setx(0)
            t.sety(100)

            t.write('You got: (1, 2, 3)', align='center', font=('8514oem', 30, 'normal'))

        else:
            t.setx(0)
            t.sety(100)

            t.write(f'You got: {p1.get_points()} points!', align='center', font=('8514oem', 30, 'normal'))

        print('----------------------------------')
        if i < 2:
            while True:
                try:
                    roll_again = t.textinput('Roll?', "Do you want to roll again? (Enter y/n): ").lower()
                    if roll_again not in ['y', 'n', 'yes', 'no']:
                        raise ValueError
                    break
                except (ValueError, TypeError, AttributeError):
                    print('Please enter y or n')
            if roll_again in ['n', 'no']:
                time.sleep(2.5)
                break
            else:
                continue
        time.sleep(2.5)
    print('----------------------------------')

    for p in players[1:]:
        print(f'Player {p.get_number()}, it is your turn.')
        for i in range(roll_count):
            t.clear()
            draw_round(p)
            p.roll_dice()
            draw_die()
            p.draw_outline()
            if p.zanzibar:
                t.setx(0)
                t.sety(100)

                t.write('You got: (4, 5, 6) Zanzibar!', align='center', font=('8514oem', 30, 'normal'))

            elif p.three_of_a_kind:
                t.setx(0)
                t.sety(100)

                t.write(f'You got: {(p.dice_one, p.dice_two, p.dice_three)}', align='center',
                        font=('8514oem', 30, 'normal'))

            elif p.one_two_three:
                t.setx(0)
                t.sety(100)

                t.write('You got: (1, 2, 3)', align='center', font=('8514oem', 30, 'normal'))

            else:
                t.setx(0)
                t.sety(100)

                t.write(f'You got: {p.get_points()} points!', align='center', font=('8514oem', 30, 'normal'))

            print('----------------------------------')
            if i < roll_count - 1:
                while True:
                    try:
                        roll_again = t.textinput('Roll?', "Do you want to roll again? (Enter y/n): ").lower()
                        if roll_again not in ['y', 'n', 'yes', 'no']:
                            raise ValueError
                        break
                    except (ValueError, TypeError, AttributeError):
                        print('Please enter y or n')
                if roll_again in ['n', 'no']:
                    time.sleep(2.5)
                    break
                else:
                    continue
            time.sleep(2.5)


def draw_standings():
    t.clear()
    t.setx(0)
    t.sety(370)
    t.write(f'---------- STANDINGS ----------', align='center', font=('Algerian', 40, 'bold'))


def draw_round_results():
    t.clear()
    t.setx(0)
    t.sety(370)
    t.write(f'---------- RESULTS FROM THE ROUND ----------', align='center', font=('Algerian', 40, 'bold'))


def determine_highest():
    screen.bgcolor('#133366')
    t.color('white')
    draw_round_results()
    highest_score = players[0]
    x, y = 0, 300
    for p in original_players:
        if p.zanzibar:
            t.setx(x)
            t.sety(y)

            t.write(f"Player {p.get_number()}'s points: Zanzibar", align='center', font=('8514oem', 30, 'normal'))

            print(f"Player {p.get_number()}'s points: Zanzibar", end=' ----- ')
        elif p.three_of_a_kind:
            t.setx(x)
            t.sety(y)

            t.write(f"Player {p.get_number()}'s points: {(p.dice_one, p.dice_two, p.dice_three)}", align='center',
                    font=('8514oem', 30, 'normal'))

            print(f"Player {p.get_number()}'s points: {(p.dice_one, p.dice_two, p.dice_three)}", end=' ----- ')
        elif p.one_two_three:
            t.setx(x)
            t.sety(y)

            t.write(f"Player {p.get_number()}'s points: (1, 2, 3)", align='center', font=('8514oem', 30, 'normal'))

            print(f"Player {p.get_number()}'s points: (1, 2, 3)", end=' ----- ')
        else:
            t.setx(x)
            t.sety(y)

            t.write(f"Player {p.get_number()}'s points: {p.get_points()}", align='center',
                    font=('8514oem', 30, 'normal'))

            print(f"Player {p.get_number()}'s points: {p.get_points()}", end=' ----- ')
        if p.get_points() > highest_score.get_points():
            highest_score = p
        y -= 40

    t.setx(0)
    t.sety(y - 100)
    t.write(f'Player {highest_score.get_number()} had the highest score!', align='center', font=('8514oem', 25, 'bold'))

    print(f'\nPlayer {highest_score.get_number()} had the highest score!', end=' ----- ')
    return highest_score


def determine_loser():
    lowest_score = players[0]
    for p in players:
        if p.get_points() < lowest_score.get_points():
            lowest_score = p
    t.setx(0)
    t.sety(t.ycor() - 70)
    t.write(f'Player {lowest_score.get_number()} had the lowest score!', align='center', font=('8514oem', 25, 'bold'))
    time.sleep(7.5)

    print(f'Player {lowest_score.get_number()} had the lowest score!')
    return lowest_score


def rearrange_order(round_winner):
    global players
    win_list = players[players.index(round_winner):]
    win_list = win_list + players[:players.index(round_winner)]
    players = win_list


def determine_token_num(round_winner):
    if round_winner.zanzibar:
        return 4
    elif round_winner.three_of_a_kind:
        return 3
    elif round_winner.one_two_three:
        return 2
    else:
        return 1


def adjust_tokens(loser, token_num):
    for p in players:
        if p == loser:
            p.adjust_tokens((len(players) - 1) * token_num)
        else:
            p.adjust_tokens(-1 * token_num)


def show_standings():
    screen.bgcolor('#133366')
    draw_standings()
    run = True
    print(players_num)
    if players_num > 5:
        x, y = -players_num * 70, 100
        alignment = 'left'
    else:
        x, y = 0, 100
        alignment = 'center'
    for p in original_players:
        t.setx(x)
        t.sety(y)

        t.write(f'Player {p.get_number()}: {p.get_tokens()} tokens', align=alignment, font=('8514oem', 25, 'normal'))

        print(f'Player {p.get_number()}: {p.get_tokens()} tokens', end='  ')
        y -= 70
        if y < - 200:
            x, y = x + 475, 100
        if p.get_tokens() <= 0:
            run = False
    print('\n')
    time.sleep(6.5)

    return run


def show_winners():
    screen.bgcolor('#237a3f')
    t.clear()
    t.setx(0)
    t.sety(370)
    t.write(f'---------- RESULTS ----------', align='center', font=('Algerian', 40, 'bold'))

    winners = []
    t.color('gold')
    for p in players:
        if p.get_tokens() == 0:
            winners.append(p)
    if len(winners) > 1:
        t.setx(-150)
        t.sety(0)

        t.write('The winners are: ', align='center', font=('8514oem', 30, 'normal'))

        print('The winners are: ', end='')
        x, y = 25, (len(winners) - 1) * 20
        for w in winners:
            t.setx(x)
            t.sety(y)

            t.write(f'Player {w.get_number()}', align='left', font=('8514oem', 30, 'italic'))

            y -= 60
            print(f'Player {w.get_number()}', end=', ')
        print('\b\b')
    else:
        t.setx(0)
        t.sety(0)

        t.write(f'The winner is: Player {winners[0].get_number()}', align='center', font=('8514oem', 30, 'italic'))

        print(f'The winner is: Player {winners[0].get_number()}')
    t.setx(0)
    t.sety(-300)
    t.color('white')
    t.write('---------- Press the X in the top right to close out of the game! ----------', align='center',
            font=('8514oem', 30, 'bold'))


def main():
    '''This function controls the main functions of the program to ensure everything runs when it is supposed to'''
    global players, round_num, players_num, original_players
    start_button.destroy()
    inst_button.destroy()
    round_num = 1
    while True:
        try:
            players_num = int(screen.textinput('num_players', "Enter a number of players: "))
            if players_num < 2:
                raise ValueError
            break
        except (ValueError, TypeError):
            print('Please enter a valid number of players (2 or more).')
    players = []
    original_players = []
    for i in range(1, players_num + 1):
        players.append(Player(i))
    for i in players:
        original_players.append(i)

    run = True

    while run:
        play_game()
        round_winner = determine_highest()
        loser = determine_loser()
        rearrange_order(round_winner)
        token_num = determine_token_num(round_winner)
        adjust_tokens(loser, token_num)
        run = show_standings()
        round_num += 1
    show_winners()


def next_page(inst):
    global inst_page
    inst_page += 1
    instructions(inst)


def back_page(inst):
    global inst_page
    inst_page -= 1
    instructions(inst)


def create_next_button(inst):
    global next_button
    canvas = screen.getcanvas()
    my_font = font.Font(size=25)
    next_button = Button(canvas.master, text="→", command=partial(next_page, inst), width=6, height=1,
                         fg='black', bg='#008080')
    next_button['font'] = my_font
    next_button.pack()
    next_button.place(x=screen.window_width() - 150, y=25)


def create_back_button(inst):
    global back_button
    canvas = screen.getcanvas()
    my_font = font.Font(size=25)
    back_button = Button(canvas.master, text="←", command=partial(back_page, inst), width=6, height=1, fg='black',
                         bg='#008080')
    back_button['font'] = my_font
    back_button.pack()
    back_button.place(x=30, y=25)


def inst_draw(page, inst):
    '''Given a specific page in the instructions, this function writes that page to the screen'''
    t.color('#9c9c9c')
    t.clear()
    t.goto(0, 370)
    t.write(f'---------- {page[0]} ----------', align='center', font=('Algerian', 40, 'bold'))
    t.goto(0, 270)
    for i in page[1:]:
        t.write(i, align='center', font=('8514oem', 30, 'normal'))
        t.sety(t.ycor() - 50)


def instructions(inst=None):
    '''This function prepares the instructions given in the .txt file for display'''
    global inst_page
    inst_button.destroy()
    start_button.destroy()
    screen.bgcolor('#500000')
    if inst_page == -5:
        try:
            infile = open('ZANZIBAR_INSTRUCTIONS.txt', 'r')
        except FileNotFoundError:
            t.clear()
            print('You did not download ZANZIBAR_INSTRUCTIONS.txt and put it in your pycharm directory.')
            t.goto(0, 50)
            t.color('red')
            t.write('You did not download ZANZIBAR_INSTRUCTIONS.txt', align='center', font=('8514oem', 30, 'bold'))
            t.sety(-50)
            t.write('and put it in your pycharm directory.', align='center', font=('8514oem', 30, 'bold'))
            t.sety(-100)
            t.write('Do this and then retry.', align='center', font=('8514oem', 30, 'bold'))
            t.color('black')
            time.sleep(5)
            main_menu()
            return None
        inst = {1: [], 2: [], 3: [], 4: [], 5: []}
        lines = infile.readlines()
        infile.close()
        for i in range(1, len(inst) + 1):
            try:
                inst[i] = lines[0:lines.index('\n')]
                lines = lines[lines.index('\n') + 1:]
            except ValueError:
                inst[i] = lines
                continue
        for i in range(1, len(inst) + 1):
            for j in range(len(inst[i])):
                inst[i][j] = inst[i][j][:-1]
        inst_page = 1
        create_next_button(inst)
        create_back_button(inst)
        instructions(inst)
    elif inst_page == 1:
        inst_draw(inst[1], inst)
    elif inst_page == 2:
        inst_draw(inst[2], inst)
    elif inst_page == 3:
        inst_draw(inst[3], inst)
    elif inst_page == 4:
        inst_draw(inst[4], inst)
    elif inst_page == 5:
        inst_draw(inst[5], inst)
    else:
        next_button.destroy()
        back_button.destroy()
        main_menu()


def open_instructions():
    global inst_page
    inst_page = -5
    instructions()


def create_start_button():
    '''This is the code for creating the button that, when pressed, starts the main code for the game'''
    global start_button
    canvas = screen.getcanvas()
    my_font = font.Font(family='8514oem', size=23)
    start_button = Button(canvas.master, text="Start Game", command=main, width=12, height=3, fg='black', bg='#46b058')
    start_button['font'] = my_font
    start_button.pack()
    start_button.place(x=screen.window_width() // 2 - 300, y=600)


def create_inst_button():
    '''This is the code for creating the button that, when pressed, opens the instructions for the code'''
    global inst_button
    canvas = screen.getcanvas()
    my_font = font.Font(family='8514oem', size=23)
    inst_button = Button(canvas.master, text="Instructions", command=open_instructions, width=12, height=3, fg='black',
                         bg='grey')
    inst_button['font'] = my_font
    inst_button.pack()
    inst_button.place(x=t.window_width() // 2 + 200, y=600)


def main_menu():
    '''This is the code for the main menu of the game'''
    t.clear()
    screen.update()
    screen.bgcolor('#133366')
    t.goto(0, 175)
    t.pencolor('white')
    t.write('Welcome to', font=('8514oem', 50, 'normal'), align='center')
    t.goto(0, -25)
    t.write('ZANZIBAR', font=('Algerian', 110, 'normal'), align='center')
    t.goto(0, -50)
    t.write('A dice game for you and your friends!', font=('8514oem', 20, 'normal'), align="center")
    t.goto(0, -100)
    t.write("Hope y'all have fun :D", font=('8514oem', 20, 'normal'), align="center")
    t.goto(0, -150)
    create_start_button()
    create_inst_button()


global screen, inst_page
screen = t.Screen()
screen.setup(width=1260, height=900)
screen.bgcolor('#133366')
screen.title('Zanzibar!')
screen.update()
t.speed(30)
t.hideturtle()
t.penup()

if __name__ == "__main__":
    main_menu()

screen.mainloop()
