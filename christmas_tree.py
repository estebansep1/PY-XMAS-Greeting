def print_christmas_tree(height):
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    trunk_spaces = " " * (height - 1)
    print(trunk_spaces + "| |")

height = 10
print_christmas_tree(height)