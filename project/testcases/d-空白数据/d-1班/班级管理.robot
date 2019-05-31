*** Settings ***
Library  pylib.SchoolClassLib

*** Test Cases ***
添加班级2-tc000002

    ${ret1}=   add school class    1   2班   60
    should be true    $ret1['retcode']==0
    ${ret2}=   list school class   1
    ${fc}=   evaluate   $ret2['retlist']
    classlist should contain   ${fc}
    ...   2班   七年级  &{ret1}[invitecode]  60  0  &{ret1}[id]

    [Teardown]    delete all school classes