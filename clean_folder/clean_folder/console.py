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


def inputy():
    PATH = sys.argv[1]  # Считування місцезнаходження папки з командної строки. Прописано вище в константах.
    return PATH


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

def search_res(val_key, list_res):  # Функція формує список проаналізованих розширень для виводу в звіт до конкретної категорії файлів.
    str_name = os.path.split(val_key)
    dir_name = str_name[0]
    str_name = os.path.split(str_name[0])
    if str_name[1] == 'archives':
        str_name = list_res[0]
    elif str_name[1] == 'audio':
        str_name = list_res[1]
    elif str_name[1] == 'documents':
        str_name = list_res[2]
    elif str_name[1] == 'images':
        str_name = list_res[3]
    elif str_name[1] == 'video':
        str_name = list_res[4]
    elif str_name[1] == 'others':
        str_name = list_res[5]
    return str_name, dir_name


def write_file(sort_path, list_dic, list_res):    # Функція зберігає звіт до файлу SORTED\ZVIT.TXT. В процесі підготовки інформації до зберігання звертається
                                        # до функції search_res(), яка виконує пошук різманітних розширень опрацьованих програмою.
    print_str = ''
    wroot1 = ''
    wroot2 = ''
    all_num = 0
    with open(sort_path, 'w') as fa:
        for dicts in list_dic:
            num = 0
            fa.write(('-' * 187) + '\n')
            for dict_key, val_key in dicts.items():
                num += 1
                all_num += 1
                print_str = ('|{:>3}|{:<90}|{:<90}|\n'.format(num, val_key, dict_key))
                fa.write(print_str)
            fa.write(('-' * 187) + '\n')
            if num != 0:
                str_name, dir_name = search_res(val_key, list_res)
                wroot1 = f'| Загалом ідентифіковано {num} файл(а/ів) в теці {dir_name}. Знайдено файли з наступними розширеннями: {str_name}'
                fa.write('{:{fill}{align}{width}}'.format(wroot1, fill = ' ', align = '<', width = 186) + '|\n')
                # fa.write('| Загалом ідентифіковано {} файл(а/ів) в теці {}. Знайдено файли з наступними розширеннями: {}\n'.format(str(num), dir_name, str_name))
        fa.write(('-' * 187) + '\n')
        wroot2 = f'| Загалом відсортовано {all_num} файл(а/ів)'
        fa.write('{:{fill}{align}{width}}'.format(wroot2, fill = ' ', align = '<', width = 186) + '|\n')
        fa.write(('-' * 187) + '\n')
        wroot2 = f'| Дата формування звіту: {datetime.datetime.now().date()}' 
        fa.write('{:{fill}{align}{width}}'.format(wroot2, fill = ' ', align = '<', width = 186) + '|\n')
        fa.write(('-' * 187) + '\n')

if __name__ == "__main__":
    pass