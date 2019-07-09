import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# noinspection PyArgumentList
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()  # make another layout inside the main layout
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name:"))
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)

        self.inside.add_widget(Label(text="Last Name:"))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text="Email:"))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)  # Adds the inside layout to the main layout

        self.submit = Button(text="Submit", font_size=30)
        self.submit.bind(on_press=self.pressed)  # If the button is pressed the 'pressed' method is called
        self.add_widget(self.submit)

    def pressed(self, instance):
        first_name = self.first_name.text
        last_name = self.last_name.text
        email = self.email.text

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")

        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
