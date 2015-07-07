from functools import partial
from dictionary import values

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# LOOK UP DICTIONARY VALUES
def dict_lookup(data, letters):
    index = [k for k, v in data.items() if letters in k]
    return index

# MAKE INPUT CAPITAL LETTERS
class CapitalInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        s = substring.upper()
        return super(CapitalInput, self).insert_text(s, from_undo=from_undo)

# MAIN APP CLASS
class EuclidApp(App):
    
    # BUILD
    def build(self):

        self.root = FloatLayout()
        self.root.bind(size = self._update_rect,
                       pos = self._update_rect)
        
        with self.root.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size = self.root.size,
                                  pos = self.root.pos)
        
        bg = Image(source = 'ec_logo.png')
        
        self.txt_in = CapitalInput(
            text = '',
            multiline = False,
            font_size = 30,
            size_hint=(0.95, 0.07),
            pos_hint = {'center_x': 0.5, 'center_y': 0.9}
            )
        
        grid = GridLayout(
            cols = 1,
            padding = 2,
            spacing = 5,
            size_hint = (1, None),
            )
        
        grid.bind(minimum_height = grid.setter('height'))

        # ADD A BUTTON TO INSTANCE
        def add_button(instance, value):
            btn = Button(
                text = value,
                size_hint = (1, None),
                font_size = 30,
                background_color = (0.4, 0.2, 0.6, 0.9),
                background_normal = ''
                )
            output = values[value]
            btn.bind(on_press = partial(self.buttonHandler, grid, output))
            instance.add_widget(btn)

        # DEFINE BEHAVIOUR FOR TEXT INPUT
        def on_text(instance, value):
            grid.clear_widgets()
            a_list = dict_lookup(values, str(value))
            if len(value) > 0:
                for i in range(len(a_list)):
                    add_button(grid, a_list[i])
                
        self.txt_in.bind(text = on_text)

        scroll = ScrollView(
            size_hint = (0.95, 0.8),
            pos_hint = {'center_x': .5, 'center_y': .4},
            do_scroll_x = False
            )

        scroll.add_widget(grid)

        self.root.add_widget(bg)
        self.root.add_widget(self.txt_in)
        self.root.add_widget(scroll)

        return self.root

    # UPDATE BACKGROUND COLOUR
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size    
    
    # BUTTON HANDLER
    def buttonHandler(self, grid, value, button):
        grid.clear_widgets()
        btn = Button(
                text = value,
                size = (0, 500),
                size_hint = (1, None),
                font_size = 30,
                background_color = (0.6, 0.2, 0.4, 0.9),
                background_normal = '',
                background_down = ''
                )
        grid.add_widget(btn)

# RUN APP
if __name__ == "__main__":
    EuclidApp().run()
