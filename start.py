#!/bin/usr/python3.8.x
# ----/ coding:utf-8 \----#
# MD5 Hash Encode & Decode Text

'''
The Hash only MD5, not support hash other
-/LeON
'''

import os,sys,hashlib
from time import sleep

class Main:
	def __init__(self):
		self.n1=['1','01']
		self.n2=['2','02']
		self.n0=['0','00']
		self.pil=("~ # ")
		self.Menu()
	
	def Menu(self):
		os.system('clear')
		print("""
--=| MD5 Hasher, Coded by : LeON |=-,-

( 01 ) Encode
( 02 ) Decode
( 00 ) Exit
		""")
		choose = input(self.pil)
		if choose in self.n1:
			text = input("\n[?] Text    : ")
			enc = hashlib.md5(text.encode()).hexdigest()
			print("[!] Results : %s "%(enc))
			print("\n")
		elif choose in self.n2:
			text = str(input("\n[?] Text   : "))
			try:
				wordlist = open('wordlist.txt','r').read()
			except IOError:
				exit("[ Error ] Not found Wordlist, please don't remove ',wordlist.txt'")
			list = [wlist for wlist in wordlist.strip('\n').split('\n')]
			result = ''
			method = ''
			try:
				for wordlists in list:
					if hashlib.md5(wordlists.encode()).hexdigest() in text:
						result = wordlists
						method = 'md5'
						break
			except KeyboardInterrupt:
				exit()
			if len(result) > 0:
				print("[!] Result : %s"%(result))
			else:
				exit("Not Found")
		elif choose in self.n0:
			exit("Exit the program")
		else:
			exit("Enter the number, lol")
			
if __name__=='__main__':
	Main()