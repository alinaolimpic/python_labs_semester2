# lab05/collection.py
from lab02.collection import BusFleet


class AdvancedBusCollection(BusFleet):

    # ---SORT BY (универсальный)---- 
    def sort_by(self, key_func):
        new = AdvancedBusCollection()
        new._items = sorted(self._items, key=key_func)
        return new
    

    # ----FILTER BY----- 
    def filter_by(self, predicate):#predicate = функция, которая возвращает True/False
        new = AdvancedBusCollection()
        for item in self._items:
            if predicate(item):
                new.add(item)
        return new

    # ------APPLY------
    
    def apply(self, func): 
        new = AdvancedBusCollection()
        for item in self._items:
            result = func(item)
            new.add(result)
        return new

    #-----MAP-------- 
    def map(self, func):
        return list(map(func, self._items))

    #-----ПЕЧАТЬ------
    def __str__(self):
        return "\n".join(str(x) for x in self._items)