@agent
Feature: Agent app is a business app
  As an agent,
  I want to login,
  I want to make successful cash in,
  I want to make B2B transfer,
  I want to make B2B request,
  I want to pay bill,
  I want to logout.

Background:
  Given the Agent app will be opened in mobile

  @onboarded
  Scenario: successful on-boarding of valid agent
    Given app registration page is displayed
    When the user will change the language
    And the user will insert agent number
    And the user will click Next
    And the user will select operator
    And the user will allow app to read and insert OTP
    Then the user will see the pin field text "Agent PIN"
    And the user will insert login pin
    And the user will press login
    And the user will turn on the agent status
    And the user will be on home page
    And close the app

  @onboarded
  Scenario: successful login
    Given app login page is displayed
    When the user will change the language
    And the user will insert login pin
    And the user will press login
    Then the user will be on home page
    And close the app

  @onboarded @onboarded-negative
  Scenario: unsuccessful login twice due to incorrect pin and see Attention message
    Given app login page is displayed
    When the user will change the language
    And the user will insert incorrect login pin
    And the user will press login
    And the user will click cross button to close the banner
    And the user will insert incorrect login pin
    And the user will press login
    Then the user will see error banner with "Attention! One more incorrect attempt will lock your PIN" message
    And close the app

  @onboarded
  Scenario: successful cash in
    Given app is in home page
    When the user will tap on Cash In
    And the user will insert customer number "01810189667"
    And the user will click proceed to the next step
    And the user will insert amount "55"
    And the user will press proceed to the next step
    And the user will insert pin
    And the user will press confirm
    And the user will press Tap and hold
    Then the user will see this message "Your Cash In transfer is complete."
    And close the app

  @onboarded
  Scenario: successful b2b transfer
    Given app is in home page
    When the user will tap on b2b transfer
    And the user will insert amount "55"
    And the user will press proceed to the next step
    And the user will insert pin
    And the user will press confirm
    And the user will press Tap and hold
    Then the user will see this message "Your B2B Transfer is complete."
    And the user will press back to home
    And the user will click yes on the confirmation
    And the user will press on very good
    And close the app

  @onboarded
  Scenario: successful e money request
    Given app is in home page
    When the user will tap on b2b request
    And the user will click on e money request
    And the user will insert amount "55"
    And the user will press proceed to the next step
    And the user will insert pin
    And the user will press confirm
    And the user will press Tap and hold
    Then the user will see this message "Your E-Money Request is Successful"
    And close the app

  @onboarded
  Scenario: successful cash request
    Given app is in home page
    When the user will tap on b2b request
    And the user will click on cash request
    And the user will insert amount "55"
    And the user will press proceed to the next step
    And the user will insert pin
    And the user will press confirm
    And the user will press Tap and hold
    Then the user will see this message "Your Cash Request is Successful"
    And close the app

  @onboarded @onboarded-negative
  Scenario: unsuccessful login due to incorrect pin
    Given app login page is displayed
    When the user will change the language
    And the user will insert incorrect login pin
    And the user will press login
    Then the user will see error banner with "Incorrect PIN" message
    And close the app