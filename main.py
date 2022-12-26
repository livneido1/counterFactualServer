# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numbers
import os
import subprocess


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#
if __name__ == '__main__':
    wd = os.getcwd()
    print(wd)
    print("list: " + str(os.listdir(wd)))
    os.chdir('./BussinessLayer/algorithmsListTest')
    print("dir list: " + str(os.listdir(os.getcwd())))
    fileName = 'helloWorld.py'
    # os.system("py " + fileName)
    f = open("myfile.txt", "w", encoding="utf-8")
    l = lambda x: x*3
    subprocess.call(["py", fileName, l], bufsize=100000)

    # subprocess.Popen()
    # p = subprocess.Popen(fileName, shell=False)
    # out, err = p.communicate()
    # os.execv()
    # subprocess.call("")
    # subprocess.call("", )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
