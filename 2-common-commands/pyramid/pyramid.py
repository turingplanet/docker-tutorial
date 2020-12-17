import sys

def print_pyramid(level: int):
    for i in range(level):
        new_line_str = ''
        new_line_str += ' ' * (level - 1 - i)
        new_line_str += '*' * ((i+1) * 2 - 1)
        print(new_line_str)

input_level = int(sys.argv[1])
print_pyramid(input_level)
