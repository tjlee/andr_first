def select_case(file_name, n=10):
    import os.path, random
        
    new_file_name = os.path.splitext(file_name)[0] + '_res.txt'
    s = []

    #Считаем количество строк в исходном файле
    count = 0
    for line in open(file_name).readlines(  ): count += 1

    print('Working...')        
        
    ch = random.sample(range(count), n) #Выбираем n рандомных номеров строк,
                                        #Позже добавлю контроль ошибки, когда выбираем больше строк чем в файле 

    with open(new_file_name, 'w') as g:
        with open(file_name) as f:
            for i,line in enumerate(f):
                if i in ch:             #Проверяем если номер строки попадает в "карту рандома ch"
                    g.write(line)       #Добавляю в файл выборки, иначе кидаю в s для последующей перезаписи исходного файла
                else:
                    s.append(line)

    with open(file_name, 'w') as f:      #Перезаписываю исходный файл
        f.writelines(s)

    return print('Complete! Look selection in:\n', os.path.abspath(new_file_name))
