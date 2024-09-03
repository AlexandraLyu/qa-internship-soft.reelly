Feature: Reelly Login and Connect Company Feature
  As a user of the Reelly platform
  I want to log in and connect my company
  So that I can manage company details on the platform

  Scenario: Log in and connect the company
    Given I am on the Reelly sign-up page
    When I log in with the email "lybchevskaya@icloud.com" and password "Abundance88!"
    And I click on "Connect the company"
    Then a new tab should open
    And I switch to the new tab
    And I should see the title "Book presentation"
    And the URL should contain "https://soft.reelly.io/book-presentation"






#Scenario: Log in and connect the company

#
#
#    When I log in with the email "lybchevskaya@icloud.com" and password "Abundance88!"
#    And I click on "Connect the company"
#    Then a new tab should open
#    And I switch to the new tab
#    And I should see the title "Expected Title"
#    And the URL should contain "https://expected.url.com"