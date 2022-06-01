# Surprise me.

def months(monthnum : int) -> str:
    with31days : list[int] = [1,3,5,7,8,10,12]
    return "31 days" if monthnum in with31days else ("28-29 days" if monthnum == 2 else "30 days")