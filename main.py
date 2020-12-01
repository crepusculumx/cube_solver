from controller import Controller
from cube import Cube
from solver import solve

if __name__ == '__main__':
    cube_s = "wbrryoyyowgowbbborgyrggw"
    cube = Cube(cube_s)
    controller = Controller()

    print(cube.to_str())

    # controller.control(cube, "cu")

    print(cube.to_str())
    print(solve(cube, controller))
