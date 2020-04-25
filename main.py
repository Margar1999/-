from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.config import Config
from random import random


# Main window config

Config.set('graphics', 'resizable', '0' )
Config.set('graphics', 'width', '700' )
Config.set('graphics', 'height', '700' )

# Load sound effects

do = SoundLoader.load('notaner/do .mp3')
re = SoundLoader.load('notaner/re .mp3')
mi = SoundLoader.load('notaner/mi .mp3')
fa = SoundLoader.load('notaner/fa .mp3')
sol = SoundLoader.load('notaner/sol .mp3')
lya = SoundLoader.load('notaner/lja .mp3')
si = SoundLoader.load('notaner/si .mp3')
all = SoundLoader.load('notaner/all.mp3')



# Class  for creating  piano application

class My_prog(App):

    # Function for play sound effect

    def do(self, instance):
        do.play()
        grac = "до--"
        self.text_input.text += grac
        instance.background_color = [random(), random(), random(), random()]

    # Function for play sound effect

    def re(self, instance):
        re.play()
        grac = "ре--"
        self.text_input.text += grac
        instance.background_color =[random(), random(), random(), random()]

    # Function for play sound effect

    def mi(self, instance):
        mi.play()
        grac = "ми--"
        self.text_input.text += grac
        instance.background_color = [random(), random(), random(), random()]

    # Function for play sound effect

    def fa(self, instance):
        fa.play()
        grac = "фа--"
        self.text_input.text += grac
        instance.background_color = [random(), random(), random(), random()]

    # Function for play sound effect

    def sol(self, instance):
        sol.play()
        grac = "соль--"
        self.text_input.text += grac
        instance.background_color = [random(), random(), random(), random()]

    # Function for play sound effect

    def lja(self, instance):
        lya.play()
        grac = "ля--"
        self.text_input.text += grac
        instance.background_color = [random(), random(), random(), random()]

    # Function for play sound effect

    def si(self, instance):
        si.play()
        grac = "си--"
        self.text_input.text += grac
        instance.background_color = [random(), random(), random(), random()]

    # Function for play  all sound effects

    def all(self, instance):
        all.play()
        instance.background_color = [random(), random(), random(), random()]

    # Method, for  app class  which  return  the widget tree  in the piano aplication

    def build(self):
        self.icon ='notaner/icon.png'
        self.nkar = "notaner/pian.png"
        verevi_mas =FloatLayout()
        nkar = Image(source = self.nkar)
        verevi_mas.add_widget(nkar)
        self.text_input = TextInput()
        self.text_input.text =""
        self.text_input.pos = (50, 590 )
        self.text_input.size_hint = (0.86,    .10)
        self.text_input.background_color =[0.70, 0.71, 0.79, 0.50]

        verevi_mas.add_widget(self.text_input)

        ekran =GridLayout(cols =3, padding = [4], spacing =20)
        ekran.pos = (80, 40)
        ekran.size_hint =(0.8, 0.70)
        tarei_tesak = ["До", "Ре", "Ми", "Фа", "Соль", "Ля", "Си", "Все"]
        ekran.add_widget(Button(text=tarei_tesak[0],  font_size=30, background_color=[0.70, 0.71, 0.79, 0.70],  on_press=self.do))
        ekran.add_widget(Button(text=tarei_tesak[1], font_size=30, background_color=[0.70, 0.71, 0.79, 0.70], on_press=self.re))
        ekran.add_widget(Button(text=tarei_tesak[2], font_size=30, background_color=[0.70, 0.71, 0.79, 0.60], on_press=self.mi))
        ekran.add_widget(Button(text=tarei_tesak[3], font_size=30, background_color=[0.70, 0.71, 0.79, 0.70], on_press=self.fa))
        ekran.add_widget(Button(text=tarei_tesak[4], font_size=30, background_color=[0.70, 0.71, 0.79, 0.70], on_press=self.sol))
        ekran.add_widget(Button(text=tarei_tesak[5], font_size=30, background_color=[0.70, 0.71, 0.79, 0.60], on_press=self.lja))
        ekran.add_widget(Button(text=tarei_tesak[6], font_size=30, background_color=[0.70, 0.71, 0.79, 0.70], on_press=self.si))
        ekran.add_widget(Button(text=tarei_tesak[7], font_size=30, background_color=[0.70, 0.71, 0.79, 0.70], on_press=self.all))
        verevi_mas.add_widget(ekran)

        return verevi_mas

My_prog.title = "Пианино"


if __name__ =="__main__":
    My_prog().run()
