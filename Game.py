import os
import random 

#-----------------------------------------------------------------------

def pause():
    try:
        input("\n(Натисни Enter, щоб продовжити...)")
    except (EOFError, KeyboardInterrupt):
        pass

def clear_screen(): # ф-кція для очищення екрану(тобто щоб попередній текст зникав і кожен екран виглядав окремо)
    os.system("cls" if os.name == "nt" else "clear")

#-----------------------------------------------------------------------

def show_intro():
    clear_screen()
    print("=" *80)
    print("                🌴    Jumanji in Ukraine    🌴")
    print("="* 80)
    print()
    print("Друже мандрівнику!😄")
    print()
    print("Ти прокидаєшся серед гранітних брил, що сягають неба.")
    print("Це - Кам'яні Могили, одне з найзагадковіших місць України.")
    print("Колись тут було море, а тепер - кам'яний хаос, де час зупинився.")
    print()
    print("У твоїй руці стара мапа, а на ній написи:")
    print('"Збери сльози землі, що розкидані від сходу до заходу,')
    print(' і відроди силу, яку давно поховали".')
    print()
    print("Перед тобою 5 шляхів до артефактів.")
    print("Кожен крок може стати останнім, але без дії -")
    print("ти назавжди залишишся тут, між каменями.")
    print()
    print("=" * 80)
    print("ПРАВИЛА ГРИ:")
    print("=" * 80)
    print("- w - рух вгору")
    print("- s - рух вниз")
    print("- a - рух вліво")
    print("- d - рух вправо")
    print("- i - переглянути інвентар")
    print("- e - взаємодіяти з об'єктом (стоячи поруч)")
    print("=" * 80)
    input("\nНатисни Enter, щоб почати...")

def show_win(thing):
    clear_screen()
    print("\n" + "=" * 80)
    print("                        🏆 ПЕРЕМОГА! 🏆")
    print("=" * 80)
    print("Ти переміг цю гру!!!")
    print(f'{thing["name"]}...')
    print(f'Зібрано балів: {thing["score"]}/100 ⭐')
    print()
    print("Ти знайшов всі потрібні матеріали і.....")
    print()
    print("Ти чуєш голос землі:")
    print(f'"ДЯКУЮ, {thing["name"].upper()}!')
    print('ТИ ЗІБРАВ РОЗКИДАНІ СКАРБИ УКРАЇНИ.')
    print('ТЕПЕР ВОНА МАЄ СИЛУ ВІКІВ.')
    print('ТИ ВРЯТУВАВ ЇЇ ВІД ЗАБУТТЯ."')
    print()
    print("=" * 80)
    print("                        ГРА ПРОЙДЕНА!")
    print("=" * 80)
    print("Твоє ім'я назавжди залишиться в легендах. 🥰")
    print("=" * 80)

def show_extra_win(thing):
    clear_screen()
    print("\n" + "=" * 80)
    print("                        ⚡🌟 МАГІЧНА ПЕРЕМОГА 🌟⚡")
    print("=" * 80)
    print(f'{thing["name"]}...')
    print(f'Зібрано балів: {thing["score"]}/100 ⭐')
    print()
    print("Ти зробив неможливе!")
    print("Ти не просто зібрав усі бонуси - ти перевершив саму долю!")
    print()
    print("За легендою, лише обраний міг пройти цей шлях.")
    print("Але ти... ти зробив це з такою легкістю й мудрістю,")
    print("що самі духи природи схилили голови перед тобою.")
    print()
    print("=" * 80)
    print("Дякуємо, що пройшов цей шлях разом з нами!")
    print("Ти назавжди залишишся в наших серцях, ВЕЛИКИЙ МАГЕ!")
    print("=" * 80)

