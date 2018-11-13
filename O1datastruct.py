
class CustomDS:

    def __init__(self, size):
        self.all = 0
        self.id = 0
        self.size = size
        self.list = [(id, self.all)] * size

    def get(self, index):
        if index >= self.size:
            return None
        tup = self.list[index]
        if tup[0] < self.id:
            return self.all
        else:
            return tup[1]

    def set(self, index, val):
        if index >= self.size:
            return False
        self.list[index] = (self.id, val)
        return True

    def setAll(self, all_val):
        self.all = all_val
        self.id += 1


data = CustomDS(10)
data.set(0, 3)
print(data.get(0))
print(data.get(9))
