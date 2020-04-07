@echo off
for %%x in (C: Z:)
do ( %%x cd %%x dir /s %1 )