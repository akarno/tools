import os
from temp_files import NamedTemporaryFile






if __name__ == '__main__':
    file = NamedTemporaryFile('w+t', prefix='temp_file_', suffix='.csv') # dir=dir, delete=False)
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