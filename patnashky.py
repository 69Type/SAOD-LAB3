

case1 = [15, 2, 1, 12, 8, 5, 6, 11, 4, 9, 10, 7, 3, 14, 13, 0]
case2 = [1, 2, 15, 12, 8, 5, 6, 11, 4, 9, 10, 7, 3, 14, 13, 0]

class Mapa:
    def __init__(self, array):
        self.size = 4
        self.SOLVED = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
        self.S_MATRIX = tuple([self.SOLVED[i*4:i*4+4] for i in range(self.size)])
        self.matrix = [array[i*4:i*4+4] for i in range(self.size)]

    def get_weight_matrix(self):
        return [self.comapre_array(self.S_MATRIX[i], self.matrix[i]) for i in range(self.size)]

    def comapre_array(self, a, b):
        from fuzzywuzzy import fuzz
        a = "".join(map(str, a))
        b = "".join(map(str, b))
        return fuzz.ratio(a, b)

    def value(self):
        a = self.get_weight_matrix()
        s = 0
        for i in range(len(a)):
            s += a[i] * len(a) - i
        return s

    def move_up(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.matrix[y][x] == 0:
                    if y == 0:
                        return False
                    buffer = self.matrix[y-1][x]
                    self.matrix[y - 1][x] = 0
                    self.matrix[y][x] = buffer
                    return True

    def move_down(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.matrix[y][x] == 0:
                    if y == 3:
                        return False
                    buffer = self.matrix[y+1][x]
                    self.matrix[y+1][x] = 0
                    self.matrix[y][x] = buffer
                    return True

    def move_left(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.matrix[y][x] == 0:
                    if x == 3:
                        return False
                    buffer = self.matrix[y][x+1]
                    self.matrix[y][x+1] = 0
                    self.matrix[y][x] = buffer
                    return True

    def move_right(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.matrix[y][x] == 0:
                    if x == 0:
                        return False
                    buffer = self.matrix[y][x-1]
                    self.matrix[y][x-1] = 0
                    self.matrix[y][x] = buffer
                    return True


    def execute(self):
        pre = []
        while self.matrix != self.SOLVED:
            max_value = -1000
            max_command = ""
            for i in ['move_up', 'move_down', 'move_left', 'move_right']:
                copy = [row[:] for row in self.matrix]

                if getattr(self, i)():
                    value = self.value()

                    if value > max_value and self.matrix not in pre:
                        max_value = value
                        max_command = i


                    self.matrix = copy

            print(max_value)
            print(self.matrix)

            if max_command != "":
                 getattr(self, max_command)()
            else: pre = pre[:-4]

            pre.append([row[:] for row in self.matrix])




game1 = Mapa(case1)
# game2 = Mapa(case2)
#
# print(game1.get_weight_matrix())
# print(game2.get_weight_matrix())
#
# print(game2.value())
print(game1.execute())

