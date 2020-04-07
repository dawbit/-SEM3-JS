@echo off
set mypath=

setlocal
for %%f in (*.txt) do echo %mypath%%%f
for /D %%d in (*) do (
    set mypath=%mypath%%%d\
    cd %%d
    call :treeProcess
    cd ..
)
endlocal