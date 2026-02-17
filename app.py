from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from random import randint
from kivy.core.window import Window
from kivy.animation import Animation

Window.clearcolor = (0.4, 0.2, 0.6, 0.1)




class GuessingGameApp(App):
    def build(self):
        self.com_num = randint(1, 100)

        main_layout = BoxLayout(
            orientation="vertical",
            padding=(50),
            spacing=30
        )

        self.lblTitle = Label(text="Guess the number", font_size="20sp", color=(1, 1, 1, 1), font_name="PressStart2P-Regular.ttf")
        main_layout.add_widget(self.lblTitle)

        self.txtInput = TextInput(hint_text="Enter number...", font_name="PressStart2P-Regular.ttf", font_size="10sp")
        main_layout.add_widget(self.txtInput)

        self.btnSubmit = Button(
            text="Submit",
            font_size="20sp",
            background_normal='',
            background_color=(0.7, 0.5, 0.9, 1),
            font_name="PressStart2P-Regular.ttf")
        main_layout.add_widget(self.btnSubmit)

        self.btnSubmit.bind(on_press=self.submit_clicked)

        self.lblResponse = Label(text="Enter a number above!", font_size="20sp", color=(1, 1, 1, 1), font_name="PressStart2P-Regular.ttf")
        main_layout.add_widget(self.lblResponse)


        return main_layout

    def submit_clicked(self, instance):
        try:
            inputted_number = int(self.txtInput.text)
            if(inputted_number == self.com_num):
                self.com_num = randint(1, 100)
                self.lblResponse.text = "Correct! Guess The new number."
            elif (inputted_number < self.com_num):
                self.lblResponse.text = "Wrong! Guess higher."
            elif (inputted_number > self.com_num):
                self.lblResponse.text = "Wrong! Guess lower."
        except ValueError:
            self.lblResponse.text = "Error: Incorrect Number"
            
        anim = Animation(font_size=25 , duration=0.1) + Animation(font_size=20, duration=0.1)
        anim.start(self.lblResponse)
        
        
        
if __name__ == "__main__":
    GuessingGameApp().run()