class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stck = []

        length = len(position)

        for i in range(length):
            stck.append((position[i], (target - position[i]) / speed[i]))

        stck.sort()

        count = 1
        current_time = stck[-1][1]

        for i in range(length - 2, -1, -1):
            if stck[i][1] > current_time:
                count += 1
                current_time = stck[i][1]

        return count