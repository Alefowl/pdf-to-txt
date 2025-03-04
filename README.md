## Pdf в txt конвертер.

Программа преобразует pdf файл в txt файл. Автоматически выделяет абзацы и главы.
Удаляет символы переноса и числа, так же заменяет {} и [] на ().

#### Зависимости
- Python 3.11^
- Библиотека: `pymupdf`


#### Аргументы командной строки.

- `-filename (-F)` : Путь к файлу pdf (Обязательно).
- `-output (-O)`   : Имя файла txt. (По умолчанию: 'output.txt').
- `-upper (-U)`    : Разница в символах между концом и началом абзац. (По умолчанию: 25).
- `-lcut (-L)`     : Страницы в начале файла исключенные из преобразования (Пример: Обложка и тп.).
- `-hcut (-H)`     : Страницы в конце файла исключенные из преобразвония (Пример: Обложка, данные об издательстве и тп.).
- `-nums (-N)`     : Флаг для удаления всех чисел из текста. (По умолчанию: False).
- `-braces (-B)`   : Флаг для замены скобок [], {} на () (По умолчанию: False).
- `-ligatures (-L)`: Заменяет лигатуры. (По умолчанию: True).
- `-align (-A)`    : Выравнивает текст по указанному краю. C - центр, R - право, L - лево, J - авто (По умолчанию: J).
- `-dehy  (-D)`    : Удаляет символ переноса. (По умолчанию: False)


#### Example

```bash
python main.py -filename input.pdf -upper 20 -lcut 3 -hcut 200 -braces true
```

#### Пояснение:

* upper 20 -> Разница между последней строчкой в абзаце и началом нового абзаца.
```
Los alimentos y vestidos que consume el trabajador, los edificios en que 
trabaja y los útiles de que se vale son cosas perecederas por naturaleza. Hay, 
sin embargo, una diferencia grande en cuanto a la duración de estos diversos 
capitales; una máquin;~. de vapor durará más que un buque; un buque más que 
el traje del trabajador, y el traje, más que el alimento que consume. 
Según que el capital se consuma rápidamente y deba ser repuesto con fre-
cuencia, o sea de desgaste lento, se le denomina circulante o fijo4• Se dice que 
un fabricante de cerveza emplea una gran parte de capital fijo, porque sus edi-
ficios y maquinarias son costosos y duraderos; por el contrario, de un zapate-
ro, cuyo capital se emplea principalmente en pagar salarios, que son gastados 
en alimentos y vestidos, bienes consumibles más rápidamente que los edifi-
cios y las máquinas, se dice que emplea la mayor parte de su capital en capi-
tal circulante.
---  15 символов

--- 74 символа
Ha de observarse también que el capital circulante puede circular, o vol-
ver a su poseedor, en plazos muy desiguales. El cereal comprado por un la-
brador para sembrarlo es un capital fijo, comparado con el cereal adquirido 
por un panadero para transformarlo en pan. Uno lo deja en la tierra y no pue-
de obtener remuneración alguna durante un año; el otro puede molerlo para 
hacer harina, venderlo luego como pan a sus clientes y tener de nuevo su ca-
pital disponible al cabo de una semana, para renovar la misma producción o 
comenzar otra cualquiera. 
```
В данном случае upper = 20 подходит, так как upper <= 20

* -lcut 3

Первые три страницы pdf файла не будут конвертированны.

* -hcut 200

Все страницы после 200 не будут конвертированны.


#### Как использовать

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

**Note:** Убедитесь в том что правильно указали путь до файла. Файл pdf должен содержать текст.



4. Если все ещё есть переносы строки воспользуйтесь dehy.py

#### Аргументы командной строки.

- `-filename` : Путь к файлу pdf (Обязательно).
- `-pattern`  : Паттерн переноса.

Пример:

```
Hello Wo-\n
rld
```

```python dehy.py -filename output.txt -pattern '-\n'```

```
Hello Wo- \n
rld
```

```python dehy.py -filename output.txt -pattern '- \n'```


***

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

#### 2. Неправильная разметка глав и абзацев.

Можно частично решить настраивая параметр ```-upper```, проблема в том для распознавания конца и начала абзаца используется эвристический метод, основанный на формальное отличие конца абзаца от его начала.
То же самое относительно названия глав. В самом pdf файле нет кого либо способа получить эту информацию.

#### 3. Не все переносы текста удаляются.
Это связано с тем что не все переносы имееют вид: ```text-\ntext```  
