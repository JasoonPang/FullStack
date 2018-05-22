# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:39:41 2018

@author: 724719274@qq.com
"""

# 教学例子

product_list = [
        ('Mac', 9000),
        ('bike', 800),
        ('book', 80),
        ('coffee', 30),
        ('glass', 15)
        ]
saving = input('请输入你的金额： 元')
shopping_car = []
if saving.isdigit():
    saving = float(saving)
    while True:
        # 打印商品内容
        for i, v in enumerate(product_list, 1):
            print(i,'>>>>', v)
        # 引导用户选择商品
        choice = input('选择购买的商品[退出: q]: ')
        # 验证输入是否合法
        if choice.isdigit():
            choice = int(choice)
            
            if choice > 0 and choice <= len(product_list):
                p_item = product_list[choice - 1]
                if p_item[1] > saving:
                    print('你的余额不足，现有金额为{}元'.format(saving))
                else:
                    saving -= p_item[1]
                    shopping_car.append(p_item)
                print('你选择的商品是：{}'.format(p_item))
            else:
                print('请输入正确的商品编号')
        elif choice == 'q':
            print('----你已购买如下商品----')
            for i in shopping_car:
                print(i)
            print('你所剩余额是{}元'.format(saving))
            break
        else:
            print('请输入合法的编号')
else:
    print('请输入合法的金额')