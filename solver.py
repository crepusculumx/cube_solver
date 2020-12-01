from copy import deepcopy
from queue import Queue

import pymongo

from controller import Controller
from cube import Cube


def solve(cube: Cube, controller: Controller):
    hash_table: set = set()

    q = Queue()
    q.put(cube.to_str())
    q.put([])
    hash_table.add(cube.to_str())

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


def _reverse_cmd(cmd_pass: list[str]):
    for cmd in cmd_pass:
        if len(cmd) == 1:
            cmd = 'c' + cmd
        else:
            cmd = cmd[1]


def pre_solve(controller: Controller):
    start_str = "rrrryyyyoooobbbbggggwwww"
    cube = Cube(start_str)
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    cube_db = client["cube"]
    hash_table = cube_db["direct_pass"]

    q = Queue()
    q.put(cube.to_str())
    q.put([])
    start_data = {"cube_str": start_str, "pass": []}
    hash_table.insert_one(start_data)

    while not q.empty():
        u = q.get_nowait()
        u_cmd: list[str] = q.get_nowait()

        for cmd in controller.enable_cmd:
            v_cube = Cube(u)
            controller.control(v_cube, cmd)
            if hash_table.count({"cube_str": v_cube.to_str()}):
                continue

            u_cmd.append(cmd)
            true_pass = u_cmd.copy()
            true_pass.reverse()
            _reverse_cmd(true_pass)
            u_data = {"cube_str": v_cube.to_str(), "pass": true_pass}
            hash_table.insert_one(u_data)

            q.put(v_cube.to_str())
            q.put(deepcopy(u_cmd))

            u_cmd.pop()
