# Created by Tomasz at 15.03.2018
Feature: User can track feeds

  Scenario: Adding new tracking entries - timer mode
    Given a user tomasz@gmail.com
    When user tomasz@gmail.com starts event today at 10:00
      And user tomasz@gmail.com stops event today at 10:15
    Then daily report for tomasz@gmail.com is not empty
      And there is 1 tracking entry with 15 minutes length for tomasz@gmail.com
      And last registered event for tomasz@gmail.com took 15 minutes


  Scenario: Adding new tracking entries - fixed time mode
    Given a user tomasz@gmail.com
    When user tomasz@gmail.com registers 20 minutes length event at 10:20
    Then daily report for tomasz@gmail.com is not empty
      And there is 1 tracking entry with 20 minutes length for tomasz@gmail.com
      And last registered event for tomasz@gmail.com took 20 minutes


  Scenario: Adding new tracking entries - multiple events
    Given a user tomasz@gmail.com
    When user tomasz@gmail.com starts event today at 10:00
      And user tomasz@gmail.com starts event today at 10:15
      And user tomasz@gmail.com stops event today at 10:30
      And user tomasz@gmail.com stops event today at 10:45
    Then daily report for tomasz@gmail.com is not empty
      And there are 2 tracking entries with 30 minutes length for tomasz@gmail.com
      And last registered event for tomasz@gmail.com took 30 minutes


  Scenario: No events provided
    Given a user tomasz@gmail.com
    Then daily report for tomasz@gmail.com is empty
