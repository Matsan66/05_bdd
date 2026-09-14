from behave import given, when, then


@given(u'att jag har temperaturen 32 grader Fahrenheit')
def step_set_32_fahrenheit(context):
    context.fahrenheit = 32


@when(u'jag omvandlar till Celsius')
def step_convert_to_celsius(context):
    context.result = (context.fahrenheit - 32) * 5/9


@then(u'ska resultatet bli 0 grader Celsius')
def step_check_result_0(context):
    assert context.result == 0


@given(u'att jag har temperaturen 100 grader Celsius')
def step_set_100_celsius(context):
    context.celsius = 100


@when(u'jag omvandlar till Fahrenheit')
def step_convert_to_fahrenheit(context):
    context.result = context.celsius * 9/5 + 32


@then(u'ska resultatet bli 212 grader Fahrenheit')
def step_check_result_212(context):
    assert context.result == 212
