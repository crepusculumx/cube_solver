from copy import deepcopy
from queue import Queue

from controller import Controller
from cube import Cube


def solve(cube: Cube, controller: Controller):
    hash_table: set = set()

    q = Queue()
    q.put(cube.to_str())
    q.put([])

    while not q.empty():
        u = q.get_nowait()
        u_cmd: list[str] = q.get_nowait()

        if Cube(u).is_solved():
            return u_cmd

        for cmd in controller.enable_cmd:
            v_cube = Cube(u)
            controller.control(v_cube, cmd)
            if cube.to_str() in hash_table:
                continue

            u_cmd.append(cmd)
            hash_table.add(v_cube.to_str())
            q.put(v_cube.to_str())
            q.put(deepcopy(u_cmd))

            u_cmd.pop()
