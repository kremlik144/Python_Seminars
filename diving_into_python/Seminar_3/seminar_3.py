# 1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# - Какие вещи взяли все три друга
# - Какие вещи уникальны, есть только у одного друга
# - Какие вещи есть у всех друзей кроме одного + имя того, у кого данная вещь отсутствует
# - Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

# from random import randint

# def variants_generator(thigs: list, freinds: list) -> dict:
#     result_dict = {}
#     index_men = 0

#     while len(result_dict) != len(freinds):
#         man_things = []
#         for i in range(3):
#             man_things.append(thigs[randint(0, len(thigs)-1)])
#         result_dict[freinds[index_men]] = tuple(man_things)
#         index_men += 1
    
#     for name in result_dict.keys():
#         result_dict[name] = set(result_dict[name])
    
#     return result_dict

# def result_1(freinds: dict) -> str:
#     case_1 = set()
#     flag_1 = True
#     for i in freinds.values():
#         if flag_1:
#             case_1 = i
#             flag_1 = False
#         elif len(case_1) <= 0:
#             case_1.clear()
#         else:
#             case_1 &= i 
#     if len(case_1):
#         return f'Вещь {case_1} - взяли все друзья'    
#     else:
#         return 'Нет общих вещей'
    
# def result_2(freinds: dict) -> str:
#     result = []
#     countc = 0
    
#     for name in freinds.keys():
#         freinds2 = freinds.copy()
#         kids = freinds.get(name)
#         res = 0
#         for i in freinds2.keys():
#             x = freinds2.get(i)
#             if i == name:
#                 continue
#             else:
#                 print(countc, x)
#                 countc += 1
#                 res = kids - x

#         if len(res) != 0:
#             result.append(str(f'Только у {name} есть {res}'))
#     print(result)
   


# list_things = ['палатка', 'удочка', 'котелок', 'лодка', 'мангал', 'гитара', 'пила', 'чайник', 'ложка', 'вилка']
# list_freinds = ['Славик', 'Алешка', 'Миша']

# dict_freinds = variants_generator(list_things, list_freinds)
# print(result_1(dict_freinds.copy())
# result_2(dict_freinds.copy())



# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

# from random import randint as ran

# initial_list = [ran(9,21) for i in range(15)]
# result_list = []

# for number in initial_list:
#     if initial_list.count(number) >= 2 and number not in result_list:
#         result_list.append(number)

# print(f'{initial_list = }\n{result_list =}')



# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки 
# препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

# word_list = []
# result_dict = {}
# sorted_dict = {}
# word_top_size = 10
# initial_line =  '''ООП методология программирования, основанная на представлении 
#                 программы в виде совокупности взаимодействующих объектов, каждый из которых является экземпляром определённого 
#                 класса, а классы образуют иерархию наследования.Идеологически, ООП  подход к программированию как к моделированию
#                 информационных объектов, решающий на новом уровне основную задачу структурного программирования, структурирование 
#                 информации с точки зрения управляемости, что существенно улучшает управляемость самим процессом моделирования, что,
#                 в свою очередь, особенно важно при реализации крупных проектов. Управляемость для иерархических систем предполагает 
#                 минимизацию избыточности данных и их целостность, поэтому созданное удобно управляемым  будет и удобно пониматься.
#                 Таким образом, через тактическую задачу управляемости решается стратегическая задача транслировать понимание задачи
#                 программистом в наиболее удобную для дальнейшего использования форму. Основные принципы структурирования в случае ООП
#                 связаны с различными аспектами базового понимания предметной задачи, которое требуется для оптимального управления 
#                 соответствующей моделью абстракция для выделения в моделируемом предмете важного для решения конкретной задачи по 
#                 предмету, в конечном счёте  контекстное понимание предмета, формализуемое в виде класса инкапсуляция для быстрой и 
#                 безопасной организации собственно иерархической управляемости, чтобы было достаточно простой команды, без одновременного
#                 уточнения как именно делать, так как это уже другой уровень управления, наследование для быстрой и безопасной организации
#                 родственных понятий: чтобы было достаточно на каждом иерархическом шаге учитывать только изменения, не дублируя всё остальное,
#                 учтённое на предыдущих шагах, полиморфизм для определения точки, в которой единое управление лучше распараллелить или наоборот
#                 собрать воедино.То есть фактически речь идёт о прогрессирующей организации информации согласно первичным семантическим 
#                 критериям. Прогрессирование, в частности, на последнем этапе даёт возможность перехода на следующий уровень детализации,
#                 что замыкает общий процесс. Обычный человеческий язык в целом отражает идеологию ООП, начиная с инкапсуляции представления 
#                 о предмете в виде его имени и заканчивая полиморфизмом использования слова в переносном смысле, что в итоге развивает 
#                 выражение представления через имя предмета до полноценного понятия класса.'''.lower().replace(',', '').replace('.', '')

# word_list = initial_line.split()

# for i in word_list:
#     if not i in result_dict.keys():
#         result_dict[i] = word_list.count(i)

# sorted_dict = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))

# for i, word in enumerate(sorted_dict.items(), 1):
#     if word_top_size == 0:
#         break
#     else:
#         print(f'{i :> 3}. {word[0]} - {word[1]}')
#         word_top_size -= 1



# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие 
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 

# from random import randint

# def variants_generator(thigs: list) -> dict:
#     result_dict = {}    
#     for thig in thigs:
#         result_dict[thig] = randint(1, 6)
#     return result_dict

# list_things = ['палатка', 'удочка', 'котелок', 'лодка', 'мангал', 'гитара', 'пила', 'чайник', 'ложка', 'вилка']

# items = variants_generator(list_things)

# max_weight = 10 
# current_weight = 0 
# backpack = {} 

# for item, weight in items.items():
#     if current_weight + weight <= max_weight:
#         backpack[item] = weight
#         current_weight += weight
        
# print(f'В рюкзак вместительностью {max_weight} кг вошли следующие вещи:')
# for item, weight in backpack.items():
#     print(f'- {item} - {weight} кг')
