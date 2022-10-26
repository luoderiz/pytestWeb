Feature:GoogleSearch


  @example
  Scenario Outline: The client search by word
    Given The client is in google page
    When The client search for word <text>
    Then The client verify that results <text> are shown properly
    Examples:
      | text       |
      | Automation |
      | Crowdar    |
      | Docker     |



