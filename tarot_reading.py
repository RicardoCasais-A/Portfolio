import random

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

# Function to shuffle the deck of cards:
def shuffle_deck(deck):
    """
    Return a new shuffled copy of `deck`.
    Does not modify the original list passed in.
    """
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled

shuffled_deck = shuffle_deck(deck)

# DEBUG STATEMENT
# print("DEBUG: first 5 cards after shuffle ->", [c["name"] for c in shuffled_deck[:5]])

# Function to draw a card from the shuffled deck and assign a random orientation:
def draw_card_with_orientation(shuffled_deck):
    """
    Remove a card from shuffled_deck and assign a random orientation.
    Returns a dictionary: {"card": card_dict, "reversed": True/False}
    """
    if not shuffled_deck:
        raise ValueError("No more cards left in the deck to draw.")
    
    card = shuffled_deck.pop()  # Remove the last card from the deck
    reversed_flag = random.choice([False, True])  # True = reversed, False = upright
    return {"card": card, "reversed": reversed_flag}

# Example single draw
drawn_card = draw_card_with_orientation(shuffled_deck)

# DEBUG STATEMENT
# print("DEBUG: Drawn card ->", drawn_card["card"]["name"], "| Reversed?", drawn_card["reversed"])

# Function to create a 3-card spread:
def draw_spread(shuffled_deck):
    """
    Draws a 3-card spread: Past, Present, Future.
    Returns a list of dictionaries with card info and orientation.
    """
    spread_result = []
    positions = ["Past", "Present", "Future"]

    for position in positions:
        card_info = draw_card_with_orientation(shuffled_deck)
        card_info["position"] = position  # add the position in the spread
        spread_result.append(card_info)

    return spread_result


# DEBUG STATEMENT
# spread_debug = draw_spread(shuffled_deck)
# for card_info in spread_debug:
#    print(f"DEBUG: {card_info['position']} -> {card_info['card']['name']} | Reversed? {card_info['reversed']}")


