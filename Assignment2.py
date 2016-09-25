#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import codecs
import crypt
import argparse


def getPassword(shadowPath, username):
	shadowFile = open (shadowPath,'r')
	for line in shadowFile.readlines():
		if line.split(':')[0] == username:
			
			passwd = line.split(':')[1]
			
			return passwd
			


def compare(passwd):
	wordlist = open ('/usr/share/dict/american-english' , 'r')
	salt = '$' + passwd.split('$')[1] + '$' + passwd.split('$')[2]
	hash = passwd.split('$')[3]
	victory = False

	for line in wordlist.readlines():
		if crypt.crypt(line.split()[0],salt) == passwd:
			print ('Password is: ' + line)
			victory = True
			break
	if victory == False:
		print 'Password was not in dictionary ( ͡° ʖ̯ ͡°)'	

def main(argv):

	compare(getPassword(argv[1], argv[2]))


if __name__ == "__main__":
    main(sys.argv)
