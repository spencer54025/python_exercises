import random
player_total = 0
dealer_total = 0
bet = 0

def win_or_lose(p_total, d_total, bet):
    if d_total > 21:
        bet =  bet * 2
        print(f'you had {p_total} and the dealer had {d_total}')
        print(f'you win!, you made ${bet}')
    elif p_total == 21:
        bet = bet * 2
        print(f'you had {p_total} and the dealer had {d_total}')
        print(f'you win!, you made ${bet}')
    elif p_total > d_total and p_total < 21:
        print(f'you had {p_total} and the dealer had {d_total}'),
        bet = bet * 2
        print(f'you win!, you made ${bet}')
    elif p_total < d_total and d_total < 21:
        print(f'you had {p_total} and the dealer had {d_total}')
        print(f'you lose... you lost ${bet}')
    else:
        print(f'you lose... you lost ${bet}')

def totals(p_total, d_total):
    print(f'your total is now {p_total}')
    print(f'the dealers total is now {d_total}')

def new_card():
    return random.randrange(1, 10)


def blackjack(p_total, d_total, bet):
    
    print('how much would you like to bet? (you have $50)')
    bet = input()
    bet = int(bet)
    player_card = new_card() 
    dealer_card = new_card() 
    print(f'your first card is a {player_card}')
    print(f'the dealers first card is a {dealer_card}')
    p_total += player_card
    d_total += dealer_card
    pause = input()
    
    player_card = new_card() 
    dealer_card = new_card() 
    p_total += player_card
    d_total += dealer_card
    
    totals(p_total, d_total)
    
    if d_total <= 15 and d_total < p_total:
        dealer_card = new_card()
        d_total += dealer_card
    
    
    print('would you like to hit? (y or n)')
    hit = input()
    if hit == 'y':
        
        player_card = new_card() 
        p_total += player_card
        if d_total <= 15 and d_total < p_total: 
            dealer_card = new_card()
            d_total += dealer_card 
        totals(p_total, d_total) 
        print('would you like to hit again?')
        hit2 = input()
        if hit2 == 'y':
            
            player_card = new_card() 
            p_total += player_card
            if d_total <= 15 and d_total < p_total: 
                dealer_card = new_card()
                d_total += dealer_card
                if d_total <= 15 and d_total < p_total: 
                    dealer_card = new_card()
                    d_total += dealer_card
            totals(p_total, d_total) 

            
            print('would you like to hit?')
            finalhit = input()
            if finalhit == 'y':
               
                player_card = new_card() 
                p_total += player_card
                if d_total <= 15 and d_total < p_total: 
                    dealer_card = new_card()
                    d_total += dealer_card
                
                if p_total <= 21:
                    print(f'you win! you won ${bet * 2}') 
                else:
                    print(f'you lost... you lose ${bet}')       

            # end of game after fourth card
            elif finalhit == 'n':
                if d_total <= 15 and d_total < p_total: 
                    dealer_card = new_card()
                    d_total += dealer_card
                totals(p_total, d_total)
                win_or_lose(p_total, d_total, bet)        

        # end of game after third draw
        elif hit2 == 'n':
            if d_total <= 15 and d_total < p_total: 
                dealer_card = new_card()
                d_total += dealer_card
            elif d_total <= 15 and d_total < p_total:
                dealer_card = new_card()
                d_total += dealer_card
            totals(p_total, d_total)
            win_or_lose(p_total, d_total, bet)        
                
    # end of game after second draw
    elif hit == 'n':
        if d_total <= 15 and d_total < p_total:
            dealer_card = new_card()
            d_total += dealer_card
        elif d_total <= 15 and d_total < p_total: 
            dealer_card = new_card()
            d_total += dealer_card
        elif d_total <= 15 and d_total < p_total:
                dealer_card = new_card()
                d_total += dealer_card
        else:
            d_total = d_total
        totals(p_total, d_total)
        win_or_lose(p_total, d_total, bet)        
    
blackjack(player_total, dealer_total, bet)