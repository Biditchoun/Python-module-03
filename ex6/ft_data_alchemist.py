import random


def comprehensions_training() -> None:
    names = ["Alice", "bob", "Charlie", "dylan", "Emma",
             "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {names}")
    all_cap = [name.capitalize() for name in names]
    uncap = [name for name in names if name.capitalize() == name]
    print(f"New list with all names capitalized: {all_cap}")
    print(f"New list capitalized names only: {uncap}\n")
    score_dict = {name: random.randint(0, 1111) for name in all_cap}
    print(f"Score dict: {score_dict}")
    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")
    high_scores = {name: score for name, score
                   in score_dict.items() if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    comprehensions_training()
