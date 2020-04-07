@echo off
set /p ilosc=”Ile liczb?: ”
FOR /L %%x IN (0,1,%ilosc%) DO echo %%x >> %1
pause