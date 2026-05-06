# Trace Anderson
# 5/5/2026
# finalProject_AndersonTrace

import random
import time
import copy

# -----------------------------
# Utility
# -----------------------------

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

# -----------------------------
# Class System
# -----------------------------

def choose_class():
    classes = {
        "rogue": {"health": 80, "energy": 70, "weapon": "Dual stuffed Squirrels"},
        "cleric": {"health": 90, "energy": 60, "weapon": "Greatstaff of Akravaari"},
        "knight": {"health": 120, "energy": 40, "weapon": "Greatsword of Rakviir"},
        "ranger": {"health": 100, "energy": 60, "weapon": "yew bow of Morwenna"},
        "shaman": {"health": 85, "energy": 75, "weapon": "Book of Minorly Inconvenient Spells"}
    }

    print("Choose your class:")
    for c in classes:
        print("-", c.title())

    choice = input("> ").lower()

    if choice not in classes:
        print("Invalid choice, defaulting to Rogue.")
        choice = "rogue"

    return choice, classes[choice]

# -----------------------------
# Player Creation
# -----------------------------

def create_player():
    name = input("Enter your character's name: ")

    chosen_class, stats = choose_class()

    player = {
        "name": name,
        "class": chosen_class,
        "health": stats["health"],
        "energy": stats["energy"],
        "gold": 10,
        "boredom": 0  # used for goblin fight
    }

    inventory = {
        stats["weapon"]: 1,
        "healing potion": 1
    }

    return player, inventory

# -----------------------------
# Rooms (Dictionary)
# -----------------------------

rooms = {
    "entrance": ["npc", "empty"],
    "hallway": ["trap", "treasure", "empty"],
    "chamber": ["rest", "npc"],
    "boss_room": ["goblin"]
}

# -----------------------------
# NPC Interaction
# -----------------------------

def npc_interaction(player):
    slow_print("\n🧙 A mysterious hooded traveler appears...")
    slow_print('"The goblin ahead cannot be defeated by strength..."')

    choice = input("Listen carefully? (yes/no): ").lower()

    if choice == "yes":
        slow_print('"Bore it... talk endlessly... it will fall asleep." 😴')
        player["energy"] += 10
        slow_print("You feel wiser. +10 energy.")
    else:
        slow_print("You ignore the advice... bold choice.")

# -----------------------------
# Encounters
# -----------------------------

def encounter(player):
    room = random.choice(list(rooms.keys()))
    event = random.choice(rooms[room])

    slow_print(f"\n🚪 You enter the {room}...")

    if event == "empty":
        slow_print("Nothing happens.")

    elif event == "treasure":
        gold = random.randint(5, 15)
        player["gold"] += gold
        slow_print(f"💰 Found {gold} gold!")

    elif event == "trap":
        dmg = random.randint(5, 10)
        player["health"] -= dmg
        slow_print(f"⚠️ Trap! You lose {dmg} health.")

    elif event == "rest":
        heal = random.randint(5, 10)
        player["health"] += heal
        slow_print(f"🌿 You rest and recover {heal} health.")

    elif event == "npc":
        npc_interaction(player)

    # elif event == "goblin":
    #    return goblin_encounter(player)

    return False

# -----------------------------
# Goblin Boss (Non-Violent Win)
# -----------------------------

