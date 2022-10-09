# class Main:
#     def __init__(self, white_list, names):
#         self.white_list = white_list
#         self.names = names
#         white_obj_list = [Main(name=names) for names in white_list]


# class func(Main):
#     def func_1(self):
#         white_list = ['Lisa', 'David', 'Michael', 'Timur']
#         names = ['George', 'Lisa', 'Miron', 'Yasha', 'David', 'Aganim_Shard']
#         for el in white_list:
#             if white_obj_list == names:
#                 print('Success')



white_list = ['Lisa', 'David', 'Michael', 'Timur']
names = ['George', 'Lisa', 'Miron', 'Yasha', 'David', 'Aganim_Shard']

for name in names:
    print(name)
    if name in white_list:
        print(f'Вы прошли в систему.{name}')