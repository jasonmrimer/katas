

def is_empty(int_array):
    return len(int_array) == 0


def single_element_not_found(number, int_array):
    return len(int_array) == 1 and int_array[0] != number


def is_match(number, element):
    return number == element


def number_in_upper_half(number, int_array, halfway_index):
    return int_array[halfway_index] < number


def number_in_lower_half(number, int_array, halfway_index):
    return int_array[halfway_index] > number


def chop(
        number,
        int_array,
        current_index=0
):
    halfway_index = int.__floordiv__(len(int_array), 2)
    if is_empty(int_array):
        return -1
    if single_element_not_found(number, int_array):
        return -1

    if is_match(number, int_array[halfway_index]):
        return halfway_index + current_index
    elif number_in_upper_half(number, int_array, halfway_index):
        current_index = current_index + halfway_index
        return chop(
            number,
            int_array[halfway_index::],
            current_index
        )
    elif number_in_lower_half(number, int_array, halfway_index):
        return chop(
            number,
            int_array[0:halfway_index]
        )
