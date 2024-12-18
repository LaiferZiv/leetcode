class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pos_steps = []
        fleets = 1
        if not position or not speed or len(position) != len(speed):
            return 0
        elif len(position) == 1:
            return 1
        for i in range(len(position)):
            pos_steps.append((position[i],(target-position[i])/speed[i]))
        pos_steps.sort(key=lambda x:x[0])
        for i in range(len(pos_steps)-2,-1,-1):
            if pos_steps[i][1] <= pos_steps[i+1][1]:
                pos_steps[i] = pos_steps[i+1]
            else:
                fleets += 1
        return fleets