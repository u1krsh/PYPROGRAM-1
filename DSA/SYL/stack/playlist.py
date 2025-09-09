import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_song(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_song(self, data):
        if not self.head:
            print("No song in playlist")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print(f"Song '{data}' not found in playlist")

    def shuffle_playlist(self):
        songs = []
        current = self.head
        while current:
            songs.append(current.data)
            current = current.next

        shuffled = []
        while songs:
            song = random.choice(songs)
            shuffled.append(song)
            songs.remove(song)
        print("Shuffled playlist:", shuffled)


