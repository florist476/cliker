import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


def read_info():
    try:
        with open('data.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
    except:
        data = {
            "score": 0,
            "power": 1
        }
    return data

def write_info(data):
    with open('data.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


class MainWindow(Screen):
    def on_shop_screen(self):
        self.manager.current = "shop"

    def on_enter(self, *args):
        data = read_info()
        self.ids.score_lbl.text = "Рахунок: " + str(data["score"])
    def click(self):
        data = read_info()
        data["score"] += data["power"]
        write_info(data)
        self.ids.score_lbl.text = "Рахунок: " + str(data["score"])
        self.ids.artifact.size_hint = (0.5, 0.5)

    def realize(self):
        self.ids.artifact.size_hint = (0.3, 0.3)



class ShopScreen(Screen):
    def on_main_screen(self):
        self.manager.current = "main"

    def buy(self, price, power):
        data = read_info()
        if data["score"] >= price:
            data["power"] += power
            data["score"] -= price
            write_info(data)
        else:
            print("НЕМАЄ ГРОШЕЙ")
class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name="main"))
        sm.add_widget(ShopScreen(name="shop"))
        return sm


app = ClickerApp()
app.run()
