from easygui import fileopenbox

# select the configuration files in GUI interface
path_files = fileopenbox("Select Files", "File Read and Sort", filetypes= "*.csv", multiple=True)
path_files.sort()
print(path_files)

# print("Input Table Name: ", end='')
# table_name = input()

for path_file in path_files:
    table_dict={}
    component_dict={}
    file1 = open(path_file, 'r')
    Lines = file1.readlines()

    temp_table = ''
    temp_component = ''
    for i in range(len(Lines)):
        try:
            if(Lines[i].split(' ')[0] == '#\tTable'):
                table_dict.update({Lines[i].split(' ')[-1].split('\n')[0]:{"start":i+2, "end":-1}})
                if temp_table != '':
                    table_dict[temp_table]['end'] = i - 1
                    temp_table = ''
                    # print('table name: ', temp_table, '\nstart:', table_dict[temp_table]['start'], '\nend:', table_dict[temp_table]['end'])
                    # input()
                if temp_component != '':
                    component_dict[temp_component]['end'] = i - 1
                    temp_component = ''
                temp_table = Lines[i].split(' ')[-1].split('\n')[0]

            if(Lines[i].split('=')[0] == 'COMPONENT'):
                component_dict.update({Lines[i].split('=')[-1].split('\n')[0]:{"start":i+1, "end":-1}})
                if temp_table != '':
                    table_dict[temp_table]['end'] = i - 1
                    temp_table = ''
                if temp_component != '':
                    component_dict[temp_component]['end'] = i - 1
                    temp_component = ''
                temp_component = Lines[i].split('=')[-1].split('\n')[0]

            if(i == len(Lines)):
                if temp_table != '':
                    table_dict[temp_table]['end'] = i
                    temp_table = ''
                if temp_component != '':
                    component_dict[temp_component]['end'] = i
                    temp_component = ''
        except IndexError:
            continue
        except Exception as err:
            print(err)
    

    # print(list1)

    # file1 = open(path_file.split('.')[-2] + '- after.txt', 'w')
    # file1.writelines(res)
    # file1.close()

    with open(path_file.split('.')[-2] + ' - after.txt', 'w') as output_file:
        for table_name in table_dict:
            res = {}
            for i in range(table_dict[table_name]['start'], table_dict[table_name]['end']):
                try:
                    # print(Lines[i].split('].')[0], '\n')
                    # print(Lines[i].split('].', 1)[1])
                    if(Lines[i].split('].')[0] not in res):
                        res.update({Lines[i].split('].')[0]:""})
                    if(Lines[i].split('].', 1)[1].split('=')[0] == 'SequenceNumber'):
                        continue
                    res[Lines[i].split('].')[0]] = res[Lines[i].split('].')[0]]+(Lines[i].split('].', 1)[1])
                    # print(res[Lines[i].split('].')[0]])
                except IndexError:
                    continue
                except Exception as err:
                    print(err)
            list1 = []
            for key in res:
                list1.append(res[key])
            list1 = sorted(list1)
            j = 1
            output_file.write('Table Name: ' + table_name + '\n')
            for element in list1:
                if(element == ''):
                    continue
                output_file.write('[' + str(j) + ']\n')
                j = j + 1
                output_file.write(element)
                output_file.write("\n")

        for component_name in component_dict:
            res = {}
            list1 = []
            for i in range(component_dict[component_name]['start'], component_dict[component_name]['end']):
                try:
                    list1.append(Lines[i].split(';',1)[-1])
                except IndexError:
                    list1.append(Lines[i])
            list1 = sorted(list1)

            output_file.write('Component Name: ' + component_name + '\n')
            for element in list1:
                if(element == ''):
                    continue
                output_file.write(element)
            output_file.write("\n")
    
    print(path_file.split('\\')[-1] + ' finished')