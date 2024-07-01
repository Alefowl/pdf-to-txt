## Pdf в txt конвертер.

Программа преобразует pdf файл в txt файл. Автоматически выделяет абзацы и главы.

#### Зависимости
- Python 3.11^
- Библиотека: `pymupdf`


#### Аргументы командной строки.

- `-filename (-F)`: Путь к файлу pdf (Обязательно).
- `-output (-O)`  : Имя файла txt. (По умолчанию: 'output.txt').
- `-symbol (-S)`  : Заменяет символ `NUL` на введённый символ.
- `-upper (-U)`   : Разница в символах между концом и началом абзац. (По умолчанию: 25).
- `-lcut (-L)`    : Страницы в начале файла исключенные из преобразования (Пример: Обложка и тп.).
- `-hcut (-H)`    : Странциы в конце файла исключенные из преобразвония (Пример: Обложка, данные об издательстве и тп.).
- `-nums (-N)`    : Флаг для удаления всех чисел из текста. (По умолчанию: False).
- `-braces (-B)`  : Флаг для замены скобок [], {} на () (По умолчанию: False).

#### Example

```bash
python main.py -filename input.pdf -output output.txt -symbol '##' -upper 20 -lcut 3 -braces true
```

### Как использовать

1. Установить и скачать python 3.11^

2. Клонировать репозиторий.

3. Установать зависимости

* С помощью pip:
<br>

```bash
pip install -r requirements.txt
```


* С помощью poetry:
<br>

```bash
poetry install
```

<br>

3. Запустите программу.

**Note:** Убедитесь в том что правильно указали путь до файла. Файл pdf должен содержать внутри текст.


### Известные баги.

#### 1. Выбросы текста.

Пример:
* В pdf файле:
<br>

``` 
Here comes the sun.
```

* В полученном txt файле:
``` 
Here
comes
the
sum.
```

К сожалению решения данной проблемы нет, не применяя OCR библиотеки.

### 2. Неправильная разметка глав и абзацев.
<br>
Можно частично решить настраивая параметр ```-upper```, проблема в том для распознавания конца и начала абзаца используется эвристический метод, основанный на формальное отличие конца абзаца от его начала.
То же самое относительно названия глав. В самом pdf файле нет кого либо способа получить эту информацию.