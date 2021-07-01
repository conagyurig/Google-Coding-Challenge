"""A video playlist class."""
from .video_library import VideoLibrary

class Playlist:
    """A class used to represent a Playlist."""
    playlists = {}
    def __init__(self):
        self._video_library = VideoLibrary()
        self.playlists = {}

    
        
        
