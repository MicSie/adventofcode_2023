import basics
import os
from functools import cmp_to_key

FIVE_OF_KIND = 7
FOUR_OF_KIND = 6
FULL_HOUSE = 5
THREE_OF_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1


def get_type(hand: str, is_jocker_wildcard: bool) -> int:
    histogram = dict()
    for card in hand:
        if card in histogram:
            histogram[card] += 1
        else:
            histogram[card] = 1

    if is_jocker_wildcard and "J" in histogram:
        jocker = histogram.pop("J")
        if jocker == 5:
            return FIVE_OF_KIND

        highest = [
            card
            for card, _ in sorted(
                histogram.items(), reverse=True, key=lambda item: item[1]
            )
        ][0]
        histogram[highest] += jocker

    if 5 in histogram.values():
        return FIVE_OF_KIND

    if 4 in histogram.values():
        return FOUR_OF_KIND

    if 3 in histogram.values():
        if 2 in histogram.values():
            return FULL_HOUSE
        return THREE_OF_KIND

    if 2 in histogram.values():
        if len([number for number in histogram.values() if number == 2]) > 1:
            return TWO_PAIR
        return ONE_PAIR

    return HIGH_CARD


def get_card_score(card: chr) -> int:
    match card:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return 11
        case "T":
            return 10
        case _:
            return int(card)


def parse_hands(
    lines: list[str], is_jocker_wildcard: bool
) -> list[tuple[str, int, int]]:
    hands = list()
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        hand_type = get_type(hand, is_jocker_wildcard)
        if is_jocker_wildcard:
            hand = hand.replace("J", "1")
        hands.append(
            (
                hand,
                bid,
                hand_type,
                is_jocker_wildcard,
            )
        )
    return hands


def sort_hands(hands: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]:
    return sorted(hands, key=cmp_to_key(compare_cards))


def compare_cards(hand1: tuple[str, int, int], hand2: tuple[str, int, int]) -> int:
    if hand1[2] < hand2[2]:
        return -1
    if hand1[2] > hand2[2]:
        return 1
    for index, card in enumerate(hand1[0]):
        if card == hand2[0][index]:
            continue
        if get_card_score(card) < get_card_score(hand2[0][index]):
            return -1
        return 1
    return 0


def get_winnings(lines: list[str], is_jocker_wildcard: bool) -> int:
    hands = parse_hands(lines, is_jocker_wildcard)
    return sum([hand[1] * (index + 1) for index, hand in enumerate(sort_hands(hands))])


def run_day():
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    lines = basics.read_file(file)
    print("Day07")
    print(f"\tPart1: {get_winnings(lines, False)}")
    print(f"\tPart2: {get_winnings(lines, True)}")


if __name__ == "__main__":
    run_day()
