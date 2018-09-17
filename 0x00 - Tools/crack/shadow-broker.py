#! /usr/bin/python

"""
	Simple shadow crack python script
"""

import sys
import crypt

OKGREEN = '\033[92m'
OKBLUE 	= '\033[94m'
YELLOW 	= '\033[93m'
RESET 	= '\033[0m'
BOLD    = '\33[1m'
RED = '\033[91m'

"""
	Check arguments
"""
def check_args():
	arguments_size = len(sys.argv)

	if arguments_size != 2:
		print(BOLD + RED + "[!] Missing arguments")
		print("[!] Example: " + sys.argv[0] + " [worlist path]")
		print("[!] Usage: " + sys.argv[0] + " /path/to/my_passwords_list.txt" + RESET)

		sys.exit()


"""
	Basic usage info
"""
def info():
	print(BOLD + YELLOW + "[+] BASIC USAGE")
	print("[+] Shadow: $1$DUr3zqwq$mtnfrf.wtqmy6tyvzS/Xs1")
	print("[+] Salt: $1$DUr3zqwq$")
	print("[+] Encrypted password: mtnfrf.wtqmy6tyvzS/Xs1")
	print(RESET)


"""
	Get all passwords from given list
"""
def get_passwords_from_list():
	global passwords_list

	passwords_list = open(sys.argv[1], "r").read()


"""
	Colect salt and encrypted password
"""
def information_gathering():
	global salt
	global encrypt_passwd

	salt = raw_input(BOLD + "[*] Salt: ")
	encrypt_passwd = raw_input(BOLD + "[*] Encrypted password: ")
	print("")


def show_info():
	print(BOLD + "[+] Information")
	print("[+] Shadow: " + salt + encrypt_passwd)
	print("[+] Number of passwords: " + str(len(passwords_list.split())))
	print(RESET)

"""
	Password Crack
"""
def crack():
	shadow = salt + encrypt_passwd

	print(BOLD + "[+] Cracking shadow")
	print("[+] This may take a while")
	print(RESET)

	for password in passwords_list.split():
		crypt_passwd = crypt.crypt(password, salt)

		if crypt_passwd == shadow:
			print(BOLD + OKGREEN + "[#] Password: " + password + RESET)

			sys.exit()

	print(BOLD + RED + "[404] Password not found" + RESET)
		


"""
	Main function
"""
def main():
	check_args()

	info()
	get_passwords_from_list()
	information_gathering()
	show_info()
	crack()

main()