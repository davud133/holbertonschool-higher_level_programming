#!/usr/bin/python3
"""defines VerboseList class"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{item}] to the list.".format(item=item))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with [{x}] items.".format(x=len(items)))

    def remove(self, item):
        print("Removed [{item}] from the list.".format(item=item))
        super().remove(item)

    def pop(self, item=-1):
        print("Popped [{item}] from the list.".format(item=self[item]))
        return super().pop(item)
