import importlib
import os
import subprocess


def execute(filename):
    # module = importlib.import_module('hello')
    # print(module.__name__)
    h = importlib.import_module(filename)
    try:
        print(h.hello.run2(lambda x: 3 * x))
    except:
        print("failed")


if __name__ == "__main__":
    execute("helloWorld")
