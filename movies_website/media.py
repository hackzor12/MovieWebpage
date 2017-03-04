import webbrowser

#This class represents the skeloton for a movie
class Movie():
	#These are valid ratings and a modular/global level variable in this class
	valid_ratings =["G","PG","PG-13","R"]

	#This is the constructor for our class it defines the instance level variables associated with our class/object
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		#Instance Level Variables
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

		#This function uses a webbrowser function that we imported from the python standard library 
		#to open a web page
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)