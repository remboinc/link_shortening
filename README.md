# link_shortening.py
Программа сокращает ссылки, которые вводит пользователь при помощи API bit.ly. 

Скрипт предлагает пользователю ввести ссылку, затем проверяет введенные им данные. 

Если введена длинная ссылка, программа ее сокращает. Если введенная ссылка - это битлинк, то программа выводит количество переходов по ней.

Если пользоатель ввел не ссылку, программа выдаст ошибку.

## Как установить
Чтобы Bitly отдал данные, получите токен. Он нужен для взаимодействия с API Bitly.

Вот пример токена: 

    17c09e20ad155405123ac1977542fecf00231da7
        
Чтобы получить токен, зарегестрируйтесь [на сайте](https://bitly.com/a/sign_in?rd=/a/oauth_apps) и сгенерируйте токен, следуя инструкции.
Затем создайте файл .env и вставьте в него следующую строку:

    BITLINK_TOKEN = '17c09e20ad155405123ac1977542fecf00231da7'


Для запуска вам понадобится Python3. Установите зависимости при помощи команды:

    pip install -r requirements.txt
    
Рекомендуется использовать [virtualenv](https://pypi.org/project/virtualenv/) для изоляции проекта.
## Пример запуска скрипта
Если все шаги выполенны верно, работа программы будет выглядеть так:

    Введите url: https://dvmn.org/encyclopedia/team-projects/tutorial_readme/
    Битлинк https://bit.ly/3xRW8ry
       
или

    Введите url: https://bit.ly/3xRW8ry
    По ссылке переходили 0 раз 
       
## Цель проекта
Скрипт написан как учебный проект.

