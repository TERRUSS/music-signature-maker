from pysine import sine

import inquirer
import cli_ui

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--scale", type=int, help="specify a scale with it's number ( --list-scales )")
parser.add_argument("--list-scales", action="count", default=0, help="list all the scales")
args = parser.parse_args()

import os, sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    print('\n')


cls()


#### SCALES LIST

if (args.list_scales):

	cli_ui.info_section("All the scales")

	with open("cleanScales.txt") as fp:
		for i, line in enumerate(fp):
			print(f"{i}) {line}", end='')

	print()
	cli_ui.info_3("You can specify a scale with --scale %d")
	print()
	exit(0)



#### SIGNATURE CREATION
cli_ui.info_section("Music Signature Generator")

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nom = inquirer.prompt( [inquirer.Text('nom', message="What's your name")] )['nom'].upper()
signature = []

for x in nom:
	if (x == 'H'):
		x = 'B'

	i = alphabet.index(x)

	signature.append(i%7)



#### SELECTION OF THE SCALE
print()
freq = []
scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
if (args.scale):

	with open("cleanScales.txt") as fp:
		for i, line in enumerate(fp):
			if i == args.scale:
				scale = line.split()[0:7]

else:
	cli_ui.info_3("You can specify a scale with --scale %d")

cli_ui.info_3(f"Scale : {' '.join(scale)}")


#### PLAY THE SIGNATURE
freq = {
	'A': 440.00, 
	'A#': 466.16, 'Bb': 466.16, 
	'B': 493.88, 'Cb': 493.88, 
	'C': 261.63, 'B#': 261.63, 
	'C#': 277.18, 'Db': 277.18,
	'D': 293.66,
	'D#': 311.13, 'Eb': 311.13,
	'E': 329.63, 'Fb': 329.63, 
	'F': 349.23, 'E#': 349.23,
	'F#': 369.99, 'Gb': 369.99,
	'G': 392.00,
	'G#': 415.30, 'Ab': 415.30,
	'H': 493.88
}


for index, i in enumerate(signature):
	if (index != len(signature)): cli_ui.dot()
	else : cli_ui.dot(last=True)
	sine(frequency=freq[ scale[i] ], duration=0.5)

print()
for i in signature:
	print(scale[i]+' ', end='')
# cli_ui.info_2(' '.join( [for i in signature: scale[i] ]))
print()