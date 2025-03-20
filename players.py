import math


class Player:
    def __init__(self,name,level,experience,add_exp):
        self.name = name
        self.level = level
        self.experience = experience
        self.add_exp = add_exp
        

    def gain_experience(self):
        self.add_exp += self.experience

    def show_stars(self):
        print ('Имя игрока ', self.name)
        print ('Уровень игрока ', self.level)
        print ('Изначальный опыт игрока ', self.experience)
        print ('Опыт игрока с учётом его уровня', self.add_exp)

    def __del__(self):
        print(' That all')


class Warrior(Player):
    def __init__(self,name,level,experience,weapon,armor):
        self.weapon = weapon
        self.armor = armor
        super().__init__(name,level,experience)

    def attack(self):
        attack = level/2 * self.weapon

    def defend(self):
        defend = ln(self.experience)* self.armor

    def __del__(self):
        print('all')


input_data = (input(' Введите имя игрока, его уровень, количество имеющегося опыта  и количество нового опыта '))
data = input_data.split()
name = str(data[0])
level = int(data[1])
experience = int(data[2])
add_exp = int(data[3])

done = Player(name,level,experience,add_exp)
done.show_stars()


