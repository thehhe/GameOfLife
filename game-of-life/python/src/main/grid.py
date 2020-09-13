from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import time

from game import GameOfLife

import matplotlib.pyplot as plt
import numpy as np

SIZE = 100
fig, ax = plt.subplots(1)

class GameOfLifeGrid(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.input_data = np.random.randint(2, size=SIZE ** 2).reshape(SIZE, SIZE)
        self.game = GameOfLife(SIZE, self.input_data)
        self.speed = 4

        ax.matshow(self.game.board, cmap='RdGy_r')
        self.add_widget(FigureCanvasKivyAgg(fig))
        self.speed_event = self.update(self.speed)
        
    def play_game(self, *args):
        self.game.move_one_generation()
        ax.clear()
        ax.matshow(self.game.board, cmap='gray_r')
        fig.canvas.draw_idle()

    def update(self, speed):
        return Clock.schedule_interval(self.play_game, 1/speed)

    def set_speed(self, speed):
        Clock.unschedule(self.speed_event)
        self.speed = speed
        self.speed_event = self.update(self.speed)

    def set_input(self, input):
        Clock.unschedule(self.speed_event)
        self.game.board = input
        self.speed_event = self.update(self.speed)