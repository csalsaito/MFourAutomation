Feature: Login
  Website to login into the homepage

  @thistest
  Scenario: Verify Admin User is able to login with valid credentials
    Given Login page is displayed
    When the user enters valid admin credentials
    Then the user arrives on homepage
  @thistest
  Scenario: Verify Admin User is not able to login with invalid credentials
    Given Login page is displayed
    When the user enters invalid admin credentials
    Then the user receives an error
  @thistest
  Scenario Outline: Verify different types of surveys can be created
    Given Valid Admin user is logged in
    And the user wants to create <type> survey
    When create project is clicked
    Then the survey is created

    Examples:
    |type                             |
    |custom                           |
    |US General Population            |
    |US Millennial Generation         |
    |US Plural Generation Z Population|

  Scenario Outline: Verify a question with multiple options is able to be saved
    Given Valid Admin user is logged in
    And the user wants to create <type> survey
    When create project is clicked
    And the user creates a <primary> question
    Then the <primary> questions are added to the survey

    Examples:
    |type                             |primary            |
    |custom                           |single selection  |
    |custom                           |multiple selection|
    |custom                           |ranked order      |
    |custom                           |date/time response|
    |custom                           |short answer      |
    |custom                           |intensity scale   |
    |custom                           |two-tap matrix    |
    |US General Population            |single selection  |
    |US General Population            |multiple selection|
    |US General Population            |ranked order      |
    |US General Population            |date/time response|
    |US General Population            |short answer      |
    |US General Population            |intensity scale   |
    |US General Population            |two-tap matrix    |
    |US Millennial Generation         |single selection  |
    |US Millennial Generation         |multiple selection|
    |US Millennial Generation         |ranked order      |
    |US Millennial Generation         |date/time response|
    |US Millennial Generation         |short answer      |
    |US Millennial Generation         |intensity scale   |
    |US Millennial Generation         |two-tap matrix    |
    |US Plural Generation Z Population|single selection  |
    |US Plural Generation Z Population|multiple selection|
    |US Plural Generation Z Population|ranked order      |
    |US Plural Generation Z Population|date/time response|
    |US Plural Generation Z Population|short answer      |
    |US Plural Generation Z Population|intensity scale   |
    |US Plural Generation Z Population|two-tap matrix    |

  Scenario Outline: Verify a multiple choice question and any primary question can be added to a survey
    Given Valid Admin user is logged in
    And the user wants to create <type> survey
    When create project is clicked
    And the user creates a multiple choice question
    And the user creates a <primary> question
    Then <primary> questions are added to the survey

    Examples:
    |type                             |primary           |
    |custom                           |single selection  |
    |custom                           |multiple selection|
    |custom                           |ranked order      |
    |custom                           |date/time response|
    |custom                           |short answer      |
    |custom                           |intensity scale   |
    |custom                           |two-tap matrix    |
    |US General Population            |single selection  |
    |US General Population            |multiple selection|
    |US General Population            |ranked order      |
    |US General Population            |date/time response|
    |US General Population            |short answer      |
    |US General Population            |intensity scale   |
    |US General Population            |two-tap matrix    |
    |US Millennial Generation         |single selection  |
    |US Millennial Generation         |multiple selection|
    |US Millennial Generation         |ranked order      |
    |US Millennial Generation         |date/time response|
    |US Millennial Generation         |short answer      |
    |US Millennial Generation         |intensity scale   |
    |US Millennial Generation         |two-tap matrix    |
    |US Plural Generation Z Population|single selection  |
    |US Plural Generation Z Population|multiple selection|
    |US Plural Generation Z Population|ranked order      |
    |US Plural Generation Z Population|date/time response|
    |US Plural Generation Z Population|short answer      |
    |US Plural Generation Z Population|intensity scale   |
    |US Plural Generation Z Population|two-tap matrix    |