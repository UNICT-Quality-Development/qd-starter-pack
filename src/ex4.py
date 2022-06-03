# Surprise me.

def months(monthnum: int) -> str:
    with31days : list[int] = [1,3,5,7,8,10,12]
    if monthnum in with31days:
        return "31 days"
    else:
        if monthnum == 2:
            return "28-29 days"
        return "30 days"