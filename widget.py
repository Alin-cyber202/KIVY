import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')  # Или более новая версия

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')  

        self.label = Label(text='Начальный текст') 

        button = Button(text='Нажми меня')
        button.bind(on_press=self.on_button_press) 

        layout.add_widget(self.label) 
        layout.add_widget(button)      
        return layout

    def on_button_press(self, instance):
        self.label.text = 'Текст изменен!'  

if __name__ == '__main__':
    MainApp().run()
