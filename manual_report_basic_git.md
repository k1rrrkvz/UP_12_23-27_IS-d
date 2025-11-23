# Report: Basic Git

Цель: записать вывод команд, подтверждающий выполнение задания «Первое знакомство с проектом».

Формат файла: используйте заголовки и блоки кода. Сохраняйте в корне репозитория (`C:\path\to\your\repo\report_basic_git.md`).

---

## Что нужно сохранить

- Краткое описание проделанных шагов (1–2 предложения).
- Вывод команды `git log` (несколько строк — 8–10 для обзора).
- Ответы на вопросы задания:
  - Сколько всего коммитов в проекте?
  - Кто основной автор коммитов?
  - Какая общая тематика сообщений коммитов (фичи / багфиксы / рефакторинг)?

---

## Автоматический способ (Windows `cmd`)

Эти команды создадут или перезапишут `report_basic_git.md` в текущей папке и добавят в него структурированный вывод.

```cmd
REM Создать заголовок отчёта (перезаписывает файл)
echo ## Отчёт по базовой задаче > report_basic_git.md

echo. >> report_basic_git.md
REM Добавить краткое описание (замените текст на своё)
echo Выполнил(а) обзор истории репозитория, экспорт последних коммитов. >> report_basic_git.md

echo. >> report_basic_git.md
REM Раздел: компактная история (oneline)
echo ### Последние 10 коммитов (oneline) >> report_basic_git.md
git log --oneline -n 10 >> report_basic_git.md

echo. >> report_basic_git.md
REM Раздел: подробный экспорт (hash|author|date|subject)
echo ### Экспорт 10 последних коммитов (hash|author|date|subject) >> report_basic_git.md
git log -n 10 --pretty=format:"%H | %an | %ad | %s" --date=iso >> report_basic_git.md

echo. >> report_basic_git.md
REM Раздел: ответы на вопросы (вы заполните вручную)
echo ### Ответы на вопросы: >> report_basic_git.md
echo 1) Всего коммитов: [вставьте число] >> report_basic_git.md
echo 2) Основной автор: [вставьте имя] >> report_basic_git.md
echo 3) Тематика сообщений: [короткое описание] >> report_basic_git.md
```

Примечание: команды `echo.` добавляют пустую строку для читаемости. Если вы выполняете эти команды в другом каталоге — используйте полный путь к `report_basic_git.md`.

---

## Альтернатива — PowerShell (рекомендую, если нужен точный контроль и кодировка UTF-8)

```powershell
# Создать/перезаписать файл и записать заголовок
"## Отчёт по базовой задаче" | Out-File -FilePath report_basic_git.md -Encoding utf8
"" | Out-File -FilePath report_basic_git.md -Append -Encoding utf8
"Выполнил(а) обзор истории репозитория, экспорт последних коммитов." | Out-File -FilePath report_basic_git.md -Append -Encoding utf8

"" | Out-File -FilePath report_basic_git.md -Append -Encoding utf8
"### Последние 10 коммитов (oneline)" | Out-File -FilePath report_basic_git.md -Append -Encoding utf8
git log --oneline -n 10 | Out-File -FilePath report_basic_git.md -Append -Encoding utf8

"" | Out-File -FilePath report_basic_git.md -Append -Encoding utf8
"### Экспорт 10 последних коммитов (hash|author|date|subject)" | Out-File -FilePath report_basic_git.md -Append -Encoding utf8
git log -n 10 --pretty=format:"%H | %an | %ad | %s" --date=iso | Out-File -FilePath report_basic_git.md -Append -Encoding utf8
```

PowerShell сохраняет в UTF-8, что полезно для кириллицы.

---

## Ручной вариант (если хотите скопировать вывод из терминала)

1. Выполните команду в `cmd` или Git Bash:

```cmd
git log --oneline -n 10
```

2. Выделите вывод в окне терминала, скопируйте и вставьте его в `report_basic_git.md` в разделе `### Последние 10 коммитов (oneline)`.

3. Заполните блок ответов на вопросы вручную.

---

## Полезные подсказки

- Если нужно только первые 8–10 строк вывода, используйте `-n 10` в `git log`.
- Для автоматического подсчёта числа коммитов: `git rev-list --count HEAD`.
- Чтобы быстро получить основного автора (по количеству коммитов):

```cmd
git shortlog -s -n --all
```

Скопируйте результат в отчёт и укажите выводы.

---

## Пример содержимого `report_basic_git.md` (короткий пример)

```
## Отчёт по базовой задаче

Выполнил(а) обзор истории репозитория, экспорт последних коммитов.

### Последние 10 коммитов (oneline)
<здесь будет вывод git log --oneline -n 10>

### Экспорт 10 последних коммитов (hash|author|date|subject)
<здесь будет вывод подробного экспорта>

### Ответы на вопросы:
1) Всего коммитов: 42
2) Основной автор: Иван Иванов
3) Тематика сообщений: преимущественно фичи и фикс багов
```

---

Если хотите, могу также:
- сгенерировать `report_1.md`…`report_12.md` с подобным шаблоном для каждого задания, или
- подготовить PowerShell-скрипт `export_reports.ps1`, который автоматически собирает нужные файлы (read-only экспорт).

