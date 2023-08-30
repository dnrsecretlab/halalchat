import os
import time
import random

try:
	import keyboard
except:
	os.system("pip install keyboard")
	os.system("cls")

import keyboard

def get_messages():
	with open("messages.txt", 'r') as file:
		return file.read().splitlines()

def get_message():
	messages = get_messages()
	return random.choice(messages)

def send_message():
	keyboard.press_and_release("y")
	time.sleep(0.05)

	keyboard.write(get_message())
	time.sleep(0.05)

	keyboard.press_and_release("enter")

def main():
	key = input("Key\n >>> ").lower()
	while True:
		if keyboard.is_pressed(key):
			send_message()

if __name__ == "__main__":
	main()