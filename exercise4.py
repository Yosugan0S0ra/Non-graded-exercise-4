import random
import sys
import tkinter as tk
import time
card_deck = [
    {'number': 1,'Name': 'Diablo','Health': 100,'Attack': 90,'Defense': 60},
    {'number': 2,'Name': 'Medusa','Health': 100,'Attack': 70,'Defense': 70},
    {'number': 3,'Name': 'Jester', 'Health': 120, 'Attack': 60, 'Defense': 90},
    {'number': 4,'Name': 'Troll','Health': 150,'Attack': 40,'Defense': 94},
    {'number': 5,'Name': 'Specter','Health': 100,'Attack': 70,'Defense': 70},
    {'number': 6,'Name': 'Mist','Health': 100,'Attack': 75,'Defense': 65},
    {'number': 7,'Name': 'Savage','Health': 100,'Attack': 90,'Defense': 50},
    {'number': 8,'Name': 'Marauder','Health': 100,'Attack': 85,'Defense': 50},
    {'number': 9,'Name': 'Wimp','Health': 110,'Attack': 40,'Defense': 85},
    {'number': 10,'Name': 'Sorcerer','Health': 100,'Attack': 70,'Defense': 55}
]

deck_size = 5
hero_card = []
hero_attack_card = []
computer_card = []
computer_attack_card = [] 
c_round = 0
# #TK ENTER
# spacing = 10
# cell_size = 120
# canvas_width = deck_size * (cell_size + spacing) + spacing
# canvas_height = 5 * (cell_size + spacing) + spacing

# #touch
# selected_card = None
# selecting_for_battle = False


def set_card():
    global hero_card, computer_card
    time.sleep(0.5)
    print("Now, it's time you choose your cards!")
    
    for _ in range(deck_size):
        chosen_hero_card = random.choice(card_deck)
        hero_card.append(chosen_hero_card)
        time.sleep(0.5)
        print(f"Hero card selected: {chosen_hero_card['Name']} (HP: {chosen_hero_card['Health']}, ATK: {chosen_hero_card['Attack']}, DEF: {chosen_hero_card['Defense']})")
        
        chosen_computer_card = random.choice(card_deck)
        computer_card.append(chosen_computer_card)  
        time.sleep(0.5)
    time.sleep(0.5)
    # print("\nFinal hero cards: ")
    # for card in hero_card:
    #     time.sleep(0.5)
    #     print(f"{card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")
    
    # print("\nFinal computer cards: ")
    # for card in computer_card:
    #     print(f"{card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")


def attack(attack_card,def_card):
    time.sleep(0.5)
    print(f"{attack_card['Name']} is attacking {def_card['Name']}")
    if attack_card['Attack'] > def_card['Defense']:
        remaining_attack = attack_card['Attack'] - def_card['Defense']
        def_card['Defense'] = 0
        def_card['Health'] -= remaining_attack
        if def_card['Health'] <= 0:
            def_card['Health'] = 0
            time.sleep(0.5)
            print(f"{def_card['Name']} died")
        else:
            time.sleep(0.5)
            print(f"{def_card['Name']} is left with {def_card['Health']} health")
    else:
        def_card['Defense'] -= attack_card['Attack']
        time.sleep(0.5)
        print(f"{def_card['Name']}'s defense is reduced to {def_card['Defense']}")



# def on_card_click(event):
#     global selected_card, selecting_for_battle
#     item_id = event.widget.find_closest(event.x, event.y)[0]
#     tags = event.widget.gettags(item_id)
    
#     if not tags:
#         return

#     card_id = tags[0]
    
#     if selecting_for_battle:
#         if card_id.startswith('hero_'):
#             card_index = int(card_id.split('_')[1])
#             if hero_card:
#                 selected_card = hero_card[card_index]
#                 hero_attack_card.append(selected_card)
#                 hero_card.remove(selected_card)
#                 print(f"选择的出战卡牌：{selected_card['Name']}")
#                 draw_war()  # 更新界面
#                 selecting_for_battle = False
#     else:
#         if card_id.startswith('hero_'):
#             card_index = int(card_id.split('_')[1])
#             selected_card = hero_card[card_index]
#             print(f"选择了出战卡牌：{selected_card['Name']}")
#             selecting_for_battle = True
#         elif card_id.startswith('computer_') and selected_card in hero_attack_card:
#             card_index = int(card_id.split('_')[1])
#             if computer_attack_card:
#                 target_card = computer_attack_card[card_index]
#                 attack(selected_card, target_card)
#                 draw_war() 
#                 selected_card = None 
#                 selecting_for_battle = False



def computer_logic():
    x = random.randint(0,3)
    if not computer_attack_card :
        x = 0
    if not computer_card :
        x = random.randint(1,3)
    match x :
        case 0 :
            if computer_card:
                chosen_card = random.choice(computer_card)
                computer_attack_card.append(chosen_card)
                computer_card.remove(chosen_card)
                time.sleep(0.5)
                print("computer choose:")
                for i, card in enumerate(computer_attack_card):
                    time.sleep(0.5)
                    print(f"{card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")
#            draw_war()
        case 1:
            if computer_attack_card:
                attack_card = max(computer_attack_card, key=lambda c: c['Attack'])
                def_card = min(hero_attack_card, key=lambda c: c['Health'] + c['Defense'])
                attack(attack_card, def_card)

        case 2:
            if computer_attack_card and hero_attack_card:
                attack_card = random.choice(computer_attack_card)
                def_card = random.choice(hero_attack_card)
                attack(attack_card, def_card)

