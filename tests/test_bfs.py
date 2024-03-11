from swap_puzzle import *
import unittest


class TestBFSSolver(unittest.TestCase):

    def test_graph1(self):
        g = Graph.graph_from_file("input/graph1.in")
        with open("input/graph1.path.out", "r") as file:
            for line in file.readlines():
                tup = list(map(int, line.replace("[", "")
                               .replace("]", "").replace(",", "").split()))
                src = tup[0]
                dst = tup[1]
                leng = tup[2]
                seq = tup[3::]
                bfs_seq = g.bfs(src, dst)
                self.assertEqual(leng, len(bfs_seq) - 1)
                self.assertEqual(seq, bfs_seq)

    def test_graph2(self):
        g = Graph.graph_from_file("input/graph2.in")
        with open("input/graph2.path.out", "r") as file:
            for line in file.readlines():
                tup = list(map(lambda i: None if i == "None" else int(i), line.replace("[", "")
                               .replace("]", "").replace(",", "").split()))
                src = tup[0]
                dst = tup[1]
                leng = tup[2]
                seq = tup[3::]
                try:
                    bfs_seq = g.bfs(src, dst)
                    self.assertEqual(leng, len(bfs_seq) - 1)
                    self.assertEqual(seq, bfs_seq)
                except BFSNoPathException as e:
                    self.assertEqual(leng, None)


if __name__ == '__main__':
    unittest.main()
