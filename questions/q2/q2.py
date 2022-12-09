import typing


def degree_of_array(arr: typing.List[int]) -> int:
    """
    degree_of_array function takes in 1 parameter:
    arr: List[int] - the array to be analyzed

    The function returns an int which is the length of the shortest subarray
    that has the same degree as the original array, the algorithm used is a
    hashmap and the time complexity is O(n) where n is the number of elements
    in the array
    """

    mapper = {}
    for idx, element in enumerate(arr):
        if element not in mapper:
            mapper[element] = {"count": 1, "start": idx, "end": idx}
        else:
            mapper[element]["count"] += 1
            mapper[element]["end"] = idx

    _, choosen = sorted(
        mapper.items(),
        key=lambda x: (x[1]["count"], x[1]["start"] - x[1]["end"]),
        reverse=True,
    )[0]
    return choosen["end"] - choosen["start"] + 1
