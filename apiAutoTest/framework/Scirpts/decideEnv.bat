@echo off
if %1==stage set /p="http://stageapi.vipabc.com/TutorGroup.Api"<nul>>%2/framework/Env.txt
if %1==product set /p="http://api.vipabc.com/TutorGroup.Api"<nul>>%2/framework/Env.txt
pause>nul