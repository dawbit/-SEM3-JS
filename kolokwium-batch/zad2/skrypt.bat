@echo off
setlocal enableextensions disabledelayedexpansion
set "textFile=%1"
set "search=%2"
set "replace=%3"

for /f "delims=" %%i in ('type "%textFile%" ^& break ^> "%textFile%" ') do (
set "line=%%i"
setlocal enabledelayedexpansion
set "line=!line:%search%=%replace%!"
>>"%textFile%" echo(!line!
endlocal
)