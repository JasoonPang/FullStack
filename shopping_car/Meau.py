# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 22:26
# @Author  : JasoonPang
# @Email   : 724719274@qq.com
""""
本例中，最精髓的是利用parent_layers这个列表来控制返回上一层
"""
meau = {
    '1':{
        '1.1':{
            '1.11':{},
            '1.12':{},
            '1.13':{},
        },
        '1.2':{
            '1.11': {},
            '1.12': {},
            '1.13': {},
        },
        '1.3':{
            '1.11': {},
            '1.12': {},
            '1.13': {},
        }
    },
    '2':{
        '2.1':{
            '2.11':{},
            '2.12':{},
            '2.13':{},
        },
        '2.2':{
            '2.11': {},
            '2.12': {},
            '2.13': {},
        },
        '2.3':{
            '2.11': {},
            '2.12': {},
            '2.13': {},
        },
    },
    '3':{
        '3.1':{
            '3.11':{},
            '3.12':{},
            '3.13':{},
        },
        '3.2':{
            '3.11': {},
            '3.12': {},
            '3.13': {},
        },
        '3.3':{
            '3.11': {},
            '3.12': {},
            '3.13': {},
        },
    },
}

print('welcome to here!')
current_meau = meau  # 当前层current_meau初始化为meau
parent_layers = []
while True:
    for key in current_meau:
        print(key,'>')
    current_layer = input('please input you want to go[exit:q]: ')
    if current_layer in current_meau:
        parent_layers.append(current_meau)
        current_meau = current_meau[current_layer]
    elif current_layer == 'b':
        if parent_layers:
            current_meau = parent_layers.pop()
    elif current_layer == 'q':
        print('OK,well done')
        exit()
    elif current_layer == 'y':
        for _ in parent_layers:
            print(_)
    else:
        print("it's has no one")
