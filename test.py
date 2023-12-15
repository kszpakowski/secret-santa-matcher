import unittest
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


class TestSecretSanta(unittest.TestCase):
    def setUp(self):
        self.pairs = generate_pairs_with_exclusions(test_participants, test_exclusions)

    def test_no_excluded_pairs_are_present(self):
        for pair in self.pairs:
            for e1, e2 in test_exclusions:
                self.assertTrue(
                    pair != (e1, e2) and pair != (e2, e1),
                    f"Found pair {pair} excluded by {(e1, e2)}",
                )

    def test_every_person_should_buy_one_gift(self):
        buyers = dict.fromkeys(test_participants, 0)

        for b, _ in self.pairs:
            buyers[b] = buyers[b] + 1

        for buyer in buyers:
            val = buyers[buyer]
            self.assertEqual(
                val, 1, f"{buyer} desn't buy exactly one gift - buys {val} instead"
            )

    def test_every_person_should_get_one_gift(self):
        recivers = dict.fromkeys(test_participants, 0)

        for _, r in self.pairs:
            recivers[r] = recivers[r] + 1

        for reciever in recivers:
            val = recivers[reciever]
            self.assertEqual(
                val, 1, f"{reciever} desn't get exactly one gift - gets {val} instead"
            )


if __name__ == "__main__":
    unittest.main()