def show_lose(thing):
    clear_screen()
    print("\n" + "=" * 80)
    print("                        💀 ВИ ЗАГИНУЛИ 💀")
    print("=" * 80)
    print()
    print(f'{thing["name"]}...')
    print(f'Зібрано балів: {thing["score"]}/100 ⭐')
    print("=" * 80)
    print("                        ❌ ГРА ЗАВЕРШЕНА ❌")
    print("=" * 80)
    print("Ми так вірили в тебе.")
    print("Ти пройшов такий довгий шлях, бачив степи, гори, печери...")
    print("Але доля розпорядилася інакше.")
    print()
    print("Україна втратила ще одного героя сьогодні.")
    print("Твоя історія обірвалася на півдорозі.")
    print()
    print("Але знаєш що?")
    print("Кожна поразка - це лише початок нового шляху.")
    print("=" * 80)


# Кортежі ля гри біля озера Лемурійського
LAKE_STAT = [
    ("Лемурійське озеро розташоване в Херсонській області.", True),
    ("У Лемурійському озері живуть дельфіни.", False),
    ("Рожевий колір з'являється завдяки мікроводоростям.", True),
    ("Озеро повністю прісне.", False),
    ("Через високу солоність вода добре тримає людину на поверхні.", True),
    ("Узимку озеро завжди стає яскраво-фіолетовим.", False),
]


#-----------------------------------------------------------------------

# Кортежі для вибору предмету на початку
ITEM1 = ("🗺️ Карта парку", -5, "Вона тобі не потрібна.")
ITEM2 = ("🧭 Компас", -1, "Ти взяв поламаний компас.")
ITEM3 = ("💧 Пляшка з водою", 25, "Тепер ти не помреш від спраги.")
ITEM4 = ("🥪 Бутерброд", 9, "Тепер ти не помреш від голоду.")
ITEM5 = ("🔦 Ліхтарик", 5, "Може, допоможе в печері.")
ITEM6 = ("📷 Фотоапарат", 1, "Фото викладеш в Інстаграм.")
ITEM7 = ("🩹 Аптечка", 40, "Джекпот! Ти знайшов цінну знахідку!")
ALL_ITEMS = (ITEM1, ITEM2, ITEM3, ITEM4, ITEM5, ITEM6, ITEM7)


def chest_event(thing):
    clear_screen()
    
    print("=" * 80)
    print("🎒 Ти знайшов старий дерев'яний сундук!")
    print("Всередині лежить декілька речей, але з собою можна взяти лише ОДНУ.")
    print("=" * 80)
    
    print("1. " + ALL_ITEMS[0][0])  
    print("2. " + ALL_ITEMS[1][0])  
    print("3. " + ALL_ITEMS[2][0])  
    print("4. " + ALL_ITEMS[3][0])  
    print("5. " + ALL_ITEMS[4][0])  
    print("6. " + ALL_ITEMS[5][0])  
    print("7. " + ALL_ITEMS[6][0])  
    print("=" * 80)
    
    choice = 0
    while choice < 1 or choice > 7:
        answer = input("Обери предмет (1-7): ")
        try:
            choice = int(answer)
        except:
            choice = 0
        if choice < 1 or choice > 7:
            print("❌ Введи число від 1 до 7.")
    
    item_number = choice - 1
    item_name = ALL_ITEMS[item_number][0]
    item_points = ALL_ITEMS[item_number][1]
    item_message = ALL_ITEMS[item_number][2]
    
    thing["inventory"].append(item_name)
    thing["score"] = thing["score"] + item_points
    
    print("")
    print("Ти береш: " + item_name)
    print(item_message)
    
    if item_points > 0:
        print("Отримано +" +str(item_points)+ " балів!")
    elif item_points < 0:
        print("Втрачено " +str(item_points)+" балів!")
    else:
        print("Бали не змінились.")
    
    pause()

#-----------------------------------------------------------------------

WIDTH = 21
HEIGHT = 15

BORDER = "██"
TREE = "🌳"
BUSH = "🌿"
EMPTY = "  "

