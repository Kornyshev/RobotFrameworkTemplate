# robot --outputdir .\results .\tests\test_cases.robot

*** Settings ***
Library    C:/Projects/RobotFrameworkTemplate/lib/MyLibrary.py

*** Test Cases ***
Log In link is present on Demoblaze homepage (custom steps + custom browser)
    [Documentation]    Verify that the Demoblaze homepage loads and displays the 'Log In' link
    [Tags]    example
    Open Browser and navigate to Main Page

#*** Test Cases ***
#Log In link is present on Demoblaze homepage
#    [Documentation]    Verify that the Demoblaze homepage loads and displays the 'Log In' link
#    [Tags]    example
#    [Setup]    Open Browser    https://www.demoblaze.com/    chrome
#    [Teardown]    Close Browser
#    Page Should Contain Element    xpath://a[contains(text(), 'Log in')]


#*** Test Cases ***
#Log In link is present on Demoblaze homepage (custom steps)
#    [Documentation]    Verify that the Demoblaze homepage loads and displays the 'Log In' link
#    [Tags]    example
#    [Setup]    Open Browser    https://www.demoblaze.com/    chrome
#    [Teardown]    Close Browser
#    ${url} =    Get Current URL
#    Log To Console    Current URL: ${url}
#    Click Element If Present    xpath://a[contains(text(), 'Log in')]
