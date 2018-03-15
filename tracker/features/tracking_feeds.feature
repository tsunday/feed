# Created by Tomasz at 15.03.2018
Feature: User can track feeds

  Scenario: Adding new tracking entries - timer mode
    Given a user tomasz@gmail.com
    When user tomasz@gmail.com starts event today at 10:00
      And user tomasz@gmail.com stops event today at 10:15
    Then there is 1 tracking entry started at 10:00 with 15 minutes length


  Scenario: Adding new tracking entries - fixed time mode
    Given a user tomasz@gmail.com
    When user tomasz@gmail.com registers 20 minutes length event at 10:20
    Then there is 1 tracking entry started at 10:00 with 20 minutes length