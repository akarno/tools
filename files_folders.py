import glob
import os
import time
from temp_files import NamedTemporaryFile

def traverse_folder(root_path):
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(root_path):
        # print('root: {}, dirs: {}, files: {}'.format(root, dirs, files))
        path = root.split(os.sep)
        # print('path: {}'.format(path))
        print((len(path) - 1) * '-', os.path.basename(root))
        for file in files:
            print(len(path) * '-', file)

def export_to_file(root_path):
    # traverse root directory, and list directories as dirs and files as files
    with open('C:\Temp\\tree.txt', 'w') as f:
        for root, dirs, files in os.walk(root_path):
            # print('root: {}, dirs: {}, files: {}'.format(root, dirs, files))
            path = root.split(os.sep)
            # print('path: {}'.format(path))
            #line = (len(path) - 1) * '-', os.path.basename(root)
            #f.write('b')
            try:
                f.write(''.join([(len(path) - 1) * '-', ' ', os.path.basename(root),'\n']))
            except UnicodeEncodeError:
                print('Could not decode folder name.')
            for file in files:
                #print(len(path) * '-', file)
                try:
                    f.write(''.join([len(path) * '-', ' ', file,'\n']))
                except UnicodeEncodeError:
                    #when needed could add method to display without encoding
                    print('Could not decode file name.')

if __name__ == '__main__':
    # file = NamedTemporaryFile('w+t', prefix='temp_file_', suffix='.csv') # dir=dir, delete=False)
    path = 'C:\Temp\\tmp'
    path_with_file = "C:\Temp\\a.txt"
    print('os.path.basename: {}'.format(os.path.basename(path))) #last component file or last folder
    # os.path.basename: tmp
    print('os.path.dirname: {}'.format(os.path.dirname(path)))
    # os.path.dirname: C:\Temp
    print('os.path.basename: {}'.format(os.path.basename(path_with_file))) #last component file or last folder
    # os.path.basename: a.txt
    print('os.path.dirname: {}'.format(os.path.dirname(path_with_file)))
    # os.path.dirname: C:\Temp

    # Merging path compoments
    print('os.path.join(\'tmp\', \'data\', \'b.txt\'): {}'.format(os.path.join('tmp', 'data', 'b.txt')))
    # os.path.join('tmp', 'data', 'b.txt'): tmp\data\b.txt

    #expanding path to user folder
    path2 = '~/Data/data.csv'
    print('os.path.expanduser(path2): {}'.format(os.path.expanduser(path2)))
    # os.path.expanduser(path2): C:\Users\Adam/Data/data.csv

    # get file extension
    print('os.path.splitext(path2): {}'.format(os.path.splitext(path2)))
    # os.path.splitext(path2): ('~/Data/data', '.csv')

    # check if file/folder exists
    print('os.path.exists(path): {}'.format(os.path.exists(path)))
    # os.path.exists(path): True

    # check if it is a file
    print('os.path.isfile({0}): {1}'.format(path, os.path.isfile(path)))
    print('os.path.isfile({0}): {1}'.format(path_with_file, os.path.isfile(path_with_file)))

    # check if it is a folder
    print('os.path.isdir({0}): {1}'.format(path, os.path.isdir(path)))
    print('os.path.isdir({0}): {1}'.format(path_with_file, os.path.isdir(path_with_file)))

    # get a real file path: for python3 return /usr/local/bin/python3.3
    #file = os.path.realpath(path_with_file)
    # with open(file) as f:
    #     print(f.read())

    # get file size
    print('os.path.getsize(path_with_file): {}B'.format(os.path.getsize(path_with_file)))

    # get last modified time
    timestamp = os.path.getmtime(path_with_file)
    print('os.path.getmtime(path_with_file): {}'.format(time.ctime(timestamp)))

    # Show unmodified list of folder contents: its files and subfolders (non recursive only first path
    root_path = 'C:\Temp'
    print('os.listdir(path): {}'.format(os.listdir(root_path)))
    # os.listdir(path): ['a.txt', 'Encoding Time.csv', 'mytempfp41hrvj.txt', 'tmp']

    # show only files
    files = [name for name in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, name))]
    print('files: {}'.format(files))
    # files: ['a.txt', 'Encoding Time.csv', 'mytempfp41hrvj.txt']

    # show only .csv files
    files = [name for name in os.listdir(root_path) if name.endswith('.csv')]
    print('csv files filtered: {}'.format(files))
    # files: ['Encoding Time.csv']

    # show only folders
    folders = [name for name in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, name))]
    print('folders: {}'.format(folders))
    # folders: ['tmp']
    print('files: {}'.format(files))

    files = glob.glob(root_path+'\*.csv')
    print('csv files filtered with glob: {}'.format(files))
    # csv files filtered with glob: ['C:\\Temp\\Encoding Time.csv']

    from fnmatch import fnmatch
    files = [name for name in os.listdir(root_path)
             if fnmatch(name, '*.csv')]
    print('csv files filtered with fnmatch: {}'.format(files))
    # csv files filtered with glob: ['Encoding Time.csv']

    #export_to_file(root_path)
    export_to_file('D:\\')

