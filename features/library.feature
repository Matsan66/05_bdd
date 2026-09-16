@library
Feature: ett bibliotek för utlåning av böcker

  Background:
    Given att biblioteket har följande böcker
        | title                         | author    |
        | Sagan om ringen               | Tolkien   |
        | Stiftelsen och imperiet       | Asimov    |
        | 2001: En rymdodyssé           | Clarke    |
        | Liftarens guide till galaxen  | Adams     |


  Scenario: söka efter böcker baserat på titel
    When jag söker efter titeln "Sagan om ringen"
    Then ska sökresultatet innehålla 1 bok
    And ska sökresultatet innehålla boken "Sagan om ringen"


  Scenario: söka efter böcker baserat på författare
    When jag söker efter författaren "Tolkien"
    Then ska sökresultatet innehålla 1 bok
    And ska sökresultatet innehålla författaren "Tolkien"


  Scenario: låna en bok
    When jag lånar boken "Stiftelsen och imperiet"
    Then ska "Stiftelsen och imperiet" markeras som utlånad


  Scenario: lämna tillbaka en bok
    Given att "Liftarens guide till galaxen" är utlånad
    When jag lämnar tillbaka boken "Liftarens guide till galaxen"
    Then ska "Liftarens guide till galaxen" markeras som tillgänglig


  Scenario: kontrollera om en viss bok är utlånad
    Given att "Liftarens guide till galaxen" är utlånad
    When jag kontrollerar om boken "Liftarens guide till galaxen" är utlånad
    Then ska "Liftarens guide till galaxen" vara utlånad


  Scenario: kontrollera om en viss bok är inte är utlånad
    When jag kontrollerar om boken "Sagan om ringen" är utlånad
    Then ska "Sagan om ringen" inte vara utlånad



