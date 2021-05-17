Webtrap-2
Test task

Задание.

Задание. Разработать простейшее вэб-приложение (раз уж проект будет на Django, то и решение ожидаем на нём) и выложить качестве git-репозитория для оценки.

Две страницы:
а) Главная (url /) с простой формой с 1 полем для ввода e-mail и кнопкой Отправить, форму снабдить csrf-токеном, для защиты от подделки

б) /api — для обслуживания API запросов. Дабы не усложнять, пускай, защиты csrf не нужно, параметры мы будет передавать в стиле GET-запроса, типа localhost:8080/api?method=ping, но тем не менее на запросы GET представление (view) отвечает ошибкой 404, а на POST запрос отвечает 200 в случае если есть GET-параметр method равен ping, иначе отвечает 400. Содержимое ответа не важно, можно пустым возвращать

в) обращения к страницам логгировать (можно в консоль или в файл). Информацию о запросе представить словарём вида {time: <время обращения>, url: <собственно url страницы>, method: <POST/GET>, status: <число статус ответа которое мы вернули>, params: <переданные нам параметры, для / это переданный email, для api — переданные параметры строкой без ?>}

Реализация.

Так как в бункте б) всеравно используется метод post, джанго отказался у меня работать без csrf токена, пришлось использовать.

Для логирования использую простой и удобный loguru.

Все необходимые зависимости в requirements.txt.

Так как в веб-форме испольузется всего 1 поле, и никакой дополнительной валидации, то использовал хтмл форму вместо форм джанго.
