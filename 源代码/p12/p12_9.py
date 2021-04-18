# p12_9.py
class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)
        # 这里使用列表的下标作为字典的键，注意不能用元素作为字典的建
        # 因为列表的不同下标可能有值一样的元素，但字典不能有两个相同的键

    def __len__(self):
        return len(self.values)
        
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]
