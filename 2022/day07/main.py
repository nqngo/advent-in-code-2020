data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ item.rstrip() for item in src.readlines() ]


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.items = []

    @property
    def size(self):
        size = 0
        for item in self.items:
            size += item.size
        return size
    
    def cd(self, target):
        if target == '..':
            if self.parent is not None:
                return self.parent
        for item in self.items:
            if isinstance(item, Directory) and (item.name == target):
                return item


# Traverse the trees
root = Directory('/', None)
cwd = root
for line in data:
    cmd = line.split()
    if cmd[1] == 'cd':
        if cmd[2] == '/':
            cwd = root
        else:
            cwd = cwd.cd(cmd[2])
    elif cmd[1] == 'ls':
        while True:
            if line.startswith('$'):
                break
    else:
        size_dir, name = cmd[0], cmd[1]
        if size_dir == 'dir':
            cwd.items.append(Directory(name, cwd))
        else:
            cwd.items.append(File(name, int(size_dir)))


def part1(tree):
    max_size = 100000
    found = []
    scan_queue = [tree]
    for dir in scan_queue:
        scan_queue.extend([i for i in dir.items if isinstance(i, Directory)])
        if dir.size <= max_size:
            found.append(dir)
    return sum(f.size for f in found)

print(part1(root))


def part2(tree):
    fs_total = 70000000
    fs_req = 30000000
    fs_free = fs_total - root.size

    found = []
    scan_queue = [tree]

    for dir in scan_queue:
        scan_queue.extend([i for i in dir.items if isinstance(i, Directory)])
        if dir.size + fs_free >= fs_req:
            found.append(dir.size)
    
    return sorted(found)[0]

print(part2(root))