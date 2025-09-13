import random
import os
import time

os.system('clear')
# 1 - Rock, 2 - Paper, 3 - Scissors
class Game:
    def __init__(self):
        self.player_obj = None
        self.pc_obj = None
        self.winner = None

    def ask_user(self):
        print('1 - Rock, 2 - Paper, 3 - Scissors\n')
        self.player_obj = input('Choose an option: ')
        while self.player_obj not in ['1','2','3']:
            os.system('clear')
            print('1 - Rock, 2 - Paper, 3 - Scissors\n')
            self.player_obj = input('Please, choose some of those options:')
        self.player_obj = int(self.player_obj)

    def define_pc_obj(self):
        self.pc_obj = random.choice([n for n in [1,2,3] if n != self.player_obj])

    def test_win(self):
        print('1 - Rock, 2 - Paper, 3 - Scissors')
        print(f'You choose {self.player_obj} and pc choose {self.pc_obj}')
        time.sleep(2)
        if self.player_obj == 1 and self.pc_obj == 2:
            self.winner = 'pc'
        elif self.player_obj == 1 and self.pc_obj == 3:
            self.winner = 'player'
        elif self.player_obj == 2 and self.pc_obj == 1:
            self.winner = 'player'
        elif self.player_obj == 2 and self.pc_obj == 3:
            self.winner = 'pc'
        elif self.player_obj == 3 and self.pc_obj == 1:
            self.winner = 'pc'
        elif self.player_obj == 3 and self.pc_obj == 2:
            self.winner = 'player'

    def show_victory(self):
        if self.winner == 'player':
            print('-------------------------')
            print('You won! Congrats')
            print('-------------------------')
        else:
            print('-------------------------')
            print('You loose!!')
            print('-------------------------')
        time.sleep(2)
    
    def play_again(self):
        ask = input('Do you wanna play again? (1 - YES, 2 - NO)')
        while ask not in ['1', '2']:
            ask = input('Choose between this two: (1 - YES, 2 - NO)')

        return ask

while True:
    game = Game()
    os.system('clear')
    game.ask_user()
    os.system('clear')
    game.define_pc_obj()
    os.system('clear')
    game.test_win()
    os.system('clear')
    game.show_victory()
    os.system('clear')
    again = game.play_again()
    if  again == '2':
        break

os.system('clear')