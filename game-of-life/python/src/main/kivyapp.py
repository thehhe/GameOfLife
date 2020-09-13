import kivy
from kivy.app import App
import argparse

from app_layout import AppLayout

class EpicApp(App):
    def build(self):
        return AppLayout()

if __name__ == "__main__":
    EpicApp().run()
