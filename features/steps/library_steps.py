from behave import given, when, then
from src.library.book import Book


# ---------- GIVEN ----------

# populate the library with the books
@given(u'att biblioteket har följande böcker')
def step_populera_biblioteket(context):
    for row in context.table:
        title = row["title"]
        author = row["author"]
        book = Book(title=title, author=author)
        context.library.add_book(book)


# Borrow a book with given title
@given(u'att "{title}" är utlånad')
def step_bok_ar_utlanad(context, title):
    context.library.borrow_book(title)


# ---------- WHEN ----------

# Search for a book with a given title
@when(u'jag söker efter titeln "{title}"')
def step_sok_titel(context, title):
    context.result = context.library.search_by_title(title)


# Search for books with a given author
@when(u'jag söker efter författaren "{author}"')
def step_sok_forfattare(context, author):
    context.result = context.library.search_by_author(author)


# Borrow a book with a given title
@when(u'jag lånar boken "{title}"')
def step_lana_bok(context, title):
    context.borrowed_book = context.library.borrow_book(title)


# Return a book with a given title
@when(u'jag lämnar tillbaka boken "{title}"')
def step_aterlamna_bok(context, title):
    context.returned_book = context.library.return_book(title)


# Control if a book with given title is borrowed
@when(u'jag kontrollerar om boken "{title}" är utlånad')
def step_kontrollera_utlanad(context, title):
    context.book_is_borrowed = context.library.is_book_borrowed(title)


# ---------- THEN ----------


# Control number of hits when searching for a book
@then(u'ska sökresultatet innehålla {count:d} bok')
def step_kontrollera_antal_traffar(context, count):
    assert len(context.result) == count


# Control the title of the returned book
@then(u'ska sökresultatet innehålla boken "{title}"')
def step_kontrollera_traff_med_titel(context, title):
    titles = [book.title for book in context.result]
    assert title in titles


# Control the author of the returned book
@then(u'ska sökresultatet innehålla författaren "{author}"')
def step_kontrollera_traff_med_forfattare(context, author):
    authors = [book.author for book in context.result]
    assert author in authors


# Control that a borrowed book is marked as not available
@then(u'ska "{title}" markeras som utlånad')
def step_kontrollera_utlaning_bok(context, title):
    assert context.borrowed_book is not None
    assert context.borrowed_book.is_available is False


# Control that a returned book is marked as available
@then(u'ska "{title}" markeras som tillgänglig')
def step_kontrollera_bok_aterlamnad(context, title):
    assert context.returned_book is not None
    assert context.returned_book.is_available is True


# Control that a borrowed book is marked as borrowed
@then(u'ska "{title}" vara utlånad')
def step_kontrollera_bok_utlanad(context, title):
    assert context.book_is_borrowed is True


# Control that an available book is marked as not borrowed
@then(u'ska "{title}" inte vara utlånad')
def step_kontrollera_bok_inte_utlanad(context, title):
    assert context.book_is_borrowed is False
