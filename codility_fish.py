def solution(A: list, B: list):
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
            return solution(A, B)
    return len(A)  # Returning the count of fishes alive


assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution([4, 2, 8, 3, 5, 9, 1], [0, 1, 1, 0, 1, 0, 0]) == 3
assert solution([4, 5, 6], [0, 0, 1]) == 3
assert solution([4, 5, 8], [1, 0, 0]) == 2
