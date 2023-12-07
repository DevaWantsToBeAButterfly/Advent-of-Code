from aocd import get_data, submit

puzzle_input = get_data(day=7, year=2023).splitlines()
hands = [{'Cards': line.split(' ')[0], 'Bid': int(line.split(' ')[1]), 'Hand type': None} for line in puzzle_input]

cards_by_value = 'AKQJT98765432'
cards_by_value_using_jokers = 'AKQT98765432J'
hand_types_by_value = ['Five of a kind', 'Four of a kind', 'Full house',
                       'Three of a kind', 'Two pair', 'One pair', 'High card']


def find_hand_type(hand_cards, using_jokers=False):
    match len(set(hand_cards)):
        case 1:
            hand_type = 'Five of a kind'

        case 2:
            if using_jokers and 'J' in hand_cards:
                hand_type = 'Five of a kind'
            else:
                if hand_cards.count(hand_cards[0]) in (1, 4):
                    hand_type = 'Four of a kind'
                else:
                    hand_type = 'Full house'

        case 3:
            if using_jokers and 'J' in hand_cards:
                for card in hand_cards:
                    if hand_cards.count(card) == 3:
                        hand_type = 'Four of a kind'
                        break
                    elif hand_cards.count(card) == 2:
                        if hand_cards.count('J') == 2:
                            hand_type = 'Four of a kind'
                        else:
                            hand_type = 'Full house'
                        break
            else:
                for card in hand_cards:
                    if hand_cards.count(card) == 3:
                        hand_type = 'Three of a kind'
                        break
                    elif hand_cards.count(card) == 2:
                        hand_type = 'Two pair'
                        break

        case 4:
            if using_jokers and 'J' in hand_cards:
                hand_type = 'Three of a kind'
            else:
                hand_type = 'One pair'

        case 5:
            if using_jokers and 'J' in hand_cards:
                hand_type = 'One pair'
            else:
                hand_type = 'High card'

    return hand_type


def find_winning_hand(first_hand, second_hand, using_jokers=False):
    if hand_types_by_value.index(first_hand['Hand type']) < hand_types_by_value.index(second_hand['Hand type']):
        return first_hand
    elif hand_types_by_value.index(first_hand['Hand type']) > hand_types_by_value.index(second_hand['Hand type']):
        return second_hand
    else:
        return find_higher_first_card(first_hand, second_hand, using_jokers)


def find_higher_first_card(first_hand, second_hand, using_jokers=False):
    if using_jokers:
        card_scores = cards_by_value_using_jokers
    else:
        card_scores = cards_by_value

    for n in range(len(first_hand['Cards'])):
        if card_scores.index(first_hand['Cards'][n]) < card_scores.index(second_hand['Cards'][n]):
            return first_hand
        elif card_scores.index(first_hand['Cards'][n]) > card_scores.index(second_hand['Cards'][n]):
            return second_hand


def quick_sort(hand_list, using_jokers=False):
    pivot_hand = hand_list[0]
    lower_hands = []
    higher_hands = []

    for hand in hand_list[1:]:
        if find_winning_hand(pivot_hand, hand, using_jokers) == pivot_hand:
            lower_hands.append(hand)
        else:
            higher_hands.append(hand)

    if len(lower_hands) > 1:
        lower_hands = quick_sort(lower_hands, using_jokers)
    if len(higher_hands) > 1:
        higher_hands = quick_sort(higher_hands, using_jokers)

    return lower_hands + [pivot_hand] + higher_hands


def reorder_hands_list(hands_list, using_jokers=False):
    for hand in hands_list:
        hand['Hand type'] = find_hand_type(hand['Cards'], using_jokers)

    return quick_sort(hands_list, using_jokers)


def count_score(hands_list):
    return sum((hands_list.index(hand) + 1) * hand['Bid'] for hand in hands_list)


def solve_puzzle(hands_list, using_jokers, part):
    sorted_hands = reorder_hands_list(hands_list, using_jokers)
    total_winnings = count_score(sorted_hands)

    print(total_winnings)
    submit(total_winnings, part=part)


solve_puzzle(hands, False, 'a')
solve_puzzle(hands, True, 'b')
