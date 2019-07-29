import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def button(self):
        print(f"Name: {self.name.text}, Email: {self.email.text}")
        self.name.text = ""
        self.email.text = ""

class My_adv_App(App):  # Name the text file associated with this program the name of your main class but remove 'app' and add '.kv'
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    My_adv_App().run()
