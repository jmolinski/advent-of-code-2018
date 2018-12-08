class Node:
    def __init__(self, dat):
        i = 2
        self.children = []
        for _ in range(dat[0]):
            n = Node(dat[i:])
            i += n.length
            self.children.append(n)

        self.length = i + dat[1]
        self.meta_val = dat[i : i + dat[1]]


with open("data.txt") as f:
    data = list(map(int, f.read().strip().split()))
    root = Node(data)


def sum_node_meta(n):
    return sum(n.meta_val) + sum(sum_node_meta(c) for c in n.children)


def part1():
    return sum_node_meta(root)


def node_value(n):
    if len(n.children) == 0:
        return sum(n.meta_val)

    return sum(
        node_value(n.children[m - 1]) for m in n.meta_val if m <= len(n.children)
    )


def part2():
    return node_value(root)


print("1)", part1(), "\n2)", part2())
