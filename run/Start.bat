@echo off 
TITLE PyRoyale v1.0
mode con: cols=120 lines=32
python -m pip install -r ../src/requirements.txt
mode con: cols=120 lines=32
python ../src/Main.py
pause