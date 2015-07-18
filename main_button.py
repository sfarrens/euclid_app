import kivy
from dictionary import values

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):
    
# BUILD
    def build(self):
        
        layout = FloatLayout()
        
        self.txt_in = TextInput(text = '',
                              multiline = False,
                              font_size = 30,
                              size_hint=(0.5, 0.07),
                              pos_hint = {'center_x': 0.5, 'center_y': 0.9})
        
        layout.add_widget(self.txt_in)
        
        button = Button(background_normal = 'button_up.png',
                        background_down = 'button_down.png',
                        pos_hint = {'center_x': 0.5, 'center_y': 0.8},
                        size_hint = (0.2, 0.1))
        
        button.bind(on_press = self.buttonClicked)
        layout.add_widget(button)

        self.im = Image(source = 'ec_logo.png',
                        pos_hint = {'center_x': 0.5, 'center_y': 0.4},
                        size_hint = (0.2, 0.1))
        layout.add_widget(self.im)
        
        return layout

# BUTTON HANDLER
    def buttonClicked(self, btn):

        if self.txt_in.text in values:
            self.im.source = 'circle.png'
            
        else:
            self.im.source = 'star.png'

# RUN APP
if __name__ == "__main__":
    MyApp().run()
