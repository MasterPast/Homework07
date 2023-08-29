import os
import shutil
import sys
import datetime

def error_1(path_del): #    Функція помилки 1. Визивається коли програма знаходить результати попередньої роботи. Пропонує запит 
                        #   користувачу на вихід із програми, або продовження ії виконання.
    ans = ''
    print('Увага! Знайдено існуючи робочі теки програми! При продовжені роботи програми дані будуть перезаписані!')
    ans = input('Продовжувати? (Так/Ні)>>>')
    if ans.lower() == 'н' or ans.lower() == 'ні' or ans.lower() == 'n':
        print('Завершення роботи програми...')
        sys.exit()
    elif ans.lower() == 'т' or ans.lower == 'так' or ans.lower() == 'y':
        shutil.rmtree(path_del)
    else:
        print('Повторіть ввод, будь ласка...')
        error_1()

def last_chance(PATH, root_path): # Функція інформує користувача про закінчення роботи програми, та пропонує вибір подальших дій.
    ans = ''
    date = datetime.datetime.now()
    res = date + datetime.timedelta(days=14)
    print('Робота програми завершена успішно. :) Сформовано теку SORTED поряд із Вашою текою, в якій класифіковані всі файли.')
    print('Детальний звіт в теці SORTED файлі ZVIT.TXT Попередня нформація ще доступна, тож будь ласка, оберіть, що з нею зробити?')
    print('     1. Видалити старі файли.')
    print(f'     2. Перейменувати стару теку {PATH} в ВИДАЛИТИ_ПІСЛЯ_{res.date()}.')
    while ans != '1' or ans != '2':    
        ans = input('?>>>')
        if ans == '1':
            shutil.rmtree(PATH)
            print(f'Видалення теки {PATH} успішно завершено.')
        elif ans == '2':
            root_path = os.path.join(root_path, 'ВИДАЛИТИ-ПІСЛЯ-' + str(res.date()))
            shutil.move(PATH, root_path)
            print(f'Стара тека успішно перейменовано в {root_path}.')
            print('Не забудьте видалити теку після указаного сроку!')
            print('Завершення роботи програми.')
            sys.exit()
        else:
            print('Повторіть ввод, будь ласка...')


def make_dirs(PATH): #  Функція створює відповідні теки в теці, розташованій на ступінь вище переданого шляху. 
                     #  При наявності вже створеної будь якої з них, викликає функцію error_1.
    path_sorted = PATH
    os.chdir(path_sorted)
    os.chdir('..')
    path_sorted = os.getcwd()
    root_path = path_sorted
    if os.path.exists(os.path.join(path_sorted, 'sorted')) == True:
        error_1(os.path.join(path_sorted, 'sorted'))
    path_sorted = os.path.join(path_sorted, 'sorted')
    os.mkdir(path_sorted)
    os.mkdir(os.path.join(path_sorted, 'archives'))
    os.mkdir(os.path.join(path_sorted, 'audio'))
    os.mkdir(os.path.join(path_sorted, 'documents'))
    os.mkdir(os.path.join(path_sorted, 'images'))
    os.mkdir(os.path.join(path_sorted, 'others'))
    os.mkdir(os.path.join(path_sorted, 'video'))
    return path_sorted, root_path
