'''
Задание 5. Консольный файловый менеджер
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.

'''
import os
import shutil

import my_function as my_f

def list_items(f):
    rez_list=[]
    if f == 'dir':
        print(f'ПАПКИ в рабочей директории {os.getcwd()}:')
        rez_list = list(filter(os.path.isdir, os.listdir()))
    elif f == 'files':
        print(f'ФАЙЛЫ в рабочей директории {os.getcwd()}:')
        rez_list = list(filter(os.path.isfile, os.listdir()))
    else:
        print(f'содержимое рабочей директории {os.getcwd()}:')
        rez_list = os.listdir()

    for i in rez_list:
        print(i)

while True:
    print('\nМЕНЮ:')
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':       # создать папку
        dir_name = input('Введите название новой папки: ')
        if os.path.exists(dir_name):
            print(f'Название {dir_name} уже существует')
        elif my_f.check_dir_name(dir_name):
            print(f'Папку с именем {dir_name} создать нельзя')
        else:
            print('mkdir', dir_name)
            os.mkdir(dir_name)
    elif choice == '2':     # удалить пвпку
        name = input('Введите название папки или папки: ')
        if os.path.isdir(name):
            shutil.rmtree(name)
        elif os.path.isfile(name):
            os.remove(name)
        else:
            print(f'Нет файла или папки с именем {name}')
    elif choice == '3':
        name_old = input('Введите название папки или файла, который надо скопировать: ')
        if not os.path.exists(name_old):
            print(f'Копирование невозможно, так как {name_old} не существует')
        else:
            name_new = input('Введите новое название: ')
            if my_f.check_dir_name(name_new):
                print(f'Копирование невозможно, так как {name_new} создать нельзя')
            elif os.path.exists(name_new):
                print(f'Копирование невозможно, так как {name_new} существует')
            else:
                if os.path.isfile(name_old):
                    shutil.copy(name_old, name_new)
                else:
                    shutil.copytree(name_old, name_new)
    elif choice == '4':
        list_items('all')
    elif choice == '5':
        list_items('dir')
    elif choice == '6':
        list_items('files')
    elif choice == '7':

        for root, dirs, files in os.walk(os.getcwd()):
            print(root, dirs, files)

        # for address, dirs, files in os.walk(os.getcwd()):
        #     for name in files:
        #         print(os.path.join(address, name))

    elif choice == '8':
        ll = os.walk(os.getcwd())
        print ([i for i in ll])

    elif choice == '9':
                pass
    elif choice == '10':
        pass
    elif choice == '11':
        pass
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню ')
