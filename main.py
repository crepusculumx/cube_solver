import solver
from controller import Controller

if __name__ == '__main__':
    # cube_s = "wbrryoyyowgowbbborgyrggw"
    # cube = Cube(cube_s)
    controller = Controller()
    # print(solve(cube, controller))
    solver.pre_solve(controller)
