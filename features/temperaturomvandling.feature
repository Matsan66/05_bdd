Feature: temperaturomvandling Fahrenheit < - > Celsius
  Scenario: omvandla Fahrenheit till Celsius
    Given att jag har temperaturen 32 grader Fahrenheit
    When jag omvandlar till Celsius
    Then ska resultatet bli 0 grader Celsius


  Scenario: omvandla Celsius till Fahrenheit
    Given att jag har temperaturen 100 grader Celsius
    When jag omvandlar till Fahrenheit
    Then ska resultatet bli 212 grader Fahrenheit
