@echo off
IF EXIST %1 del %1
set /p n=”Podaj n: ”
set /a n=%n%+1
set /a licznik=1
:again
if %licznik%==%n% (goto :eof) else (echo %licznik% >> %1)
SET /a licznik=%licznik%+1
goto :again