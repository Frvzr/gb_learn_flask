# Используем базовый образ Python
FROM python:3.8.10-buster

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в рабочую директорию
COPY . .

EXPOSE 5000

# Задаем переменную окружения FLASK_APP и указываем файл, содержащий приложение Flask
#ENV FLASK_APP=blog/app.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]