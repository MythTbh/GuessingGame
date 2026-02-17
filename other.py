from kivy.app import App
from kivy.uix.label import Label

class GuessingGameApp(App):
    def build(self):
     return Label(text="Test Passed!")


if __name__== "__main_":
    app = GuessingGameApp()
    app.run()
