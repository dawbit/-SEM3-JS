@echo off
set /p n=”podaj liczbe: ”
FOR /L %%i IN (1,1,%n%) do echo %%i >> %1
pause