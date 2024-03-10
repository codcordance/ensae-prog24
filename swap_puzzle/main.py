from swap_puzzle import *

if __name__ == '__main__':
    g: Grid = Grid(2, 3)
    print(g)

    data_path: str = "../input/"
    file_name: str = data_path + "grid0.in"

    print(file_name)

    g: Grid = Grid.grid_from_file(file_name)
    print(g)
