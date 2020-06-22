from board import Board

# b = Board()
# b.print_board()
# b.update(1, 1, 1)
# b.print_board()
# b.update(0, 0, 0)
# b.print_board()
#
# if b.update(1, 0, 3) == 0:
#     b.print_board()
# else:
#     print("Wrong Input")

user_input = [[1, -1, -1], [0, 1, 0], [0, -1, 1]]
# for i in range(0, 3):
#     for j in range(0, 3):
#         print(user_input[i][j])
# b = Board()
# b.print_board()
# b.build(user_input)
# b.print_board()
# print(b.check_state())

b = Board()
b.set_board(user_input)
b.print_board()
print(b.check_state())




