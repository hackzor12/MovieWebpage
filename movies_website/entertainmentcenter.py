#importing modules
import media
import freshtomatoes

#These are instances of objects that represent my favorite movies in the format (TITLE, DESCRIPTION, COVER IMAGE, YOUTUBE TRAILER LINK)

#Mr Nobody is my favorite movie!
mrNobody = media.Movie("Mr. Nobody", 
	"A boy stands on a station platform as a train is about to leave. Should he go with his mother or stay with his father? Infinite possibilities arise from this decision. As long as he doesn't choose, anything is possible.", 
	"https://images-na.ssl-images-amazon.com/images/I/51ulC1aDjtL.jpg", 
	"https://www.youtube.com/watch?v=mpi0qsp3v_w")

#Darjeeling Limited is a story about 3 brothers traveling
darjeelingLimited = media.Movie("Darjeeling Limited", 
	"A year after their father's funeral, three brothers travel across India by train in an attempt to bond with each other.", 
	"https://upload.wikimedia.org/wikipedia/en/1/1e/Darjeeling_Limited_Poster.jpg", 
	"https://www.youtube.com/watch?v=ipybfk2lh6A")

#Cosmopolis is quite strange
cosmopolis = media.Movie("Cosmopolis", 
	"Riding across Manhattan in a stretch limo in order to get a haircut, a 28-year-old billionaire asset manager's day devolves into an odyssey with a cast of characters that start to tear his world apart.", 
	"https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/Cosmopolis_Poster.jpg/220px-Cosmopolis_Poster.jpg", 
	"https://www.youtube.com/watch?v=3DUdOVGXkuM")

#A movie about a special forces tank unit in WW2
fury = media.Movie("Fury",
 "A grizzled tank commander makes tough decisions as he and his crew fight their way across Germany in April, 1945.", 
 "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4MDU0NTUyN15BMl5BanBnXkFtZTgwMzQxMzY4MjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", 
 "https://www.youtube.com/watch?v=SKu5lGfRBxc")

#Donnie Darko classic
donnieDarko = media.Movie("Donnie Darko", 
	"A troubled teenager is plagued by visions of a man in a large rabbit suit who manipulates him to commit a series of crimes, after he narrowly escapes a bizarre accident.",
	 "http://i.ebayimg.com/images/i/320829347561-0-1/s-l1000.jpg",
	  "https://www.youtube.com/watch?v=ZZyBaFYFySk")

#Abide
theBigLebowski = media.Movie("The Big Lebowski", "\"The Dude\" Lebowski, mistaken for a millionaire Lebowski, seeks restitution for his ruined rug and enlists his bowling buddies to help get it.",
 "https://resizing.flixster.com/HnvdNWu_ezMpAlQOqBnsLJG93Mw=/206x305/v1.bTsxMTE3NzcxNztqOzE3MzE5OzEyMDA7ODAwOzEyMDA", 
 "https://www.youtube.com/watch?v=cd-go0oBF4Y")

#A list of all the movies
movies = [mrNobody,darjeelingLimited,cosmopolis,fury,donnieDarko,theBigLebowski]

#Using an imported module to render the webpage
freshtomatoes.open_movies_page(movies)
