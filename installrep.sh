#!/bin/bash
echo Repman Updator Installation
if [ ! -d $HOME/.rep-updator ]; then
    mkdir -p $HOME/.rep-updator;
fi;

echo Directory created at
echo $HOME/.rep-updator/
cp ./ans.sh $HOME/.rep-updator/
chmod +x $HOME/.rep-updator/ans.sh

cp ./rep.sh $HOME/.rep-updator/
chmod +x $HOME/.rep-updator/rep.sh

cp ./rep-logo.png $HOME/.rep-updator/

echo Scripts installed
cp ./repman-up $HOME/.rep-updator/
cp ./repman-up $HOME/Desktop/

echo repman updator installed




