from src.verify import verify
import random

def genRandomList() -> list[int]:
  randomlist = []
  for i in range(0,5):
    n = random.randint(1,30)
  randomlist.append(n)
  return randomlist


def test_verify() -> None:
  assert verify([2,3,4,5,6,8], 7) is False
  assert verify([2,3,4,5,6,8], 2 ) is True
  assert verify([2,3,4,5,6,8], 99 ) is False
  assert type(verify([2,3,4,5,6,8], 99 )) is bool

