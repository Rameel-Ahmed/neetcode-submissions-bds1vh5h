class Solution:
    def isValid(self, s: str) -> bool:
        closeToopen = {"]":"[","}":"{",")":"("}
        list1 = []
        for char in s:
            if char in closeToopen:

                if list1 and closeToopen[char]==list1[-1]:
                    list1.pop()
                else:
                    return False
            else:
                list1.append(char)
        return True if not list1 else False


