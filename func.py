import os
from PyPDF2 import PdfReader
import tkinter.filedialog
import tkinter.messagebox


def base(directory, mode, type_f):
    if type_f == 0:
        if os.path.isdir(directory):
            files = sorted([directory+'/'+f for f in os.listdir(directory) if os.path.isfile(directory+'/'+f)
                            and f.endswith('.pdf')])
            alph = '0123456789'
            ex = ''
            check_flag = 0
            if len(files) != 0:
                for k in range(len(files)):
                    pdf_doc = files[k]
                    names = []
                    check_name = []
                    extra_check_name = []
                    with open(pdf_doc, 'rb') as file:
                        pdf_file = PdfReader(file)
                        pages = (pdf_file.pages[0], pdf_file.pages[1], pdf_file.pages[2])
                        data = pages[0].extract_text()
                        check = pages[1].extract_text()
                        extra_check = pages[2].extract_text()
                        for j in range(len(check) - 11):
                            if check[j] == check[j + 3] and check[j] == check[j + 11] and check[j] == ':':
                                count = 0
                                for num in range(j + 12, j + 20):
                                    if check[num] in alph:
                                        count += 1
                                    else:
                                        break
                                if mode == 0:
                                    check_name.append('{}_{}_{}_{}'.format(check[j - 2:j], check[j + 1: j + 3],
                                                                           check[j + 4:j + 11],
                                                                           check[j + 12:j + 12 + count]))
                                elif mode == 1:
                                    check_name.append('{},{},{},{}'.format(check[j - 2:j], check[j + 1: j + 3],
                                                                           check[j + 4:j + 11],
                                                                           check[j + 12:j + 12 + count]))
                                elif mode == 2:
                                    check_name.append('{};{};{};{}'.format(check[j - 2:j], check[j + 1: j + 3],
                                                                           check[j + 4:j + 11],
                                                                           check[j + 12:j + 12 + count]))
                        for i in range(len(data) - 11):
                            if data[i] == data[i + 3] and data[i] == data[i + 11] and data[i] == ':':
                                count = 0
                                for num in range(i + 12, i + 20):
                                    if data[num] in alph:
                                        count += 1
                                    else:
                                        break
                                    if mode == 0:
                                        if '{}_{}_{}_{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                data[i + 4:i + 11], data[i + 12:i + 12 + count]) in\
                                                check_name:
                                            names.append('{}_{}_{}_{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                              data[i + 4:i + 11],
                                                                              data[i + 12:i + 12 + count]))
                                    elif mode == 1:
                                        if '{},{},{},{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                data[i + 4:i + 11], data[i + 12:i + 12 + count]) in\
                                                check_name:
                                            names.append('{},{},{},{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                              data[i + 4:i + 11],
                                                                              data[i + 12:i + 12 + count]))
                                    elif mode == 2:
                                        if '{};{};{};{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                data[i + 4:i + 11], data[i + 12:i + 12 + count]) in\
                                                check_name:
                                            names.append('{};{};{};{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                              data[i + 4:i + 11],
                                                                              data[i + 12:i + 12 + count]))

                    if len(names) == 1:
                        try:
                            os.rename(pdf_doc, directory+'/'+'{}.pdf'.format(names[0]))
                            check_flag += 1
                        except FileExistsError:
                            os.remove(files[k])
                            check_flag += 1

                    elif 2 <= len(names) <= 5:
                        for m in range(len(extra_check) - 11):
                            if extra_check[m] == extra_check[m + 3]\
                                    and extra_check[m] == extra_check[m + 11] and extra_check[m] == ':':
                                count = 0
                                for num in range(m + 12, m + 20):
                                    if extra_check[num] in alph:
                                        count += 1
                                    else:
                                        break
                                if mode == 0:
                                    extra_check_name.append('{}_{}_{}_{}'.format(extra_check[m - 2:m],
                                                            extra_check[m + 1: m + 3],
                                                            extra_check[m + 4:m + 11],
                                                            extra_check[m + 12:m + 12 + count]))
                                elif mode == 1:
                                    extra_check_name.append('{},{},{},{}'.format(extra_check[m - 2:m],
                                                            extra_check[m + 1: m + 3],
                                                            extra_check[m + 4:m + 11],
                                                            extra_check[m + 12:m + 12 + count]))
                                elif mode == 2:
                                    extra_check_name.append('{};{};{};{}'.format(extra_check[m - 2:m],
                                                            extra_check[m + 1: m + 3],
                                                            extra_check[m + 4:m + 11],
                                                            extra_check[m + 12:m + 12 + count]))
                        for item in names:
                            if item != extra_check_name[0]:
                                names.remove(item)
                        try:
                            os.rename(pdf_doc, directory + '/' + '{}.pdf'.format(names[0]))
                            check_flag += 1
                        except FileExistsError:
                            os.remove(files[k])
                            check_flag += 1

                    else:
                        ex += f'{pdf_doc.replace(directory + "/", "")}, '

                if len(ex.split(' ')) == 2:
                    tkinter.messagebox.showinfo(title='Информация', message=f'В файле {ex[:-2]}'
                                                f' не найдено кадастровых номеров')
                elif len(ex.split(' ')) > 2:
                    tkinter.messagebox.showinfo(title='Информация', message=f'В файлах {ex[:-2]}'
                                                f' не найдено кадастровых номеров')
                if check_flag != 0:
                    tkinter.messagebox.showinfo(title='Оповешение', message='Готово',
                                                detail='Результат находится в указанной папке')
                else:
                    tkinter.messagebox.showinfo(title='Оповешение', message='Повторите процедуру',
                                                detail='В выбранной папке нет подходящих файлов')

            else:
                tkinter.messagebox.showerror(title='Ошибка', message='В выбраной папке нет файлов указанного формата')
        else:
            tkinter.messagebox.showerror(title='Ошибка', message='Вы не указали путь')

    elif type_f == 1:
        if os.path.isdir(directory):
            files_xml = sorted([directory + '/' + f for f in os.listdir(directory)
                                if os.path.isfile(directory + '/' + f)
                                and f.endswith('.xml')])
            ex_xml = ''
            check_flag_xml = 0
            if len(files_xml) != 0:
                for k in range(len(files_xml)):
                    names_xml = []
                    open_data = open(files_xml[k], encoding='UTF-8').read()
                    if '<cad_number>' in open_data:
                        data_xml = [x for x in open_data.replace('<object>', '[flag_r]').
                                    replace('</object>', '[flag_r]').split('[flag_r]')[1].
                                    replace('<cad_number>', '[flag]').
                                    replace('</cad_number>', '[flag]').split('[flag]')]
                    else:
                        data_xml = []

                    for item in data_xml:
                        if len(item) > 13:
                            if item[2] == item[5] == item[13] == ':':
                                first, second, third, fourth = item.split(':')
                                if mode == 0:
                                    names_xml.append('{}_{}_{}_{}'.format(first, second, third, fourth))
                                if mode == 1:
                                    names_xml.append('{},{},{},{}'.format(first, second, third, fourth))
                                if mode == 2:
                                    names_xml.append('{};{};{};{}'.format(first, second, third, fourth))

                    if len(names_xml) != 0:
                        try:
                            os.rename(files_xml[k], directory + '/' + '{}.xml'.format(names_xml[0]))
                            check_flag_xml += 1
                        except FileExistsError:
                            os.remove(files_xml[k])
                            check_flag_xml += 1
                    else:
                        ex_xml += f'{files_xml[k].replace(directory + "/", "")}, '

                if len(ex_xml.split(' ')) == 2:
                    tkinter.messagebox.showinfo(title='Информация', message=f'В файле {ex_xml[:-2]}'
                                                f' не найдено кадастровых номеров')
                elif len(ex_xml.split(' ')) > 2:
                    tkinter.messagebox.showinfo(title='Информация', message=f'В файлах {ex_xml[:-2]}'
                                                f' не найдено кадастровых номеров')

                if check_flag_xml != 0:
                    tkinter.messagebox.showinfo(title='Оповешение', message='Готово',
                                                detail='Результат находится в указанной папке')
                else:
                    tkinter.messagebox.showinfo(title='Оповешение', message='Повторите процедуру',
                                                detail='В выбранной папке нет подходящих файлов')

            else:
                tkinter.messagebox.showerror(title='Ошибка', message='В выбраной папке нет файлов указанного формата')
        else:
            tkinter.messagebox.showerror(title='Ошибка', message='Вы не указали путь')

    elif type_f == 2:
        if os.path.isdir(directory):
            files = sorted([directory + '/' + f for f in os.listdir(directory) if os.path.isfile(directory + '/' + f)
                            and (f.endswith('.pdf') or f.endswith('.xml'))])
            alph = '0123456789'
            ex = ''
            check_flag = 0
            if len(files) != 0:
                for k in range(len(files)):
                    names = []
                    check_name = []
                    extra_check_name = []
                    if '.pdf' in files[k]:
                        pdf_doc = files[k]
                        with open(pdf_doc, 'rb') as file:
                            pdf_file = PdfReader(file)
                            pages = (pdf_file.pages[0], pdf_file.pages[1], pdf_file.pages[2])
                            data = pages[0].extract_text()
                            check = pages[1].extract_text()
                            extra_check = pages[2].extract_text()
                            for j in range(len(check) - 11):
                                if check[j] == check[j + 3] and check[j] == check[j + 11] and check[j] == ':':
                                    count = 0
                                    for num in range(j + 12, j + 20):
                                        if check[num] in alph:
                                            count += 1
                                        else:
                                            break
                                    if mode == 0:
                                        check_name.append('{}_{}_{}_{}'.format(check[j - 2:j], check[j + 1: j + 3],
                                                                               check[j + 4:j + 11],
                                                                               check[j + 12:j + 12 + count]))
                                    elif mode == 1:
                                        check_name.append('{},{},{},{}'.format(check[j - 2:j], check[j + 1: j + 3],
                                                                               check[j + 4:j + 11],
                                                                               check[j + 12:j + 12 + count]))
                                    elif mode == 2:
                                        check_name.append('{};{};{};{}'.format(check[j - 2:j], check[j + 1: j + 3],
                                                                               check[j + 4:j + 11],
                                                                               check[j + 12:j + 12 + count]))
                            for i in range(len(data) - 11):
                                if data[i] == data[i + 3] and data[i] == data[i + 11] and data[i] == ':':
                                    count = 0
                                    for num in range(i + 12, i + 20):
                                        if data[num] in alph:
                                            count += 1
                                        else:
                                            break
                                        if mode == 0:
                                            if '{}_{}_{}_{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                    data[i + 4:i + 11], data[i + 12:i + 12 + count])\
                                                    in check_name:
                                                names.append('{}_{}_{}_{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                                  data[i + 4:i + 11],
                                                                                  data[i + 12:i + 12 + count]))
                                        elif mode == 1:
                                            if '{},{},{},{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                    data[i + 4:i + 11], data[i + 12:i + 12 + count])\
                                                    in check_name:
                                                names.append('{},{},{},{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                                  data[i + 4:i + 11],
                                                                                  data[i + 12:i + 12 + count]))
                                        elif mode == 2:
                                            if '{};{};{};{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                    data[i + 4:i + 11], data[i + 12:i + 12 + count])\
                                                    in check_name:
                                                names.append('{};{};{};{}'.format(data[i - 2:i], data[i + 1: i + 3],
                                                                                  data[i + 4:i + 11],
                                                                                  data[i + 12:i + 12 + count]))

                        if len(names) == 1:
                            try:
                                os.rename(pdf_doc, directory + '/' + '{}.pdf'.format(names[0]))
                                check_flag += 1
                            except FileExistsError:
                                os.remove(files[k])
                                check_flag += 1

                        elif 2 <= len(names) <= 5:
                            for m in range(len(extra_check) - 11):
                                if extra_check[m] == extra_check[m + 3] \
                                        and extra_check[m] == extra_check[m + 11] and extra_check[m] == ':':
                                    count = 0
                                    for num in range(m + 12, m + 20):
                                        if extra_check[num] in alph:
                                            count += 1
                                        else:
                                            break
                                    if mode == 0:
                                        extra_check_name.append('{}_{}_{}_{}'.format(extra_check[m - 2:m],
                                                                                     extra_check[m + 1: m + 3],
                                                                                     extra_check[m + 4:m + 11],
                                                                                     extra_check[
                                                                                     m + 12:m + 12 + count]))
                                    elif mode == 1:
                                        extra_check_name.append('{},{},{},{}'.format(extra_check[m - 2:m],
                                                                                     extra_check[m + 1: m + 3],
                                                                                     extra_check[m + 4:m + 11],
                                                                                     extra_check[
                                                                                     m + 12:m + 12 + count]))
                                    elif mode == 2:
                                        extra_check_name.append('{};{};{};{}'.format(extra_check[m - 2:m],
                                                                                     extra_check[m + 1: m + 3],
                                                                                     extra_check[m + 4:m + 11],
                                                                                     extra_check[
                                                                                     m + 12:m + 12 + count]))
                            for item in names:
                                if item != extra_check_name[0]:
                                    names.remove(item)
                            try:
                                os.rename(pdf_doc, directory + '/' + '{}.pdf'.format(names[0]))
                                check_flag += 1
                            except FileExistsError:
                                os.remove(files[k])
                                check_flag += 1

                        else:
                            ex += f'{pdf_doc.replace(directory + "/", "")}, '

                    elif '.xml' in files[k]:
                        open_data = open(files[k], encoding='UTF-8').read()
                        if '<cad_number>' in open_data:
                            data_xml = [x for x in open_data.replace('<object>', '[flag_r]').
                                        replace('</object>', '[flag_r]').split('[flag_r]')[1].
                                        replace('<cad_number>', '[flag]').
                                        replace('</cad_number>', '[flag]').split('[flag]')]
                        else:
                            data_xml = []

                        for item in data_xml:
                            if len(item) > 13:
                                if item[2] == item[5] == item[13] == ':':
                                    first, second, third, fourth = item.split(':')
                                    if mode == 0:
                                        names.append('{}_{}_{}_{}'.format(first, second, third, fourth))
                                    if mode == 1:
                                        names.append('{},{},{},{}'.format(first, second, third, fourth))
                                    if mode == 2:
                                        names.append('{};{};{};{}'.format(first, second, third, fourth))

                        if len(names) != 0:
                            try:
                                os.rename(files[k], directory + '/' + '{}.xml'.format(names[0]))
                                check_flag += 1
                            except FileExistsError:
                                os.remove(files[k])
                                check_flag += 1
                        else:
                            ex += f'{files[k].replace(directory + "/", "")}, '

                if len(ex.split(' ')) == 2:
                    tkinter.messagebox.showinfo(title='Информация', message=f'В файле {ex[:-2]}'
                                                f' не найдено кадастровых номеров')
                elif len(ex.split(' ')) > 2:
                    tkinter.messagebox.showinfo(title='Информация', message=f'В файлах {ex[:-2]}'
                                                f' не найдено кадастровых номеров')
                if check_flag != 0:
                    tkinter.messagebox.showinfo(title='Оповешение', message='Готово',
                                                detail='Результат находится в указанной папке')
                else:
                    tkinter.messagebox.showinfo(title='Оповешение', message='Повторите процедуру',
                                                detail='В выбранной папке нет подходящих файлов')

            else:
                tkinter.messagebox.showerror(title='Ошибка', message='В выбраной папке нет файлов указанного формата')
        else:
            tkinter.messagebox.showerror(title='Ошибка', message='Вы не указали путь')


def need_dir():
    file = tkinter.filedialog.askopenfilename()
    re_file = os.path.dirname(file)
    return re_file


if __name__ == '__main__':
    print(os.path.abspath('tes_prog.xlsx'))
    direct = input()
    mod = 1
    base(direct, 1, 0)
