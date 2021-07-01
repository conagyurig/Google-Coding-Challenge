"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    playing = " "
    paused = False
    playlists = {}
    playlistnames = []
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = " "
        self.playlistnames = []
        self.playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        vids = self._video_library.get_all_videos()
        deck = {}
        for vid in vids:
            deck[vid.title] = (vid.video_id, vid.tags)
        decklist = sorted(deck)
        print("Here's a list of all available videos:")
        for key in decklist:
            id = deck[key][0]
            tags = ''
            for tag in deck[key][1]:
                tags = tags + tag + ' '
            tags = tags[:-1]
            print(" " +key + " (" + id + ") [" + tags + "]") 


    def play_video(self, video_id):
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """
        vid = self._video_library.get_video(video_id)
        if vid == None:
            print("Cannot play video: Video does not exist")
            return
        if self.playing != " ":
            vid2 = self._video_library.get_video(self.playing)
            print("Stopping video: " + vid2.title)
        self.playing = video_id
        self.paused = False
        print("Playing video: " + vid.title)

    def stop_video(self):
        """Stops the current video."""
        vid = self._video_library.get_video(self.playing)
        if vid == None:
            print("Cannot stop video: No video is currently playing")
            return
        self.playing = " "
        print("Stopping video: " + vid.title)
        

    def play_random_video(self):
        """Plays a random video from the video library."""
        max = len(self._video_library.get_all_videos())
        vids = self._video_library.get_all_videos()
        id = random.randint(0,max)
        vidId = ""
        count = 0
        name = ""
        if self.playing != " ":
            print("Stopping video: " + self._video_library.get_video(self.playing).title)
        for vid in vids:
            name = vid.title
            vidId = vid.video_id
            if count == id:
                break
            count = count+1
        print("Playing video: " + name)
        self.playing = vidId
        self.paused = False

    def pause_video(self):
        """Pauses the current video."""
        if self.playing == " ":
            print("Cannot pause video: No video is currently playing")
            return
        if self.paused == True:
            print("Video already paused: " + self._video_library.get_video(self.playing).title)
            return
        self.paused = True
        print("Pausing video: " + self._video_library.get_video(self.playing).title)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.playing == " ":
            print("Cannot continue video: No video is currently playing")
            return
        if self.paused == False:
            print("Cannot continue video: Video is not paused")
            return
        self.paused = False
        print("Continuing video: " + self._video_library.get_video(self.playing).title)

    def show_playing(self):
        """Displays video currently playing."""
        if self.playing == " ":
            print("No video is currently playing")
            return
        name = self._video_library.get_video(self.playing).title
        id = self._video_library.get_video(self.playing).video_id
        tags = self._video_library.get_video(self.playing).tags
        tag2 = ""
        for tag in tags:
            tag2 = tag2 + tag + " "
        tag2 = tag2[:-1]
        if self.paused == True:
            print("Currently playing: " + name + " (" + id + ") [" + tag2 + "] - PAUSED")
            return
        print("Currently playing: " + name + " (" + id + ") [" + tag2 + "]")
        

        

    def create_playlist(self, playlist_name):
        if " " in playlist_name:
            print("Cannot create playlist: whitespace")
            return
        if playlist_name.lower() in self.playlists.keys():
            print("Cannot create playlist: A playlist with the same name already exists ")
            return
        self.playlists[playlist_name.lower()] = []
        self.playlistnames.append(playlist_name)
        print("Successfully created new playlist: " + playlist_name)
        

    def add_to_playlist(self, playlist_name, video_id):
        if playlist_name.lower() not in self.playlists.keys():
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")
            return
        vid = self._video_library.get_video(video_id)
        if vid == None:
            print("Cannot add video to " + playlist_name + ": Video does not exist")
            return
        playlist = self.playlists[playlist_name.lower()]
        if video_id in playlist:
            print("Cannot add video to " + playlist_name + ": Video already added")
            return
        playlist.append(video_id)
        self.playlists[playlist_name.lower()] = playlist
        print("Added video to " + playlist_name + ": " + self._video_library.get_video(video_id).title)

    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlistnames == []:
            print("No playlists exist yet")
            return
        print("Showing all playlists:")
        display = sorted(self.playlistnames)
        for name in display:
            print(" " + name)


    def show_playlist(self, playlist_name):
        if playlist_name.lower() not in self.playlists.keys():
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")
            return
        print("Showing playlist: " + playlist_name)
        playlist = self.playlists[playlist_name.lower()]
        if playlist == []:
            print("No videos here yet")
            return
        for vids in playlist:
            name = self._video_library.get_video(vids).title
            id = self._video_library.get_video(vids).video_id
            tags = self._video_library.get_video(vids).tags
            tag2 = ""
            for tag in tags:
                tag2 = tag2 + tag + " "
            tag2 = tag2[:-1]
            print(" " + name + " (" + id + ") [" + tag2 + "]")
        

    def remove_from_playlist(self, playlist_name, video_id):
        if playlist_name.lower() not in self.playlists.keys():
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")
            return
        vid = self._video_library.get_video(video_id)
        if vid == None:
            print("Cannot remove video from " + playlist_name + ": Video does not exist")
            return
        playlist = self.playlists[playlist_name.lower()]
        if video_id not in playlist:
            print("Cannot remove video from " + playlist_name + ": Video is not in playlist")
            return
        playlist.remove(video_id)
        self.playlists[playlist_name.lower()] = playlist
        print("Removed video from " + playlist_name + ": " + self._video_library.get_video(video_id).title)


    def clear_playlist(self, playlist_name):
        if playlist_name.lower() not in self.playlists.keys():
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")
            return
        self.playlists[playlist_name.lower()] = []
        print("Successfully removed all videos from " + playlist_name)

    def delete_playlist(self, playlist_name):
        if playlist_name.lower() not in self.playlists.keys():
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")
            return
        del self.playlists[playlist_name.lower()]
        print("Deleted playlist: " + playlist_name)

    def search_videos(self, search_term):
        videos = self._video_library.get_all_videos()
        results = {}
        for vid in videos:
            name = vid.title
            nameL = name.lower()
            if search_term.lower() in nameL:
                name = vid.title
                id = vid.video_id
                tags = vid.tags
                tag2 = ""
                for tag in tags:
                    tag2 = tag2 + tag + " "
                tag2 = tag2[:-1]
                results[name] = (id,tag2)
                #results[name] = " (" + id + ") [" + tag2 + "]"
        
        if len(results) == 0:
            print("No search results for " + search_term)
            return
        print("Here are the results for "+ search_term + ":")
        resultnames = results.keys()
        resultnames = sorted(resultnames)
        for i in range(len(resultnames)):
            index = i+1
            print(str(index) + ") " + resultnames[i] + " (" + results[resultnames[i]][0] + ") [" + results[resultnames[i]][1] + "]")
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        flag = True
        while flag == True:
            command = input()
            if not command.isnumeric():
                return
            choice = int(command)-1
            if choice > (len(resultnames)-1) or choice < 0:
                return
                flag = False
                return
            self.play_video(results[resultnames[choice]][0])
            flag = False

        

    def search_videos_tag(self, video_tag):
        videos = self._video_library.get_all_videos()
        results = {}
        for vid in videos:
            name = vid.title
            id = vid.video_id
            tags = vid.tags
            for tag in tags:
                tagl = tag.lower()
                intagl = video_tag.lower()
                if tagl == intagl:
                    tag2 = ""
                    for tag3 in tags:
                        tag2 = tag2 + tag3 + " "
                    tag2 = tag2[:-1]
                    results[name] = (id,tag2)
        if len(results) == 0:
            print("No search results for " + video_tag)
            return
        print("Here are the results for "+ video_tag + ":")
        resultnames = results.keys()
        resultnames = sorted(resultnames)
        for i in range(len(resultnames)):
            index = i+1
            print(str(index) + ") " + resultnames[i] + " (" + results[resultnames[i]][0] + ") [" + results[resultnames[i]][1] + "]")
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        flag = True
        while flag == True:
            command = input()
            if not command.isnumeric():
                return
            choice = int(command)-1
            if choice > (len(resultnames)-1) or choice < 0:
                return
                flag = False
                return
            self.play_video(results[resultnames[choice]][0])
            flag = False

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
