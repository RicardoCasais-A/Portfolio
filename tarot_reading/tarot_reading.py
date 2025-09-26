import random

# Defining a TarotDeck class to encapsulate deck operations:
class TarotDeck:
    def __init__(self, deck):
        self.deck = deck
        self.normalize_meanings()
        self.shuffled_deck = self.shuffle()

    def normalize_meanings(self):
        """Ensure every card's meaning ends with a period."""
        for card in self.deck:
            if not card["meaning"].endswith("."):
                card["meaning"] += "."

    def shuffle(self):
        """Return a new shuffled copy of the deck."""
        shuffled = self.deck.copy()
        random.shuffle(shuffled)
        return shuffled

    def draw_card(self):
        """Draw a single card from the shuffled deck with a random orientation."""
        if not self.shuffled_deck:
            raise ValueError("No more cards left to draw.")
        card = self.shuffled_deck.pop()
        reversed_flag = random.choice([False, True])  # True = reversed, False = upright
        return {"card": card, "reversed": reversed_flag}

    def draw_spread(self, positions=["Past", "Present", "Future"]):
        """Draw multiple cards for a spread and assign positions."""
        spread = []
        for pos in positions:
            card_info = self.draw_card()
            card_info["position"] = pos
            spread.append(card_info)
        return spread
    
    def format_card_info(self, card_info, include_position=True):
        """Return a string describing a card with orientation and meaning."""
        card = card_info["card"]
        orientation = "Reversed" if card_info["reversed"] else "Upright"
        lines = []
        if include_position and "position" in card_info:
            lines.append(f"{card_info['position']}: {card['name']} ({orientation})")
        else:
            lines.append(f"You drew: {card['name']} ({orientation})")
        lines.append(f"Meaning: {card['meaning']}")
        return "\n".join(lines)

    def print_card(self, drawn):
        """Print a single drawn card."""
        print("\n" + self.format_card_info(drawn, include_position=False))

    def print_spread(self, spread):
        """Print multiple cards in a spread."""
        print("\nYour spread:")
        for info in spread:
            print(self.format_card_info(info), "\n")

# Defining the main application class to handle user interaction:
class TarotApp:
    def __init__(self, deck):
        """Initialize the app with a TarotDeck instance."""
        self.deck = TarotDeck(deck)
        self.choice_map = {"1": "single", "2": "spread"}

    def main_menu(self):
        """Show the main menu and return user choice as '1', '2', or '3'."""
        print("\n--- Tarot Reading ---")
        print("\nNote on card orientations:")
        print("Upright interpretation: → Positive, direct, manifesting naturally.")
        print("Reversed interpretation: → Blocked, opposite, or internalized.\n")
        print("1: Draw a single card")
        print("2: Draw a 3-card spread")
        print("3: Quit")
        choice = input("Choose an option (1-3): ").strip().lower()
        return choice

    def ask_next_step(self):
        """Ask user if they want to draw again, switch type, or quit."""
        valid = {"again", "switch", "quit"}
        while True:
            choice = input(
                "Do you want to draw again (same type), switch type, or quit? (again/switch/quit): "
            ).strip().lower()
            if choice in valid:
                return choice
            print("Invalid input, please enter 'again', 'switch', or 'quit'.")

    def draw_and_print(self, draw_type):
        """Handles drawing and printing cards based on draw_type."""
        try:
            if draw_type == 'single':
                drawn = self.deck.draw_card()
                self.deck.print_card(drawn)
            elif draw_type == 'spread':
                spread = self.deck.draw_spread()
                self.deck.print_spread(spread)
            return True
        except ValueError:
            prompt = "Deck empty. Reshuffle? (y/n): " if draw_type == 'single' else "Not enough cards. Reshuffle deck? (y/n): "
            if input(prompt).strip().lower() == "y":
                self.deck.shuffled_deck = self.deck.shuffle()
                return self.draw_and_print(draw_type)
            return False

    def run(self):
        """Run the main application loop."""
        while True:
            choice = self.main_menu()
            if choice == "3":
                print("\nGoodbye! May the cards guide you.\n")
                return

            draw_type = self.choice_map.get(choice)
            if not draw_type:
                print("Invalid option, please choose 1, 2, or 3.\n")
                continue

            while True:
                if not self.draw_and_print(draw_type):
                    msg = "Exiting program." if draw_type == "single" else "Cannot draw a 3-card spread. Exiting."
                    print(msg)
                    return

                next_step = self.ask_next_step()
                if next_step == "quit":
                    print("\nGoodbye! May the cards guide you.\n")
                    return
                elif next_step == "switch":
                    break  # Return to main menu to choose a new option


