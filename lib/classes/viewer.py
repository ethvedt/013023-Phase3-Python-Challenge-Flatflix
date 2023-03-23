from .review import Review

class Viewer:
    all = []
    
    def __init__(self, username):
        self.username = username
        self._reviews = []
        self._reviewed_movies = []
        Viewer.all.append(username)

    # username property goes here!
    def get_username(self):
        return self._username
    def set_username(self, username):
        if isinstance(username, str) and 5 < len(username) < 17 and username not in Viewer.all:
            self._username = username
        else:
            raise Exception("Username must be a unique string between 6 and 16 characters")
    username = property(get_username, set_username)

    def get_reviews(self):
        return self._reviews 
    def set_reviews(self, review):
        self._reviews.append(review)
    reviews = property(get_reviews, set_reviews)

    def get_reviewed_movies(self):
        return self._reviewed_movies
    def set_reviewed_movies(self, movie):
        self._reviewed_movies.append(movie)
    reviewed_movies = property(get_reviewed_movies, set_reviewed_movies)

    def add_review(self, review):
        self.set_reviews(review)
        self.set_reviewed_movies(review.movie)

    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies
    
    def rate_movie(self, movie, rating):
        for review in self.reviews:
            if review.movie == movie:
                review.rating = rating
                return
        return Review(self, movie, rating)

        
    