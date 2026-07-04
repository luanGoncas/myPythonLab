import random

size = int(input('Enter the tree size: '))
bottom = (' ' * (size - 1)) + '#' + (' ' * (size - 1))

# for i in range(1, size + 1):
#     row = ''
#     blank_num = size - i
#     branch_num = (2 * i) - 1

#     for j in range(branch_num):
#         chance = random.randint(1, 4)

#         if chance == 1:
#             row += 'o'
#         else:
#             row += '^'

#     print((' ' * blank_num) + row + (' ' * blank_num))

# i = 1

# while i <= size:
#     row = ''
#     blank_num = size - i
#     branch_num = (2 * i) - 1

#     j = 0
    
#     while j < branch_num:
#         chance = random.randint(1, 4)

#         if chance == 1:
#             row += 'o'
#         else:
#             row += '^'
        
#         j = j + 1

#     print((' ' * blank_num) + row + (' ' * blank_num))
    
#     i = i + 1

print(bottom)
print(bottom)