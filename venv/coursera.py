class SquareIterator:
    def __init__(self,current,end):
        self.current=current
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current-1 >= self.end:
            raise StopIteration
        result=self.current ** 2
        self.current += 1
        return result
for i in SquareIterator(1,5):
    print(i)
