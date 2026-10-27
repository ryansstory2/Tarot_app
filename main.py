import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window
import random

# Salvador Dalí inspired surrealist tarot deck sample
TAROT_DECK = [
    {
        "name": "The Fool",
        "keywords": "New Beginnings, Innocence, Spontaneity",
        "description": "Stepping off the edge of time into surreal potential. Trust the journey."
    },
    {
        "name": "The Magician",
        "keywords": "Manifestation, Resourcefulness, Power",
        "description": "Blending fluid reality and cosmic forces to shape destiny."
    },
    {
        "name": "The High Priestess",
        "keywords": "Intuition, Sacred Knowledge, Mystery",
        "description": "Veiled wisdom flowing through dual reflections of intuition."
    },
    {
        "name": "The Empress",
        "keywords": "Femininity, Beauty, Nature, Abundance",
        "description": "Creation melting into organic tapestry and abundance."
    },
    {
        "name": "The Emperor",
        "keywords": "Authority, Structure, Control",
        "description": "Architect of time standing firm within fluid landscapes."
    },
    {
        "name": "The Lovers",
        "keywords": "Love, Harmony, Relationships, Choices",
        "description": "Dual reflections mirroring connection and divine choice."
    },
    {
        "name": "The Wheel of Fortune",
        "keywords": "Good Luck, Karma, Life Cycles, Destiny",
        "description": "The cosmic wheel spins endlessly through melting time."
    },
    {
        "name": "The Sun",
        "keywords": "Joy, Success, Celebration, Positivity",
        "description": "Radiant illumination bringing clarity to surreal shadows."
    },
    {
        "name": "The World",
        "keywords": "Completion, Integration, Accomplishment, Travel",
        "description": "Harmonious completion of the journey through dimensions."
    }
]

class TarotApp(App):
    def build(self):
        self.title = "Surrealist Tarot"
        
        # Main background container
        root_layout = FloatLayout()
        
        # Background color layout
        main_box = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # Header title
        header = Label(
            text="[b]SURREALIST TAROT[/b]",
            markup=True,
            font_size='24sp',
            size_hint_y=0.1,
            color=(0.95, 0.85, 0.5, 1)
        )
        main_box.add_widget(header)

        # Card Display Area (Card Back Image)
        self.card_image = Image(
            source='card_back.png',  # Use your exported card back asset
            allow_stretch=True,
            keep_ratio=True,
            size_hint_y=0.6
        )
        main_box.add_widget(self.card_image)

        # Interactive Shuffle & Draw Button
        draw_button = Button(
            text="Draw Card",
            font_size='18sp',
            size_hint=(0.8, 0.12),
            pos_hint={'center_x': 0.5},
            background_color=(0.7, 0.5, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        draw_button.bind(on_release=self.draw_card)
        main_box.add_widget(draw_button)

        root_layout.add_widget(main_box)
        return root_layout

    def draw_card(self, instance):
        # Pick a random card from the deck
        card = random.choice(TAROT_DECK)
        
        # Create reading popup content
        content = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        title_label = Label(
            text=f"b[/b]",
            markup=True,
            font_size='22sp',
            size_hint_y=0.2,
            color=(0.95, 0.85, 0.5, 1)
        )
        keywords_label = Label(
            text=f"i[/i]",
            markup=True,
            font_size='14sp',
            size_hint_y=0.15,
            color=(0.8, 0.8, 0.8, 1)
        )
        desc_label = Label(
            text=card['description'],
            font_size='16sp',
            size_hint_y=0.45,
            halign='center',
            valign='middle'
        )
        desc_label.bind(size=desc_label.setter('text_size'))

        close_btn = Button(
            text="Close Reading",
            size_hint=(0.6, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0.5, 0.3, 0.1, 1)
        )

        content.add_widget(title_label)
        content.add_widget(keywords_label)
        content.add_widget(desc_label)
        content.add_widget(close_btn)

        popup = Popup(
            title="Tarot Reading",
            content=content,
            size_hint=(0.85, 0.6),
            auto_dismiss=False
        )
        close_btn.bind(on_release=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    TarotApp().run()
