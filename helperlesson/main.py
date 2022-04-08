# if module is in different directory

# import sys
# sys.path.insert(0, './libs')
import helper

def render():
    print(helper.greeting('hello,', 'there'))

render()