# import subprocess
import yt_dlp
import sys

# downloading video using yt-dlp
def downloadUrl(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            return True
    except:
        return False

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QLineEdit
)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Videos Downloader")
window.setGeometry(100, 100, 400, 300) 

central = QWidget()
window.setCentralWidget(central)
layout = QVBoxLayout(central)

debuging = QLabel("", )
debuging.setStyleSheet("font-size: 25px;")
input_field = QLineEdit()
input_field.setPlaceholderText("Enter video url ...")
button = QPushButton("Download")

def OnClickDownload():
    inputtextnospace = input_field.text().replace(" ", "")
    debuging.setText("Downloading ...")
    if (downloadUrl(inputtextnospace) == True):
        debuging.setText("Download complete ✅")
        return
    else:
        debuging.setText("Download failed ❌")
        return

button.clicked.connect(OnClickDownload)

layout.addWidget(input_field)
layout.addWidget(button)
layout.addWidget(debuging)

window.show()
sys.exit(app.exec_())