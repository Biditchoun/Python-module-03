import random


def gen_player_achievements() -> set:
    achievements = ["Crafting Genius", "World Savior", "Master Explorer",
                    "Collector Supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Unstoppable", "Speed Runner",
                    "Survivor", "Treasure Hunter", "First Steps",
                    "Sharp Mind", "Very killable Demon King", "Egg",
                    "Pencil Sharpener", "Pen duller", "Faker"]
    return set(random.sample(achievements, random.randint(5, 10)))


def achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    print()
    all_ach = Alice.union(Bob, Charlie, Dylan)
    print(f"All distinct achievements: {all_ach}\n")
    print(f"Common achievements: {Alice.intersection(Bob, Charlie, Dylan)}\n")
    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Alice, Bob, Charlie)}\n")
    print(f"Alice is missing: {all_ach.difference(Alice)}")
    print(f"Bob is missing: {all_ach.difference(Bob)}")
    print(f"Charlie is missing: {all_ach.difference(Charlie)}")
    print(f"Dylan is missing: {all_ach.difference(Dylan)}")


if __name__ == "__main__":
    achievement_tracker()
