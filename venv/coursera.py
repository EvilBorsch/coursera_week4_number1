class File:
    def __init__(self,path):
        self.path=path
        self.current_position=0
    def __iter__(self):
        return self
    def __next__(self):
        with open(self.path,'r') as f:
            f.seek(self.current_position)
            line=f.readline()
            if not line:
                raise StopIteration
            self.current_position=f.tell()
            return line
    def write(self,String):
        with open(self.path,'w') as f:
            try:
                f.write(String)
            except(TypeError):
                print("TYPE ERROR")
    def __str__(self):
        return self.path


path=f"C:\PythonFiles\log.txt"
obj = File(path)
obj.write("""newTest ahsdjk 
fksjSad TESTTEST test
test
""")
for line in obj:
    print(line)
print(obj)