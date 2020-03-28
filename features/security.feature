Feature: Security Feature


@owasp
  Scenario: Check basic security after login
    Given The testpage page is loaded
    When the user enter login "qatdxtu@gmail.com" and password "password2019"
    And the user click login
    Then the user do a scanner
