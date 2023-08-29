import os
import shutil


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

def sorting(cur_path, sort_path, list_dic, list_res): # Функція сортування файлів за розширенням. Перебирає об'єкти в поточній теці, якщо об'єкт 
                                                      # є текою, - входить до рекурсивної перевірки. якщо об'єкт є файлом, копіює його у теку,
                                                      # що відповідає типу розширення.
    new_path = ''
    ind = 0
    for file_obj in os.listdir(cur_path):
        if os.path.isdir(os.path.join(cur_path, file_obj)) == True:          
            sorting(os.path.join(cur_path, file_obj), sort_path, list_dic, list_res)          
        elif os.path.isfile(os.path.join(cur_path, file_obj)) == True:
            filen, res = normalize(file_obj)
            if res.lower() == 'zip' or res.lower() == 'gz' or res.lower() == 'targ':
                sort_arch(cur_path, file_obj, sort_path, filen, list_dic[0])
                res = ' ' + res + ' '
                if list_res[0].find(res) == -1:
                    list_res[0] += res
            elif res.lower() == 'mp3' or res.lower() == 'ogg' or res.lower() == 'wav' or res.lower() == 'amr':
                sort_aud(cur_path, file_obj, sort_path, filen, list_dic[1])
                res = ' ' + res + ' '
                if list_res[1].find(res) == -1:
                    list_res[1] += res          
            elif res.lower() == 'doc' or res.lower() == 'docx' or res.lower() == 'txt' or res.lower() == 'pdf' or res.lower() == 'xls'\
                                                                                 or res.lower() == 'xlsx' or res.lower() == 'pptx':
                sort_doc(cur_path, file_obj, sort_path, filen, list_dic[2])
                res = ' ' + res + ' '
                if list_res[2].find(res) == -1:
                    list_res[2] += res
            elif res.lower() == 'jpeg' or res.lower() == 'png' or res.lower() == 'jpg' or res.lower() == 'svg':
                sort_imag(cur_path, file_obj, sort_path, filen, list_dic[3])
                res = ' ' + res + ' '
                if list_res[3].find(res) == -1:
                    list_res[3] += res
            elif res.lower() == 'avi' or res.lower() == 'mp4' or res.lower() == 'mov' or res.lower() == 'mkv':
                sort_vid(cur_path, file_obj, sort_path, filen, list_dic[5])
                res = ' ' + res + ' '
                if list_res[4].find(res) == -1:
                    list_res[4] += res 
            else:
                sort_oth(cur_path, file_obj, sort_path, filen, list_dic[4]) 
                res = ' ' + res + ' '
                if list_res[5].find(res) == -1:
                    list_res[5] += res


def sort_arch(cur_path, file_obj, sort_path, filen, dic_arch):  # Функція копіює та розпаковує архів в теку з ім'ям файлу в нове місце розташування.
    print(f'Знайдено новий файл: {file_obj}. Транслітеруємо в: {filen}. Копіюємо...')    
    shutil.copy2(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'archives', filen))
    new_path = unpack_arch(filen, os.path.join(sort_path, 'archives'))
    dic_arch.update([(os.path.join(cur_path, file_obj), new_path)])


def sort_aud(cur_path, file_obj, sort_path, filen, dic_aud): # Функція копіює файл в відповідне нове місце розташування.
    print(f'Знайдено новий файл: {file_obj}. Транслітеруємо в: {filen}. Копіюємо...')    
    shutil.copy2(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'audio', filen))
    dic_aud.update([(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'audio', filen))])
    

def sort_doc(cur_path, file_obj, sort_path, filen, dic_doc):  # Функція копіює файл в відповідне нове місце розташування.
    print(f'Знайдено новий файл: {file_obj}. Транслітеруємо в: {filen}. Копіюємо...')    
    shutil.copy2(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'documents', filen))
    dic_doc.update([(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'documents', filen))])
    

def sort_imag(cur_path, file_obj, sort_path, filen, dic_imag): # Функція копіює файл в відповідне нове місце розташування.
    print(f'Знайдено новий файл: {file_obj}. Транслітеруємо в: {filen}. Копіюємо...')    
    shutil.copy2(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'images', filen))
    dic_imag.update([(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'images', filen))])


def sort_vid(cur_path, file_obj, sort_path, filen, dic_vid): # Функція копіює файл в відповідне нове місце розташування.
    print(f'Знайдено новий файл: {file_obj}. Транслітеруємо в: {filen}. Копіюємо...')    
    shutil.copy2(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'video', filen))
    dic_vid.update([(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'video', filen))])
    

def sort_oth(cur_path, file_obj, sort_path, filen, dic_oth): # Функція копіює файл в відповідне нове місце розташування.
    print(f'Знайдено новий файл: {file_obj}. Транслітеруємо в: {filen}. Копіюємо...')    
    shutil.copy2(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'others', filen))
    dic_oth.update([(os.path.join(cur_path, file_obj), os.path.join(sort_path, 'others', filen))])
    
def unpack_arch(cur_file, cur_path):    # Функція розпаковки архіву, створює теку відповідно імені архиву, після розпаковки до неї, видаляє архів.
                                        # Якщо знаходить вже розпакований архів, видаляє його, та розпаковує наново.
    tmp = ()
    filen, res = normalize(cur_file)
    tmp = os.path.splitext(filen)
    if os.path.exists(os.path.join(cur_path, tmp[0])) == True:
        shutil.rmtree(os.path.join(cur_path, tmp[0]))
        os.mkdir(os.path.join(cur_path, tmp[0]))
    shutil.unpack_archive(os.path.join(cur_path, cur_file), os.path.join(cur_path, tmp[0]))
    os.remove(os.path.join(cur_path, cur_file))
    return os.path.join(cur_path, tmp[0])

if __name__ == "__main__":
    pass