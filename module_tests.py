import pytest
from main_module import count_words_and_sentences

# Фікстура для створення тимчасового файлу
@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test.txt"
    return file_path

