*** Settings ***
Library  course_mgr

*** Test Cases ***
测试用例
    @{courses}=  listCourse
    :FOR  ${course}  IN  @{courses}
    \  log to console   ${course}[name]
