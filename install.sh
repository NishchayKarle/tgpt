#!/bin/bash


# install requirements
python3 -m pip install -r requirements.txt
python3 -m pip install pyinstaller

# make the executable
sudo python3 -OO -m PyInstaller --onedir --noconfirm --distpath=/usr/local/bin --name=tgpt_app --clean tgpt.py

# create link to executable accessible anywhere
sudo ln -s /usr/local/bin/tgpt_app/tgpt_app /usr/local/bin/tgpt
