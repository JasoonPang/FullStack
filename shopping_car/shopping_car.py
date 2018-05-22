# -*- coding: utf-8 -*-
"""
Created on Tue May 22 09:51:30 2018

@author: 724719274@qq.com
"""

product_list = [
        ('Mac', 9000),
        ('bike', 800),
        ('book', 80),
        ('coffee', 30),
        ('glass', 15)
        ]

# 显示余额
while True:
    saving = input('Please enter your money: ')
    if saving.isdigit():
        saving = float(saving)
        print('Your saving money is {}'.format(saving))
        break
    else:
        print('Please enter an integer!')
        
# 展示物品列表
print('This is product_list, please choose as you like.')
for i, v in enumerate(product_list, 1):
    print(i,'>>>>', v )

# 选择物品
def Choice():
    choice = input('Please enter your choice: ')
    if choice.isdigit():
        choice = int(choice)    
        if choice > 0 and choice <= len(product_list):
            pass
    else:
        print('Please enter the right number of list!')
    return choice

# 确认选择
def make_Choice():
    global saving, FLAG
    choice = Choice()
    print('You choose is {} {}'.format(choice, product_list[choice - 1]))
    flag = input('Are you sure? y/n[exit:q]: ')  
    if flag == 'y':
        if saving >= product_list[choice - 1][1]:
            saving -= product_list[choice - 1][1]
            shopping_car.append(product_list[choice - 1])
            print('You choose list is {}'.format(shopping_car))
            print('Now, your saving is {}'.format(saving))
        else:
            print("----You don't have enough money----")
            print('Now, your saving is {}'.format(saving))
    elif flag == 'n':
        pass
    else:
        print('Welcome back next time!')        
        FLAG = False
    return FLAG

# 选择并成交       
shopping_car = []
FLAG = True
make_choice = make_Choice()
while FLAG:  
    Flag = input('Maybe you want to choose another one? y/n: ')
    if Flag == 'y':
        make_choice = make_Choice()
    else:
        FLAG = False
        print('Welcome back next time!')

    
   






