#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.name = ''

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Random player'

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Human player'

    def move(self):
        choice = input("What move do you want to make? ")
        while choice != 'quit' and choice not in moves:
            choice = input("What move do you want to make? ")
        return choice

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.last = ''
        self.name = 'Reflect player'

    def move(self):
        if self.last == '':
            return random.choice(moves)
        else:
            return self.last

    def learn(self, my_move, their_move):
        self.last = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last = ''
        self.name = 'Cycle player'

    def move(self):
        if self.last == '':
            return random.choice(moves)
        else:
            lastIndex = moves.index(self.last)
            currIndex = (lastIndex+1) % len(moves)
            return moves[currIndex]

    def learn(self, my_move, their_move):
        self.last = my_move


def beats(one, two):

    if one == two:
        return 0
    else:
        if ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock')):
            return 1
        else:
            return -1


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        print(f"Player 1: {self.p1.name}")
        print(f"Player 2: {self.p2.name}")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}")
        print(f"Player 2: {move2}")

        if move1 == 'quit' or move2 == 'quit':
            return 'quit'

        compare = beats(move1, move2)

        winnerMessage = ''
        if compare == -1:
            self.p2.score += 1
            winnerMessage = "Player 2 won"
        elif compare == 1:
            self.p1.score += 1
            winnerMessage = "Player 1 won"
        else:
            winnerMessage = "It's a tie"

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print(winnerMessage)
        print(f"Player 1 score: {self.p1.score}")
        print(f"Player 2 score: {self.p2.score}")

        return winnerMessage

    def play_game(self):
        print("Game start!")
        minWins = 3
        diff = 0
        round = 0
        while diff < minWins:
            print(f"\nRound {round}:")
            msg = self.play_round()
            if msg == 'quit':
                break
            round += 1
            diff = abs(self.p1.score-self.p2.score)

        print("\nGame over!")
        print(f"Player 1 score: {self.p1.score}")
        print(f"Player 2 score: {self.p2.score}")

        if self.p1.score > self.p2.score:
            print("Player 1 won!")
        elif self.p1.score < self.p2.score:
            print("Player 2 won!")
        else:
            print("It's a tie")


if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
