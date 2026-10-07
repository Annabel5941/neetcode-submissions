class Solution:

    def encode(self, strs: List[str]) -> str:
        string = 'भा'
        for s in strs:
            string += s + 'भा'
        
        return string

    def decode(self, s: str) -> List[str]:
        s = s.split("भा")

        s.pop(0)
        s.pop()

        print(s)

        return s