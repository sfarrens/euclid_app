from functools import partial
from dictionary import values

from kivy.app import App
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

# LOOK UP DICTIONARY VALUES
def dict_lookup(data, letters):
    
    index = [k for k, v in data.items() if letters in k]
    return index

# NEW BUTTON
class NewButton(Button):

    def buttonHandler(self, *args):
        value = args[0]
        output = values[value]
        popup = PopupHandler(
            title = value,
            text1 = output[0],
            text2 = output[1])
        popup.open()
    
    text = StringProperty('')
    
# POPUP HANDLER
class PopupHandler(Popup):
    
    def buttonHandler(self, *args):
        self.dismiss()

    title = StringProperty('')
    text1 = StringProperty('')
    text2 = StringProperty('')

    
# ROOT WIDGET
class RootWidget(FloatLayout):

    def handle_text(self, *args):

        def addButton(instance, value):
            btn = NewButton(text = value)
            instance.add_widget(btn)
            
        self.ids.grid.clear_widgets()
        value = args[0]
        a_list = dict_lookup(values, str(value))
        if len(value) > 0:
            for i in range(len(a_list)):
                addButton(self.ids.grid, a_list[i])

# MAIN APP CLASS
class EuclidApp(App):
    def build(self):
        return RootWidget()

# READ KV FILE
Factory.register('RootWidget', cls = RootWidget)
Factory.register('NewButton', cls = NewButton)
Factory.register('PopupHandler', cls = PopupHandler)
    
# RUN APP
if __name__ == "__main__":
    EuclidApp().run()
