import argparse
import os
import sys
from os.path import isfile, join

class user_inf:
    choose = ""
    length = 0

    def __init__(self, Chos: str, Leng: int):
        self.choose = Chos
        self.length = Leng

def create_file(dir: str) -> None:
    print()
    file_name = str(input("Insert file name: "))
    if file_name == "":
        return
    f = open(dir + "/" + file_name, 'w')
    f.close()
    print("File " + file_name + " was created!")

def create_folder(dir: str) -> None:
    print()
    folder_name = str(input("Insert folder name: "))
    if folder_name == "":
        return
    os.mkdir(dir + "/" + folder_name)
    print("Folder " + folder_name + " was created!")

def create_project(dir: str) -> None:
    print()
    choose = int(input("1 - create Python project\n2 - create C++ Project\n3 - cancel\n\nChoose: "))
    print()

    if choose == 1:
        pyt_name_c = str(input("Insert Python project name: "))
        os.mkdir("/home/avairon/CodePython" + "/" + pyt_name_c)
        f = open(dir + "/" + pyt_name_c + "/" + "main.py", 'w')
        f.write("\n\nif __name__ == '__main__':\n    pass")
        print("Python project " + pyt_name_c + " was created!")

    if choose == 2:
        cpp_name_c = str(input("Insert C++ project name: "))
        os.mkdir("/home/avairon/CodeCPP" + "/" + cpp_name_c)
        f = open(dir + "/" + cpp_name_c + "/" + "main.cpp", 'w')
        f.write("#include <iostream>\n\nint main(){\n\n}")
        print("Python project " + cpp_name_c + " was created!")
    


def delete_file_folder(dir: str) -> None:
    print()
    choose = int(input("1 - delete file\n2 - delete folder\n3 - cancel action\n\nChoose: "))
    print()

    if choose == 1:
        file_name_d = str(input("Insert file name: "))
        try:
            os.remove(dir + "/" + file_name_d)
            print("file: " + file_name_d + " was deleated!")
        except:
            print("File deleting error!")

    if choose == 2:
        folder_name_d = str(input("Insert folder name: "))
        try:
            os.rmdir(dir + "/" + folder_name_d)
            print("folder: " + folder_name_d + " was deleated!")
        except:
            print("Folder deleting error!")

def header(dir: str) -> None:
    print("Papapevniy Provodnik")
    print("dir -> " + dir)
    print("--------------------")

def check_content(dir: str) -> list:
    cont = []
    try:
        for f in os.listdir(dir): 
            if not f.startswith('.'):
                cont.append(str(f))
        return cont
    except:
        return cont
    

def print_actions(files: list, dir: str) -> user_inf:
    header(dir)
    
    if len(files) == 0:
        print()
        print("empty")
        print()
        print("0 - other actions")
        print(str(1) + " - back")
        print("\033[31m{}".format(str(2) + " - exit"))
        print("\033[0m")


    for i in range(0, len(files)):
        
        if str(files[i]).rfind(".") == -1:
            try:
                print(" - " + files[i] + "(" + str(len(check_content(dir + "/" + files[i]))) + ")")
            except:
                print(" - " + files[i])
        else:
            print(str(" - " + files[i]))

        if i == len(files) - 1:
            print("0 - other actions")
            print(str(1) + " - back")
            print("\033[31m{}".format(str(2) + " - exit"))
            print("\033[0m")

    out = user_inf(str(input("Choose: ")), len(files))
    #out = [int() - 1, ]
    print()
    return out

def update(dir: str) -> user_inf:
    return print_actions(check_content(dir), dir)

def dirl(dir: str) -> str:
    if len(dir) > 0:
        if dir[0] == '/' and dir.rfind("/") == 0:
            return "/"
        return dir.rsplit('/', 1)[0]
    return "/"

def manipulate_file(dir: str) -> None:
    header(dir)

    print("0 - return")
    print("1 - create file")
    print("2 - create folder")
    print("3 - create project")
    print("4 - delete file/folder")
    print()
    ch = int(input("Choose action: "))
    print()
    match ch:
        case 0:
            return
        case 1:
            create_file(dir)
        case 2:
            create_folder(dir)
        case 3:
            create_project(dir)
        case 4:
            delete_file_folder(dir)
        case _:
            return

def search(dir: str, param: str) -> int:
    in_search = check_content(dir)
    for f in range(0, len(in_search)):
        index = in_search[f].find(param)
        if index != -1:
            return f
    return -1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_direct', help = 'start directory', default = '/home')

    input_dir = ""

    try:
        input_dir = parser.parse_args().input_direct
    except Exception as e:
        print(f'Error! {e}')
    
    print(input_dir)
    dir = str(input_dir)
    user_data = user_inf("-5", -5)

    while(user_data.choose != str(user_data.length + 1)):
        
        user_data = update(dir)

        if user_data.choose == "1":
            dir = dirl(dir)

        if user_data.choose == "2":
            break


        if user_data.choose == "0":
            manipulate_file(dir)

        if user_data.choose != "" and user_data.choose != "0" and user_data.choose != "1" and user_data.choose != "2":
            result = search(dir, user_data.choose)
            print(result)
            if result != -1:
                files = check_content(dir)
                if dir == "/":
                    if files[result].rfind(".") == -1:
                        dir = dir + str(files[result])
                    else:
                        file = open(dir + str(files[result]))
                        print("File " + files[result] + ":")
                        for line in file:
                            print(line)
                else:
                    if files[result].rfind(".") == -1:
                        dir = dir + "/" + str(files[result])
                    else:
                        file = open(dir + "/" + str(files[result]))
                        print("\033[33m", end = '')
                        print('#' * 60)
                        print("File " + files[result] + ":")
                        i = 1
                        for line in file:
                            i += 1
                            print(str(i) + " " + line, end = '')
                        print('#' * 60)
                        print("\033[0m", end = '')

        #print(dir)# -> DEBUG