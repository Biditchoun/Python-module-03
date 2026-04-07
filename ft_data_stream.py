import random


def gen_event() -> None:
	players = ["alice", "bob", "charlie", "dylan", "eliane"]
	actions = ["run", "eat", "sleep", "grab", "run", "move", "climb", "swim", "release"]
	while 1:
		name = random.choice(players)
		action = random.choice(actions)
		yield (name, action)


def consume_event(events: list) -> None:
	while 1:
		removed = random.choice(events)
		events.remove(removed)
		yield removed


def main() -> None:
	print("=== Game Data Stream Processor ===")
	i = 0
	while (i < 1000):
		event = gen_event()
		print(f"Event {i}: Player {event[0]} did action {event[1]}")
		i += 1
	i = 0
	events_list = []
	while (i < 10):
		events_list.append(gen_event())
	print(f"Built list of {i} events: {events_list}")
	while (len(events_list) > 0):
		removed = consume_event(events_list)
		print(f"Got event from list: {removed}")
		print(f"Remains in list: {events_list}")


if __name__ == "__main__":
	main()
