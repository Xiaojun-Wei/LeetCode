# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def shortest_board_length(A):
    max_hole_pos = max(A)
    min_hole_pos = min(A)
    min_board_length = max_hole_pos - min_hole_pos + 1
    for board_length in range(1, max_hole_pos - min_hole_pos + 1):
        can_cover_all_holes = True
        for hole_pos in A:
            if not (min_hole_pos <= hole_pos <= min_hole_pos + board_length or
                    max_hole_pos - board_length <= hole_pos <= max_hole_pos):
                can_cover_all_holes = False
                break
        if can_cover_all_holes:
            min_board_length = min(min_board_length, board_length)
    return min_board_length



if __name__ == "__main__":
    # A = input()
    A = [11, 20, 15]
    print(shortest_board_length(A))