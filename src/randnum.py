'''
  Write a program that generates a random number.
  Output:
  The random number is: 4
'''

static_cnt : int = 1

def rand(seed : int, l : int, r : int) -> int:
    global static_cnt
    randn = (((static_cnt*seed) + ((seed-static_cnt) + static_cnt//4))%(r-l+1))+l
    static_cnt += randn
    return randn
