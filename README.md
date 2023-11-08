# add-commit-push

Alias to get to the sprint-5 directory from anywhere on the machine:
    function sprint-5 {Set-Location -Path C:\Users\user\Lewis\cpsc-20000\sprint-5\
    Set-Alias -Name g5 -Value sprint-5}

Alias for the add-commit-push python application that can be run from anywhere in the machine: 
    function addcomp { python C:\Users\user\Lewis\cpsc-20000\sprint-5\add-commit-and-push-with-python\add-commit-push\add-commit-push.py @args }
    Set-Alias -Name acp -Value addcomp
