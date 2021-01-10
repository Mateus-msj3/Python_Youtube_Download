from PyQt5 import uic, QtWidgets
from pytube import YouTube, Playlist
from PyQt5.QtWidgets import QFileDialog, QMessageBox


def dowload_options():

    if view_youtube_dowload.option_video.isChecked():

        dowload_video()

    elif view_youtube_dowload.option_playlist.isChecked():

        download_playlist()

    elif view_youtube_dowload.option_audio.isChecked():

        dowload_audio()

    else:
        alert_msg()


def alert_msg():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText("Escolha uma opção para download")
    msg_box.setWindowTitle("Alerta")
    msg_box.setStandardButtons(QMessageBox.Ok)

    returnValue = msg_box.exec()
    if returnValue == QMessageBox.Ok:
        view_youtube_dowload.show()


def dowload_video():

    video_url = view_youtube_dowload.lineEdit_2.text()
    pasta = QFileDialog.getExistingDirectory()
    youtube = YouTube(video_url)

    for video in youtube.streams:
        video = youtube.streams.get_highest_resolution()
        video.download(pasta)
        break


def download_playlist():

    playlist_url = view_youtube_dowload.lineEdit_2.text()
    pasta = QFileDialog.getExistingDirectory()
    playlist = Playlist(playlist_url)

    for url in playlist:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(pasta)
        break


def dowload_audio():

    video_url = view_youtube_dowload.lineEdit_2.text()
    youtube = YouTube(video_url)
    pasta = QFileDialog.getExistingDirectory()

    for audio in youtube.streams:
        audio = youtube.streams.filter(only_audio=True)[0]
        audio.download(pasta)
        break


# Carregamento da interface do sistema
app = QtWidgets.QApplication([])
view_youtube_dowload = uic.loadUi("home.ui")

# Botões que aciona as defs

view_youtube_dowload.pushButton.clicked.connect(dowload_options)


# Execução da tela home
view_youtube_dowload.show()
app.exec()
