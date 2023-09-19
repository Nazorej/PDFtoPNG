# Это программа на Python
# Импортируем модули
import sqlite3

# Создание соединения с базой данных SQLite
conn = sqlite3.connect('settings.db')
c = conn.cursor()

# Создание таблицы settings, если она не существует
c.execute('''
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY,
        pdf_path TEXT,
        output_folder TEXT,
        poppler_path TEXT,
        first_page INTEGER,
        last_page INTEGER,
        output_file_prefix TEXT,
        output_file_suffix TEXT,
        file_format TEXT
    )
''')

# Вставка настроек в таблицу settings
c.execute('''
    INSERT INTO settings (pdf_path, output_folder, poppler_path, first_page, last_page, output_file_prefix, output_file_suffix, file_format)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', ('your-pdf.pdf', 'output-folder', 'D:/Release-23.08.0-0/poppler-23.08.0/Library/bin', 1, 10, 'output-', '.png', 'PNG'))

# Сохранение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()
