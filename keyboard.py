from pynput import keyboard
from pynput.keyboard import Key, Listener

f = open("log", 'a')


def pressed(key):
    print(key)


def released(value):
    value('some')


print('run');

released(pressed)
