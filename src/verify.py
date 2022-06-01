def verify(number_to_search: int) -> bool:
    static_array = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]

    should_add_not = '' if number_to_search in static_array else 'not '

    print(f'The number {number_to_search} is {should_add_not}present in the array.')
    return number_to_search in static_array

