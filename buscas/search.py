from kivymd.app import MDApp
from kivy.lang.builder import Builder
import webbrowser

code = """
FloatLayout:
    MDToolbar:
        title: "My Toolbar"
        size_hint: 1, 0.1
        pos_hint: {"top":1}
        left_action_items: [['menu', lambda x: self]]
    MDTextField:
        id: search
        hint_text: "Search"
        helper_text: "Busque aqui o que você quiser!"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.500, "center_y":0.650}
        size_hint: 0.75, 0.1
        on_text_validate: app.urlOpen()
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(code)

    def urlOpen(self):
        var = self.root.ids.search.text
        webbrowser.open(f"https://www.google.com/search?q={var}&rlz=1C5CHFA_enBR930BR930&oq=pesquisa&aqs=chrome..69i57j0l6j69i61.967j0j7&sourceid=chrome&ie=UTF-8")


Body().run()
