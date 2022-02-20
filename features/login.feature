Feature: Login scenario

  Background: Steps commons
    Given Open the browser

  Scenario: Make incorrect login
    When Enter an incorrect login
    And Verify validation of incorrect login

  Scenario: Make correct login
    When Clear fields
    And Make a login correctly and validate login
    Then Close the browser

