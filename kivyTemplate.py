from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout




Builder.load_string("""
<Phone>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'Menu'
                GridLayout:
                    cols: 1
                    padding: 100
                    Label:
                        markup: True
                        text: '[size=24]Welcome to [color=dd88ff]Help With Band[/color][/size]'
                    Button:
                        text: 'Bass Notes'
                        on_press: _screen_manager.current='bass'

                    Button:
                        text: 'Bass Notes'
                        on_press: _screen_manager.current='treble'


            Screen:
                name: 'treble'
                GridLayout:
                    cols: 3
                    padding: 50
                    Button:
                        text: "a"
                    Button:
                        text: "b"
                    Button:
                        text: "c"
                    Button:
                        text: "d"
                    Button:
                        text: "e"
                    Button:
                        text: "f"
                    Button:
                        text: "g"
                    Button:
                        text: "High e"
                    Button:
                        text: "High f"

            Screen:
                name: 'bass'
                GridLayout:
                    cols: 1
                    padding: 50
                    Label:
                        markup: True
                        text: '[size=24] I was thinking of having an image here of random note[/size]'
                    GridLayout:
                        cols: 3
                        padding: 50


                        Button:
                            text: "a"
                        Button:
                            text: "b"
                        Button:
                            text: "c"
                        Button:
                            text: "d"
                        Button:
                            text: "e"
                        Button:
                            text: "f"
                        Button:
                            text: "g"
                        Button:
                            text: "High e"
                        Button:
                            text: "High f"

            Screen:
                name: 'Rules'
                Label:
                    markup: True
                    text: '[size=24]Welcome to [color=dd88ff]THE RULES!!!![/color][/size]'

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Go to Menu'
                on_press: _screen_manager.current='Menu'
            Button:
                text: 'Go to Rules'
                on_press: _screen_manager.current='Rules'
            Button:
                text: 'Quit'
                on_press: app.get_running_app().stop()
""")

# Python code:



# Some helper functions:
def checkAnswer(answer,note):
    # answer is the user's answer taken from a button click
    # note is the name of the random note chosen when selected
    return True if (note == answer) else False




# Defining classes used:
class Phone(FloatLayout):
    pass

class TestApp(App):
    def build(self):
        return Phone()


if __name__ == '__main__':
    TestApp().run()
