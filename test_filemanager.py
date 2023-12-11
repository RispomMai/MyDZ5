from functions_file_manager import *
from console_games.game_count import *
from console_games.game_victorina import *
def test_read_write_count():
    write_count('test.bin',999)
    assert read_count('test.bin') == 999
    write_count('test.bin', 0)
    assert read_count('test.bin') == 0
    os.remove('test.bin')

def test_read_write_history():
    write_history('test1.txt', ('90','90','90'))
    assert read_history('test1.txt') == ['90','90','90']
    os.remove('test1.txt')

def test_add_count():
    assert add_count(300,500) == 800
    assert add_count(0, 500) == 500
    assert add_count(300, 0) == 300

def test_separate():
    assert  separate(['1','2','3','4','5'],2,[1,2,3,4]) != 0
    assert set(separate(['1','2','3','4','5'],2,[1,2,3,4])).issubset(['1','2','3','4','5'])

def test_list_dir():
    if os.path.exists('testdir') :
        shutil.rmtree('testdir')
    os.mkdir('testdir')
    os.chdir('testdir')
    assert list(list_dir('dir')) == []
    assert list(list_dir('file')) == []
    file = os.open('test.txt', os.O_CREAT)
    os.close(file)
    assert list(list_dir('file')) == ['test.txt']
    os.chdir('..')
    shutil.rmtree('testdir')

def test_del_dir_file():
    if os.path.exists('testdir'):
        shutil.rmtree('testdir')
    os.mkdir('testdir')
    assert del_dir_file('testdir') == True
    assert del_dir_file('testdi') == False
    assert del_dir_file('test.txt') == False



