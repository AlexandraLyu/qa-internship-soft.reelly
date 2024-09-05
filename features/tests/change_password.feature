# Created by AlexandraLyubchevska at 9/4/2024
Feature: Change Password
  As a user, I want to change my password from the settings page
  so that I can maintain the security of my account.

  Scenario: Successfully change password
    Given I am logged in on the main page
    When I navigate to the settings page
    And I select the Change password option
    And I enter "NewPassword123!" as the new password
    And I enter "NewPassword123!" as the repeated password
    Then the "Change password" button should be enabled

