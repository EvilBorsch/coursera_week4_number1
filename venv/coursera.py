"""""
 этом задании вам нужно создать интерфейс для работы с файлами. Класс File должен поддерживать несколько необычных операций.

Класс инициализируется полным путем.



Класс должен поддерживать метод write.



Объекты типа File должны поддерживать сложение.



В этом случае создается новый файл и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.

Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам файла.



И наконец, при выводе файла с помощью функции print должен печататься его полный путь, переданный при инициализации.



Опишите свой класс в скрипте и загрузите на платформу.
"""



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
        tempdir = os.path.join(tempfile.gettempdir(), 'tempfile')
        with open(self.path,'r') as f:
            temp_data=f.read()
        with open (tempdir,'w') as f:
            f.write(temp_data)
            for line in other:
                f.write(line)
        return File(tempdir)

    def write(self,String):
        with open(self.path,'w') as f:
            try:
                f.write(String)
            except(TypeError):
                print("TYPE ERROR")
    def read(self):
        with open(self.path,'r') as f:
            return f.read()
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
print(new_obj)
print((new_obj.read()))
