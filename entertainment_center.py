import media
import fresh_tomatoes

'''
Set the movie objects and their properties
    title: the title of the movie
    story_line: short description of the movie
    poster_image_url: url to the poster image of the movie
    trailer_youtube_url: url to the youtube trailer of the movie
'''
ready_player_one = media.Movie(
    "Ready Player One",
    "When the creator of a virtual reality world called the OASIS dies, he releases a video in which he challenges all OASIS users to find his Easter Egg, which will give the finder his fortune.",
    "https://upload.wikimedia.org/wikipedia/en/7/74/Ready_Player_One_%28film%29.png",
    "https://www.youtube.com/watch?v=cSp1dM2Vj48")
iron_man = media.Movie(
    "Iron Man",
    "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=7H0yo-lDuk0")
last_crusade = media.Movie(
    "Indiana Jones and the Last Crusade",
    "In 1938, after his father Professor Henry Jones, Sr. goes missing while pursuing the Holy Grail, Indiana Jones finds himself up against Adolf Hitler's Nazis again to stop them obtaining its powers.",
    "https://upload.wikimedia.org/wikipedia/en/8/8c/Indiana_Jones_and_the_Last_Crusade.png",
    "https://www.youtube.com/watch?v=a6JB2suJYHM")
school_of_rock = media.Movie(
    "School of Rock",
    "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")
speed_racer = media.Movie(
    "Speed Racer",
    "A young driver, Speed Racer, aspires to be champion of the racing world with the help of his family and his high-tech Mach 5 automobile.",
    "https://upload.wikimedia.org/wikipedia/en/8/82/Speed_racer_ver5_xlg.jpg",
    "https://www.youtube.com/watch?v=8V8sLlqJB2w")
avengers = media.Movie(
    "The Avengers",
    "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

'''
Set movies in array list
'''
movies = [ready_player_one,iron_man,last_crusade,school_of_rock,speed_racer,avengers]

'''
Call open_movies_page method with the movies array passed in
'''
fresh_tomatoes.open_movies_page(movies)
