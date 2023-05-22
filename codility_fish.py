def solution_with_recursion(A: list, B: list):
    """_summary_
    Resolving codility Fish test with recursion
    """
    for i in range(len(A) - 1):
        pair_of_fishes = A[i : i + 2]
        pair_of_directions = B[i : i + 2]

        if pair_of_directions == [1, 0]:  # Making sure left and right ones meet
            eaten_fish = min(pair_of_fishes)
            index_eaten_fish = A.index(eaten_fish)
            A.pop(index_eaten_fish)
            B.pop(index_eaten_fish)
            return solution_with_recursion(A, B)
    return len(A)  # Returning the count of fishes alive


def solution_with_stack(A, B):
    stack_fish_going_right = []
    survivals = 0

    for fish, direction in zip(A, B):
        if not direction:  # Fish going left
            while stack_fish_going_right:
                if stack_fish_going_right[-1] < fish:
                    stack_fish_going_right.pop()
                else:
                    break
            else:
                survivals += 1
        else:  # Fish going right
            stack_fish_going_right.append(fish)

    return survivals + len(stack_fish_going_right)


assert solution_with_recursion([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution_with_recursion([4, 2, 8, 3, 5, 9, 1], [0, 1, 1, 0, 1, 0, 0]) == 3
assert solution_with_recursion([4, 5, 6], [0, 0, 1]) == 3
assert solution_with_recursion([4, 5, 8], [1, 0, 0]) == 2

assert solution_with_stack([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution_with_stack([4, 2, 8, 3, 5, 9, 1], [0, 1, 1, 0, 1, 0, 0]) == 3
assert solution_with_stack([4, 5, 6], [0, 0, 1]) == 3
assert solution_with_stack([4, 5, 8], [1, 0, 0]) == 2
