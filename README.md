# Automated Testing for Effective-Mobile

UI тесты для главной страницы [effective-mobile.ru](https://effective-mobile.ru/) с использованием Python, Selenium и Allure.

## Быстрый запуск

### Docker (рекомендуется)

```bash

# 1. Скачайте проект и перейдите в папку (используйте терминал)
git clone https://github.com/vazhgin/testeffmobile.git

cd testask

# 2. Соберите Docker билд
docker build -t effective-tests .

# 3. Запустите тесты
docker run effective-tests