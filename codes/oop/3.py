# -*- coding: utf-8 -*-

class Character(object):

    # 인스턴스 변수: name, health, damage, inventory
    # 생성자 함수의 키워드(keyword) 인자: speed
    
    def __init__(self, name, health, damage, inventory, speed=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory
        self.speed = speed
        
    def fly(self, speed = 0):
        if self.speed == 0:
            print("저는 날지 못합니다")
        elif speed == 0:
            print("시속 %dkm로 날아가는 중입니다" % self.speed)
        else:
            print("시속 %dkm로 날아가는 중입니다" % speed)
        
    def nameCall(self):
        print("저는 %s입니다." % self.name)

    def introduction(self):
        print("제 이름은 %s입니다" % self.name)
        print("현재 저의 체력은 %s입니다." % self.health)
        print("저는 공격할 때마다 상대방에게 %s만큼의 손상을 줍니다." % self.damage)
        print("제 수트의 방어력은 %d이며 사용하는 무기는 %s입니다." % \
              (self.inventory['suit'], self.inventory['weapon']))

ironman = Character("아이언맨", 100, 200, {'suit': 500, 'weapon': '레이저'}, 1000)
captainAmerica = Character("캡틴아메리카", 200, 100, {'suit': 300, 'weapon': '방패'})







'''
hero_name = '아이언맨'
hero_health = 100
hero_damage = 200
hero_inventory = {'suit': 500, 'weapon': '레이저'}

print("제 이름은 %s입니다" % hero_name)
print("현재 저의 체력은 %s입니다." % hero_health)
print("저는 공격할 때마다 상대방에게 %s만큼의 손상을 줍니다." % hero_damage)
print("제 수트의 방어력은 %d이며 사용하는 무기는 %s입니다." % \
      (hero_inventory[0]['suit'], hero_inventory[1]['weapon']))

print("제 이름은 %s입니다" % hero_1_name)
print("현재 저의 체력은 %s입니다." % hero_1_health)
print("저는 공격할 때마다 상대방에게 %s만큼의 손상을 줍니다." % hero_1_damage)
print("제 수트의 방어력은 %d이며 사용하는 무기는 %s입니다." % \
      (hero_1_inventory[0]['suit'], hero_1_inventory[1]['weapon']))
'''
