#!/usr/bin/python3

import random


# vars
PRISONERS_COUNT = 100
TRY_COUNT = 50
STATISTIC_COUNT = 10000


# shuffle cards func
def generate_cards() -> list:
    cards_list = [x for x in range(PRISONERS_COUNT)]
    random.shuffle(cards_list)
    return cards_list

# trying to open the box with the card
def dead_or_alive() -> str:
    random_cards = generate_cards()

    result = check_that_cards_is_correct(random_cards)

    if result == PRISONERS_COUNT:
        return "All of the prisoners are alive"
    else:
        return "Some people were unlucky, all of the prisoners are dead now"

def check_that_cards_is_correct(random_cards) -> int:
    win_prisoners_count = 0

    for prisoner in range (PRISONERS_COUNT):
        some_try = random_cards[prisoner]

        for try_count in range (TRY_COUNT):
            some_try = random_cards[some_try]
            if some_try == prisoner:
                win_prisoners_count += 1
                break

    return win_prisoners_count

def get_statistic() -> str:
    good_tryes = 0

    for i in range (STATISTIC_COUNT):
        result = dead_or_alive()
        if result == "All of the prisoners are alive":
            good_tryes += 1

    get_percent = good_tryes / STATISTIC_COUNT * 100
    return_value = "{:.2f}".format(get_percent)

    return "Survive percent is: {}, we tried {} times".format(return_value, STATISTIC_COUNT)

# use loop for statistic
for i in range(10):
    print(get_statistic())
