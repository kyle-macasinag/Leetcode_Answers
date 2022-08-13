class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            reduced_num = num / 2
            counter + 1
            if reduced_num == 1:
                reduced_num - 1
                counter + 1
        return counter