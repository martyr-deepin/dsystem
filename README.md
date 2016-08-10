# autotest-dde-dock


# prepare the enviroment
## install dogtail
download from https://github.com/wangyingtaodeepin/dogtail
> sudo python3 setup.py install

## install packages
> sudo apt-get install python3-pyatspi python3-pip libwnck-3-dev  
> sudo pip3 install PyUserInput

## run the test
> python3 dde-dock.py

## about the result.txt
The result is saved to the current file result.txt.  
Every line has the testlink case id and the test result.
The result file is aimed for posting to testlink.
