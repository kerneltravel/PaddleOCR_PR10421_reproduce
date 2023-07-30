# 通过 pyinstaller 打包为 exe

import os

dirPath = os.getcwd()

os.system(f'cd /d {dirPath}')

os.system(r'pyinstaller.exe -F --collect-all paddleocr --add-data .\paddleocr;.\paddleocr    --add-data .\mklml.dll;. main.py')
