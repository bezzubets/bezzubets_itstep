# Задание 1
# Создайте класс Device, который содержит информа-
# цию об устройстве.
# С помощью механизма наследования, реализуйте класс
# CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы.

# class Devices:
#     print('Devices for kitchen.')
#     def __init__(self):
#         self.voltage='Voltage is 220 V'
#         self.elsocket='European electrical socket'
#         self.warranty='Product warranty 12 months'
#     def set_voltage(self,voltage):
#          self.voltage=voltage
#     def set_elsocket(self,elsocket):
#          self.elsocket=elsocket
#     def set_warranty(self,warranty):
#          self.warranty=warranty
#     def get_voltage(self):
#         return self.voltage
#     def get_elsocket(self):
#         return self.elsocket
#     def get_warranty(self):
#         return self.warranty
#     def show_cof(self):
#         print(self.voltage)
#         print(self.elsocket)
#         print(self.warranty)
# print(' ')
# class CoffeeMachine(Devices):
#     def __init__(self):
#         self.cof_machine='Coffee Machine'
#         self.cof_mach_name=''
#         self.country_fab=''
#         self.color=''
#         self.weight=0
#         self.milk=''
#         self.auto_power_off=''
#         self.eldisplay=''
#     #Sets
#     def set_cof_mach_name(self,cof_mach_name):
#         self.cof_mach_name=cof_mach_name
#     def set_country_fab(self,country_fab):
#         self.country_fab=country_fab
#     def set_color(self,color):
#         self.color=color
#     def set_weight(self,weight):
#         self.weight=weight
#     def set_milk(self,milk):
#         self.milk=milk
#     def set_auto_power_off(self, auto_power_off):
#         self.auto_power_off=auto_power_off
#     def set_eldisplay(self,eldisplay):
#         self.eldisplay=eldisplay
#     #Gets
#     def get_cof_mach_name(self):
#         return self.cof_mach_name
#     def get_country_fab(self):
#         return self.country_fab
#     def get_color(self):
#         return self.color
#     def get_weight(self):
#         return self.weight
#     def get_milk(self):
#         return self.milk
#     def get_auto_power_off(self):
#         return self.auto_power_off
#     def get_eldisplay(self):
#         return self.eldisplay
#     def show_coff(self):
#         print(self.cof_machine)
#         print('Company ',self.cof_mach_name)
#         print('Country ',self.country_fab)
#         print('Color ',self.color)
#         print('Weight ',self.weight,'kg')
#         print('Milk accessories ',self.milk)
#         print('Auto power off ',self.auto_power_off)
#         print('LCD display is ',self.eldisplay)
# coffeeMachine1=CoffeeMachine()
# coffeeMachine1.set_cof_mach_name(cof_mach_name='Bosh')
# coffeeMachine1.set_country_fab(country_fab='Germany')
# coffeeMachine1.set_color(color='Black')
# coffeeMachine1.set_weight(weight=5)
# coffeeMachine1.set_milk(milk='Glass for the milk')
# coffeeMachine1.set_auto_power_off(auto_power_off='is include')
# coffeeMachine1.set_eldisplay(eldisplay='is include')
# coffeeMachine1.show_coff()
# device=Devices()
# device.show_cof()
# print(' ')
# class Blender(Devices):
#     def __init__(self):
#         self.blender='Blender'
#         self.bl_mach_name=''
#         self.country_fab=''
#         self.color=''
#         self.weight=0
#         self.speed=''
#         self.hand_or_table=''
#         self.bigKnives=''
#     #Sets
#     def set_bl_mach_name(self,bl_mach_name):
#         self.bl_mach_name=bl_mach_name
#     def set_country_fab(self,country_fab):
#         self.country_fab=country_fab
#     def set_color(self,color):
#         self.color=color
#     def set_weight(self,weight):
#         self.weight=weight
#     def set_speed(self,speed):
#         self.speed=speed
#     def set_hand_or_table(self, hand_or_table):
#         self.hand_or_table=hand_or_table
#     def set_bigKnives(self,bigKnives):
#         self.bigKnives=bigKnives
#     #Gets
#     def get_bl_mach_name(self):
#         return self.bl_mach_name
#     def get_country_fab(self):
#         return self.country_fab
#     def get_color(self):
#         return self.color
#     def get_weight(self):
#         return self.weight
#     def get_speed(self):
#         return self.speed
#     def get_hand_or_table(self):
#         return self.hand_or_table
#     def get_bigKnives(self):
#         return self.bigKnives
#     def show_bl(self):
#         print(self.blender)
#         print('Company ',self.bl_mach_name)
#         print('Country ',self.country_fab)
#         print('Color ',self.color)
#         print('Weight ',self.weight,'kg')
#         print('Knives speed ',self.speed)
#         print('For table or manual ',self.hand_or_table)
#         print('Big knives ',self.bigKnives)
# blender1=Blender()
# blender1.set_bl_mach_name(bl_mach_name='Moulinex')
# blender1.set_country_fab(country_fab='Sweden')
# blender1.set_color(color='White')
# blender1.set_weight(weight=2)
# blender1.set_speed(speed='500')
# blender1.set_hand_or_table(hand_or_table='for table.')
# blender1.set_bigKnives(bigKnives='is include')
# blender1.get_country_fab()
# blender1.show_bl()
# device=Devices()
# device.show_cof()
# print('Страна-изготовитель ',blender1.country_fab)
# print(' ')
# class MeatGrinder(Devices):
#     def __init__(self):
#         self.grinder='Meat grinder.'
#         self.mg_name=''
#         self.country_fab=''
#         self.color=''
#         self.weight=0
#         self.speed=''
#         self.hand_or_table=''
#         self.acc_for_juice=''
#     #Sets
#     def set_mg_name(self,mg_name):
#         self.mg_name=mg_name
#     def set_country_fab(self,country_fab):
#         self.country_fab=country_fab
#     def set_color(self,color):
#         self.color=color
#     def set_weight(self,weight):
#         self.weight=weight
#     def set_speed(self,speed):
#         self.speed=speed
#     def set_hand_or_table(self, hand_or_table):
#         self.hand_or_table=hand_or_table
#     def set_acc_for_juice(self,acc_for_juice):
#         self.acc_for_juice=acc_for_juice
#     #Gets
#     def get_mg_name(self):
#         return self.mg_name
#     def get_country_fab(self):
#         return self.country_fab
#     def get_color(self):
#         return self.color
#     def get_weight(self):
#         return self.weight
#     def get_speed(self):
#         return self.speed
#     def get_hand_or_table(self):
#         return self.hand_or_table
#     def get_acc_for_juice(self):
#         return self.acc_for_juice
#     def show_mg(self):
#         print(self.grinder)
#         print('Company ',self.mg_name)
#         print('Country ',self.country_fab)
#         print('Color ',self.color)
#         print('Weight ',self.weight,'kg')
#         print('Knives speed ',self.speed)
#         print('For table or manual ',self.hand_or_table)
#         print('Accessories for juice ',self.acc_for_juice)
# grinder1=MeatGrinder()
# grinder1.set_mg_name(mg_name='Philips')
# grinder1.set_country_fab(country_fab='Netherlands')
# grinder1.set_color(color='White')
# grinder1.set_weight(weight=4)
# grinder1.set_speed(speed='800')
# grinder1.set_hand_or_table(hand_or_table='Manual')
# grinder1.set_acc_for_juice(acc_for_juice='is include.')
# grinder1.get_country_fab()
# grinder1.show_mg()
# device=Devices()
# device.show_cof()
# print('')
# print('Компания-изготовитель ',grinder1.mg_name)

# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.

# class ship:
#     print('Ships')
#     def __init__(self):
#         self.country='Made in Ukraine.'
#         self.year='Year of product 2021'
#         self.prod='Produced in Nikolaev shipbuilding factory'
#     def get_country(self):
#         return self.country
#     def get_year(self):
#         return self.year
#     def get_prod(self):
#         return self.prod
#     def show_all(self):
#         print(self.country)
#         print(self.year)
#         print(self.prod)
# print('')
# class destroyer(ship):
#     def __init__(self):
#         self.name_des=''
#         self.dispacement=0
#         self.weapons=''
#         #Sets
#     def s_name_des(self,name_des):
#         self.name_des=name_des
#     def s_disp(self,displacement):
#         self.dispacement=displacement
#     def s_weapons(self,weapons):
#         self.weapons=weapons
#         #Gets
#     def get_name_des(self):
#         return self.name_des
#     def get_dis(self):
#         return self.dispacement
#     def get_weapons(self):
#         return self.weapons
#     def des_show(self):
#         print(self.name_des)
#         print('Displacement -',self.dispacement,'tn.')
#         print('Weapons on board ',self.weapons)
# name1=destroyer()
# name1.s_name_des(name_des="Destroyer 'Kharkiv'")
# name1.s_disp(displacement=1500)
# name1.s_weapons(weapons= 'are include.')
# name1.des_show()
# ships=ship()
# ships.show_all()
# print(' ')
# class frigate(ship):
#     def __init__(self):
#         self.name_fr = ''
#         self.dispacement = 0
#         self.weapons = ''
#         # Sets
#     def s_name_fr(self, name_fr):
#         self.name_fr = name_fr
#     def s_disp(self, displacement):
#         self.dispacement = displacement
#     def s_weapons(self, weapons):
#         self.weapons = weapons
#         # Gets
#     def get_name_fr(self):
#         return self.name_fr
#     def get_disf(self):
#         return self.dispacement
#     def get_weapons(self):
#         return self.weapons
#     def def_show(self):
#         print(self.name_fr)
#         print('Displacement -', self.dispacement, 'tn.')
#         print('Weapons on board ', self.weapons)
# namefr1 = frigate()
# namefr1.s_name_fr(name_fr="Frigate 'Dnipro'")
# namefr1.s_disp(displacement=3000)
# namefr1.s_weapons(weapons='are include.')
# namefr1.def_show()
# ships = ship()
# ships.show_all()
# print(' ')
# class cruiser(ship):
#     def __init__(self):
#         self.name_cr = ''
#         self.dispacement = 0
#         self.weapons = ''
#         # Sets
#     def s_name_cr(self, name_cr):
#         self.name_cr = name_cr
#     def s_disp(self, displacement):
#         self.dispacement = displacement
#     def s_weapons(self, weapons):
#         self.weapons = weapons
#         # Gets
#     def get_name_cr(self):
#         return self.name_cr
#     def get_disp(self):
#         return self.dispacement
#     def get_weapons(self):
#         return self.weapons
#     def dec_show(self):
#         print(self.name_cr)
#         print('Displacement -', self.dispacement, 'tn.')
#         print('Weapons on board ', self.weapons)
# namecr1 = cruiser()
# namecr1.s_name_cr(name_cr="Cruiser 'Lviv'")
# namecr1.s_disp(displacement=4000)
# namecr1.s_weapons(weapons='are include.')
# namecr1.dec_show()
# ships = ship()
# ships.show_all()
# print('')
# name1.get_dis()
# namefr1.get_disf()
# namecr1.get_disp()
# print('Destroyer`s displacement is',name1.dispacement,'tn.')
# print('Frigate`s displacement is',namefr1.dispacement,'tn.')
# print('Cruiser`s displacement is',namecr1.dispacement,'tn.')

