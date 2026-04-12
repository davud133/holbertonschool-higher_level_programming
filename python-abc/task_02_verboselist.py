#!/usr/bin/python3
"""defines VerboseList class"""


from abc import ABC, abstractmethod


class VerboseList(list):
    def append(item):
        super().append(item)
        print("Added [{item}] to the list.".format(item=item))
    def extend(items):
        super().extend(items)
        print("Extended the list with [{x}] items.".format(x=len(items)))
    def remove(item):
        print("Removed [{item}] from the list.".format(item=item))
        super().remove(item)
    def pop(item=len(self) - 1):
        print("Popped [{item}] from the list.".format(item=self[item]))
        super().pop(item)
