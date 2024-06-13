# Created by AlexandraLyubchevska at 5/30/2024
Feature: Filter Secondary deals by "want to sell" option

  @browserstack
  Scenario: User can filter the Secondary deals by "want to sell" option on BrowserStack
    Given the user is on the main page
    When the user logs in with valid credentials
    When  the user clicks on the "Secondary" option
    When the user filters the products by "want to sell"
    Then the user verifies all cards have a "for sale" tag

  @mobile
  Scenario: User can filter the Secondary deals by "want to sell" option on mobile
    Given the user is on the main page
    When the user logs in with valid credentials
    When the user clicks on the "Secondary" option
    When the user filters the products by "want to sell"
    Then the user verifies all cards have a "for sale" tag
