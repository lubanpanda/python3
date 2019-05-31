*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
login
    [Arguments]    ${username}    ${password}
    open browser  http://localhost/mgr/login/login.html    chrome
    set selenium implicit wait    5
    input text  id=username      ${username}
    input text  id=password      ${password}
    click element  css=.btn-success

AddCourse
    [Arguments]  ${name}    ${desc}    ${display_idx}
    click element  css=button[ng-click^=showAddOne]

    input text     css=input[ng-model="addData.name"]           ${name}
    input text     css=textarea[ng-model="addData.desc"]        ${desc}
    input text     css=input[ng-model="addData.display_idx"]    ${display_idx}
    click element  css=Button[ng-click="addOne()"]

listCourse
     ${display_idxs}        Get WebElements     css=tr[total-items="totalNum"]>td:nth-child(1)
     ${names}=              Get WebElements     css=tr[total-items="totalNum"]>td:nth-child(2)
     ${indexList}=  evaluate   [display.text for display in $display_idxs]
     ${nameList}=   evaluate   [name.text for name in $names]

     [Return]  ${indexList}   ${nameList}

deleteAllCourse
    login  auto  sdfsdfsdf
    set selenium implicit wait  2
    :For  ${i}   IN Range 999999
    \  ${btns}   Get WEbElements   css=button[ng-click="delOne(one)"]
    \  exit for loop if  $btns=[]
    \  click element   @[btns][0]
    \  click element   class=btn-primary
    \  set selenium implicit wait  5





