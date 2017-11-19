# Making temporary folders and files
from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile, gettempdir


def test_temp_files_1():
    with TemporaryFile('w+t') as f:
        f.write('Hello \n')
        f.write('Test')
        # Go back to first line
        f.seek(0)
        data = f.read()
        print(data)


def test_temp_files_2():
    f = TemporaryFile('w+t')
    f.write('Hello \n')
    f.write('Test2')
    # Go back to first line
    f.seek(0)
    data = f.read()
    print(data)
    #f.close not needed


def test_named_temp_files_1():
    with NamedTemporaryFile('w+t') as f:
        print('Filename is {}'.format(f.name))


def test_named_temp_files_2(prefix='mytemp', suffix='.txt', dir='C:\Temp'):
    with NamedTemporaryFile('w+t', prefix=prefix, suffix=suffix, dir=dir, delete=False) as f:
        print('Filename is {}'.format(f.name))


def test_dictionary():
    with TemporaryDirectory() as dirname:
        print('Dirname is {}'.format(dirname))


if __name__ == '__main__':
    # test_temp_files_1()
    # test_temp_files_2()
    # test_named_temp_files_1()
    test_named_temp_files_2()
    test_dictionary()
    print('Default temp path: {}'.format(gettempdir()))