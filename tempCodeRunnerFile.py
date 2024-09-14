import random
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

#TK ENTER
spacing = 10
cell_size = 120
canvas_width = deck_size * (cell_size + spacing) + spacing
canvas_height = 5 * (cell_size + spacing) + spacing

#touch
selected_card = None
selecting_for_battle = False


def set_card():
    global hero_card, computer_card
    hero_card = []
    computer_card = []
    for _ in range(deck_size):
        hero_card.append(random.choice(card_deck))
        computer_card.append(random.choice(card_deck))

def attack(attack_card,def_card):
    print(f"{attack_card['Name']} is attacking {def_card['Name']}")
    if attack_card['Attack'] > def_card['Defense']:
        remaining_attack = attack_card['Attack'] - def_card['Defense']
        def_card['Defense'] = 0
        def_card['Health'] -= remaining_attack
        #delete card from hero_attack_hard or computer_attack_card
        if def_card['Health'] <= 0:
            def_card['Health'] = 0
            print(f"{def_card['Name']} died")
        else:
            print(f"{def_card['Name']} is left with {def_card['Health']} health")
    else:
        def_card['Defense'] -= attack_card['Attack']
        print(f"{def_card['Name']}'s defense is reduced to {def_card['Defense']}")

# def card_choose(chosed_card, enterd_card, number):
    if 1 <= number <= len(chosed_card):
        enterd_card.append(chosed_card[number - 1])  
        del chosed_card[number - 1]
        draw_war()

def on_card_click(event):
    global selected_card, selecting_for_battle
    item_id = event.widget.find_closest(event.x, event.y)[0]  # 获取被点击的图形ID
    tags = event.widget.gettags(item_id)
    
    if not tags:
        return

    card_id = tags[0]
    
    if selecting_for_battle:
        # 如果当前选择模式是选择出战卡牌
        if card_id.startswith('hero_'):
            card_index = int(card_id.split('_')[1])
            if hero_card:
                selected_card = hero_card[card_index]
                hero_attack_card.append(selected_card)
                hero_card.remove(selected_card)
                print(f"choose card：{selected_card['Name']}")
                draw_war()  # 更新界面
                selecting_for_battle = False
    else:
        # 如果当前不是选择模式，则选择手牌
        if card_id.startswith('hero_'):
            card_index = int(card_id.split('_')[1])
            selected_card = hero_card[card_index]
            print(f"choose attack card：{selected_card['Name']}")
            # 这里可以设置为开始选择出战卡牌模式
            selecting_for_battle = True


def computer_logic():
    x = random.randint(0,3)
    if computer_attack_card == None :
        x = 0
    match x :
        case 0 :
            if computer_card:
                chosen_card = random.choice(computer_card)
                computer_attack_card.append(chosen_card)
                computer_card.remove(chosen_card)
            draw_war
            pass
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

def hero_choose():
    if hero_card:
        print("请选择一张手牌出战：")
        for i, card in enumerate(hero_card):
            print(f"{i + 1}. {card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")

        try:
            choice = int(input("输入卡牌编号选择出战（输入0跳过）："))
            if choice > 0 and choice <= len(hero_card):
                hero_attack_card.append(hero_card[choice - 1])
                del hero_card[choice - 1]
                print("你选择了出战卡牌。")
            else:
                print("你跳过了出战卡牌。")
        except ValueError:
            print("无效输入，跳过出战。")
    else:
        print("没有手牌可以出战！")

    # 如果英雄已经有出战卡牌，选择攻击
    if hero_attack_card and computer_attack_card:
        print("请选择一张出战卡牌进行攻击：")
        for i, card in enumerate(hero_attack_card):
            print(f"{i + 1}. {card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")

        try:
            choice = int(input("输入出战卡牌编号进行攻击（输入0跳过）："))
            if choice > 0 and choice <= len(hero_attack_card):
                attack_card = hero_attack_card[choice - 1]
                # 选择攻击目标
                print("请选择一个目标进行攻击：")
                for i, card in enumerate(computer_attack_card):
                    print(f"{i + 1}. {card['Name']} (HP: {card['Health']}, ATK: {card['Attack']}, DEF: {card['Defense']})")

                target_choice = int(input("输入敌方卡牌编号："))
                if target_choice > 0 and target_choice <= len(computer_attack_card):
                    def_card = computer_attack_card[target_choice - 1]
                    attack(attack_card, def_card)
                else:
                    print("无效选择，跳过攻击。")
            else:
                print("跳过攻击。")
        except ValueError:
            print("无效输入，跳过攻击。")
    else:
        print("没有出战卡牌可以攻击！")

def update_game(first_to_attack):
    global round 
    round += 1    
    print("round %i"%(round))

    if first_to_attack == 'hero':
        print("hero part")
        #hero choose and attack
        time.sleep(3)
        print("computer part")
        computer_logic()
        time.sleep(3)
    else:
        print("computer part")
        computer_logic()
        time.sleep(3)
        print("hero part")
        #hero_choice
        time.sleep(3)
    
    if hero_card == None and hero_attack_card == None:
        print("Game over! Computer wins!")
        return
    elif computer_card == None and computer_attack_card == None:
        print("Game over! Hero wins!")
        return
    
    draw_war()


    
def start():
    global first_hero
    while True:
        #先后顺序
        hero_number = random.randint(0,10)
        computer_number = random.randint(0,10)

        if hero_number > computer_number :
            first_hero = True
            print("first action is hero")
            break
        elif hero_number < computer_number:
            first_hero - False
            print("first action is computer")
            break
        else :
            continue
        

#tkinter draw
def draw_war():
    tk.canvas.delete("all")
    
    for i, card in enumerate(computer_card):
        draw_card((i, 0), card, "lightblue", f"computer_{i}")
    
    for i, card in enumerate(hero_card):
        draw_card((i, 4), card, "lightgreen", f"hero_{i}")
    
    for i, card in enumerate(computer_attack_card):
        draw_card((i, 2), card, "red", f"comp_attack_{i}")
    
    for i, card in enumerate(hero_attack_card):
        draw_card((i, 3), card, "green", f"hero_attack_{i}")

def draw_card(pos, card, color, tag):
    x, y = pos
    x_pos = x * (cell_size + spacing)
    y_pos = y * (cell_size + spacing)
    card_id = tk.canvas.create_rectangle(x_pos, y_pos, x_pos + cell_size, y_pos + cell_size, fill=color, tags=tag)
    tk.canvas.create_text(x_pos + cell_size // 2, y_pos + 20, text=card['Name'], font=('Arial', 12, 'bold'), tags=tag)
    tk.canvas.create_text(x_pos + cell_size // 2, y_pos + 40, text=f"HP: {card['Health']}", font=('Arial', 10), tags=tag)
    tk.canvas.create_text(x_pos + cell_size // 2, y_pos + 60, text=f"ATK: {card['Attack']}", font=('Arial', 10), tags=tag)
    tk.canvas.create_text(x_pos + cell_size // 2, y_pos + 80, text=f"DEF: {card['Defense']}", font=('Arial', 10), tags=tag)
    tk.canvas.tag_bind(tag, '<Button-1>', on_card_click)





root = tk.Tk()

tk.canvas.bind("<Button-1>", on_card_click)
tk.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
tk.canvas.pack()
draw_war()

root.mainloop()