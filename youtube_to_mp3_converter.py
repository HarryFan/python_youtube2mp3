from pytube import YouTube
from pydub import AudioSegment

# 設定要下載的影片 URL
url = "https://www.youtube.com/watch?v=7LjXRbCKBIw"

# 建立 YouTube 物件
yt = YouTube(url)

# 取得影片的音軌
audio_stream = yt.streams.filter(only_audio=True).first()

# 下載音軌到指定的路徑
audio_stream.download(output_path="path/to/save/directory", filename="audio")

# 讀取下載下來的音檔
audio_file = AudioSegment.from_file("path/to/save/directory/audio")

# 檢查音檔是否可以正常解碼
print(audio_file)

# 將音檔轉換為 MP3 格式
mp3_file = audio_file.export("path/to/save/directory/audio.mp3", format="mp3")