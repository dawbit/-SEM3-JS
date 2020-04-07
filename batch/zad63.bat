@echo off
echo Menu skryptow:
echo.1. Odpal skrypt nr 2
echo.2. Odpal skrypt nr 11
echo.
set /p x=Wybor:
if %x% == 1 call zad2.bat
if %x% == 2 call zad11.bat
pause