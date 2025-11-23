# Практическая пошаговая инструкция: Git + Python (учебный репозиторий)

Цель: создать локальный репозиторий, добавить маленькую Python-минипрограмму `main.py`, зафиксировать шаги в Git и записать результаты в `report_basic_git.md`. Инструкция ориентирована на Windows `cmd` (новичок-friendly): теоретическое пояснение — вне блоков кода, команды — внутри ```cmd```.

---

**Требования:** установленный Git (Windows) и Python 3.x.

**Файлы, которые будут созданы:** `README.md`, `main.py`, `.gitignore`, `report_basic_git.md` (шаблон уже есть в репозитории), и сам Git-репозиторий.

---

## 1) Создать рабочую папку и перейти в неё
Пояснение: создаём новую папку для практики и переходим в неё; используйте `cd /d` чтобы переключить диск, если нужно.
```cmd
mkdir "%USERPROFILE%\Desktop\git-practice-tutorial"
cd /d "%USERPROFILE%\Desktop\git-practice-tutorial"
```

Повтори сам: замените путь на свою удобную папку и выполните те же команды.

---

## 2) Инициализировать пустой репозиторий Git
Пояснение: `git init` создаёт скрытую папку `.git` и делает текущую папку репозиторием.
```cmd
C:\path\to\your\repo>git init
```

Пояснение: если Git ещё не знает ваше имя/email — задайте их глобально (выполните один раз):
```cmd
C:\path\to\your\repo>git config --global user.name "Ваше Имя"
C:\path\to\your\repo>git config --global user.email "you@example.com"
```

---

## 3) Создать файлы проекта
Пояснение: создадим `README.md`, `.gitignore` и `main.py` (минипрограмма). Содержимое `main.py` — минимально, чтобы можно было запускать и изменять.

Пояснение: `echo` используется для быстрого создания простых файлов; для создания `main.py` лучше открыть редактор и вставить код, но ниже — пример создания через `cmd` и отдельный блок с полноценным кодом.

```cmd
C:\path\to\your\repo>echo # Git + Python Tutorial > README.md
C:\path\to\your\repo>echo __pycache__/ > .gitignore
```

Пояснение: создаём `main.py` — ниже полный код (копируйте в редактор и сохраните как `main.py`).

```python
# main.py
# Мини-программа: вычисляет "оценку" по списку чисел и демонстрирует изменение и коммит
# Функция calculate_score берёт список чисел и возвращает среднее и максимальное значение

def calculate_score(values):
    if not values:
        return {"count": 0, "avg": 0, "max": None}
    count = len(values)
    avg = sum(values) / count
    return {"count": count, "avg": round(avg, 2), "max": max(values)}

if __name__ == "__main__":
    sample = [10, 7, 9, 8, 10]
    result = calculate_score(sample)
    print("Input:", sample)
    print("Result:", result)
```

Повтори сам: запустите программу командой `python main.py` и проверьте вывод.

```cmd
C:\path\to\your\repo>python main.py
```

---

## 4) Добавить файлы в индекс и сделать первый коммит
Пояснение: `git add` помещает файлы в staging area; `git commit -m` создаёт коммит с указанным сообщением (используйте `-m`, чтобы не открывался редактор).

```cmd
C:\path\to\your\repo>git add README.md main.py .gitignore
C:\path\to\your\repo>git commit -m "Initial commit: add main.py, README and .gitignore"
```

Пояснение: проверьте краткую историю коммитов командой `git log --oneline`.

```cmd
C:\path\to\your\repo>git log --oneline
```

---

## 5) Внести простые изменения и закоммитить их (демонстрация истории)
Пояснение: добавим в код одну строку или поменяем sample, затем снова добавим и закоммитим изменения, чтобы в истории было как минимум 2 коммита.

```cmd
C:\path\to\your\repo>echo "# Дополнение в README" >> README.md
C:\path\to\your\repo>git add README.md
C:\path\to\your\repo>git commit -m "Update README: add note"
```

Пояснение: ещё раз проверяем историю.

```cmd
C:\path\to\your\repo>git log --oneline
```

---

## 6) Экспортировать вывод истории в `report_basic_git.md`
Пояснение: шаблон `report_basic_git.md` уже находится в корне репозитория (мы создали его ранее). Здесь покажу конкретные команды, как записать в него последние 5 коммитов и добавить шаблон для группировки по теме.

```cmd
C:\path\to\your\repo>echo ### Последние 5 коммитов (oneline) >> report_basic_git.md
C:\path\to\your\repo>git log --oneline -n 5 >> report_basic_git.md
C:\path\to\your\repo>echo. >> report_basic_git.md
C:\path\to\your\repo>echo ### Группировка по теме >> report_basic_git.md
C:\path\to\your\repo>echo - Настройка: >> report_basic_git.md
C:\path\to\your\repo>echo - Фича: >> report_basic_git.md
C:\path\to\your\repo>echo - Фикс: >> report_basic_git.md
```

Пояснение: откройте `report_basic_git.md` и вручную распределите строки под соответствующие темы (Настройка/Фича/Фикс).

```cmd
C:\path\to\your\repo>notepad report_basic_git.md
```

---

## 7) Дополнительные полезные команды для исследования
Пояснение: быстрые команды, которые помогут при выполнении упражнений из `t1.md`.

- Показать подробный формат (хэш|автор|дата|сообщение):
```cmd
git log -n 10 --pretty=format:"%H | %an | %ad | %s" --date=iso
```

- Показать изменения в `main.py` (патчи):
```cmd
git log -p -- main.py
```

- Суммарный рейтинг авторов:
```cmd
git shortlog -s -n --all
```

---

## 8) Задания "Повтори сам"
- Задание A: инициализируйте репозиторий и сделайте первый коммит; прикрепите вывод `git log --oneline` в `report_basic_git.md`.
- Задание B: внесите небольшое изменение в `main.py` (например, измените sample или добавьте новую строку вывода), закоммитьте, получите `git log --oneline -n 5` и распределите 5 последних коммитов по категориям в `report_basic_git.md`.
- Задание C: используйте `git log -p -- main.py` и приложите краткий анализ изменений в `report_8.md`.

---

## 9) Советы и отладка (Windows)
- Если `git commit` открывает редактор — используйте `-m "сообщение"` чтобы избежать этого.
- Для переключения диска используйте `cd /d "C:\path\to\folder"`.
- Если файл не отображается в `git status`, убедитесь, что он не в `.gitignore`.

---

## 10) Что дальше (опционально)
- Могу автоматически сгенерировать готовую структуру репозитория `git-practice-tutorial` прямо в рабочей папке (создать файлы и сделать коммиты) — это будет имитация локальной работы (внесу файлы в рабочее дерево репозитория, но НЕ буду запускать `git` на вашей машине). Согласовать? 
- Могу создать `export_reports.ps1` для автоматического сбора кратких отчётов (read-only экспорт).

---

Файл создан на основе материалов `t1.md` и `report_basic_git.md` и следует формату: пояснения вне блоков, примеры команд — в `cmd` блоках, код Python — в `python` блоке. Уточните, нужно ли автоматически сгенерировать репозиторий и коммиты прямо в этом рабочем каталоге (я подготовлю файлы и дам команды, которые вы выполните локально), или достаточно этой инструкции.
