Feature: calcLength

    Background: Open App
        Given Open the Unit Conversion app

    Scenario: Length conversion km to miles
        Given the app Unit Conversion has opened
        When the user selects the menu icon
        Then the Menu becomes visible
        When length is selected
        Then length conversion window becomes visible
        When C is selected
        Then the converted value clears
        When kilometres is selected as first unit
        And miles is selected as second unit
        And value 200 is entered
        Then "124.27" is displayed as the converted measurements