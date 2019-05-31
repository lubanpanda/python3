*** Settings ***
Library  DeleteCourse
Library  SeleniumLibrary

*** Test Cases ***
添加课程
    [setup]      deleteAllCourse
    open browser  http://localhost/mgr/login/login.html    chrome
    set selenium implicit wait    5
    input text  id=username    auto
    input text  id=password    sdfsdfsdf
    click element  css=.btn-success

    sleep  3
    click element  css=button[ng-click^=showAddOne]

    input text     css=input[ng-model="addData.name"]    初中物理
    input text     css=textarea[ng-model="addData.desc"]    初中物理描述
    click element  css=Button[ng-click="addOne()"]

    @{eles}=       Get WebElements     css=tr>td:nth-child(2)
    :FOR   ${ele}  IN  @{eles}
    \  should be equal   ${ele.text}  初中物理

    close browser




    #[teardown]   deleteAllCourse
