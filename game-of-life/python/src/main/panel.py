import kivy
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import numpy as np


class GameOfLifePanel(GridLayout):
    def __init__(self, **kwargs):
        self.game_grid = kwargs.get('game_grid')
        del kwargs['game_grid']
        super().__init__(**kwargs)
        self.cols = 2

        if os.path.isfile('defaults.csv'):
            with open('defaults.csv', 'r') as f:
                d = f.read().split(',')
                prev_speed = d[0]
                prev_input = d[1]
        else:
            prev_speed = ''
            prev_input = ''

        

        self.add_widget(Label(text='Speed:', color=[105, 106, 188, 1]))

        self.speed = TextInput(text=prev_speed, multiline=False)
        self.add_widget(self.speed)
        self.add_widget(Label(text='Input:', color=[105, 106, 188, 1]))

        self.input = TextInput(text=prev_input, multiline=False)
        self.add_widget(self.input)

        self.add_widget(Label(text=''))

        self.apply_changes_button = Button(text='Apply')
        self.add_widget(self.apply_changes_button)
        self.apply_changes_button.bind(on_press=self.apply_changes)

    def apply_changes(self, instance):
        try:
            speed = int(self.speed.text)
            self.game_grid.set_speed(speed)
        except ValueError:
            print('Wrong value in speed. . . ignoring')
        
        input = self.input.text
        try:
            input_data = np.genfromtxt(input, delimiter=',')
            self.game_grid.set_input(input_data)
        except:
            print('Wrong input. . . ignoring')

        print(f'speed changed to {speed}, input changed to {input}')

        with open('defaults.csv', 'w') as f:
            f.write(f'{speed},{input}')