# Задание 3
# Запрограммируйте класс Money (объект класса опе-
# рирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хра-
# нения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, за-
# дания значений для частей.

# class money:
#     print('Ваши деньги.')
#     def __init__(self):
#         self.hryvna=1000
#         self.kopiyka=100
#     def set_hryvna(self,hryvna):
#         self.hryvna=hryvna
#     def set_kopiyka(self,kopiyka):
#         self.kopiyka=kopiyka
#     def get_hryvna(self):
#         return self.hryvna
#     def get_kopiyka(self):
#         return self.kopiyka
#     def show_hryvna(self):
#         print('В гривне, у вас есть',self.hryvna, 'грн.')
#         print('и',self.kopiyka,'копеек.')
# print('')
# class dollar(money):
#     def __init__(self):
#         self.dollar=0
#         self.cent=0
#         #Sets
#     def s_dollar(self,dollar):
#         self.dollar=dollar
#     def s_cent(self,cent):
#         self.cent=cent
#     def get_dollar(self):
#         return self.dollar
#     def get_cent(self):
#         return self.cent
#     def doll_show(self):
#         print('В долларах, у вас есть',self.dollar,'долларов,')
#         print('и',self.cent,'цнт.')
# d1=dollar()
# d1.s_dollar(dollar=100)
# d1.s_cent(cent=50)
# d1.doll_show()
# moneys=money()
# moneys.show_hryvna()
# class euro(money):
#     def __init__(self):
#         self.euro =0
#         self.eurocent = 0
#         # Sets
#     def s_euro(self, euro):
#         self.euro= euro
#     def s_eurocent(self, eurocent):
#         self.eurocent = eurocent
#         # Gets
#     def get_euro(self):
#         return self.euro
#     def get_eurocent(self):
#         return self.eurocent
#     def euro_show(self):
#         print('В евро у вас есть',self.euro)
#         print('и',self.eurocent,'евроцентов.')
# euro1 = euro()
# euro1.s_euro(euro=200)
# euro1.s_eurocent(eurocent=50)
# euro1.euro_show()
# print(' ')
# moneys.get_hryvna()
# d1.get_dollar()
# euro1.get_euro()
# print('Итого, у вас есть',moneys.hryvna,'гривен,',d1.dollar,'долларов',euro1.euro,'евро.')
# moneys.get_kopiyka()
# d1.get_cent()
# euro1.get_eurocent()
# print('А также, у вас есть',moneys.kopiyka,'копеек,',d1.cent,'центов',euro1.eurocent,'евроцентов.')
