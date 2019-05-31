*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
测试用例
    open browser    https://www.vmall.com/index.html    chrome
    set selenium implicit wait  5
    @{eles}=     Get Webelements    css= .home-hot-goods .grid-title
    :For  ${ele}  IN  @{eles}
    \  log to console    ${ele.text}
    close browser