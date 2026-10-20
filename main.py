from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Line, Ellipse
import random

class SurrealCardWidget(FloatLayout):
    def __init__(self, card_data, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (280, 420)
        
        name, subtitle, symbol_type = card_data
        
        with self.canvas.before:
            # Surreal deep twilight background
            Color(0.12, 0.08, 0.18, 1)
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[18])
            
            # Inner mystical border
            Color(0.85, 0.65, 0.25, 1)
            self.border = Line(rounded_rectangle=(self.x + 8, self.y + 8, self.width - 16, self.height - 16, 12), width=1.5)
            
            # Programmatic surreal artwork element based on card motif
            if symbol_type == "sun":
                Color(0.9, 0.4, 0.2, 0.8)
                self.art1 = Ellipse(pos=(self.center_x - 50, self.y + 180), size=(100, 100))
                Color(0.95, 0.8, 0.3, 1)
                self.art2 = Line(circle=(self.center_x, self.y + 230, 45), width=2)
            elif symbol_type == "eye":
                Color(0.2, 0.5, 0.7, 0.8)
                self.art1 = Ellipse(pos=(self.center_x - 60, self.y + 190), size=(120, 70))
                Color(0.9, 0.9, 0.9, 1)
                self.art2 = Ellipse(pos=(self.center_x - 20, self.y + 205), size=(40, 40))
            elif symbol_type == "tower":
                Color(0.4, 0.1, 0.1, 0.9)
                self.art1 = RoundedRectangle(pos=(self.center_x - 25, self.y + 160), size=(50, 140), radius=[5])
                Color(0.9, 0.2, 0.2, 1)
                self.art2 = Line(points=[self.center_x - 40, self.y + 300, self.center_x, self.y + 330, self.center_x + 40, self.y + 300], width=2)
            else:
                Color(0.3, 0.2, 0.4, 0.9)
                self.art1 = Ellipse(pos=(self.center_x - 50, self.y + 180), size=(100, 100))
                Color(0.8, 0.8, 0.9, 1)
                self.art2 = Line(circle=(self.center_x + 10, self.y + 230, 40), width=1.5)

        self.bind(pos=self.update_canvas, size=self.update_canvas)
        
        # Card Text labels
        self.title_label = Label(
            text=name,
            font_size='18sp',
            bold=True,
            halign='center',
            valign='middle',
            color=(0.95, 0.9, 0.8, 1),
            pos_hint={'center_x': 0.5, 'y': 0.15},
            size_hint=(0.9, 0.2)
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        
        self.sub_label = Label(
            text=subtitle,
            font_size='13sp',
            italic=True,
            halign='center',
            valign='middle',
            color=(0.75, 0.75, 0.8, 1),
            pos_hint={'center_x': 0.5, 'y': 0.03},
            size_hint=(0.9, 0.18)
        )
        self.sub_label.bind(size=self.sub_label.setter('text_size'))
        
        self.add_widget(self.title_label)
        self.add_widget(self.sub_label)

    def update_canvas(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.border.rounded_rectangle = (self.x + 8, self.y + 8, self.width - 16, self.height - 16, 12)

class TarotApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = Label(
            text="DALI SURREAL TAROT (78 CARDS)",
            font_size='20sp',
            size_hint=(1, 0.1),
            color=(0.9, 0.75, 0.3, 1)
        )
        
        self.card_container = FloatLayout(size_hint=(1, 0.75))
        
        shuffle_btn = Button(
            text="SHUFFLE & DRAW CARD",
            size_hint=(1, 0.15),
            background_color=(0.25, 0.15, 0.35, 1),
            font_size='16sp'
        )
        shuffle_btn.bind(on_press=self.draw_random_card)
        
        root.add_widget(header)
        root.add_widget(self.card_container)
        root.add_widget(shuffle_btn)
        
        self.draw_random_card(None)
        
        return root

    def get_full_deck(self):
        deck = [
            ("0 - The Fool", "Leap into the unknown abyss", "sun"),
            ("I - The Magician", "Willpower bending reality", "eye"),
            ("II - The High Priestess", "Secrets of the deep subconscious", "cosmic"),
            ("III - The Empress", "Abundance, nature, fertility", "sun"),
            ("IV - The Emperor", "Rigid structures dissolving", "tower"),
            ("V - The Hierophant", "Spiritual wisdom & tradition", "cosmic"),
            ("VI - The Lovers", "Harmony, choices, union", "sun"),
            ("VII - The Chariot", "Determination and control", "tower"),
            ("VIII - Strength", "Inner courage and patience", "eye"),
            ("IX - The Hermit", "Soul-searching and introspection", "cosmic"),
            ("X - Wheel of Fortune", "Infinite shifting cycles", "cosmic"),
            ("XI - Justice", "Fairness, truth, and law", "tower"),
            ("XII - The Hanged Man", "Surrender & new perspective", "cosmic"),
            ("XIII - Death", "Profound surreal rebirth", "tower"),
            ("XIV - Temperance", "Balance and moderation", "sun"),
            ("XV - The Devil", "Attachment and shadow self", "tower"),
            ("XVI - The Tower", "Sudden upheaval and awakening", "tower"),
            ("XVII - The Star", "Hope, faith, and renewal", "sun"),
            ("XVIII - The Moon", "Melting illusions in the dark", "eye"),
            ("XIX - The Sun", "Joy, success, and vitality", "sun"),
            ("XX - Judgement", "Rebirth and inner calling", "cosmic"),
            ("XXI - The World", "The final cosmic integration", "cosmic")
        ]
        
        suits = [
            ("Wands", "Fire, passion, and inspiration", "tower"),
            ("Cups", "Water, emotion, and relationships", "eye"),
            ("Swords", "Air, intellect, and truth", "tower"),
            ("Pentacles", "Earth, wealth, and manifestation", "sun")
        ]
        
        ranks = [
            ("Ace", "Pure primal energy"),
            ("2", "Duality and choices"),
            ("3", "Initial growth & collaboration"),
            ("4", "Stability and stagnation"),
            ("5", "Conflict and friction"),
            ("6", "Harmony and recovery"),
            ("7", "Strategy and persistence"),
            ("8", "Movement and diligence"),
            ("9", "Culmination and resilience"),
            ("10", "Completion and cycles"),
            ("Page", "A messenger of new energy"),
            ("Knight", "Action, speed, and pursuit"),
            ("Queen", "Mastery and emotional depth"),
            ("King", "Authority, leadership, vision")
        ]
        
        for suit_name, suit_desc, suit_motif in suits:
            for rank_name, rank_desc in ranks:
                name = f"{rank_name} of {suit_name}"
                meaning = f"{rank_desc}: {suit_desc}"
                deck.append((name, meaning, suit_motif))
                
        return deck

    def draw_random_card(self, instance):
        self.card_container.clear_widgets()
        
        deck = self.get_full_deck()
        random.shuffle(deck)
        chosen_card = deck[0]
        
        card_widget = SurrealCardWidget(card_data=chosen_card)
        card_widget.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        self.card_container.add_widget(card_widget)

if __name__ == '__main__':
    TarotApp().run()
