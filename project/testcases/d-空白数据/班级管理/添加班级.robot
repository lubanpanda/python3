*** Settings ***
Library  pylib.SchoolClassLib


*** Test Cases ***
添加班级1-tc000001

    ${ret1}=   add school class    1   2班   60
    should be true    $ret1['retcode']==0
    ${ret2}=   list school class   1
    ${retlist}=   evaluate   $ret2['retlist']
    should be true  $fc['id']==$ret1['id']
    should be true  $fc['invitecode']==$ret1['invitecode']
    [Teardown]    delete all school classes


