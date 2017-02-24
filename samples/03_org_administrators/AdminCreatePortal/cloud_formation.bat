REM This is a batch file to be called by Esri AWS ArcGIS cloud formation tool
REM What this batch file does:
REM 1. Download miniconda windows edition to currnet active dir
REM 2. Install miniconda
REM 3. Install arcgis package
REM 4. Run cleanup.py script
REM 5. Run create_groups.py script
REM 6. Run create_users. py script
REM 7. Run publish_content.py script

REM Call this script with portal URL, admin username, admin password
REM Prints CF_success at the end

ECHO off
REM 1. Download miniconda to active dir
ECHO Downloading latest miniconda
powershell -Command "Invoke-WebRequest https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe -OutFile miniconda.exe"

REM 2. Install miniconda
ECHO Install miniconda in user profile. Not registering Python
start /wait "" miniconda.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%UserProfile%\miniconda3

REM 3a. Create new env called 'cloud_formation
ECHO Creating new environment
conda create --name cloud_formation python=3.6
conda activate cloud_formation

REM 3b. Install arcgis
ECHO Installing arcgis package
conda isntall -c esri arcgis

REM 4. Run clean up script
python.exe cleanup.py %1 %2 %3

REM 5. Run create_groups script
python.exe create_groups.py %1 %2 %3

REM 6. Run create_users script
python.exe create_users.py %1 %2 %3

REM 7. Run publish_content script
python.exe publish_content.py %1 %2 %3