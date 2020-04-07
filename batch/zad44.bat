@echo off
set /p typ=co usunac?
if exist *.%typ% (goto usun) else (goto nieusuwaj)
:usun
del *.%typ%
goto end
:nieusuwaj
echo Nie ma takich.
:end
pause