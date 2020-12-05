from typing import Set

from cube import Cube


class Controller:
    enable_cmd: Set[str] = {
        "r", "b", "u",
        "cr", "cb", "cu"
    }

    def control(self, cube: Cube, cmd: str):
        if not (cmd in self.enable_cmd):
            return

        if cmd == "r":
            cube.revolve_r(False)
        if cmd == "b":
            cube.revolve_b(False)
        if cmd == "u":
            cube.revolve_u(False)
        if cmd == "cr":
            cube.revolve_r(True)
        if cmd == "cb":
            cube.revolve_b(True)
        if cmd == "cu":
            cube.revolve_u(True)

    def reverse_control(self, cube: Cube, cmd: str):
        if not (cmd in self.enable_cmd):
            return

        if cmd == "r":
            cube.revolve_r(True)
        if cmd == "b":
            cube.revolve_b(True)
        if cmd == "u":
            cube.revolve_u(True)
        if cmd == "cr":
            cube.revolve_r(False)
        if cmd == "cb":
            cube.revolve_b(False)
        if cmd == "cu":
            cube.revolve_u(False)
