Feature: Information is split up into subjects

  As a user, I want the information on the page split up in
  subjects so that I can easily find my information.
    
  Scenario: Set the language
    Given the home page is in front of me
    And I see a button with a country flag 
    When I select my preferred language flag
    Then the page is translated into my preferred language
  
  Scenario: See the different subjects
    Given the home page is in front of me
    And I have selected the English language
    Then I see the following subjects
      | subject         |
      | What's on       |
      | See and do      |
      | To Texel        |
      | Spend the night |
      | About Texel     |

  Scenario Outline: Visiting one of the information pages
    Given I am on the <subject> page
    When I scan the page
    Then I find information about <nugget>
    
    Examples:
      | subject         | nugget           |
      | What's on       | Order tickets    |
      | See and do      | Webcams on Texel |
      | To Texel        | By ferry         |
      | Spend the night | Bungalow parks   |
      | About Texel     | History          |
