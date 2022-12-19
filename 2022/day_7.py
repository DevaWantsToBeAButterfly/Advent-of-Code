from generic_functions import read_lines


class ElfFolder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []
        self.file_size = 0
        self.total_size = 0

    def add_child(self, child_name):
        self.children.append(ElfFolder(name=child_name, parent=self))

    def add_file(self, elf_file):
        self.files.append(elf_file)

    def update_file_size(self):
        self.file_size = sum(self.files)

    def update_total_size(self):
        self.update_file_size()
        children_size = 0

        for child in self.children:
            child.update_total_size()
            children_size += child.total_size

        self.total_size = self.file_size + children_size

    def find_small_folders(self, small_folders_list):
        for child in self.children:
            small_folders_list = child.find_small_folders(small_folders_list)

        self.update_total_size()
        if self.total_size <= 100000:
            small_folders_list.append(self.total_size)

        return small_folders_list

    def find_smallest_folder_to_delete(self, target_space, smallest_viable_folder):
        for child in self.children:
            smallest_viable_folder = child.find_smallest_folder_to_delete(target_space, smallest_viable_folder)

        if target_space <= self.total_size < smallest_viable_folder:
            smallest_viable_folder = self.total_size

        return smallest_viable_folder


puzzle_input = read_lines('.\data_files\day_7_input.txt')
elf_file_system = ElfFolder('System', None)
elf_file_system.add_child('/')
current_folder = elf_file_system
total_system_space = 70000000
wanted_free_space = 30000000

for line in puzzle_input:
    split_line = line.split(' ')
    if split_line[0] == "$":
        if split_line[1] == 'cd':
            if split_line[2] == '..':
                current_folder = current_folder.parent
            else:
                for child_folder in current_folder.children:
                    if child_folder.name == split_line[2]:
                        current_folder = child_folder
                        break

        elif split_line[1] == 'ls':
            pass

    elif split_line[0] == 'dir':
        current_folder.add_child(split_line[1])

    else:
        current_folder.add_file(int(split_line[0]))

small_folders = elf_file_system.find_small_folders([])
print(sum(small_folders))
# This is the total used space atm
currently_used_space = elf_file_system.total_size
currently_free_space = total_system_space - currently_used_space

space_to_clear = wanted_free_space - currently_free_space

print(elf_file_system.find_smallest_folder_to_delete(space_to_clear, 999999999))