from behave import given, when, then

from src.stock_item import StockItem
from src.stock import Stock


@given(u'att jag har 5 stycken Hammare')
def step_skapa_5_hammare(context):
    context.stock = Stock()
    context.product = StockItem(u'Hammare', 5)


@when(u'jag lägger till hammarna i lagret')
def step_lägg_till_5_hammare_i_lagret(context):
    context.stock.add_product(context.product)


@then(u'ska lagerstatusen öka med 5 hammare')
def step_kontrollera_5_hammare(context):
    item = context.stock.items[0]
    assert item.name == u'Hammare' and item.amount == 5


@given(u'att jag har 7 stycken Hammare')
def step_skapa_7_hammare(context):
    context.stock = Stock()
    context.product = StockItem(u'Hammare', 7)
    context.stock.add_product(context.product)


@when(u'jag tar bort 3 hammare')
def step_ta_bort_3_hammare_från_lagret(context):
    context.stock.remove_product(u'Hammare', 3)


@then(u'ska lagerstatusen på hammare bli 4 hammare')
def step_kontrollera_4_hammare(context):
    item = context.stock.items[0]
    assert item.name == u'Hammare'
    assert item.amount == 4
