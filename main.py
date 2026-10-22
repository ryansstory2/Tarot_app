from kivy.uix.image import Image
from kivy.uix.label import Label
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

        # Load card image (expects files like 'ace_of_wands.png' or matches card name in root folder)
        img_filename = f"{card_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}.png"
        try:
            self.add_widget(Image(
                source=img_filename, 
                size_hint=(0.85, 0.6), 
                pos_hint={'center_x': 0.5, 'top': 0.88}
            ))
        except Exception:
            pass  # Fallback if specific image file is not found

        # Card text description
        self.add_widget(Label(
            text=f"[b]{card_name}[/b]\n{card_meaning}",
            markup=True,
            halign='center',
            valign='middle',
            size_hint=(0.9, 0.25),
            pos_hint={'center_x': 0.5, 'y': 0.05}
        ))

    def _update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


def draw_random_card(self, instance):
    self.card_container.clear_widgets()
    deck = self.get_full_deck()
    random.shuffle(deck)
    chosen_card = deck[0]  # Tuple of (name, description)
    
    card_widget = SurrealCardWidget(card_data=chosen_card)
    card_widget.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
    self.card_container.add_widget(card_widget)
