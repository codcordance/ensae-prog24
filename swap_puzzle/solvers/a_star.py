from swap_puzzle import *


class AStarSolver(Solver):
    """
    A* solver.

    NB: The neighbors calculation are poorly implemented and are not efficient.
    """

    def work(self, m: int, n: int, state: state, acc: object) -> (list[tuple[cell, cell]], object):
        """
        Parameters
        ----------
        acc:
            Here the solver compute all the swaps in the first call to _work,
            then pass it each step through the accumulator.
        """
        if acc is None:
            d = SPUtils.dict_possible_states(m, n)
            src, dst = SPUtils.state_to_str(state), SPUtils.state_to_str(next(iter(d.values())))

            def astar() -> list[str]:
                """
                A Star algorithm.

                Returns
                -------
                list[str]
                    Path from start to end using A* algorithm.

                Raises
                ------
                BFSNoPathException
                    Raised if dst is not reachable from src.
                """
                visited = {src: None}
                queue = PriorityQueue()
                queue.put((0, src))

                neighbors = {}
                neighbors_c = {}

                def neighbors_cache(node1, node2):
                    """
                    Cache for the neighbors calculations. Returns True if and only if two states (given as nodes)
                    are direct neighbors.
                    """
                    if (node1, node2) not in neighbors_c:
                        b = SPUtils.neighbour_states(d[node], d[k])
                        neighbors_c[(node1, node2)] = b
                        neighbors_c[(node2, node1)] = b
                    return neighbors_c[(node1, node2)]

                while not queue.empty():
                    cost, node = queue.get()
                    if node == dst:
                        path = []
                        while node is not None:
                            path.append(node)
                            node = visited[node]
                        return [*reversed(path)]
                    if node not in neighbors:
                        n = []
                        for k in d.keys():
                            if k != node and neighbors_cache(node, k):
                                n.append(k)
                        neighbors[node] = n
                    for neighbor in neighbors[node]:
                        if neighbor not in visited:
                            visited[neighbor] = node
                            queue.put((cost + len(SPUtils.cell_difference(d[dst], d[neighbor])), neighbor))

                raise AStarNoPathException(src, dst)

            path = astar()
            swaps = []
            for i in range(len(path) - 1):
                swaps.append(SPUtils.swap_between_states(d[path[i]], d[path[i + 1]]))
            return swaps[0:1], swaps[1:]
        else:
            return acc[0:1], acc[1:]

    def __init__(self, callback: Callable[[list[tuple[cell, cell]]], None] = lambda _: None) -> None:
        """
        Parameters
        ----------
        callback: Callable[[list[tuple[Coordinates, Coordinates]]], None], optional
            Function called when a swap is operated on the grid. Default does nothing.
        """
        super().__init__("A*", callback=callback)
