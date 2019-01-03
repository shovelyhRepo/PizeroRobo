@echo off

:@echo pyrcc5 .\..\resources\resources_image.qrc -o ..\resources_image_rc.py
:pyrcc5 .\..\resources\resources_image.qrc -o ..\resources_image_rc.py

FOR /r %%i IN (.\..\ui\*.ui) DO (
@echo pyuic5 .\..\ui\%%~ni.ui -o .\..\ui\%%~ni_design.py
pyuic5 .\..\ui\%%~ni.ui -o .\..\ui\%%~ni_design.py
)


