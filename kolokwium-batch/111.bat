for %%a in (test.txt) do (
    set file=%%~fa
    set filepath=%%~dpa
    set filename=%%~nxa
)    
echo %file% = %filepath% + %filename%