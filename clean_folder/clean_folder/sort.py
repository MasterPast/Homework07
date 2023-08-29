#   Тут і надалі під текою МОТЛОХ розуміється тека, що вказана користувачем в якості аргументу при запуску програми.
#   Програма створює поряд із текою МОТЛОХ теку SORTED, куди поміщає всі файли, знайдені в МОТЛОХ, та її вкладеннях.
#   При переміщенні назви всіх файлів транслітеруються. Пробіли, а також спецсімволи заміняються на "_". Розширення залишаються без змін.
#   В теці SORTED всі файли знаходяться у відповідних теках згідно розширення, а саме:
#           zip, gz, targ                           розпаковані у відповідні теки архіви, будуть знаходитись у теці ARCHIVES
#           mp3, ogg, wav, amr                      будуть знаходитись у теці AUDIO
#           doc, docx, txt, pdf, xls, xlsx, pptx    будуть знаходитись у теці DOCUMENTS
#           jpeg, png, jpg, svg                     будуть знаходитись у теці IMAGES
#           avi, mp4, mov, mkv                      будуть знаходитись у теці VIDEO
#           всі інші розширення                     будуть знаходитись у теці OTHERS
#   В процесі роботи програми генерується файл звіту ZVIT.TXT в якому наглядно відображено які файли де знаходяться, та їх попереднє 
#   місторозташування. Також під кожною групою файлів відображається їх кількість. А загальна кількість опрацьованих файлів є в кінці звіту.
#   Якщо при виконанні програма знайде попередню папку SORTED, користувачу буде повідомлено про це, а також запитано, чи потрібно продовжувати 
#   виконання програми, чи ні. Якщо користувач погоджується продовжувати, тека SORTED видаляється, та створюється знов з подальшим сортуванням.
#   Якщо користувач відмовляється від продовження роботи, програма завершує своє виконання, не вносячи ніякіх змін.
#   По закінченю роботи програми користувачу буде запропоновано видалити інформацію в попередньому вигляді, або зберегти її на 14 днів.
#   Якщо користувач погоджується на збереження інформації, тека МОТЛОХ переіменовується в теку ВИДАЛИТИ-ПІСЛЯ- та вказується дата, після якої
#   можна сміливо видаляти теку.  

import os
import datetime
from console import error_1, make_dirs, last_chance
from sorting import sort_arch, sorting, sort_aud, sort_doc, sort_imag, sort_oth, sort_vid

PATH = 'c:\Pastore\Py\Temp\Мотлох' # Строка аргументу, використовувалась при розробці.
sort_path = ''
root_path = ''
dic_arch = {}
dic_aud = {}
dic_doc = {}
dic_imag = {}
dic_oth = {}
dic_vid = {}
list_res = ['', '', '', '', '', '']
list_dic = [dic_arch, dic_aud, dic_doc, dic_imag, dic_oth, dic_vid]




def normalize(file_name): # Функція транслітерації імені файлу із заміною всіх спецзнаків та пробілів на "_". Розширення не змінюється.
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    res = ''
    temp = ()
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION): # Злиття словників для в ітоговий для транслітерації
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()   
    temp = os.path.splitext(file_name)
    file_name = temp[0]
    res = temp[1]
    file_name = file_name.translate(TRANS) # Транслітерація
    if file_name.isalnum() == False:  # Перевірка на входження до строки будь-яких елементів окрім цифр та літер, та заміна таких символів на '_'
        for ind in file_name:
            if (ind.isalnum() or ind.isdigit()) == False:
                file_name = file_name.replace(ind, '_', 1) 
    file_name += res
    res = res[1::]
    return file_name, res


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


def write_file(sort_path, list_dic):    # Функція зберігає звіт до файлу SORTED\ZVIT.TXT. В процесі підготовки інформації до зберігання звертається
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

# PATH = sys.argv[1]  # Считування місцезнаходження папки з командної строки. Прописано вище в константах.
sort_path, root_path = make_dirs(PATH)
sorting(PATH, sort_path, list_dic, list_res)
write_file(sort_path + '/ZVIT.TXT', list_dic)
last_chance(PATH, root_path)
