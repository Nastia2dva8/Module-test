import pytest
from main_module import count_words_and_sentences

# Фікстура для створення тимчасового файлу
@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test.txt"
    return file_path

# Тест з параметризацією
@pytest.mark.parametrize("content, expected_words, expected_sentences", [
    ("Hello, world! How are you?", 5, 2),
    ("Test... Another test.", 4, 2),
    ("Simple text: with separators", 4, 1),
    ("", 0, 0),  # Порожній файл
])
def test_count_words_and_sentences(temp_file, content, expected_words, expected_sentences):
    # Записуємо вміст у тимчасовий файл
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Викликаємо функцію
    result = count_words_and_sentences(temp_file)
    
    # Перевіряємо результат
    assert result['word_count'] == expected_words
    assert result['sentence_count'] == expected_sentences

# Тест для неіснуючого файлу
def test_file_not_found(temp_file):
    non_existent_file = temp_file.with_name("non_existent.txt")
    result = count_words_and_sentences(non_existent_file)
    assert result == "Файл не знайдено"