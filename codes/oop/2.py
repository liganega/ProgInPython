# -*- coding: utf-8 -*-

##class Character(object):
##    name
##    health
##    damage
##    inventory

hero_name = '아이언맨'
hero_health = 100
hero_damage = 200
hero_inventory = [
    {'suit': 500},
    {'weapon': '레이저'}
]

print("제 이름은 %s입니다" % hero_name)
print("현재 저의 체력은 %s입니다." % hero_health)
print("저는 공격할 때마다 상대방에게 %s만큼의 손상을 줍니다." % hero_damage)
print("제 수트의 방어력은 %d이며 사용하는 무기는 %s입니다." % \
      (hero_inventory[0]['suit'], hero_inventory[1]['weapon']))

print("=====")

hero_1_name = '캡틴아메리카'
hero_1_health = 200
hero_1_damage = 100
hero_1_inventory = [
    {'suit': 300},
    {'weapon': '방패'}
]

print("제 이름은 %s입니다" % hero_1_name)
print("현재 저의 체력은 %s입니다." % hero_1_health)
print("저는 공격할 때마다 상대방에게 %s만큼의 손상을 줍니다." % hero_1_damage)
print("제 수트의 방어력은 %d이며 사용하는 무기는 %s입니다." % \
      (hero_1_inventory[0]['suit'], hero_1_inventory[1]['weapon']))
