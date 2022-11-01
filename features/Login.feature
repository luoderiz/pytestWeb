@smoke
Feature: Login
  Background:
    Given I am in automationtesting site
    Given I click on My Account Menu

    @success
  Scenario: Login success
    When I enter my valid existing username <raffaella@carra.com> in the Login Textbox
    When I enter my valid password <Raffaella0303456> in the Login Textbox
    When I click on Login Button
    Then I am redirected to My Account Home Page