#!/usr/bin/python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, item):
        super().extend(item)
        x = len(item)
        print(f"Extended the list with {[x]} items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed {[item]} from the list.")

    def pop(self, index=-1):
        poped_item = super().pop(index)
        print(f"Popped {[poped_item]} from the list.")
        return poped_item
