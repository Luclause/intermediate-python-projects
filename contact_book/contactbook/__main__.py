import sys
from .classmodule import MyClass
from .funcmodule import my_function

def main():
    print('in main')
    args = sys.argv[1:]
    print(f'count of args {len(args)}')

    for arg in args:
        print(f'passed argument: {arg}')

    my_function('hello world')

    my_object = MyClass('Jun')
    my_object.say_name()

if __name__ == '__main__':
    main()
