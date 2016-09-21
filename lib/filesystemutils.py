#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import configparser


cmdlist = ['touch /mnt/a.txt','mkdir /mnt/中文','sudo mkdir /mnt/test','mkdir /mnt/中文test',
            'touch /mnt/中文/中文.txt','touch /mnt/中文/test.txt','touch /mnt/中文/中文test.txt',
            'touch /mnt/test/中文.txt','touch /mnt/test/test.txt','touch /mnt/test/中文test.txt',
            'touch /mnt/中文test/中文.txt','touch /mnt/中文test/test.txt','touch /mnt/中文test/中文test.txt']

def getDevInfo(section,part):
    config = configparser.ConfigParser()
    currentdir = os.getcwd()
    config.read(currentdir + '/lib/dev.info')
    info = config[section][part]
    return info

def mkextx(ext,*rootcmds):
    sda = getDevInfo('partition','name')
    print('need format: %s' % sda)
    if ext == 'xfs' or ext == 'reiserfs':
        cmd1 = 'sudo mkfs.' + ext + ' ' + sda + ' -f'
    elif ext == 'vfat':
        cmd1 = 'sudo mkfs.' + ext + ' ' + sda
    else:
        cmd1 = 'sudo mkfs.' + ext + ' -F ' + sda
    cmd2 = 'sudo mount ' + sda + ' /mnt'
    print('cmd1 = %s' % cmd1)
    print('cmd2 = %s' % cmd2)
    subprocess.check_call(cmd1,shell=True)
    subprocess.check_call(cmd2,shell=True)
    rootcmds = cmdlist
    output = subprocess.getoutput("df -hl /dev/sda4 |awk 'END{print $NF}'")
    print(output)
    if output == '/mnt':
        for rootcmd in rootcmds:
           subprocess.check_call('sudo ' + rootcmd,shell=True)
        subprocess.check_call('sudo ls -R /mnt',shell=True)
    else:
        raise Exception('mount did not successed!')


def chroot(*cmds):
    for cmd in cmds:
        subprocess.check_call('sudo '+ cmd,shell=True)
