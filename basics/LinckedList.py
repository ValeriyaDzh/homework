from typing import Optional


class ObjList:

    def __init__(self, data: str):
        self.__data: str = data
        self.__next: ObjList | None = None
        self.__prev: ObjList | None = None

    @property
    def get_next(self) -> Optional["ObjList"]:
        return self.__next

    def set_next(self, obj: Optional["ObjList"]):
        self.__next = obj

    @property
    def get_prev(self) -> Optional["ObjList"]:
        return self.__prev

    def set_prev(self, obj: Optional["ObjList"]):
        self.__prev = obj

    @property
    def get_data(self) -> str | None:
        return self.__data

    def set_data(self, obj: str):
        self.__data = obj


class LinckedList:

    def __init__(self):
        self.head: ObjList | None = None
        self.tail: ObjList | None = None

    def add_obj(self, obj: ObjList):
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            current = self.tail
            current.set_next(obj)
            obj.set_prev(current)
            self.tail = obj

    def remove_obj(self):
        if self.tail:
            current = self.tail.get_prev
            if current:
                self.tail = current
                self.tail.set_next(None)
            else:
                self.head = None
                self.tail = None
        else:
            print("List is already empty")

    def get_data(self) -> list[str]:
        values = []
        if self.head:
            current = self.head
            while current:
                values.append(current.get_data)
                current = current.get_next

        return values
