# import subprocess
import yt_dlp
import sys

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

# 1. Always create the app first
app = QApplication(sys.argv)

# 2. Create main window
window = QMainWindow()
window.setWindowTitle("Videos Downloader")
window.setGeometry(100, 100, 400, 300)  # x, y, width, height

# 3. Central widget + layout
central = QWidget()
window.setCentralWidget(central)
layout = QVBoxLayout(central)

# 4. Add widgets
debuging = QLabel("", )
debuging.setStyleSheet("font-size: 25px;")
input_field = QLineEdit()
input_field.setPlaceholderText("Enter video url ...")
button = QPushButton("Download")

def OnClickDownload():
    inputtextnospace = input_field.text().replace(" ", "")
    debuging.setText("Downloading ...")
    if (downloadUrl(inputtextnospace) == True):
        debuging.setText("Download complete! ✅")
        return
    else:
        debuging.setText("Download failed. ❌")
        return

button.clicked.connect(OnClickDownload)

# layout.addWidget(label)
layout.addWidget(input_field)
layout.addWidget(button)
layout.addWidget(debuging)

# 7. Show and run
window.show()
sys.exit(app.exec_())