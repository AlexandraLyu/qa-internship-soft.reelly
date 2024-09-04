Feature: User Registration

  Scenario: Create a new account
    Given I open the registration page
    When I enter "test+Ale+careerist" as first and last name
    And I enter "+971 test careerist" as phone number
    And I enter "lybchevskaya@gmail.com" as email
    And I enter "test12345!" as password
    And I enter "Test" as company
    And I select "Broker" as role
    And I select "United States of America" as country
    And I select "I work alone" as company size
    Then the data was entered correctly

