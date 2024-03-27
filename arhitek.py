import os, os.path, shutil, zipfile

def wait():
    input('Нажмите Enter для продолжения...')

print(f'Текущая директория:{os.getcwd()}')
wait()
print(f'Логин текущего пользователя операционной системы:{os.getlogin()}')
wait()
print(f'Тип операционной системы:{os.name}')
wait()
print(f'Существует ли файл "test.txt":{os.access("test.txt", os.R_OK)}')
wait()
print(f'Распечатать содержимое текущей папки:{os.listdir()}')
wait()
print(f'Распечатать файловую структуру текущей директории с учётом вложенности:')
for dirpath, dirnames, filenames in os.walk("."):
    for dirname in dirnames:
        print(f'Каталог:{os.path.join(dirpath, dirname)}')
    for filename in filenames:
        print(f'Файл:{os.path.join(dirpath, filename)}')
wait()
if not os.path.exists('test'):
    os.mkdir('test')
    print("Папка 'test' создана")
wait()
os.chdir('test')
print("Текущая директория после перехода в 'test':", os.getcwd())
wait()
fi = input("Введите имя файла для создания: ")+'.txt'
im = input('Введите имя:')
with open(fi,'w') as file:
    file.write(im)
if os.path.isfile(fi):
    print(f"Файл '{fi}' успешно создан")
else:
    print("Ошибка при создании файла")
wait()
put = os.path.abspath(fi)
siz = os.path.getsize(fi)
print(f"Абсолютный путь до файла: {put}")
print(f"Размер файла: {siz} байт")
wait()
shutil.copy(fi, '..')
wait()
os.chdir('..')
wait()
print("Содержимое папки после поднятия на уровень выше:")
for root, dirs, files in os.walk('.'):
    print(f"Папка: {root}")
    for file in files:
        print(f"  Файл: {file}")
copied_file_path = os.path.join(os.getcwd(), fi)
wait()
with open(copied_file_path) as copied_file:
    print(f"Содержимое скопированного файла '{fi}':")
    print(copied_file.read())
wait()
shutil.rmtree('test')
wait()
os.remove(fi)
wait()
print("Папка 'test' и файл удалены")
cur = os.getcwd()
shutil.make_archive("archive", "zip", cur)
print("Содержимое текущей папки:")
for i in os.listdir():
    print(i)
before_size = sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))
archive_size = os.path.getsize("archive.zip")
print(f"Размер до архивации: {before_size} байт")
print(f"Размер архива: {archive_size} байт")
shutil.unpack_archive("archive.zip", "unzipped_folder", "zip")
original_files = set(os.listdir())
unzipped_files = set(os.listdir("unzipped_folder"))
if original_files == unzipped_files:
    print("Содержимое разархивированной папки совпадает с исходной.")
else:
    print("Содержимое разархивированной папки не совпадает с исходной.")
os.remove("archive.zip")
shutil.rmtree("unzipped_folder")
