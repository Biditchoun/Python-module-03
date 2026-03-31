import sys


def process_input(argv: list) -> list:
    rt = []
    i = 1
    while (i < len(argv)):
        try:
            score = int(argv[i])
            rt.append(score)
        except ValueError:
            print(f"Invalid parameter: '{argv[i]}'")
        i += 1
    return (rt)


def print_stats(scores: list) -> None:
    scores_nb = len(scores)
    if (scores_nb == 0):
        print("No scores provided. Usage: ", end="")
        print("python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {scores_nb}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / scores_nb}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = process_input(sys.argv)
    print_stats(scores)
