from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import json

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


def read_info():
    try:
        with open('data.json', 'r', encoding="utf-8") as file:
            data = json.load(file)

    except:
        data = {
            "score":0,
            "power":1
        }

    return data
class MainWindow(Screen):
    def on_shop_screen(self):
        self.manager.current = "shop"

    def click(self):
        self.ids.artifact.size_hint = (0.5, 0.5)


class ShopScreen(Screen):
    def on_main_screen(self):
        self.manager.current = "main"


class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name="main"))
        sm.add_widget(ShopScreen(name="shop"))
        return sm


app = ClickerApp()
app.run()
