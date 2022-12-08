from enum import Enum
import os
import sys
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import re
from utils import read


lines = read.read_puzzle(7)

cd_regex = re.compile(r"\$ cd (.*)")
ls_regex = re.compile(r"\$ ls")
dir_regex = re.compile("dir (.*)")
file_regex = re.compile(r"(\d+) (.*)")


class NodeType(Enum):
    DIR = 0
    FILE = 1


class Node:
    def __init__(self, name: str, type: NodeType, size: int = 0, parent=None):
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_size(self):
        if self.type == NodeType.FILE:
            return self.size
        else:
            return sum([child.get_size() for child in self.children])


def print_graph(node: Node, level=0):
    if node.type == NodeType.DIR:
        print(f"{'  '*level}{node.get_size()} {node.name} ({node.type.name})")
        for child in node.children:
            print_graph(child, level + 1)

    elif node.type == NodeType.FILE:
        print(f"{'  '*level}{node.get_size()} {node.name} ({node.type.name})")


def sum_dir_size_gt_100_000(node: Node) -> int:
    if node.type == NodeType.DIR:
        size = node.get_size()

        totalsize = 0
        if node.children:
            totalsize += sum(
                [
                    sum_dir_size_gt_100_000(child)
                    for child in node.children
                    if child.type == NodeType.DIR
                ]
            )
        if size <= 100000:
            totalsize += size

        return totalsize


def get_dirs_with_at_least(node: Node, min_size: int) -> List[Node]:
    nodes = []
    if node.type == NodeType.DIR:
        if node.get_size() >= min_size:
            nodes.append(node)
        if node.children:
            for child in node.children:
                nodes.extend(get_dirs_with_at_least(child, min_size))

    return nodes


def get_root_dir(node: Node) -> Node:
    while True:
        if not node.parent:
            break
        node = node.parent
    return node


current_dir = Node("/", NodeType.DIR)
for line in lines:
    if m := cd_regex.match(line):
        dirname = m.group(1)

        if dirname == "..":
            if current_dir.parent:
                current_dir = current_dir.parent
            else:
                raise Exception()

        elif dirname == "/":
            get_root_dir(current_dir)

        else:
            dir = Node(m.group(1), NodeType.DIR, parent=current_dir)
            if current_dir:
                current_dir.add_child(dir)
            current_dir = dir

    if m := ls_regex.match(line):
        pass

    if m := dir_regex.match(line):
        pass

    if m := file_regex.match(line):
        file = Node(m.group(2), NodeType.FILE, size=int(m.group(1)), parent=current_dir)
        current_dir.add_child(file)


root_dir = get_root_dir(current_dir)
# print_graph(root_dir)

print(f"Sum of sizes for directories gt 100.000: {sum_dir_size_gt_100_000(root_dir)}")

unused_space = 70000000 - root_dir.get_size()
required_space = 30000000 - unused_space

candiates = sorted(
    get_dirs_with_at_least(root_dir, required_space), key=lambda n: n.get_size()
)
print(
    "Size of the smallest directory to delete "
    f"in order to get the required space for the update is: {candiates[0].get_size()}"
)
