def is_element_in_list(values:list[int], value:int ) -> bool:
    for x in values:
        if x == value:
            return True
    return False
