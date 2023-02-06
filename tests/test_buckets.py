from tests.context import utils


class MockDirEntry:
    def __init__(self, name, dir):
        self.name = name
        self.dir = dir

    def is_dir(self):
        return self.dir


def test_separate_by_number(mocker):
    mocker.patch("os.scandir", return_value=[])
    assert utils.separate_by_number(0) == {}


def test_separate_by_number_2(mocker):
    mocker.patch("os.scandir", return_value=[
        MockDirEntry("file1", False),
        MockDirEntry("file2", False)
    ])
    expected_files_dic = {0: ["file1"],
                          1: ["file2"]}

    assert utils.separate_by_number(1) == expected_files_dic
