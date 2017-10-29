from random import randint
from queue import *

def shuffle_with_queue(artists, num_of_songs, init_val):
	list_length = 0
	for elem in num_of_songs:
		list_length += elem
	res = [init_val] * list_length
	q = init_queue(list_length)

	#maybe consider using PQueue?

def init_queue(list_length):
	q = Queue(maxsize=list_length)
	for i in range(list_length):
		q.put(i)
	return q

def shuffle(artists, num_of_songs, init_val):
	list_length = 0
	for elem in num_of_songs:
		list_length += elem
	res = [init_val] * list_length
	for i in range(len(artists)):
		song_number = num_of_songs[i]
		for j in range(song_number):
			max_offset = list_length / song_number
			offset = get_offset(max_offset)
			place(res, offset + (max_offset*j), init_val, artists[i])
	return res

def place(res, start_index, init_val, artist):
	i = start_index
	while res[i] != init_val:
		if i==len(res)-1: i = 0
		else: i += 1
	res[i] = artist

def get_offset(max_offset):
	return randint(0, max_offset-1)

if __name__ == '__main__':
	temp = raw_input("Enter the number of artists: ").strip()
	artist_number = int(temp)
	artists = []
	num_of_songs = []
	for i in range(artist_number):
		question = "What is the name of Artist " + str(i) + "? :"
		artist = raw_input(question)
		artists.append(artist)
		question = "How many songs does " + artist + " have? :"
		song_number = raw_input(question)
		num_of_songs.append(int(song_number))
	res = shuffle(artists, num_of_songs, -1)
	print "RES: ", res