def show_zone():
    print("Computer's Attack Zone:")
    if computer_attack_card:
        for i, card in enumerate(computer_attack_card):
            print(f"{i + 1}. {card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")
    else:
        print("No cards in computer's attack zone.")

    print("\nHero's Attack Zone:")
    if hero_attack_card:
        for i, card in enumerate(hero_attack_card):
            print(f"{i + 1}. {card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")
    else:
        print("No cards in hero's attack zone.")

    print("\n" + "="*50)

def hero_choose():
    
    if not hero_card and not hero_attack_card:
        print("no card!")
        sys.exit("Game Over!Computer win")

    if not hero_attack_card:
        action_choice = 1 
        time.sleep(0.5)
        print("you have no card to attack, plz choose a card into attack zone")
    else:
        print("plz choose a action")
        print("1. choose a card into attack zone")
        print("2. use card to attack enermy")
        try:
            action_choice = int(input("\n"))
        except ValueError:
            print("invalid, skip your turn")
            return
    

    if action_choice == 1 and hero_card:
        print("plz choose a card into attack zone(1 to %i):"%(len(hero_card)))
        for i, card in enumerate(hero_card):
            print(f"{i + 1}. {card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")

        try:
            choice = int(input())
            if choice > 0 and choice <= len(hero_card):
                hero_attack_card.append(hero_card[choice - 1])
                print(f"You chose {hero_card[choice - 1]['Name']} to enter the attack zone.")
                del hero_card[choice - 1]
                
            else:
                print("empty number, skip your turn")
        except ValueError:
            print("invalid, skip your turn")
    else:
        print("you have no card!")

    if action_choice == 2 :
        print("choose card to attack")

        print("computer")
        for i, card in enumerate(computer_attack_card):
            print(f"{i + 1}. {card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")

        print("hero")
        for i, card in enumerate(hero_attack_card):
            print(f"{i + 1}. {card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")

        try:
            choice = int(input("enter attack card number:"))
            if choice > 0 and choice <= len(hero_attack_card):
                attack_card = hero_attack_card[choice - 1]
                print("choose a target number")
                target_choice = int(input())
                if target_choice > 0 and target_choice <= len(computer_attack_card):
                    def_card = computer_attack_card[target_choice - 1]
                    attack(attack_card, def_card)
                else:
                    print("empty target,skip round")
            else:
                print("you dont have this card, skip round")
        except ValueError:
            print("invalid, skip round")
    else:
        pass


def update_game():
    
    #回合数
    global c_round 
    c_round += 1    
    show_zone()
    print("round %i"%(c_round))

    if first_hero == 'hero':
        time.sleep(0.2)
        print("hero part")
        hero_choose()
        show_zone()
        time.sleep(3)
        print("computer part")
        computer_logic()
        show_zone
        time.sleep(3)
    else:
        time.sleep(0.2)
        print("computer part")
        computer_logic()
        show_zone()
        time.sleep(3)
        print("hero part")
        hero_choose()
        show_zone()
        time.sleep(3)
    
    if  not hero_card and  not hero_attack_card:
        print("Game over! Computer wins!")
        return
    elif not computer_card and not computer_attack_card:
        print("Game over! Hero wins!")
        return
    
#    draw_war()


    
def start():
    global first_hero
    time.sleep(0.5)
    print("game start,now choose the first action")
    time.sleep(1)
    while True:
        #先后顺序
        hero_number = random.randint(0,10)
        computer_number = random.randint(0,10)
        time.sleep(0.5)
        print("the hero number is %i"%(hero_number))
        time.sleep(0.5)
        print("the computer number is %i"%(computer_number))
        
        if hero_number > computer_number :
            first_hero = True
            time.sleep(0.5)
            print("first action is hero")
            break
        elif hero_number < computer_number:
            first_hero = False
            time.sleep(0.5)
            print("first action is computer")
            break
        else :
            time.sleep(0.5)
            print("same number, retry!")
            continue
        

#tkinter draw
#def draw_war():
#    canvas.delete("all")
#
#    for i in range(len(computer_card)):
#        draw_card((i, 0), computer_card[i], "lightblue")
#    
#    for i in range(len(hero_card)):
#        draw_card((i, 4), hero_card[i], "lightgreen")
#    
#    for i in range(len(computer_attack_card)):
#        draw_card((i, 2), computer_attack_card[i], "red")
#    
#    for i in range(len(hero_attack_card)):
#        draw_card((i, 3), hero_attack_card[i], "green")

#def draw_card(pos, card, color):
#    x, y = pos
#    x_pos = x * (cell_size + spacing)
#    y_pos = y * (cell_size + spacing)
#    canvas.create_rectangle(x_pos, y_pos, x_pos + cell_size, y_pos + cell_size, fill=color)
#    canvas.create_text(x_pos + cell_size // 2, y_pos + 20, text=card['Name'], font=('Arial', 12, 'bold'))
#    canvas.create_text(x_pos + cell_size // 2, y_pos + 40, text=f"HP: {card['Health']}", font=('Arial', 10))
#    canvas.create_text(x_pos + cell_size // 2, y_pos + 60, text=f"ATK: {card['Attack']}", font=('Arial', 10))
#    canvas.create_text(x_pos + cell_size // 2, y_pos + 80, text=f"DEF: {card['Defense']}", font=('Arial', 10))



#root = tk.Tk()
#canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
#canvas.pack()
#canvas.bind("<Button-1>", on_card_click)

start()
set_card()
#draw_war()
while True:
    update_game()

#root.mainloop()