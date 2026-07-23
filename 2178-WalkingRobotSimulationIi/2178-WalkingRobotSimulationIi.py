# Last updated: 22/7/2026, 11:36:23 p.m.
class Robot:

    def __init__(self, width: int, height: int):
        self.mod = 2*width + 2*height - 4
        self.coord = [[0,0]]
        self.directions = ['East']
        self.index = 0

        x, y = 0, 0
        d = 0 # east, south, west, north
        vectors = [(1,0), (0,-1), (-1,0), (0,1)]
        aux_directions = ['East', 'South', 'West', 'North']

        for i in range(1, 2*width + 2*height - 3):
            x += vectors[d][0]
            y += vectors[d][1]

            self.coord.append([x,y])
            self.directions.append(aux_directions[d])

            if i == width - 1: d = 3
            elif i == width + height - 2: d = 2
            elif i == 2*width + height - 3: d = 1

    def step(self, num: int) -> None:
        if num > 0: self.directions[0] = 'South'
        self.index = (self.index + num) % self.mod

    def getPos(self) -> List[int]:
        return self.coord[self.index]

    def getDir(self) -> str:
        return self.directions[self.index]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()