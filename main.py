from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Line
import random

class TarotCardWidget(FloatLayout):
    def __init__(self, card_name, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (260, 400)
        
        with self.canvas.before:
            Color(0.15, 0.12, 0.2, 1)  # Deep mystical tone
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[15])
            
            Color(0.85, 0.7, 0.3, 1)
            self.border = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 15), width=2)
            
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        
        self.label = Label(
            text=card_name,
            font_size='20sp',
            halign='center',
            valign='middle',
            color=(0.95, 0.95, 0.95, 1)
        )
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

    def update_canvas(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.border.rounded_rectangle = (self.x, self.y, self.width, self.height, 15)
        self.label.pos = self.pos
        self.label.size = self.size

class TarotApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=25, spacing=20)
        
        title = Label(
            text="SURREAL TAROT DECK",
            font_size='24sp',
            size_hint=(1, 0.15),
            color=(0.9, 0.8, 0.4, 1)
        )
        
        self.card_area = FloatLayout(size_hint=(1, 0.65))
        
        draw_btn = Button(
            text="SHUFFLE & DRAW",
            size_hint=(1, 0.15),
            background_color=(0.3, 0.2, 0.4, 1),
            font_size='18sp'
        )
        draw_btn.bind(on_press=self.shuffle_and_draw)
        
        root.add_widget(title)
        root.add_widget(self.card_area)
        root.add_widget(draw_btn)
        
        self.shuffle_and_draw(None)
        
        return root

    def shuffle_and_draw(self, instance):
        self.card_area.clear_widgets()
        
        deck = [
            "0 - The Fool\n\nLeap of faith, infinite potential.",
            "I - The Magician\n\nWillpower, creation, mastery.",
            "II - The High Priestess\n\nIntuition, mystery, inner voice.",
            "III - The Empress\n\nAbundance, nature, fertility.",
            "IV - The Emperor\n\nStructure, authority, stability.",
            "X - Wheel of Fortune\n\nCycles, destiny, turning point.",
            "XIII - Death\n\nTransformation, profound rebirth.",
            "XVIII - The Moon\n\nIllusion, subconscious, anxiety.",
            "XXI - The World\n\nCompletion, accomplishment, unity."
        ]
        
        random.shuffle(deck)
        drawn_card_text = deck[0]
        
        card = TarotCardWidget(card_name=drawn_card_text)
        card.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        self.card_area.add_widget(card)

if __name__ == '__main__':
    TarotApp().run()
