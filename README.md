Youtube to MP3 轉換器
==================

這個專案提供了一個簡單的程式，讓你可以從 YouTube 下載音軌並轉換成 MP3 格式。

系統需求
----

*   Python 3.x
    
*   pip
    

安裝
--

1.  下載或克隆這個專案至本地端。
    
2.  在終端機中移動到專案資料夾的根目錄下。
    
3.  安裝必要的套件: `pip3 install -r requirements.txt`
    

使用方法
----

1.  打開 `youtube_to_mp3_converter.py` 檔案。
    
2.  修改 `url` 變數為你要下載的 YouTube 影片網址。
    
3.  修改 `output_path` 變數為你要存放轉換後的 MP3 檔案的路徑。
    
4.  執行 `python3 youtube_to_mp3_converter.py`。
    
5.  程式將會下載音軌並將其轉換為 MP3 格式，然後儲存在指定的 `output_path` 中。
    

注意事項
----

*   該程式僅支援下載 YouTube 影片的音軌，不支援下載影像。
    
*   程式下載的音軌格式為 M4A，需進行轉換成 MP3 格式。
    
*   使用本程式轉換時，請注意版權法規定，務必遵守相關法律規定。