*** Settings ***
Resource  rc.robot


*** Test Cases ***
测试用例
    deleteAllCourse
    login    auto     sdfsdfsdf
    AddCourse    初中物理    初中物理描述    2
    ${indexList}  ${nameList}=   listCourse
    log to console  @{nameList}
    log to console  @{indexList}
    should be equal  @{indexList}[0]    2
    should be equal  @{nameList}[0]    初中物理
    log to console   第一次添加完成

    sleep  5
    AddCourse    初中化学    初中化学描述    1
   ${indexList1}  ${nameList1}=   listCourse
   log to console  @{indexList1}
   log to console  @{nameList1}
    should be equal  @{indexList1}[0]    1
    should be equal  @{nameList1}[0]    初中化学
    close browser
