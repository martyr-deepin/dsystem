#!/bin/bash

apt-get install -y python3-pyatspi python3-pip python3-setuptools libwnck-3-dev  python3-tk xsel git ssh && \
	pip3 install PyUserInput pyautogui pexpect configparser pyperclip

cd .. && \
	git clone https://github.com/wangyingtaodeepin/dogtail && \
	cd dogtail && \
	python3 setup.py install

gsettings set org.gnome.desktop.interface toolkit-accessibility true
