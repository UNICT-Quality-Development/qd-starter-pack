def is_element_in_list(list:list[int], value:int ) -> bool:
    for x in list:
        if x == value:
            return True
    return False
