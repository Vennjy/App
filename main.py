

import kivy as kv
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

kv.require('2.0.0')


# TODO: chapter 3 in current kivy python course

class Main(GridLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.cols = 2

        # Checks if file exists
        if os.path.isfile('details.txt'):
            with open('details.txt', 'r')as f:
                index = f.read().split(',')  # Splitting the text from comas
                ip = index[0]  # Previous info
                port = index[1]
                username = index[2]

        else:  # If file does not exist just return blank
            ip = ''
            port = ''
            username = ''

        # ip

        self.add_widget(Label(text='IP:'))
        self.ip = TextInput(text=ip, multiline=False)
        self.add_widget(self.ip)

        # Username

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(text=username, multiline=False)
        self.add_widget(self.username)

        # Port

        self.add_widget(Label(text='Port:'))
        self.port = TextInput(text=port, multiline=False)
        self.add_widget(self.port)

        # Creating and adding Button widget
        self.join = Button(text='Join')
        self.join.bind(on_press=self.join_button)
        self.add_widget(self.join)

    def join_button(self, useless_variable=True):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text
        print(f'Attempting to join {ip}:{port} as {username}')
        with open('details.txt', 'w') as info:
            info.write(f'{ip},{port},{username}')


class TheApp(App):
    def build(self):
        return Main()


if __name__ == '__main__':
    TheApp().run()

