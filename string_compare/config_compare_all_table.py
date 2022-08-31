import re
from easygui import fileopenbox

path_files = fileopenbox("Select Files", "File Read and Sort", filetypes= "*.csv", multiple=True)
path_files.sort()
print(path_files)

# print("Input Table Name: ", end='')
# table_name = input()

for path_file in path_files:
    res = {}
    table_dict={}
    file1 = open(path_file, 'r')
    Lines = file1.readlines()

    # for i in range(len(Lines)):
    #     Lines[i] = Lines[i].split('.')[-1]
    # Lines = sorted(Lines, key = lambda s: s.split(';')[1:])
    # for i in range(len(Lines)):
    #     Lines[i] = Lines[i].split(';')[1] + ":" + Lines[i].split(';')[2]
    # Lines.sort()

    temp = ''
    for i in range(len(Lines)):
        try:
            if(Lines[i].split(' ')[0] == '#\tTable'):
                table_dict.update({Lines[i].split(' ')[-1].split('\n')[0]:{"start":i+2, "end":-1}})
                if temp != '':
                    table_dict[temp]['end'] = i - 1
                    # print('table name: ', temp, '\nstart:', table_dict[temp]['start'], '\nend:', table_dict[temp]['end'])
                    # input()

                temp = Lines[i].split(' ')[-1].split('\n')[0]
            if(Lines[i].split('=')[0] == 'COMPONENT'):
                if temp != '':
                    table_dict[temp]['end'] = i - 1
                    temp = ''
            if(i == len(Lines)):
                if temp != '':
                    table_dict[temp]['end'] = i
                    temp = ''
        except IndexError:
            continue
        except Exception as err:
            print(err)
    

    # print(list1)

    # file1 = open(path_file.split('.')[-2] + '- after.txt', 'w')
    # file1.writelines(res)
    # file1.close()

    with open(path_file.split('.')[-2] + '- after.txt', 'w') as output_file:
        for table_name in table_dict:
            res = {}
            for i in range(table_dict[table_name]['start'], table_dict[table_name]['end']):
                try:
                    # print(Lines[i].split('].')[0], '\n')
                    # print(Lines[i].split('].', 1)[1])
                    if(Lines[i].split('].')[0] not in res):
                        res.update({Lines[i].split('].')[0]:""})
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
    
    print('finished')