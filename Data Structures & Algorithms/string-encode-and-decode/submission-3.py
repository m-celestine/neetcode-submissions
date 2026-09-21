class Solution:

    def encode(self, strs: List[str]) -> str:
        #empty case
        if not strs:
            return ""

        # init encode var
        encoded_string = ""

        # encode strs
        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        # return encoded strs
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            # get length of next str
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            #
            i = j + 1 
            j = i + length

            decoded.append(s[i:j])
            i = j

        return decoded