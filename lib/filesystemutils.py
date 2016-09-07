#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect

mypasswd = 'a'
cmdlist = ['touch /mnt/a.txt','mkdir /mnt/中文','mkdir /mnt/test','mkdir /mnt/中文test', 
            'touch /mnt/中文/中文.txt','touch /mnt/中文/test.txt','touch /mnt/中文/中文test.txt', 
            'touch /mnt/test/中文.txt','touch /mnt/test/test.txt','touch /mnt/test/中文test.txt', 
            'touch /mnt/中文test/中文.txt','touch /mnt/中文test/test.txt','touch /mnt/中文test/中文test.txt']

def mkextx(ext,sda,*rootcmds):
    if ext == 'xfs':
        cmd1 = 'mkfs.' + ext + ' /dev/' + sda + ' -f'
    else:
        cmd1 = 'mkfs.' + ext + ' /dev/' + sda
    cmd2 = 'mount /dev/' + sda + ' /mnt'
    c = pexpect.spawnu('sudo su - root')
    c.expect('sudo')
    c.sendline(mypasswd)
    c.expect('root')
    c.sendline(cmd1)
    c.expect('#')
    c.sendline('y')
    c.expect('root', timeout=60)
    c.sendline(cmd2)
    print(c.before)
    c.expect('root', timeout=60)
    print(c.before)
    rootcmds = cmdlist
    for rootcmd in rootcmds:
        c.sendline(rootcmd)
        c.expect('root', timeout=60)
        print(c.before)
    c.sendline('ls -R /mnt')
    c.expect('root')
    c.sendline('exit')
    c.interact()

def chroot(*cmds):
    c = pexpect.spawnu('sudo su - root')
    c.expect('sudo')
    c.sendline(mypasswd)
    c.expect('root')
    for cmd in cmds:
        c.sendline(cmd)
        c.expect('#',timeout=60)
        print(c.before)
    c.sendline('exit')
    c.interact()