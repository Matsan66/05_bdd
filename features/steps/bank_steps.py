from behave import given, when, then
from src.bank.bank import Bank


# ---------- GIVEN: förutsättningar ----------

@given(u'att jag har ett bankkonto med saldo {amount:d}')
def step_skapa_konto_med_saldo(context, amount):
    context.account = Bank(amount)


@given(u'att jag har ett bankkonto {konto} med saldo {amount:d}')
def step_skapa_namngivet_konto(context, konto, amount):
    if not hasattr(context, 'accounts'):
        context.accounts = {}
    context.accounts[konto] = Bank(amount)


# ---------- WHEN: handlingar ----------

@when(u'jag sätter in {amount:d} kr')
def step_satta_in_pengar(context, amount):
    context.balance_before = context.account.check_balance()
    context.account.deposit_money(amount)


@when(u'jag tar ut {amount:d} kr')
def step_ta_ut_pengar(context, amount):
    context.balance_before = context.account.check_balance()
    context.account.withdraw_money(amount)


@when(u'jag erhåller {amount:d} % ränta')
def step_erhall_ranta(context, amount):
    context.balance_before = context.account.check_balance()
    context.account.apply_interest(amount)


@when(u'jag överför {amount:d} kr från konto {fran} till konto {till}')
def step_overfor_pengar(context, amount, fran, till):
    context.accounts[fran].withdraw_money(amount)
    context.accounts[till].deposit_money(amount)


# ---------- THEN: kontroller ----------

@then(u'ska kontots saldo vara {expected:d} kr')
def step_kontrollera_saldo(context, expected):
    assert context.account.check_balance() == expected


@then(u'ska kontots saldo öka med {amount:d} kr')
def step_kontrollera_okning(context, amount):
    assert context.account.check_balance() == context.balance_before + amount


@then(u'ska kontots saldo minska med {amount:d} kr')
def step_kontrollera_minskning(context, amount):
    assert context.account.check_balance() == context.balance_before - amount


@then(u'ska räntan öka kontots saldo med {amount:d} kr')
def step_kontrollera_ranta(context, amount):
    assert context.account.check_balance() == context.balance_before + 25


@then(u'ska konto {konto}:s saldo vara {expected:d} kr')
def step_kontrollera_kontosaldo(context, konto, expected):
    assert context.accounts[konto].check_balance() == expected
