from kivymd.app import MDApp
from kivy.lang.builder import Builder as NewLanguageAndroid
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty


ANDROID_LANG = '''
#:import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton

MyFloatLayout

    Label:
        text: ""+str(root.score)
        pos_hint: {"center_x":0.500, "center_y":0.900}
        font_size: "30dp"
        color: (0, 0, 0, 1)
        
    MDFillRoundFlatButton
        text: 'HORIZONTAL'
        size_hint: 0.18, 0.3
        pos_hint: {'center_y':.500}
        id: mdbutton_horizontal
'''


class MyFloatLayout(FloatLayout):
    value = 2.5
    pop = SoundLoader.load("pop.mp3")
    score = NumericProperty()

    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        Clock.schedule_interval(self.my_callback, 0.001)  # função que chama função a cada 0.001 segundos

    def my_callback(self, dt):  # função que movimenta objeto para direita a 2.5 passos
        self.ids.mdbutton_horizontal.x += self.value

        if self.ids.mdbutton_horizontal.x >= self.width:
            self.ids.mdbutton_horizontal.x = 0  # se o objeto bater na parede direita ele retorna ao ponto zero
            self.value += 2.5  # é adcionado 2.5 passos a mais na variavel value
            self.pop.play()  # pop sound ligado
            self.score += 1  # aumenta pontuação do score


class Builder(MDApp):
    def build(self):
        return NewLanguageAndroid.load_string(ANDROID_LANG)


Builder().run()
