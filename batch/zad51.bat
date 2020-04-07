@echo off
set /p a=”Podaj a: ”
:petla
set /p d=”1 Dodawanie 2 Odejmowanie 3 Dzielenie 4 Mnozenie: ”
set /p b=”Podaj b: ”
if %d%==1 (set /a a=%a% + %b%)
if %d%==2 (set /a a=%a% – %b%)
if %d%==3 (set /a a=%a% / %b%)
if %d%==4 (set /a a=%a% * %b%)
echo Wynik to %a%
set /p n=”Uruchomic kalkulator ponownie? (y)”
if %n%==y goto :petla
else goto:EOF