class Movie:
    all = []
    
    def __init__(self, title):
        self.title = title
        self._reviews = []
        self._reviewers = []
        Movie.all.append(self)

    # title property goes here!

    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception('Title must be a string and not empty')

    title = property(get_title, set_title)

    def add_review(self, review):
        self.set_reviews(review)
        self.set_reviewers(review.viewer)

    def get_reviews(self):
        return self._reviews
    
    def set_reviews(self, review):
        self._reviews.append(review)

    reviews = property(get_reviews, set_reviews)

    def get_reviewers(self):
        return self._reviewers
    
    def set_reviewers(self, reviewer):
        self._reviewers.append(reviewer)

    reviewers = property(get_reviewers, set_reviewers)
    

    def average_rating(self):
        rating = 0
        for review in self.reviews:
            rating += review.rating
        return rating/len(self.reviews)

    @classmethod
    def highest_rated(cls):
        # movie_ratings = {}
        # for movie in cls.all:
        #     if movie not in movie_ratings:
        #         movie_ratings[movie] = movie.average_rating()
        # return max(movie_ratings, key=movie_ratings.get)
        return max(cls.all, key=lambda movie: movie.average_rating())
