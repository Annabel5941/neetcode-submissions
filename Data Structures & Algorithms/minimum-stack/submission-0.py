class MinStack:

    def __init__(self):
        self._stack = []
        self._minVals = [] #stores the minimum value for this index (includes all numbers before this index)
        

    def push(self, val: int) -> None:
        self._stack.append(val)

        #update minVals
        if len(self._minVals) == 0:
            self._minVals.append(val)
        else:
            self._minVals.append(min(val, self._minVals[-1]))       

    def pop(self) -> None:
        self._stack.pop()
        self._minVals.pop()
        
    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._minVals[-1]
        
