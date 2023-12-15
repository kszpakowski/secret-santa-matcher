import random
import copy


def generate_pairs_with_exclusions(participants, exclusions, max_attempts=50):
    exclusion_dict = {}
    for exclusion in exclusions:
        left, right = exclusion
        exclusion_dict.setdefault(left, []).append(right)
        exclusion_dict.setdefault(right, []).append(left)

    possible_partners = {}
    for participant in participants:
        possible_partners[participant] = [
            x
            for x in participants
            if not x == participant and not x in exclusion_dict.get(participant, [])
        ]

    sorted_possible_partners = sorted(
        possible_partners.items(), key=lambda kv: len(kv[1])
    )

    def attempt():
        pairs = []
        partners_copy = copy.deepcopy(sorted_possible_partners)
        for buyer, partners in partners_copy:
            partner = random.choice(partners)
            pairs.append((buyer, partner))
            for k in partners_copy:
                if partner in k[1]:
                    k[1].remove(partner)
        return pairs

    for i in range(max_attempts):
        print(f"attempt {i}")
        try:
            return attempt()
        except IndexError:
            pass

    raise RuntimeError("Unable to figure out secret sants")
