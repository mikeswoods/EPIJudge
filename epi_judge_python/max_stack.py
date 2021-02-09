class MaxStack:
  def __init__(self):
    self.items = []
    self.max_item = None

  def push(self, item):
    self.items.append(item)
    if self.max_item is None:
      self.max_item = item
    else:
      self.max_item = max(self.max_item, item)

  def pop(self):
    if len(self.items) == 0:
      raise Exception("empty stack")
    item = self.items.pop()
    return item
