@echo off

@echo pyrcc5 .\..\resource.qrc -o ..\resource_rc.py
pyrcc5 .\..\resource.qrc -o ..\resource_rc.py

FOR /r %%i IN (.\..\ui\*.ui) DO (
@echo pyuic5 .\..\ui\%%~ni.ui -o .\..\ui\%%~ni_design.py
pyuic5 .\..\ui\%%~ni.ui -o .\..\ui\%%~ni_design.py
)