LOCATIONS = {
    0: {
        "name": "КАМ'ЯНІ МОГИЛИ",
        "emoji": " 🪨",
        "about": 
            "Найвища точка Приазовської височини (324 м).\n"
            "Унікальний гранітний масив, що залишився від давніх гір.\n"
            "Тут ростуть реліктові рослини, а вітер постійно змінює обриси каменів.\n"
            "У 2009 році ця територія стала ландшафтним заказником." ,
        "item": None,
        "npc": "",
    },
    1: {
        "name": "МАРМУРОВА ПЕЧЕРА",
        "emoji": " 🕯️",
        "about": 
            "Одна з найкрасивіших печер Європи, на Демерджі-яйла (Крим).\n"
            "Протяжність - понад 2 км, глибина - 60 м.\n"
            "Зали рожевого мармуру, сталактити та сталагміти.\n"
            "Температура в печері постійно тримається близько +9°C."
        ,
        "item": "Кристал життя",
        "npc": "Кажан на ім'я Гриць",
    },
    2: {
        "name": "СТАРА ФОРТЕЦЯ",
        "emoji": " 🏛️",
        "about": 
            "Одна з найкраще збережених середньовічних фортець України.\n"
            "Розташована на скелястому острові над каньйоном річки Смотрич,\n"
            "у місті Кам'янець-Подільський."
        ,
        "item": "Скарб везучості",
        "npc": "Тамтешній житель",
    },
    3: {
        "name": "ЛЕМУРІЙСЬКЕ ОЗЕРО",
        "emoji": "🌊",
        "about": 
            "Унікальне рожеве солоне озеро в Херсонській області.\n"
            "Незвичайний колір утворюється завдяки мікроводоростям.\n"
            "Дуже висока концентрація солі."
        ,
        "item": "Рожева сіль",
        "npc": "Лемура",
    },
    4: {
        "name": "СКОЛІВСЬКІ БЕСКИДИ",
        "emoji": " ⛰️",
        "about": 
            "Край гір, працьовитих бойків і природних див.\n"
            "Резерват природи біля Східниці, Славська, Тисовця,\n"
            "з найвищою горою 1268 метрів."
        ,
        "item": "Золотий мухомор",
        "npc": "Живчик",
    },
    5: {
        "name": "ТАЄМНИЙ ПОРТАЛ",
        "emoji": "🟢",
        "about": "Прихований шлях, про який мало хто знає...",
        "item": None,
        "npc": "",
    },
}

LOCATIONS_LIST = [
    {"row": 3, "col": 3, "id": 0},   # Кам'яні Могили
    {"row": 10, "col": 13, "id": 1},  # Мармурова печера
    {"row": 2, "col": 9, "id": 2},   # Стара фортеця
    {"row": 8, "col": 7, "id": 3},   # Лемурійське озеро
    {"row": 5, "col": 14, "id": 4},  # Сколівські Бескиди
    {"row": 12, "col": 18, "id": 5},  # Таємний портал
]

def build_map():
    grid = []
    for r in range(HEIGHT):
        row = []
        for c in range(WIDTH):
            if r == 0 or r == HEIGHT - 1 or c == 0 or c == WIDTH - 1:
                row.append(BORDER)
            else:
                row.append(EMPTY)
        grid.append(row)

    for i in range(25):
        r = random.randint(1, HEIGHT - 2)
        c = random.randint(1, WIDTH - 2)
        grid[r][c] = TREE

    for i in range(15):
        r = random.randint(1, HEIGHT - 2)
        c = random.randint(1, WIDTH - 2)
        grid[r][c] = BUSH

    for loc in LOCATIONS_LIST:
        row = loc["row"]
        col = loc["col"]
        loc_id = loc["id"]
        grid[row][col] = LOCATIONS[loc_id]["emoji"]

    return grid


def render_map(grid, player_row, player_col):

    rows = []
    for row in range(HEIGHT):

        line = ""
        for col in range(WIDTH):
            if row == player_row and col == player_col:
                line = line + "👤" 
            else:
                line = line + grid[row][col] 
        
        rows.append(line)
    return "\n".join(rows)



#-----------------------------------------------------------------------

