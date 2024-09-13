# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: Movie object finder within Streaming Service dictionaries using Streaming Guide list organizer
# 3 Separate classes for each tool/ object category to retrieve objects inside of dictionary inside a list
# Contains method to determine if movie title exists in any recorded streaming service.
# Print services with movie, year of movie, and title.


class Movie:
    """Represents a movie"""

    def __init__(self, title, genre, director, year):
        """Creates data members for Movie to include: title, genre, director, and year"""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = int(year)

    def get_title(self):
        """Affirms the title is a private data member of Movie that should be accessed using get method"""
        return self._title

    def get_genre(self):
        """Affirms the genre is a private data member of Movie that should be accessed using get method"""
        return self._genre

    def get_director(self):
        """Affirms the director is a private data member of Movie that should be accessed using get method"""
        return self._director

    def get_year(self):
        """Affirms the year is a private data member of Movie that should be accessed using get method"""
        return self._year


class StreamingService:
    """Represents a streaming service"""

    def __init__(self, name):
        """Creates data members for StreamingService to include: name and catalog"""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Affirms the name is a private data member of StreamingService that should be accessed using get method"""
        return self._name

    def get_catalog(self):
        """Affirms the name is a private data member of StreamingService that should be accessed using get method"""
        return self._catalog

    def add_movie(self, movie_object):
        """Adds Movie object to catalog"""
        title = movie_object.get_title()
        self._catalog[title] = movie_object

    def delete_movie(self, movie_title):
        """Deletes Movie object from catalog"""
        if movie_title in self._catalog:
            self._catalog.pop(movie_title)
        else:
            print(movie_title, "not found in:", self._name)


class StreamingGuide:
    """Represents Streaming Services"""

    def __init__(self):
        """Takes no argument, but initializes the data member to an empty list"""
        self._guide = []  # List for streaming guide to iterate through once filled

    def add_streaming_service(self, stream_serv_obj):
        """Adds streaming service to guide list"""
        self._guide.append(stream_serv_obj)

    def delete_streaming_service(self, stream_serv_name):
        """Removes streaming service from guide list"""
        for stream_service in self._guide:
            # Compare names of input to names in streaming services, remove if match is found
            if stream_service.get_name() == stream_serv_name:
                self._guide.remove(stream_service)
        else:
            print(stream_serv_name, "not found.")

    def who_streams_this_movie(self, movie_title):
        """Takes movie title and returns dictionary that contains title, year, and streaming services offering movie"""
        for stream_service in self._guide:
            catalog = stream_service.get_catalog()
            
            if movie_title in catalog:
                movie = catalog[movie_title]
                year = movie.get_year()
                services = [stream_services.get_name() for stream_services in self._guide if movie_title in
                            stream_services.get_catalog()]
                return print({'title': movie_title, 'year': year, 'services': services})
        
        return print("No results")


if __name__ == '__main__':
    movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
    movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
    movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
    movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

    stream_serv_1 = StreamingService('Netflick')
    stream_serv_1.add_movie(movie_3)

    stream_serv_2 = StreamingService('Hula')
    stream_serv_2.add_movie(movie_1)
    stream_serv_2.add_movie(movie_4)
    stream_serv_2.delete_movie('The Seventh Seal')
    stream_serv_2.add_movie(movie_2)

    stream_serv_3 = StreamingService('Dizzy+')
    stream_serv_3.add_movie(movie_4)
    stream_serv_3.add_movie(movie_3)
    stream_serv_3.add_movie(movie_1)

    stream_guide = StreamingGuide()
    stream_guide.add_streaming_service(stream_serv_1)
    stream_guide.add_streaming_service(stream_serv_2)
    stream_guide.add_streaming_service(stream_serv_3)
    stream_guide.delete_streaming_service('Hula')
    search_results = stream_guide.who_streams_this_movie('Little Women')
