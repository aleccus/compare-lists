#Написать скрипт для сравнения двух списков с указанием что добавилось в список, что ушло,
#  насколько позиций произошло смещение элемента в списке.
#  Порядок элементов важен.
#Список 1: A, B, C, D, E, F, G, H, I, J, K, L, M, N
#Список 2: B, C, D, A, F, E, Z, M, N, J, K, L

import pymorphy2
        
def inflect_nomn(number, say):
    morph = pymorphy2.MorphAnalyzer()
    word = morph.parse(say)[0]

    vs_nomn = word.inflect({'sing', 'nomn'})
    vs_gent = word.inflect({'sing', 'gent'})
    vs_datv = word.inflect({'sing', 'datv'})
    vs_accs = word.inflect({'sing', 'accs'})
    vs_ablt = word.inflect({'sing', 'ablt'})
    vs_voct = word.inflect({'sing', 'voct'})

    vp_nomn = word.inflect({'plur', 'nomn'})
    vp_gent = word.inflect({'plur', 'gent'})
    vp_datv = word.inflect({'plur', 'datv'})
    vp_accs = word.inflect({'plur', 'accs'})
    vp_ablt = word.inflect({'plur', 'ablt'})
    vp_voct = word.inflect({'plur', 'voct'})

    if number % 10 == 1:
        return vs_accs.word
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        return vp_accs.word
    else:
        return vp_gent.word

#print(vs_nomn.word, vs_gent.word, vs_datv.word, vs_accs.word, vs_ablt.word, vs_voct.word)
#print(vp_nomn.word, vp_gent.word, vp_datv.word, vp_accs.word, vp_ablt.word, vp_voct.word)


list_one = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
list_two = ['B','C','D','A','F','E','Z','M','N','J','K','L',]

for position_one, el_one in enumerate(list_one):
    if el_one in list_two:
        position_two = list_two.index(el_one)
        diff_position = position_two - position_one
        if diff_position > 0:
            print(f"Элемент {el_one} сместился вправо на {diff_position} {inflect_nomn(diff_position, 'позиция')}.")
        elif diff_position < 0:
            print(f"Элемент {el_one} сместился влево на {-diff_position} {inflect_nomn(-diff_position, 'позиция')}.")
        else:
            print(f"Элемент {el_one} остался на месте.")
    else:
        print(f"Элемент {el_one} удален.")
for position_two, el_two in enumerate(list_two):
    if el_two not in list_one:
        print(f"Элемент {el_two} добавлен на {position_two+1} позицию.")


