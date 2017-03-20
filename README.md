# autotest-dde-dock

# prepare the enviroment
## install packages
> sudo apt-get install python3-pyatspi python3-pip python3-setuptools libwnck-3-dev  python3-tk
>
> sudo pip3 install PyUserInput pyautogui pexpect configparser pyperclip

## prepare /etc/sudoers file and partition 
> sudo vi /etc/sudoers, add `yoursystemname  ALL=(ALL) NOPASSWD:ALL` at the end of file(if yoursystemname is deepin, then add `deepin  ALL=(ALL) NOPASSWD:ALL`), you do not need input your password if you use root any more
>
> make sure your system has another useless partition, the partition is /dev/sda4 in this case, you can edit it in `dsystem/compatibility/dev.info` if your partition is not /dev/sda4

## install dogtail
download from https://github.com/wangyingtaodeepin/dogtail
> git clone https://github.com/wangyingtaodeepin/dogtail
>
> cd dogtail
>
> sudo python3 setup.py install

## enable accessibility with sniff or by running:
> gsettings set org.gnome.desktop.interface toolkit-accessibility true

## run the test
> python3 dde-dock.py

## about the result.txt
```
The result is saved to the current file result.txt.
Every line has the testlink case id and the test result.
The result file is aimed for posting to testlink.
```

## for autorun the testcase from your testlink
First, you should edit file tools/param.env and fill in the parameters.
And then, source the file
> source tools/param.env

Execute below command. The testcase will be run and the result will be uploaded to testlink.
> python3 run.py

