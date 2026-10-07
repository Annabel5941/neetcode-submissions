class DynamicArray:
    
    def __init__(self, capacity: int):
        self.__array = [0] * capacity
        self.__capacity = capacity
        self.__length = 0

    def get(self, i: int) -> int:
        return self.__array[i]

    def set(self, i: int, n: int) -> None:
        self.__array[i] = n

    def pushback(self, n: int) -> None:
        if self.__length == self.__capacity:
            self.resize()
        self.__array[self.__length] = n
        self.__length += 1

    def popback(self) -> int:
        self.__length -= 1
        return self.__array[self.__length]
 
    def resize(self) -> None:
        self.__capacity *= 2
        new_arr = [0] * self.__capacity
        for i in range(self.__length):
            new_arr[i] = self.__array[i]
        self.__array = new_arr

    def getSize(self) -> int:
        return self.__length
        

    def getCapacity(self) -> int:
        return self.__capacity
