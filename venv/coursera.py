import os
import tempfile
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

    def __add__(self, other):
        tempdir=tempfile.gettempprefix()
        with open(self.path,'r') as f:
            temp_data=f.readlines()
        with open (tempdir,'w') as f:
            f.writelines(temp_data)
            for line in other:
                f.writelines(line)
        return File(tempdir)

    def write(self,String):
        with open(self.path,'w') as f:
            try:
                f.write(String)
            except(TypeError):
                print("TYPE ERROR")
    def read(self):
        with open(self.path,'r') as f:
            return f.readlines()
    def __str__(self):
        return self.path


path=f"C:\PythonFiles\log.txt"
other=f"C:\PythonFiles\MyText.txt"
obj = File(path)
obj.write("""newTest ahsdjk 
fksjSad TESTTEST test
test
""")
obj2=File(other)
print(obj2)
new_obj=obj+obj2
print((new_obj.read()))
