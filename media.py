import webbrowser

class Movie():
    '''
    Define the Movie class
    '''

    def __init__(self, title, story_line, poster_image_url, trailer_youtube_url):
        '''
        Initializes the Movie object

        :param title: string that holds the title of the movie
        :param story_line: string that holds description of the movie
        :param poster_image_url: string that holds the url of the movie poster
        :param trailer_youtube_url: string that holds the url of the movie trailer
        '''
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        '''
        :return: opens and shows the movie trailer in a web page
        '''
        webbrowser.open(self.trailer_youtube_url)
