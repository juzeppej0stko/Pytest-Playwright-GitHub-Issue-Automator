# 🚀 Pytest-Playwright-GitHub-Issue-Automator 🚀

## 📚 Дополнительная информация
Этот проект был разработан с целью демонстрации навыков для потенциального работодателя.

## 📝 Описание
Проект представляет собой автоматизированные тесты для GitHub с использованием Playwright и Pytest. Он включает в себя тесты API и веб-тесты. Важной особенностью этого проекта является использование модели Page Object для организации структуры тестов.
Проект разработан для автоматизации процесса создания и проверки issue на GitHub. Он включает в себя функции для создания issue через API и веб-интерфейс, а также для проверки созданных issue.

## 🛠️ Установка
Для установки зависимостей проекта выполните следующую команду:
```bash
pip install -r requirements.txt
```
## 🏃 Использование
Для запуска тестов выполните следующую команду:
```bash
pytest
```
## 📁 Файлы
- github_page.py: Определяет класс GitHubPage, который использует модель Page Object для взаимодействия с GitHub через API и веб-интерфейс. Этот класс включает в себя методы для создания issue, проверки первого issue в списке, входа в систему на веб-сайте GitHub, создания и проверки issue через веб-интерфейс и API, получения issue через API и проверки issue через API.
- test_api.py: Содержит тесты API для создания отчетов об ошибках и запросов на функции. Эти тесты используют методы из класса GitHubPage для создания issue и проверки созданных issue.
- test_api_and_website.py: Содержит веб-тесты, которые проверяют, что последний созданный issue является первым в списке, и что последний созданный issue присутствует на сервере. Эти тесты также используют методы из класса GitHubPage.
- conftest.py: Содержит фикстуры pytest для настройки и завершения работы, а также для создания контекста запроса API. Этот файл также включает в себя фикстуры для создания и удаления тестового репозитория на GitHub.
