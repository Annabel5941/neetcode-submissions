class Solution:
    def isValid(self, s: str) -> bool:

        ##using a stack...

        stack = []

        #map close to open
        d = {}
        d[')'] = '('
        d['}'] = '{'
        d[']'] = '['

        for p in list(s):
            if p in d.values():
                stack.append(p)
            
            else:
                try:
                    if stack[-1] == d[p]:
                        stack.pop()
                    else:
                        return False
                #add except in case out of range...
                except:
                    return False

        #check stack now empty
        if len(stack) == 0:
            return True
        
        return False
        