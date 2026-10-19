from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class TarotApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Title label
        self.title_label = Label(
            text="Tarot Reading",
            font_size='28sp',
            size_hint=(1, 0.2),
            halign='center',
            valign='middle'
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        
        # Card display label
        self.card_label = Label(
            text="Tap the button below to draw a card.",
            font_size='18sp',
            size_hint=(1, 0.6),
            halign='center',
            valign='middle'
        )
        self.card_label.bind(size=self.card_label.setter('text_size'))
        
        # Draw button
        draw_button = Button(
            text="Draw Card",
            size_hint=(1, 0.2),
            font_size='18sp'
        )
        draw_button.bind(on_press=self.draw_card)
        
        # Add widgets to layout
        layout.add_widget(self.title_label)
        layout.add_widget(self.card_label)
        layout.add_widget(draw_button)
        
        return layout

    def draw_card(self, instance):
        cards = [
            "The Fool - New beginnings, spontaneity, leap of faith.",
            "The Magician - Manifestation, resourcefulness, power.",
            "The High Priestess - Intuition, unconscious, inner voice.",
            "The Empress - Fertility, femininity, nature, abundance.",
            "The Emperor - Authority, structure, control, fatherhood.",
            "The Wheel of Fortune - Good luck, karma, life cycles, destiny.",
            "Death - Endings, change, transformation, transition."
        ]
        self.card_label.text = random.choice(cards)

if __name__ == '__main__':
    TarotApp().run()