def goblin_encounter(player):
    slow_print("\n👹 A massive goblin blocks your path!")
    slow_print("It looks WAY stronger than you...")

    attack_count = 0
    player_class = player["class"]

    # -----------------------------
    # Class-Based Dialogue
    # -----------------------------

    dialogue = {
        "rogue": {
            "joke": [
                "I’d tell you a stealth joke… but you’d never see it coming.",
                "Why do rogues hate loud noises? It ruins the sneak preview.",
                "I tried to pickpocket a ghost once… got nothing but boo’d."
            ],
            "talk": [
                "Life’s just a series of risks, right? You either take them or get left behind.",
                "Trust is currency… and most people are broke.",
                "Maybe survival is the only meaning that really matters."
            ],
            "lecture": [
                "You’re really just standing here all day? No ambition?",
                "You could’ve been clever… instead you’re predictable.",
                "Even amateurs know when to move on."
            ]
        },

        "cleric": {
            "joke": [
                "I tried to bless my food… it became holy guacamole.",
                "Why don’t clerics get lost? Because they follow the light.",
                "I told a joke in the temple once… it was divine comedy."
            ],
            "talk": [
                "Perhaps life is about service to something greater than ourselves.",
                "Meaning comes from compassion, not conquest.",
                "Every soul has purpose… even yours, I think."
            ],
            "lecture": [
                "Your ancestors are watching… and they are not impressed.",
                "This is not a righteous path you walk.",
                "You were meant for more than this idle existence."
            ]
        },

        "knight": {
            "joke": [
                "Why don’t knights ever get tired? Because they’re always armored with energy.",
                "I tried to fight a dragon once… turns out it was just my in-laws.",
                "This armor isn’t just for looks… it’s knight-approved."
            ],
            "talk": [
                "Honor gives life meaning. Without it, what are we?",
                "A life without purpose is no life at all.",
                "We define ourselves by the battles we choose."
            ],
            "lecture": [
                "Stand up straight. You lack discipline.",
                "This is dishonorable conduct… even for a goblin.",
                "Your father would expect more strength from you."
            ]
        },

        "ranger": {
            "joke": [
                "Why don’t trees gossip? They keep things rooted.",
                "I once tracked a deer for days… turns out it was just my shadow.",
                "Nature called… you didn’t answer."
            ],
            "talk": [
                "Life flows like a river… always moving, never stopping.",
                "Balance is everything in this world.",
                "We’re all just part of a bigger ecosystem."
            ],
            "lecture": [
                "You’ve disrupted the natural balance just by being here.",
                "Predators adapt… you clearly haven’t.",
                "Even the wild has standards. You don’t meet them."
            ]
        },

        "shaman": {
            "joke": [
                "The spirits told me a joke… I forgot it, but it was funny.",
                "Why did the wind laugh? Because it swept the competition.",
                "I asked the ancestors for humor… this is what I got."
            ],
            "talk": [
                "The spirits whisper that life is a journey, not a destination.",
                "Energy flows through all things… even this awkward moment.",
                "You and I are connected, whether we like it or not."
            ],
            "lecture": [
                "The ancestors are… shaking their heads at you.",
                "Your spirit is… deeply unimpressive.",
                "You’ve angered forces you don’t even understand."
            ]
        }
    }
    class_dialogue = copy.deepcopy(dialogue[player_class])

    for category in class_dialogue:
        random.shuffle(class_dialogue[category])

    def get_line(category):
        if len(class_dialogue[category]) == 0:
            class_dialogue[category] = copy.deepcopy(dialogue[player_class][category])
            random.shuffle(class_dialogue[category])

        return class_dialogue[category].pop()

    # -----------------------------
    # Goblin Loop
    # -----------------------------

    while True:
        choice = input("\nDo you (attack / talk / joke / lecture): ").lower()

        if choice == "attack":
            attack_count += 1
            damage = random.randint(12, 20)

            slow_print("⚔️ You strike at the goblin!")
            slow_print("👹 The goblin effortlessly counters...")
            slow_print(f"💥 You take {damage} damage!")

            player["health"] -= damage

            if attack_count >= 3:
                slow_print("\n👹 The goblin grows tired of your attacks...")
                slow_print("💀 It knocks you out cold. You failed.")
                return False

        elif choice in ["joke", "talk", "lecture"]:
            line = get_line(choice)

            if choice == "joke":
                slow_print(f"\n😂 You say: \"{line}\"")
                boredom_gain = random.randint(15, 25)

            elif choice == "talk":
                slow_print(f"\n🧠 You say: \"{line}\"")
                boredom_gain = random.randint(10, 20)

            elif choice == "lecture":
                slow_print(f"\n📢 You say: \"{line}\"")
                boredom_gain = random.randint(20, 30)

            player["boredom"] += boredom_gain
            slow_print(f"😐 The goblin looks increasingly bored... (+{boredom_gain})")

        else:
            slow_print("You hesitate... the goblin stares.")

        # Win condition
        if player["boredom"] >= 100:
            slow_print("\n😴 The goblin collapses from boredom and falls asleep!")
            slow_print("🏆 You escape the dungeon. Victory!")
            return True

        # Lose condition
        if player["health"] <= 0:
            return False


# -----------------------------
# Inventory
# -----------------------------

def use_item(player, inventory):
    print("\n🎒 Inventory:", inventory)

    choice = input("Use item? (healing potion / no): ").lower()

    if choice == "healing potion" and inventory.get("healing potion", 0) > 0:
        player["health"] += 20
        inventory["healing potion"] -= 1
        slow_print("❤️ You healed +20 health.")
    else:
        slow_print("Nothing used.")

# -----------------------------
# Status
# -----------------------------

def show_status(player):
    print("\n📊 STATUS")
    for key, value in player.items():
        print(f"{key.title()}: {value}")

# -----------------------------
# Main
# -----------------------------

def main():
    slow_print("🏰 Welcome to the Dungeon of Endless Conversation...\n")

    while True: # restart loop
        player, inventory = create_player()

        explore_count = 0
        npc_triggered = False
        post_npc_explore = 0    

        while player["health"] > 0:
            show_status(player)

            action = input("\nChoose action (explore / inventory / quit): ").lower()

            if action == "explore":
                explore_count += 1

                # --- NPC on 3rd explore ---
                if explore_count == 3 and not npc_triggered:
                    npc_interaction(player)
                    npc_triggered = True
                    post_npc_explore = 0
                    continue

                # --- After NPC ---
                if npc_triggered:
                    post_npc_explore += 1

                    # --- Goblin on 2nd explore AFTER NPC ---
                    if post_npc_explore == 2:
                        won = goblin_encounter(player)

                        # (loss vs win handling)
                        if won:
                            slow_print("\n🎉 You escaped the dungeon successfully!")
                            return  # end game completely

                        else:
                            slow_print("\n💀 You were defeated... restarting your journey.\n")
                            break  # breaks inner loop → restarts game

                # --- Normal encounters ---
                encounter(player) 

            elif action == "inventory":
                use_item(player, inventory)

            elif action == "quit":
                return

            else:
                print("Invalid choice.")

            player["energy"] -= 2

            if player["energy"] <= 0:
                player["health"] -= 5
                slow_print("😓 Exhaustion hurts you.")

            time.sleep(1)

        if player["health"] <= 0:
            slow_print("\n💀 You collapse before escaping the dungeon...")
            slow_print("🔁 Your journey begins again...\n")
            time.sleep(2)            
            

# -----------------------------
# Run
# -----------------------------

if __name__ == "__main__":
    main()