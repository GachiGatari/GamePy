from  classes import Enemy,Seller,Player
import random
Seller = Seller()
Player = Player(100,10,2)


def increase_attack():
      global Player
      Player.attack += 5


def increase_armor():
      global Player
      Player.armor += 2


def add_potion():
      global Player
      Player.potion += 1

def get_loot():
      global Player
      gold_loot = random.randint(0,100)
      Player.money += gold_loot
      print(f"Обыскивая труп врага ты находишь {gold_loot} золота")
      if random.randint(0,100) > 66:
            add_attack = random.randint(1,4)
            Player.attack += add_attack
            print(f"Ого,да тебе повезло,помимо золота ты увеличиваешь свой урон на {add_attack}")

def fight(Enemy):
      global Player
      Enemy = Enemy(100,5,0)
      print("Перед вами стоит варвар\n"
            "У него в руках огромная дубина и он размахивает ей,очевидно зазывая вас на поединок\n"
            "Вы решаете испытать свои судьбу и попиздиться")
      print(f"У тебя {Player.health} здоровья.\n"
            f"У врага {Enemy.health} здоровья.")
      while True:
            print("Ваш ход,что будете делать? ")
            action = input()
            if not action.isdigit():
                  print("Даун,введи команду из списка...")
                  continue
            if int(action) == 1:
                  damage = round(Player.attack * random.uniform(0, 2)) - Enemy.armor
                  if damage < 0:
                        damage = 0
                  Enemy.health = Enemy.health - damage
                  print(f"Ты нанёс {damage} урона врагу, у него осталось {Enemy.health} жизней")
            elif int(action) == 2:
                  if Player.potion != 0:
                        Player.potion -= 1
                        Player.health += 15
                        print(f"Тёплый эликсир разливается по твоему телу, ты похилился на 15 очков, теперь у тебя "
                              f"{Player.health}  здоровья, а хилок {Player.potion}")
                  else:
                        print("Лох,ты проебал все хилки и не можешь похилится))))")
            if Enemy.health < 0:
                  print(f" Варвар получает смертельный удар, и спуская дух успеваете сказать: {Enemy.death_phrase}\n"
                        f"На этом его приключение заканчивается...\n"
                        f"\t\tПоздравялю, вы победили!!")
                  return True

            damage = round(Enemy.attack * random.uniform(0, 2)) - Enemy.armor
            if damage < 0:
                  damage = 0
            Player.health = Player.health - damage
            print(f"Враг нанёс тебе {damage} урона , у тебя осталось {Player.health} жизней")
            if Player.health < 0:
                  print(f"Вы получаете смертельный удар, и спуская дух успеваете сказать: {Player.death_phrase}\n"
                        f"На этом ваши приключение заканчиваются...")
                  return False


def break_down():
      global Player
      print(f"Фухх, передышка\n"
            f"Чтобы продолжить пиздится нажми 1\n"
            f"Чтобы похилиться нажми 2\n")
      while True:
            print(f"У тебя к слову {Player.potion} хилки и {Player.health} здоровья")
            try:
                  action = int(input())
            except:
                  print("Это не команда...")
                  continue
            if action == 1:
                  break
            else:
                  if Player.potion > 0:
                        Player.potion -= 1
                        Player.health += 20
                  else:
                        print("У тебя кончились хилки...")

def lavka():
      global Seller
      global Player

      alias = [increase_attack,increase_armor,add_potion]

      print("Вы,обливаясь потом после прошлых битв, заходите в одиноко стоящую лавку торговца...\n"
            "О,покупатель!\n"
            "Ну привет дорогой,как жизнь,как дела?\n"
            "Вот к слову что у меня есть в наличии:")
      print(f"Увеличение уроня за {Seller.catalog['products']['1']}\n"
            f"Увеличение брони за {Seller.catalog['products']['2']}\n"
            f"Зелья здоровья за {Seller.catalog['products']['3']}")
      print("Что жедаешь купить?(1-3, 4 - выход) ")
      while True:
            print(f"Твои статы:\n"
                  f"{Player.health} здоровья\n"
                  f"{Player.attack} атаки\n"
                  f"{Player.armor} брони\n"
                  f"{Player.potion} хилок\n"
                  f"{Player.money} денег\n")
            try:
                  action = int(input())
                  if action<1 or action>4:
                        print("Всё хуйня, давай по новой")
                        continue
            except:
                  print("Это не команда...")
                  continue

            if action == 4:
                  break
            else:
                  if Player.money - Seller.catalog['products'][str(action)] < 0:
                        print("У тебя недостаточно денег")
                  else:
                        Player.money -= Seller.catalog['products'][str(action)]
                        alias[action-1]()

      while True:
            print("Перед битвой не желаешь ли похилиться?(1-да, 2-нет)")
            try:
                  action = int(input())
                  if action!=1 and action!=2:
                        print("Всё хуйня, давай по новой")
                        continue
            except:
                  print("Это не команда...")
                  continue
            if action == 2:
                  break
            else:
                  if Player.potion != 0:
                        Player.potion -= 1
                        Player.health += 15
                        print(f"Тёплый эликсир разливается по твоему телу, ты похилился на 15 очков, теперь у тебя "
                              f"{Player.health}  здоровья, а хилок {Player.potion}")
                  else:
                        print("Лох,ты проебал все хилки и не можешь похилится))))")





print("Вы странствующий воитель.\n"
      "Вот уже много лет вы путешествуете по бескрайнему королевству и бьётесь насмерть с различными врагами...\n"
      "Сегодня ваше путешествие начинается с входа в дремучий лес\n"
      "Перед вами бесконечное кол-во врагов, а через каждые 2 врага есть лавка с полезными предметами\n"
      "Ну что? Погнали!")
while True:
      win = fight(Enemy)
      if not win:
            break
      get_loot()
      break_down()
      win = fight(Enemy)
      if not win:
            break
      get_loot()
      lavka()


