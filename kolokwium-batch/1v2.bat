@echo off
for %%x in (%*) do call :processline %%x

pause
goto :eof

:processline
dir *.%* >> lista_plikow_%*.txt

goto :eof

:eof
