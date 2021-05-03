import rumps
import pafy
import vlc


class Funkkopf(rumps.App):
    playing = False
    v = vlc.Instance("--novideo")
    player = v.media_player_new()
    station = 0
    source = [
        "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "https://www.youtube.com/watch?v=DWcJFNfaw9c",
    ]

    def __init__(self):
        super(Funkkopf, self).__init__("lofi radio")

    @rumps.clicked("Play/Pause")
    def play_pause(self, _):
        if self.playing:
            self.pause()
        else:
            self.play()

    def play(self):
        self.prepare_media()
        self.playing = True
        print("Starting lofi radio")
        self.player.play()

    def pause(self):
        self.playing = False
        print("Stopping lofi radio")
        self.player.stop()

    def prepare_media(self):
        media = pafy.new(self.source[self.station])
        url = media.streams[3].url
        media = self.v.media_new(url)
        self.player.set_media(media)

    @rumps.clicked("Next Station")
    def next(self, _):
        self.player.stop()

        if self.station == 0:
            self.station = 1
        else:
            self.station = 0

        self.play()


if __name__ == "__main__":
    Funkkopf().run()
