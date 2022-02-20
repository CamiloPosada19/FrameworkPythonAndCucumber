Feature: Fill in the form

  Scenario Outline: Fill in the form with different data

    Given Enter the environment
    When Fill in the fields "<name>" "<email>" "<password>"
    Then Validate entry "<name>"


    Examples:
      | name | email | password |
      |Daniel| correo1@correo.com |123 |
      |Pedro|  correo2@correo.com |123 |
      |Angela| correo3@correo.com |123 |
      |Carlos| correo4@correo.com |123 |
      |Esteban| correo5@correo.com |123 |


