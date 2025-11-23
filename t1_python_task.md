# Практическое задание: Python-файл — создать, закоммитить, изменить и снова закоммитить

Цель: научиться создавать небольшой Python-файл, фиксировать изменения в Git, затем внести улучшение (дописать условие) и снова закоммитить — после этого ученик сам подсчитает, сколько коммитов получилось за занятие.

Важно: в тексте инструкции мы не указываем, что это будет именно "второй" коммит — ученику нужно самому посчитать количество коммитов в конце.

---

Требования: установлен Python 3.x и Git. Работаем в `cmd`/PowerShell под Windows; пояснения — вне блоков кода, команды — внутри ```cmd```.

## Шаг 1 — создаём рабочую папку и инициализируем репозиторий
Пояснение: создаём отдельную папку для упражнения и инициализируем Git.
```cmd
mkdir "%USERPROFILE%\Desktop\git-python-exercise"
cd /d "%USERPROFILE%\Desktop\git-python-exercise"
C:\path\to\your\repo>git init
```

Пояснение: при необходимости задайте своё имя и email (делается один раз):
```cmd
C:\path\to\your\repo>git config --global user.name "Ваше Имя"
C:\path\to\your\repo>git config --global user.email "you@example.com"
```

---

## Шаг 2 — создаём простой Python-файл (первый вариант)
Пояснение: ниже — аккуратный, понятный код для новичков. Скопируйте его в редактор и сохраните как `exercise.py`.

```python
# exercise.py
# Программа для новичков: проверяет число и выводит базовую информацию

def analyze_number(n):
    """Возвращает словарь с простой информацией о числе."""
    if n > 0:
        sign = "positive"
    else:
        sign = "non-positive"
    return {"value": n, "sign": sign}

if __name__ == "__main__":
    sample = 5
    info = analyze_number(sample)
    print("Input:", sample)
    print("Info:", info)
```

Пояснение: запустите программу, чтобы убедиться, что она работает.
```cmd
C:\path\to\your\repo>python exercise.py
```

---

## Шаг 3 — добавляем файл в индекс и делаем коммит (фиксируем состояние)
Пояснение: `git add` — помещает файл в индекс; `git commit -m` — создает коммит с сообщением (флаг `-m` позволяет не открывать редактор).
```cmd
C:\path\to\your\repo>git add exercise.py
C:\path\to\your\repo>git commit -m "Add exercise.py: initial version"
```

Пояснение: проверьте историю кратко:
```cmd
C:\path\to\your\repo>git log --oneline -n 5
```

---

## Шаг 4 — внести изменение: добавить новое условие в `exercise.py`
Пояснение: внесите изменение в код — добавьте проверку на чётность/нечётность и расширьте вывод (это делает программу лучше). Скопируйте и замените содержимое `exercise.py` на код ниже.

```python
# exercise.py
# Улучшенная версия: добавлена проверка чётности/нечётности

def analyze_number(n):
    """Возвращает словарь с информацией о числе: знак и чётность."""
    if n > 0:
        sign = "positive"
    else:
        sign = "non-positive"

    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    return {"value": n, "sign": sign, "parity": parity}

if __name__ == "__main__":
    sample = 6
    info = analyze_number(sample)
    print("Input:", sample)
    print("Info:", info)
```

Пояснение: после сохранения файла выполните программу для теста:
```cmd
C:\path\to\your\repo>python exercise.py
```

---

## Шаг 5 — зафиксировать изменение (сделать ещё один коммит)
Пояснение: снова добавляем изменённый файл в индекс и выполняем коммит с осмысленным сообщением.
```cmd
C:\path\to\your\repo>git add exercise.py
C:\path\to\your\repo>git commit -m "Enhance exercise: add parity check"
```

Пояснение: проверьте историю коротко — ученик должен сам посчитать, сколько коммитов получилось в репозитории после выполнения всех шагов.
```cmd
C:\path\to\your\repo>git log --oneline
```

---

## Шаг 6 — записать результаты в `report_basic_git.md`
Пояснение: добавьте в `report_basic_git.md` раздел с выводом `git log --oneline` и своими наблюдениями (сколько коммитов и краткие выводы).
```cmd
C:\path\to\your\repo>echo ### Exercise: git log output >> report_basic_git.md
C:\path\to\your\repo>git log --oneline -n 10 >> report_basic_git.md
C:\path\to\your\repo>echo. >> report_basic_git.md
C:\path\to\your\repo>echo ### Наблюдения: >> report_basic_git.md
C:\path\to\your\repo>echo - Сколько коммитов в проекте (впишите число): >> report_basic_git.md
C:\path\to\your\repo>echo - Краткие выводы: >> report_basic_git.md
```

Пояснение: откройте `report_basic_git.md` и заполните ответы.
```cmd
C:\path\to\your\repo>notepad report_basic_git.md
```

---

## Подсказки для преподавателя (не показывать ученику)
- Не сообщайте ученику, что он выполняет именно второй коммит — формулируйте как "сделайте ещё один коммит после изменения".
- Убедитесь, что ученик использует `git log --oneline` самостоятельно, чтобы посчитать количество коммитов.

---

## Повтори сам
- Выполни все шаги от 1 до 5.
- Затем выполни `git log --oneline` и посчитай, сколько коммитов получилось; запиши число и краткое наблюдение в `report_basic_git.md`.

