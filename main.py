# Это программа на Python
# Конвертер из PDF в PNG
# https://github.com/oschwartz10612/poppler-windows

# Импортируем модули
from pdf2image import convert_from_path
import os
import sqlite3

def convert_pdf_to_png():
    # Повторное открытие соединения с базой данных для чтения настроек
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()

    # Чтение настроек из таблицы settings
    c.execute('SELECT * FROM settings ORDER BY id DESC LIMIT 1')
    settings = c.fetchone()

    # Закрытие соединения с базой данных
    conn.close()

    # Извлечение настроек из записи в базе данных
    pdf_path, output_folder, poppler_path, first_page, last_page, output_file_prefix, output_file_suffix, file_format = settings[1:]

    # Создание папки для вывода, если она не существует
    os.makedirs(output_folder, exist_ok=True)

    # Конвертирование PDF в список изображений
    images = convert_from_path(pdf_path, poppler_path=poppler_path, first_page=first_page, last_page=last_page)

    for i, image in enumerate(images, start=first_page):
        # Сохранение изображений в выбранном формате
        image.save(f'{output_folder}/{output_file_prefix}{i}{output_file_suffix}', file_format)

# Пример использования функции
convert_pdf_to_png()
