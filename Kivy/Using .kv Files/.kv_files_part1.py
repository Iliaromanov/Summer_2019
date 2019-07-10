import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGrid(Widget):
        pass


class MyApp(App):  # Name the text file associated with this program the name of your main class but remove 'app' and add '.kv'
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
