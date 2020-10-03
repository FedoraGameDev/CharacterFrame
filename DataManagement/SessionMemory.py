from ..ErrorHandling.Errors import ExceptionMessage
from ..Debug import Debug
from typing import List


class MemoryFragment:
    name: str
    obj: any

    def __init__(self, name: str, obj: any):
        self.name = name
        self.obj = obj


class SessionMemory:
    data: List[MemoryFragment] = []

    @staticmethod
    def Init() -> None:
        Debug.LogInfo("Wiping Session Memory")
        while len(SessionMemory.data) > 0:
            SessionMemory.data.remove(SessionMemory.data[0])

    @staticmethod
    def Add(name: str, obj: any) -> None:
        Debug.LogInfo(f"Adding '{name}' to Session Memory")
        SessionMemory.data.append(MemoryFragment(name, obj))

    @staticmethod
    def Get(name: str) -> any:
        index: int = SessionMemory.IndexOf(name)
        if index == -1:
            return None
        else:
            return SessionMemory.data[index]

    @staticmethod
    def Remove(name: str) -> None:
        index: int = SessionMemory.IndexOf(name)
        if index == -1:
            return
        else:
            Debug.LogInfo(f"Removing '{name}' from Session Memory")
            SessionMemory.data.remove(SessionMemory.data[index])

    @staticmethod
    def Contains(name: str) -> bool:
        index: int = SessionMemory.IndexOf(name)
        return not (index == -1)

    @staticmethod
    def IndexOf(name: str) -> int:
        for i in range(len(SessionMemory.data)):
            if SessionMemory.data[i].name == name:
                return i
        return -1
