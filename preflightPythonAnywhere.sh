# preflight.sh
#!/usr/bin/bash

if [ "$#" -ne "1" ] 
then
    echo "Usage: ./preflight.sh <appname>"
    echo "<appname> is either MURAL, QR or DELETE"
    exit;
fi

rm -r Flask_App

export FLASK_APP=flask_app.py

if [ $1 == "MURAL" ] 
then
    cp -R mural Flask_App
    cp Configurations/PythonAnywhereConfig.json Flask_App/config.json
    exit;
fi

if [ $1 == "QR" ] 
then
    cp -R qrDonate Flask_App
    cp Configurations/PythonAnywhereConfig.json Flask_App/config.json
    exit;
fi

if [ $1 == "DELETE" ] 
then
    exit;
fi