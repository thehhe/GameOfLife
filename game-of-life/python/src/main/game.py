import numpy as np
import matplotlib.pyplot as plt


class GameOfLife:
    def __init__(self, size, board):
        self.size = (size, size)
        self.board = board
        self.next_generation_change = np.zeros(self.size)
    
    def get_number_of_alive_neighbours(self, i, j):
        neighbour_coordinates = self.get_neighbour_coordinates(i, j, self.size[0])
        neighbour_alive = [1 for neighbour in neighbour_coordinates if self.board[neighbour] > 0.0]

        return len(neighbour_alive)

    @staticmethod
    def get_neighbour_coordinates(i, j, size):
        possible_xs = [i - 1, i, i + 1]
        possible_ys = [j - 1, j, j + 1]

        neighbour_coordinates = [(x, y) for x in possible_xs for y in possible_ys if x >= 0 and x < size and y >= 0 and y < size and (x, y) != (i, j)]
        return neighbour_coordinates

    def gather_next_generation_data(self):
        self.next_generation_change = np.zeros(self.size)
        for i in range(0, self.size[0]):
            for j in range(0, self.size[0]):
                number_of_alive_neighbours = self.get_number_of_alive_neighbours(i, j)
                if number_of_alive_neighbours < 2 or number_of_alive_neighbours > 3:
                    self.next_generation_change[i, j] = 0.0
                elif number_of_alive_neighbours == 2 and self.board[i, j] == 0:
                    self.next_generation_change[i, j] = 0.0
                elif number_of_alive_neighbours == 2 and self.board[i, j] != 0:
                    self.next_generation_change[i, j] = 1.0
                else:
                    self.next_generation_change[i, j] = 1.0

    def update_board(self):
        self.board = (self.board + self.next_generation_change) * self.next_generation_change
        self.board = np.clip(self.board, 0, 5)

    def move_one_generation(self):
        self.gather_next_generation_data()
        self.update_board()



if __name__ == "__main__":
    game = GameOfLife(3, np.array([[1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]))

    game.gather_next_generation_data()
    print(game.next_generation_change)
    game.update_board()
    print(game.board)