Feature: login and logout on SauceDemo

  Scenario: login as standard user
    Given I am on SauceDemo homepage
    And I am logged out
    When I type my username "standard_user"
    And I type my password "secret_sauce"
    And I click on the Login button
    Then I should be redirected to the "inventory" page
    And I should see "6" items listed on the page
    And I should "not see" wrong images on products

  Scenario: login as problem user
    Given I am on SauceDemo homepage
    When I type my username "problem_user"
    And I type my password "secret_sauce"
    And I click on the Login button
    Then I should be redirected to the "inventory" page
    And I should "see" wrong images on products

  Scenario: try to login as a locked out user
    Given I am on SauceDemo homepage
    When I type my username "locked_out_user"
    And I type my password "secret_sauce"
    And I click on the Login button
    Then I should see the error message "Sorry, this user has been locked out."

  Scenario: Try to login using invalid username and password
    Given I am on SauceDemo homepage
    When I type my username "invalid_username"
    And I type my password "invalid_password"
    And I click on the Login button
    Then I should see the error message "Username and password do not match any user"

Scenario: Logout from app
    Given I am logged in
    When I click on the hamburger menu button
    And I click on the "logout" link inside the hamburger menu
    Then I should be redirected to the "home" page