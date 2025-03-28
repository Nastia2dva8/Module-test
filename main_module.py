def count_words_and_sentences(filename):
    try:
        # Відкриваємо файл для читання
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Символи, що позначають кінець речення
        sentence_endings = {'.', '!', '?', '...'}
        
        # Символи-розділювачі для слів
        separators = {',', ' ', ':', ';', '\n'}
        
        # Підрахунок речень
        sentences = 0
        i = 0
        while i < len(text):
            if text[i] == '.' and i + 2 < len(text) and text[i:i+3] == '...':
                sentences += 1
                i += 3
            elif text[i] in sentence_endings:
                sentences += 1
                i += 1
            else:
                i += 1
                
        # Розділяємо текст на слова
        current_word = ''
        words = []
        
        for char in text:
            if char in separators:
                if current_word:
                    words.append(current_word)
                    print(current_word)
                    current_word = ''
            else:
                current_word += char
        
        # Додаємо останнє слово, якщо воно є
        if current_word:
            words.append(current_word)
            print(current_word)
            
        # Повертаємо результат
        return {
            'word_count': len(words),
            'sentence_count': sentences
        }
    
    except FileNotFoundError:
        return "Файл не знайдено"
    except Exception as e:
        return f"Сталася помилка: {str(e)}"

# Приклад використання
filename = "example.txt"
result = count_words_and_sentences(filename)

if isinstance(result, dict):
    print(f"Кількість слів: {result['word_count']}")
    print(f"Кількість речень: {result['sentence_count']}")
else:
    print(result)