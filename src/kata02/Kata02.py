def chop(
        number,
        int_array,
        cumulative_index=0
):
    empty = -1
    if is_empty(int_array):
        return empty
    if is_not_single_element_match(number, int_array):
        return empty

    midpoint = halfway(int_array)
    element_at_midpoint = int_array[midpoint]

    if is_match(number, element_at_midpoint):
        return adjusted_index(cumulative_index, midpoint)
    elif is_number_above_midpoint(number, element_at_midpoint):
        cumulative_index = adjusted_index(midpoint, cumulative_index)
        return chop(number, int_array[midpoint::], cumulative_index)
    elif is_number_below_midpoint(number, element_at_midpoint):
        return chop(number, int_array[0:midpoint])


def halfway(int_array):
    return int.__floordiv__(len(int_array), 2)


def is_empty(int_array):
    return len(int_array) == 0


def is_not_single_element_match(number, int_array):
    return len(int_array) == 1 and int_array[0] != number


def is_match(number, element):
    return number == element


def is_number_above_midpoint(number, halfway_element):
    return halfway_element < number


def is_number_below_midpoint(number, halfway_element):
    return halfway_element > number


def adjusted_index(current_index, halfway_index):
    return halfway_index + current_index
