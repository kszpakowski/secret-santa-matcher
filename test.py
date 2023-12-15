import random
from main import generate_pairs_with_exclusions

test_participants = [
    "Karol",
    "Beata",
    "Marcin Ł",
    "Karolina",
    "Mateusz",
    "Ania",
    "Paweł",
    "Amanda",
    "Marcin P",
    "Julia",
    "Jacek",
    "Kamila",
]

test_exclusions = [
    ("Karol", "Beata"),
    ("Marcin Ł", "Karolina"),
    ("Mateusz", "Ania"),
    ("Paweł", "Amanda"),
    ("Marcin P", "Julia"),
    ("Jacek", "Kamila"),
    ("Paweł", "Mateusz"),
]


def test_every_person_should_get_one_gift(participants, pairs):
    recivers = dict.fromkeys(participants, 0)

    for _, r in pairs:
        recivers[r] = recivers[r] + 1

    for reciever in recivers:
        val = recivers[reciever]
        assert val == 1, f"{reciever} desn't get exactly one gift - gets {val} instead"


def test_every_person_should_buy_one_gift(participants, pairs):
    buyers = dict.fromkeys(participants, 0)

    for b, _ in pairs:
        buyers[b] = buyers[b] + 1

    for buyer in buyers:
        val = buyers[buyer]
        assert val == 1, f"{buyer} desn't buy exactly one gift - buys {val} instead"


def test_no_excluded_pairs_are_present(exclusions, pairs):
    for pair in pairs:
        for e1, e2 in exclusions:
            assert pair != (e1, e2) and pair != (
                e2,
                e1,
            ), f"Found pair {pair} excluded by {(e1, e2)}"


for i in range(10_000):
    print(i)
    random.shuffle(test_participants)
    pairs = generate_pairs_with_exclusions(test_participants, test_exclusions)

    print(pairs)

    test_every_person_should_buy_one_gift(test_participants, pairs)
    test_every_person_should_get_one_gift(test_participants, pairs)
    test_no_excluded_pairs_are_present(test_exclusions, pairs)
