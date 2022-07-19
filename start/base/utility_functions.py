from base.important_variables import keyboard, game_window
from pyglet_library.utility_functions import *


def key_is_pressed(key_index_index):
    return keyboard.get_key_event(key_index_index).happened_this_cycle


def key_is_hit(key_index_index):
    return keyboard.get_key_event(key_index_index).is_click()


def key_has_been_released(key_index_index):
    return keyboard.get_key_event(key_index_index).has_stopped()


def get_time_of_key_being_held_in(key_index_index):
    return keyboard.get_key_timed_event(key_index_index).current_time


def mouse_is_clicked():
    return keyboard.mouse_clicked_event.is_click()


def mouse_is_clicked():
    return keyboard.mouse_clicked_event.is_click()

def get_index_of_range(range_lengths, number):
    index = -1
    start_time = 0

    for x in range(len(range_lengths)):
        end_time = start_time + range_lengths[x]

        if number >= start_time and number <= end_time:
            index = x

        start_time = end_time

    return index

def get_items(data, new_item_ch):
    current_item = ""
    items = []

    for ch in data:
        if ch == new_item_ch:
            items.append(current_item)
            current_item = ""

        else:
            current_item += ch

    if current_item != "":
        items.append(current_item)

    return items

