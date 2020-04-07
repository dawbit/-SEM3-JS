@echo off
for %%a in (*.txt) do (
set /p "=%%a " <nul >>zad3output.txt
call zad.exe %%a >> zad3output.txt
echo( >>zad3output.txt
)