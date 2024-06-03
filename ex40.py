class Song(object):
   def __init__(self, lyrics): # Song class is defined with an __init__ method that takes lyrics as a parameter and stores it in self.lyrics
       self.lyrics = lyrics

   def sing_me_a_song(self): # defines a function sing_me_a_song 
    for line in self.lyrics: # checks line is there in self.lyrics
      print(line)

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song() #prints each line of the happy_bday lyrics.

bulls_on_parade.sing_me_a_song() # prints each line of the bulls_on_parade lyrics.