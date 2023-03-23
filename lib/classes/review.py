class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        viewer.add_review(self)
        movie.add_review(self)

    # rating property goes here!
    def get_rating(self):
        return self._rating
    
    def set_rating(self, rating):
        if isinstance(rating, int) and 0 < rating < 6:
            self._rating = rating
        else:
            raise Exception("Invalid rating")
    
    rating = property(get_rating, set_rating)

    # viewer property goes here!
    def get_viewer(self):
        return self._viewer
    
    def set_viewer(self, viewer):
        if type(viewer).__name__ == 'Viewer':
            self._viewer = viewer
    
    viewer = property(get_viewer, set_viewer)

    # movie property goes here!
    def get_movie(self):
        return self._movie
    
    def set_movie(self, movie):
        if type(movie).__name__ == 'Movie':
            self._movie = movie
    
    movie = property(get_movie, set_movie)
