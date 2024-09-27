import time
import tracemalloc



def game(my_cards, opp_cards, r):
    rank = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K','A']
    suit = ['S', 'C', 'D', 'H']
    for card in opp_cards[r]:
        for my_card in my_cards[r]:
            if rank.index(my_card) > rank.index(card):
                opp_cards[r].remove(card)
                my_cards[r].remove(my_card)
                break
        if opp_cards[r]:
            return False
    suit.remove(r)
    for char in suit:
        for card in opp_cards[char]:
            for my_card in my_cards[char]:
                if rank.index(my_card) > rank.index(card):
                    opp_cards[char].remove(card)
                    my_cards[char].remove(my_card)
                    break
            if opp_cards[char]:
                for card in opp_cards[char]:
                    if my_cards[r]:
                        opp_cards[char].remove(card)
                        my_cards[r] = my_cards[r][1:]
                    else:
                        return False
            if opp_cards[char]:
                return False
    return True

def main():
    with open('input.txt') as f:
        my_cards = {'S': [], 'C': [], 'D': [], 'H': []}
        opp_cards = {'S': [], 'C': [], 'D': [], 'H': []}
        n, m, r = [i for i in f.readline().split()]
        for my_card_m_r in f.readline().split():
            my_cards[my_card_m_r[1]].append(my_card_m_r[0])
        for oppo_card_m_r in f.readline().split():
            opp_cards[oppo_card_m_r[1]].append(oppo_card_m_r[0])
    with open("output.txt", "w") as f:
        f.write(('NO', 'YES')[game(my_cards, opp_cards, r)])


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()

