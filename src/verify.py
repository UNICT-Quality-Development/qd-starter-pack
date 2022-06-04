def verify(number_to_search: int) -> bool:
    static_array = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
    is_number_present = number_to_search in static_array

    should_add_not = '' if is_number_present else 'not '

    print(f'The number {number_to_search} is {should_add_not}present in the array.')
    return is_number_present