# Creating a major list of dicts to hold the deck data:
deck = [
    # Major Arcana
    {"name": "The Fool", "meaning": "Beginnings, innocence, spontaneity, free spirit"},
    {"name": "The Magician", "meaning": "Manifestation, resourcefulness, power, inspired action"},
    {"name": "The High Priestess", "meaning": "Intuition, unconscious knowledge, mystery"},
    {"name": "The Empress", "meaning": "Fertility, nurturing, abundance, nature"},
    {"name": "The Emperor", "meaning": "Authority, structure, control, stability"},
    {"name": "The Hierophant", "meaning": "Tradition, conformity, spiritual wisdom"},
    {"name": "The Lovers", "meaning": "Love, harmony, relationships, choices"},
    {"name": "The Chariot", "meaning": "Willpower, determination, success"},
    {"name": "Strength", "meaning": "Courage, persuasion, influence, compassion"},
    {"name": "The Hermit", "meaning": "Introspection, inner guidance, solitude"},
    {"name": "Wheel of Fortune", "meaning": "Cycles, fate, karma, turning points"},
    {"name": "Justice", "meaning": "Fairness, truth, law, accountability"},
    {"name": "The Hanged Man", "meaning": "Pause, surrender, new perspective"},
    {"name": "Death", "meaning": "Endings, transformation, transition"},
    {"name": "Temperance", "meaning": "Balance, moderation, purpose"},
    {"name": "The Devil", "meaning": "Bondage, addiction, materialism, shadow self"},
    {"name": "The Tower", "meaning": "Sudden change, upheaval, revelation"},
    {"name": "The Star", "meaning": "Hope, faith, renewal, inspiration"},
    {"name": "The Moon", "meaning": "Illusion, intuition, fear, subconscious"},
    {"name": "The Sun", "meaning": "Joy, success, vitality, optimism"},
    {"name": "Judgement", "meaning": "Rebirth, inner calling, absolution"},
    {"name": "The World", "meaning": "Completion, accomplishment, wholeness"},
    
    # Minor Arcana - Wands
    {"name": "Ace of Wands", "meaning": "Inspiration, new opportunities, growth, potential"},
    {"name": "Two of Wands", "meaning": "Planning, decisions, progress"},
    {"name": "Three of Wands", "meaning": "Expansion, foresight, overseas opportunities"},
    {"name": "Four of Wands", "meaning": "Celebration, harmony, home, community"},
    {"name": "Five of Wands", "meaning": "Conflict, competition, disagreements"},
    {"name": "Six of Wands", "meaning": "Victory, success, public recognition"},
    {"name": "Seven of Wands", "meaning": "Challenge, perseverance, defense"},
    {"name": "Eight of Wands", "meaning": "Speed, progress, movement, quick action"},
    {"name": "Nine of Wands", "meaning": "Resilience, persistence, boundaries"},
    {"name": "Ten of Wands", "meaning": "Burden, responsibility, hard work"},
    {"name": "Page of Wands", "meaning": "Exploration, enthusiasm, discovery"},
    {"name": "Knight of Wands", "meaning": "Energy, passion, adventure, impulsiveness"},
    {"name": "Queen of Wands", "meaning": "Courage, determination, confidence"},
    {"name": "King of Wands", "meaning": "Leadership, vision, honor, entrepreneurship"},

    # Minor Arcana - Cups
    {"name": "Ace of Cups", "meaning": "Love, new relationships, compassion, creativity"},
    {"name": "Two of Cups", "meaning": "Partnership, attraction, harmony"},
    {"name": "Three of Cups", "meaning": "Friendship, community, celebration"},
    {"name": "Four of Cups", "meaning": "Apathy, contemplation, reevaluation"},
    {"name": "Five of Cups", "meaning": "Loss, grief, disappointment"},
    {"name": "Six of Cups", "meaning": "Reunion, nostalgia, childhood memories"},
    {"name": "Seven of Cups", "meaning": "Choices, illusion, wishful thinking"},
    {"name": "Eight of Cups", "meaning": "Withdrawal, retreat, moving on"},
    {"name": "Nine of Cups", "meaning": "Contentment, satisfaction, gratitude"},
    {"name": "Ten of Cups", "meaning": "Harmony, marriage, happiness, alignment"},
    {"name": "Page of Cups", "meaning": "Creative opportunities, curiosity, possibility"},
    {"name": "Knight of Cups", "meaning": "Romance, charm, imagination"},
    {"name": "Queen of Cups", "meaning": "Compassion, calm, intuition"},
    {"name": "King of Cups", "meaning": "Emotional balance, diplomacy, generosity"},

    # Minor Arcana - Swords
    {"name": "Ace of Swords", "meaning": "Breakthrough, clarity, truth, new ideas"},
    {"name": "Two of Swords", "meaning": "Difficult decisions, avoidance, stalemate"},
    {"name": "Three of Swords", "meaning": "Heartbreak, grief, sorrow"},
    {"name": "Four of Swords", "meaning": "Rest, recovery, meditation"},
    {"name": "Five of Swords", "meaning": "Conflict, defeat, tension, betrayal"},
    {"name": "Six of Swords", "meaning": "Transition, moving on, change"},
    {"name": "Seven of Swords", "meaning": "Deception, strategy, betrayal"},
    {"name": "Eight of Swords", "meaning": "Restriction, fear, paralysis"},
    {"name": "Nine of Swords", "meaning": "Anxiety, worry, nightmares"},
    {"name": "Ten of Swords", "meaning": "Endings, ruin, rock bottom, betrayal"},
    {"name": "Page of Swords", "meaning": "Curiosity, vigilance, communication"},
    {"name": "Knight of Swords", "meaning": "Ambition, speed, determination"},
    {"name": "Queen of Swords", "meaning": "Perception, independence, clarity"},
    {"name": "King of Swords", "meaning": "Authority, truth, intellect, discipline"},

    # Minor Arcana - Pentacles
    {"name": "Ace of Pentacles", "meaning": "Manifestation, new financial opportunity, prosperity"},
    {"name": "Two of Pentacles", "meaning": "Balance, adaptability, time management"},
    {"name": "Three of Pentacles", "meaning": "Teamwork, collaboration, skill"},
    {"name": "Four of Pentacles", "meaning": "Control, security, saving, scarcity"},
    {"name": "Five of Pentacles", "meaning": "Financial loss, isolation, insecurity"},
    {"name": "Six of Pentacles", "meaning": "Generosity, charity, giving and receiving"},
    {"name": "Seven of Pentacles", "meaning": "Patience, investment, long-term view"},
    {"name": "Eight of Pentacles", "meaning": "Apprenticeship, skill development, diligence"},
    {"name": "Nine of Pentacles", "meaning": "Luxury, self-sufficiency, abundance"},
    {"name": "Ten of Pentacles", "meaning": "Wealth, inheritance, family, establishment"},
    {"name": "Page of Pentacles", "meaning": "Opportunity, manifestation, ambition"},
    {"name": "Knight of Pentacles", "meaning": "Hard work, responsibility, efficiency"},
    {"name": "Queen of Pentacles", "meaning": "Nurturing, practicality, resourcefulness"},
    {"name": "King of Pentacles", "meaning": "Abundance, security, leadership, prosperity"},
]


# Running the application:
if __name__ == "__main__":
    app = TarotApp(deck)
    app.run()


