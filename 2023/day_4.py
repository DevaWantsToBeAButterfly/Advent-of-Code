from aocd import get_data, submit

puzzle_input = get_data(year=2023, day=4).splitlines()
cleaned_input = []

score = 0
owned_cards = 0

for card in puzzle_input:
    card = card[card.index(':')+2:].split(' | ')
    winning_numbers = set(card[0].split())
    owned_numbers = set(card[1].split())
    owned_winning_numbers = winning_numbers & owned_numbers

    cleaned_input.append({'Winning numbers': len(owned_winning_numbers), 'Amount owned': 1})

for card in cleaned_input:
    if card['Winning numbers']:
        score += 2**(card['Winning numbers'] - 1)

print(score)
submit(score, part='a')

for card_index, card in enumerate(cleaned_input):
    for n in range(1, card['Winning numbers'] + 1):
        if card_index + n >= len(cleaned_input):
            break
        cleaned_input[card_index + n]['Amount owned'] += (1 * card['Amount owned'])

    owned_cards += card['Amount owned']

print(owned_cards)
submit(owned_cards, part='b')
