## 📊 Status Veckouppgift 5 BDD


Här nedan presenteras en översikt över statusen på lösande av uppgfterna.

| Uppgift                 | Status |
|:------------------------|:------:|
| 1. Temperaturomvandling |   🟢   |
| 2. Lagerhållning        |   🟢   |
| 3. Bankkonto            |   🟢   |
| 4. Bibliotek            |   🟢   |


## 1️⃣ Temperaturomvandling
Skriv tester med BDD för funktioner som omvandlar temperaturer från Fahrenheit till Celsius och tvärtom.   
Exempel på testfall:
- Givet temperaturen 32°F, ska funktionen svara 0°C
- Givet temperaturen 100°C, ska funktionen svara 212°F

### Lösning
För att köra testerna:
````python
behave --tags=@temperatur --no-skipped --format=plain
````
 

## 2️⃣ Lagerhållning
Skriv tester med BDD för ett lagerhanteringssystem.   
Testa att:
- Det går att lägga till en valfri produkt: namn och antal är korrekt
- Det går att minska antalet av en specifik produkt

### Lösning
För att köra testerna:
````python
behave --tags=@lager --no-skipped --format=plain
````

## 3️⃣ Bankkonto
Skriv tester med BDD för ett bankkonto:  
- skapa nytt konto - saldot är noll
- sätta in pengar
- ta ut pengar
- applicera 5% ränta
- överföra pengar mellan två konton

### Lösning
För att köra testerna:
````python
behave --tags=@bank --no-skipped --format=plain
````


## 4️⃣ Bibliotek
Skriv tester med BDD för ett biblioteksystem, där man kan:  
- söka efter böcker baserat på titel 
- söka efter böcker baserat på författare
- låna en bok
- lämna tillbaka en bok
- kontrollera om en viss bok är utlånad eller inte

### Lösning
Scenarios är samma som ovan krav  

För att köra testerna:
````python
behave --tags=@library --no-skipped --format=plain
````

Notera 1:  
I "environment.py" instansieras ett Library objekt som ett "before" scenario. Objektet lagras 
i context och blir tillgängliogt för samtliga tester.
````python
def before_scenario(context, scenario):
    """
    Adds a library object to context
    """
    context.library = Library().
````

Exempel:
````python
# Borrow a book with given title
@given(u'att "{title}" är utlånad')
def step_bok_ar_utlanad(context, title):
    context.library.borrow_book(title)
````

Notera 2:  
Böckerna i biblioteket läggs till i en tabell i feature-filen. De skapas med en "background" tagg 
och används som en "given" för alla tester. 
````python
  Background:
    Given att biblioteket har följande böcker
        | title                         | author    |
        | Sagan om ringen               | Tolkien   |
        | Stiftelsen och imperiet       | Asimov    |
        | 2001: En rymdodyssé           | Clarke    |
        | Liftarens guide till galaxen  | Adams     |
````
I step-filen skapas en inledande "given" som läser in böckerna i tabellen till bibliotekets 
boklista i klassen Library.
````python
# populate the library with the books
@given(u'att biblioteket har följande böcker')
def step_populera_biblioteket(context):
    for row in context.table:
        title = row["title"]
        author = row["author"]
        book = Book(title=title, author=author)
        context.library.add_book(book)
´´´´