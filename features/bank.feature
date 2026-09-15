@bank
Feature: ett flexibelt bankkonto

  Scenario: skapa ett nytt konto med saldo 0
    Given att jag har ett bankkonto med saldo 0
    Then ska kontots saldo vara 0 kr


  Scenario: sätta in pengar på kontot
    Given att jag har ett bankkonto med saldo 0
    When jag sätter in 100 kr
    Then ska kontots saldo öka med 100 kr


  Scenario: ta ut pengar från kontot
    Given att jag har ett bankkonto med saldo 100
    When jag tar ut 40 kr
    Then ska kontots saldo minska med 40 kr


  Scenario: applicera 5 % ränta
    Given att jag har ett bankkonto med saldo 500
    When jag erhåller 5 % ränta
    Then ska räntan öka kontots saldo med 25 kr


  Scenario: överföra pengar mellan två konton
    Given att jag har ett bankkonto A med saldo 500
    And att jag har ett bankkonto B med saldo 200
    When jag överför 100 kr från konto A till konto B
    Then ska konto A:s saldo vara 400 kr
    And ska konto B:s saldo vara 300 kr
