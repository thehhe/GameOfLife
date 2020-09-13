from panel import GameOfLifePanel
from grid import GameOfLifeGrid
import kivy
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class AppLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 1

        game_grid = GameOfLifeGrid()

        self.add_widget(game_grid)
        self.add_widget(GameOfLifePanel(size_hint_x=None, size_hint_y=None, width=100, game_grid=game_grid))
