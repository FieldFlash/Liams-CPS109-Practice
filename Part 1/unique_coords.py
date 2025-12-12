def unique_coords(coords):
    """
    Problem 3 — Unique Coordinates
    You are given a list of coordinate pairs (tuples), possibly with duplicates.
    Write a function unique_coords(coords) that:
    ● takes a list like [(1,2), (3,4), (1,2), (3,4), (5,6)]
    ● returns a set of all unique coordinates.
    Example:
    unique_coords([(1,2), (3,4), (3,4), (1,2)]) → {(1,2), (3,4)}
    """
    uniqueSet = set(coords)
    return uniqueSet

def main():
    coords = [(1,2), (3,4), (3,4), (1,2)]
    print(unique_coords(coords))

main()