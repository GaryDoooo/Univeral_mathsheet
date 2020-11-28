from copy import deepcopy

color = ["x", "o"]
color_name = ["black", "white"]
char2index = {}
for i, c in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
    char2index[c] = i
handi = {
    9: [(2, 6), (6, 2), (6, 6), (2, 2), (4, 4)],
    13: [(3, 9), (9, 3), (9, 9), (3, 3), (6, 6), (6, 3), (6, 9), (3, 6), (9, 6)],
    19: [(3, 15), (15, 3), (15, 15), (3, 3), (9, 9), (9, 3), (9, 15), (3, 9), (15, 9)]
}


def board_equals(a, b):
    for i, j in zip(a, b):
        if i != j:
            return False
    return True


class Go:

    def __init__(self, height, width=None):
        self.height = height
        if width is None:
            width = height
        self.width = width
        if height < 1 or height > 25 or width < 1 or width > 25:
            height = 1 / 0
        self.size = {"height": height, "width": width}
        # self.all = [set(), set()]  # Black is 0, white is 1
        # self.groups[[],[]] #
        self.reset()

    def handicap_stones(self, n):
        if self.width != self.height or len(
                self.history) > 1 or self.height not in handi:
            self.height = 1 / 0
        for i in range(n):
            y, x = handi[self.height][i]
            self.board[y][x] = "x"

    def reset(self):
        self.current_turn = 0
        self.turn = "black"
        self.board = [["."] * self.width for _ in range(self.height)]
        self.history = [deepcopy(self.board)]

    def get_coords(self, position):
        h = self.height - int(position[0])
        w = char2index[position[1]]
        return h, w

    def get_position(self, position):
        h, w = self.get_coords(position)
        return self.board[h][w]

    def move(self, *moves):
        for move in moves:
            h, w = self.get_coords(move)
            if self.board[h][w] != ".":
                self.height = 1 / 0
            self.board[h][w] = color[self.current_turn]
            # Check capture
            captured = self.check_capture(h, w)
            # Check suicide
            if not captured:
                if not self.check_alive(h, w):
                    self.board = deepcopy(self.history[-1])
                    self.height = 1 / 0
            # check KO
            try:
                if board_equals(self.board, self.history[-2]):
                    self.board = deepcopy(self.history[-1])
                    self.height = 1 / 0
            except IndexError:
                pass
            self.pass_turn()

    def check_capture(self, h, w):
        c = self.board[h][w]
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x = dx + w
            y = dy + h
            if 0 <= x < self.width and 0 <= y < self.height:
                if self.board[y][x] != c and self.board[y][x] != ".":
                    self.check_alive(y, x)

    def check_alive(self, hh, ww):
        c = self.board[hh][ww]
        done = []
        todo = [(hh, ww)]
        while todo:
            h, w = todo.pop()
            done.append((h, w))
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = dx + w
                y = dy + h
                if 0 <= x < self.width and 0 <= y < self.height:
                    if self.board[y][x] == ".":
                        return True
                    if self.board[y][x] == c:
                        if (y, x) not in done and (y, x) not in todo:
                            todo.append((y, x))
        for y, x in done:
            self.board[y][x] = "."
        return False

    def pass_turn(self):
        board = deepcopy(self.board)
        self.history.append(board)
        self.current_turn = self.current_turn ^ 1
        self.turn = color_name[self.current_turn]

    def roll_back_1step(self):
        self.current_turn = self.current_turn ^ 1
        self.history.pop()
        self.board = deepcopy(self.history[-1])
        self.turn = color_name[self.current_turn]

    def rollback(self, steps):
        print(len(self.history))
        for i in range(steps):
            self.roll_back_1step()
