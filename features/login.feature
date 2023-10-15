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