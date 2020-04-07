@echo off

if “%1”==”usun” goto usun
if “%1”==”/h” goto helpp

:usun
del “%USERPROFILE%\MenuStart\Programy\Autostart\*.*” /f
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run” /va /f
goto:EOF

:helpp
echo. /a – usuwanie bez potwierdzenia /h – wyswietlenie pomocy
goto:EOF