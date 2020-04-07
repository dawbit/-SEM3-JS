@echo off
if exist "test.txt" (
del "test.txt"
exit
) else (
NUL > test.txt
)