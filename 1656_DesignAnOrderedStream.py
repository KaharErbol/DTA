class OrderStream:
  def __init__(self, n):
    self.arr = [None] * n
    self.ptr = 0

  def insert(self, id, val):
    self.arr[id-1] = val

    chunk = []

    while self.ptr < len(self.arr) and self.arr[self.ptr] is not None:
      chunk.append(self.arr[self.ptr])
      self.ptr += 1

    return chunk