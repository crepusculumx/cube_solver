class Cube:
    colors: dict[str, list[str]] = {
        'B': ["0", "0", "0", "0"],
        'D': ["0", "0", "0", "0"],
        'F': ["0", "0", "0", "0"],
        'L': ["0", "0", "0", "0"],
        'R': ["0", "0", "0", "0"],
        'U': ["0", "0", "0", "0"],
    }

    def __init__(self, s: str):
        color_order = ['B', 'D', 'F', 'L', 'R', 'U']
        for i in range(6):
            for j in range(4):
                self.colors[color_order[i]][j] = s[i * 4 + j]

    def to_str(self) -> str:
        s = ""
        for key in self.colors:
            for c in self.colors[key]:
                s += c
        return s

    def is_solved(self) -> bool:
        for face in self.colors:
            for color in self.colors[face]:
                if color != self.colors[face][0]:
                    return False
        return True

    def rotate_face(self, face: str, counter: bool):
        if not counter:
            for i in range(1, 4):
                # swap
                temp = self.colors[face][i]
                self.colors[face][i] = self.colors[face][0]
                self.colors[face][0] = temp
        else:
            for i in range(3, 0, -1):
                # swap
                temp = self.colors[face][i]
                self.colors[face][i] = self.colors[face][0]
                self.colors[face][0] = temp

    def revolve(self, face_order: list[str], change_pos: list[list[int]], counter: bool):
        if counter:
            face_order.reverse()
            change_pos.reverse()

        for i in range(1, 4):
            temp1 = self.colors[face_order[0]][change_pos[0][0]]
            self.colors[face_order[0]][change_pos[0][0]] = self.colors[face_order[i]][change_pos[i][0]]
            self.colors[face_order[i]][change_pos[i][0]] = temp1
            temp2 = self.colors[face_order[0]][change_pos[0][1]]
            self.colors[face_order[0]][change_pos[0][1]] = self.colors[face_order[i]][change_pos[i][1]]
            self.colors[face_order[i]][change_pos[i][1]] = temp2

    def revolve_r(self, counter: bool):
        face_order = ['F', 'U', 'B', 'D']
        change_pos = [
            [2, 1],
            [2, 1],
            [0, 3],
            [2, 1]
        ]

        self.revolve(face_order, change_pos, counter)
        self.rotate_face('R', counter)

    def revolve_l(self, counter: bool):
        face_order = ['F', 'D', 'B', 'U']
        change_pos = [
            [0, 3],
            [0, 3],
            [2, 1],
            [0, 3]
        ]

        self.revolve(face_order, change_pos, counter)
        self.rotate_face('L', counter)

    def revolve_f(self, counter: bool):
        face_order = ['U', 'R', 'D', 'L']
        change_pos = [
            [3, 2],
            [0, 3],
            [1, 0],
            [2, 1]
        ]

        self.revolve(face_order, change_pos, counter)
        self.rotate_face('F', counter)

    def revolve_b(self, counter: bool):
        face_order = ['U', 'L', 'D', 'R']
        change_pos = [
            [1, 0],
            [0, 3],
            [3, 2],
            [2, 1]
        ]

        self.revolve(face_order, change_pos, counter)
        self.rotate_face('B', counter)

    def revolve_u(self, counter: bool):
        face_order = ['F', 'L', 'B', 'R']
        change_pos = [
            [1, 0],
            [1, 0],
            [1, 0],
            [1, 0]
        ]

        self.revolve(face_order, change_pos, counter)
        self.rotate_face('U', counter)

    def revolve_d(self, counter: bool):
        face_order = ['F', 'U', 'B', 'D']
        change_pos = [
            [3, 2],
            [3, 2],
            [3, 2],
            [3, 2]
        ]

        self.revolve(face_order, change_pos, counter)
        self.rotate_face('D', counter)
