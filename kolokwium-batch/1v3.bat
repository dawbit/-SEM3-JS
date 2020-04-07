@echo off
for /L %%i in (1,1,100) do echo %%i
dir *.%i >> lista_plikow_%i.txt
pause