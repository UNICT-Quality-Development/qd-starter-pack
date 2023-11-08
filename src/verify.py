def verify(l:list[int], v:int ) -> bool:
    for x in l:
        if x == v:
            return True
    return False
