#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

from systemcommand.test_useradd import Useradd
from systemcommand.test_userdel import Userdel
from systemcommand.test_passwd import Passwd

from systemcommand.test_pwd import Pwd
from systemcommand.test_cd import Cd
from systemcommand.test_mkdir import Mkdir
from systemcommand.test_rmdir import Rmdir
from systemcommand.test_cp import Cp
from systemcommand.test_mv import Mv
from systemcommand.test_rm import Rm
from systemcommand.test_file import File
from systemcommand.test_find import Find
from systemcommand.test_grep import Grep
from systemcommand.test_chown import Chown
from systemcommand.test_sort import Sort
from systemcommand.test_wc import Wc

from systemcommand.test_apt_get import Apt_get
from systemcommand.test_apt_cache import Apt_cache

from systemcommand.test_kill import Kill
from systemcommand.test_ps import Ps

from systemcommand.test_man import Man
from systemcommand.test_who import Who
from systemcommand.test_whoami import Whoami
from systemcommand.test_cal import Cal
from systemcommand.test_date import Date
from systemcommand.test_more import More
from systemcommand.test_redirect import Redirect
from systemcommand.test_pipe import Pipe
>>>>>>> b4e1cfa6b8c93c7036cf46ff681ca1a70e96fa9d

def main():
    classes = []

    # 常用命令测试

    # 用户管理命令
    classes.append(Useradd)
    classes.append(Userdel)
    classes.append(Passwd)

    # 文件/文件夹操作命令
    classes.append(Pwd)
    classes.append(Cd)
    classes.append(Mkdir)
    classes.append(Rmdir)
    classes.append(Cp)
    classes.append(Mv)
    classes.append(Rm)
    classes.append(File)
    classes.append(Find)
    classes.append(Grep)
    classes.append(Chown)
    classes.append(Sort)
    classes.append(Wc)
   
    # 其他命令
    classes.append(Man)
    classes.append(Who)
    classes.append(Whoami)
    classes.append(Cal)
    classes.append(Date)
    classes.append(More)
    classes.append(Redirect)
    classes.append(Pipe)
    classes.append(Kill)
    classes.append(Ps)
    # 软件包管理命令
    classes.append(Apt_get)
    classes.append(Apt_cache)

    for c in classes:
        suite = c.suite()
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(suite)

if __name__ == "__main__":
    main()
