size = int(input('Enter the tree size: '))

bottom = (' ' * (size - 1)) + '#' + (' ' * (size - 1))

# for i in range(1, size + 1):
#     blank_num = size - i
#     branch_num = (2 * i) - 1

#     print((' ' * blank_num) + ('^' * branch_num) + (' ' * blank_num))

i = 1

# while i <= size:
#     blank_num = size - i
#     branch_num = (2 * i) - 1

#     print((' ' * blank_num) + ('^' * branch_num) + (' ' * blank_num))
#     i = i + 1

print(bottom)
print(bottom)