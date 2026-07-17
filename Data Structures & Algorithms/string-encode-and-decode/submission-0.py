class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded =""
        for strng in strs:
            for chr in strng:
                encoded+=str(ord(chr))
                encoded+='[NEW]'
            encoded+="[AND]"
        return encoded


    def decode(self, s: str) -> List[str]:
        arr = s.split("[AND]")
        for i in range(len(arr)-1):
            s=""
            letters = arr[i].split("[NEW]")
            for letter in letters:
                if letter:
                    s+=chr(int(letter))
            arr[i] = s
        return arr[:-1]
