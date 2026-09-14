Feature: system för lagerhantering
  Scenario: lägga till en produkt där namn och antal är korrekt
    Given att jag har 5 stycken Hammare
    When jag lägger till hammarna i lagret
    Then ska lagerstatusen öka med 5 hammare


  Scenario: minska antal av en befintlig produkt
    Given att jag har 7 stycken Hammare
    When jag tar bort 3 hammare
    Then ska lagerstatusen på hammare bli 4 hammare