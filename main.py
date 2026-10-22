from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
import random

class SurrealCardWidget(FloatLayout):
    def __init__(self, card_data, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (280, 420)
        
        card_name, card_meaning = card_data
        
        # Background styling
        with self.canvas.before:
            Color(0.12, 0.08, 0.18, 1)
            self.bg = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(pos=self._update_bg, size=self._update_bg)

        # Load card image (expects files named after the card in root folder)
        img_filename = f"{card_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}.png"
        try:
            self.add_widget(Image(
                source=img_filename, 
                size_hint=(0.85, 0.6), 
                pos_hint={'center_x': 0.5, 'top': 0.88}
            ))
        except Exception:
            pass

        # Card text description
        self.add_widget(Label(
            text=f"{card_name}\n{card_meaning}",
            markup=False,
            halign='center',
            valign='middle',
            size_hint=(0.9, 0.25),
            pos_hint={'center_x': 0.5, 'y': 0.05}
        ))

    def _update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class TarotLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        # Card container display area
        self.card_container = FloatLayout(size_hint=(1, 0.8))
        self.add_widget(self.card_container)

        # Button to draw card
        draw_btn = Button(
            text="Draw Random Card",
            size_hint=(1, 0.15),
            background_color=(0.3, 0.2, 0.4, 1)
        )
        draw_btn.bind(on_press=self.draw_random_card)
        self.add_widget(draw_btn)

    def get_full_deck(self):
        deck = [
            ("The Fool", "New beginnings, innocence, spontaneity"),
            ("The Magician", "Manifestation, resourcefulness, power"),
            ("The High Priestess", "Intuition, sacred knowledge, divine feminine"),
            ("The Empress", "Femininity, beauty, nature, abundance"),
            ("The Emperor", "Authority, establishment, structure"),
            ("The Hierophant", "Spiritual wisdom, religious beliefs, conformity")
        ]
        return deck

    def draw_random_card(self, instance):
        self.card_container.clear_widgets()
        deck = self.get_full_deck()
        random.shuffle(deck)
        chosen_card = deck[0]
        
        card_widget = SurrealCardWidget(card_data=chosen_card)
        card_widget.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.card_container.add_widget(card_widget)


class TarotApp(App):
    def build(self):
        return TarotLayout()


if __name__ == '__main__':
    TarotApp().run()
