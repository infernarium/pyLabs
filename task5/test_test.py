import pytest
import main as Task
import split_module as split

def testfilefound():
    with pytest.raises(FileNotFoundError):
        assert Task.read_data_from_file('file1.csv')

def testfilepermission():
    with pytest.raises(PermissionError):
        assert Task.read_data_from_file('txt_noread.csv')

def testcodefail():
    with pytest.raises(UnicodeDecodeError):
        assert Task.read_data_from_file('file.o')

def testonecolumn():
    z = Task.read_data_from_file('one.csv')
    with pytest.raises(IndexError):
        assert split.split_data(z, 1)

def testdatatype():
    z = Task.read_data_from_file('type.csv')
    with pytest.raises(ValueError):
        assert split.split_data(z, 1)

def testsplittime():
    z = Task.read_data_from_file('spt.csv')
    assert split.split_data(z, 5) == [[[1,6],[2,3]],[[6,10]],[[15,7]]]

def teststatistics():
    z = Task.read_data_from_file('spt.csv')
    x = split.split_data(z, 5)
    t = Task.calculate_statistics(x[0])
    assert t == [2, 4.5, 6, 4.5]




