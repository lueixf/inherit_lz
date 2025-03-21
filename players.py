# lueixf
# laba about players

import math
# parent's class
class Player:
    def __init__(self, name, level, experience, add_exp):
        self.name = name
        self.level = level
        self.experience = experience
        self.add_exp = add_exp

    # function gain experience
    def gain_experience(self):
        self.experience += self.add_exp

    # function output of all known data and change of level
    def show_stars(self):
        print('Имя игрока ', self.name)
        print('Уровень игрока ', self.level)
        print('Изначальный опыт игрока ', self.experience)
        print('Новый опыт игрока ', self.add_exp)
        
        self.experience += self.add_exp
        print('Текущий опыт ', self.experience)
    

    def __del__(self):
        print('That all')


class Warrior(Player):
    def __init__(self, name, level, experience, add_exp, weapon, armor):
        super().__init__(name, level, experience, add_exp)
        self.weapon = weapon
        self.armor = armor

    def attack(self):
        while self.level < len(levels) and self.experience >= levels[self.level]:
            self.level += 1
        print('Уровень повышен! Текущий уровень ' ,self.level)
        att = (self.level/2) * self.weapon 
        print('Уровень атаки игрока равен ', att)
        print(self.level)

    def defend(self):
        df = math.log(self.experience)*armor
        print(df)
    def __del__(self):
        print('Also thats all')


levels = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]
input_data = input('Введите имя игрока, его уровень, количество имеющегося опыта, количество нового опыта, уровень урона оружия и уровень защиты брони: ')
data = input_data.split()
name = str(data[0])
level = int(data[1])
experience = int(data[2])
add_exp = int(data[3])
weapon = int(data[4])
armor = int(data[5])


player = Player(name, level, experience, add_exp)
player.show_stars()
player = Warrior(name,level,experience,add_exp,weapon,armor)
player.attack()
player.defend()