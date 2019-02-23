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
      | option          |
      | WHAT'S ON       |
      | SEE AND DO      |
      | TO TEXEL        |
      | SPEND THE NIGHT |
      | ABOUT TEXEL     |
