# Created by AlexandraLyubchevska at 5/30/2024
Feature: Filter Secondary deals by "want to sell" option

  Scenario: User can filter the Secondary deals by "want to sell" option
    Given the user is on the main page
    When the user logs in with valid credentials
    And the user clicks on the "Secondary" option in the left side menu
    #Then the user should be on the Secondary deals page
    When the user filters the products by "want to sell"
    Then the user verifies all cards have a "for sale" tag