def new_state(name):
    thing = {
        "name": name,
        "health": 100,
        "score": 0,
        "inventory": [],        
        "position": (3, 3),     
        "visited": set(),       
    }
    return thing




def show_screen(thing, grid):
    
    clear_screen()
    player_row = thing["position"][0]
    player_col = thing["position"][1]

    loc_id = None
    for loc in LOCATIONS_LIST:
        if loc["row"] == player_row and loc["col"] == player_col:
            loc_id = loc["id"]
            break
    
    print("=" * 80)
    print("               🌴  Jumanji in Ukraine  🌴")
    print("=" * 80)
    
    hp = thing["health"]
    if hp < 0:
        hp = 0
    print("👤 " + thing["name"] + " | " + str(hp) + "❤️ | ⭐ " + str(thing["score"]))
    print("-" * 80)
    

    if loc_id is not None:
        loc = LOCATIONS[loc_id]
        print("📍 " + loc["name"] + " " + loc["emoji"])
        if loc["npc"] == "":
            print("👥 NPC: відсутні")
        else:
            print("👥 NPC: " + loc["npc"])
    else:
        print("📍 Джунглі")
        print("👥 NPC: відсутні")
    
    if len(thing["inventory"]) == 0:
        print("📦 Предмети: Немає")
    else:
        print("📦 Предмети: " + ", ".join(thing["inventory"]))
    print("-" * 80)
    
    print("🗺️  КАРТА ДЖУНГЛІВ:")
    print(render_map(grid, player_row, player_col))
    print("-" * 80)
    
    if loc_id is not None:
        print("🏞️ Про місце:")
        print(LOCATIONS[loc_id]["about"])
        print("-" * 80)
    
    print("WASD - рух | E - взаємодія | I - інвентар | Q - вихід")
    print()
    print("🌴 Шукай 💖Серце Джунглів! Потрібно набрати рівно 100 балів.")

#-----------------------------------------------------------------------

def move_player(thing, grid, direction):
    
    row = thing["position"][0]
    col = thing["position"][1]
    
    if direction == "w":
        new_row = row - 1
        new_col = col
    elif direction == "s":
        new_row = row + 1
        new_col = col
    elif direction == "a":
        new_row = row
        new_col = col - 1
    elif direction == "d":
        new_row = row
        new_col = col + 1
    else:
        return  
    
    
    if grid[new_row][new_col] == BORDER:
        thing["health"] = thing["health"] - 100
        print("🚫 Тут стіна! -100 здоров'я.")
        pause()
        return
    

    thing["position"] = [new_row, new_col]
    
    

#-----------------------------------------------------------------------



def event_cave(thing):
    if 1 in thing["visited"]:
        print("\n🦇 Кажан Гриць мовчки дивиться на тебе. Тут уже нічого не лишилось.")
        return

    print("\n🦇 Кажан Гриць вилітає назустріч і шепоче загадку:")
    print("Чи є висота Роман-Кош вищою за 1500 метрів?")
    print("1 - Так")
    print("2 - Ні")
    
    choice = input("Твій вибір: ")
    
    if choice == "1":
        thing["score"] += 20
        thing["inventory"].append("Мармуровий кристал")
        print("✅ Правильно! +20 балів. Отримано: Мармуровий кристал")
    else:
        thing["health"] -= 100
        print("❌ Неправильно! Печера обвалилась. -100 здоров'я")

    thing["visited"].add(1)

def event_fortress(thing):

    print("\n🏛️ Тамтешній житель пропонує ризикнути на удачу...")
    roll = random.randint(0, 1)

    if roll == 1:
        thing["score"] -= 10
        thing["health"] -= 20
        print("💧 Не пощастило! -10 балів, -20 здоров'я.")

    else:
        thing["score"] += 20
        thing["health"] -= 15
        if LOCATIONS[2]["item"] not in thing["inventory"]:
            thing["inventory"].append(LOCATIONS[2]["item"])
        print(f'🍀 Пощастило! +20 балів, -15 здоров\'я. Отримано предмет: {LOCATIONS[2]["item"]}')




