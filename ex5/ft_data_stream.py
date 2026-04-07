import random
import typing


def gen_event() -> typing.Generator:
    players = ["alice", "bob", "charlie", "dylan", "eliane"]
    actions = ["run", "eat", "sleep", "grab", "run",
               "move", "climb", "swim", "release"]
    while 1:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list) -> typing.Generator:
    while 1:
        removed = random.choice(events)
        events.remove(removed)
        yield removed


def train_yields() -> None:
    create_event = gen_event()
    i = 0
    while (i < 1000):
        event = next(create_event)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1
    events_list = []
    i = 0
    while (i < 10):
        events_list.append(next(create_event))
        i += 1
    print(f"Built list of {i} events: {events_list}")
    del_event = consume_event(events_list)
    while (len(events_list) > 0):
        removed = next(del_event)
        print(f"Got event from list: {removed}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    train_yields()
