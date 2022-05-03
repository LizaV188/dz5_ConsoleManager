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

while True:
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
            os.rmdir(name)
        elif os.path.isfile(name):
            os.remove(name)
        else:
            print(f'Нет файла или папки с именем {name}')
    elif choice == '3':
        dir_old = input('Введите название папки или файла, который надо скопировать: ')
        dir_new = input('Введите новое название: ')
        shutil.copy(dir_old,dir_new)
#        shutil.copytree(dir_old, dir_new)
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        pass
    elif choice == '8':
        pass
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
