import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl

if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(__file__)

file_path = os.path.join(base_dir, './patapim.mp4')

class SimpleVideoApp(QMainWindow):
    def __init__(self, video_source):
        super().__init__()
        self.setWindowTitle("PATAPIM 67 67 67")
        self.resize(1280, 720)

        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.video_widget)
        self.audio_output.setVolume(0.8)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.addWidget(self.video_widget)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.media_player.setSource(QUrl.fromLocalFile(video_source))
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    player = SimpleVideoApp(file_path)
    player.show()
    
    sys.exit(app.exec())