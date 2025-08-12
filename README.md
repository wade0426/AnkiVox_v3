# Gemini Anki TTS

## 專案簡介

Gemini Anki TTS 是一個專為 Anki 學習設計的文字轉語音工具。本程式能夠自動化將音訊檔案移動到 Anki 媒體資料夾、進行格式轉換、調整播放速度，並自動生成 Anki 音訊標籤，大幅簡化語音卡片的製作流程。

## 功能特色

- **自動化流程**：一鍵完成檔案移動、重新命名和 Anki 標籤生成
- **簡易操作介面**：清晰的指令提示，方便使用者操作
- **高度可自訂性**：可自訂 FFmpeg 路徑、Anki 媒體資料夾路徑以及目標音訊格式
- **格式轉換**：支援將原始音訊檔案轉換為 `mp3` 或 `wav` 格式
- **音訊播放速度調整**：可自訂音訊的播放速度，並透過 FFmpeg 進行處理
- **剪貼簿整合**：自動將 Anki 所需的 `[sound:...]` 標籤複製到剪貼簿

## 安裝需求

### Python 依賴
```bash
pip install -r requirements.txt
```

### 外部軟體
- **FFmpeg**：用於音訊格式轉換和變速處理
  - 下載地址：https://ffmpeg.org/download.html
  - 請確保 FFmpeg 可執行檔的路徑正確設定

## 使用方法

### 1. 啟動程式
```bash
python main.py
```

### 2. 主選單操作
程式啟動後會顯示主選單：
```
--- Gemini Anki TTS ---
按 Enter 將檔案移動到Anki資料夾，'s' 進入設定，'c'複製 Prompt，'q' 退出。
```

### 3. 操作說明

#### 按 `Enter` - 處理音訊檔案
- 自動讀取來源音訊檔案
- 根據設定進行格式轉換或變速處理
- 移動檔案至 Anki 媒體資料夾並重新命名
- 將 Anki 音訊標籤複製到剪貼簿

#### 按 `s` - 設定模式
可設定以下項目：
- **來源檔案路徑**：音訊檔案的來源位置
- **FFmpeg 執行檔路徑**：FFmpeg 程式的完整路徑
- **Anki 媒體資料夾路徑**：Anki 的 collection.media 資料夾路徑
- **音訊格式**：目標格式（mp3 或 wav）
- **播放速度**：音訊播放速度（0.1-3.0 倍速）

#### 按 `c` - 複製 Prompt
- 複製預設或自訂的提示詞到剪貼簿
- 可建立 `Prompt.txt` 檔案來自訂提示詞內容

#### 按 `q` - 退出程式

## 設定檔說明

程式會自動建立 `config.json` 設定檔，預設內容如下：

```json
{
    "source_path": "D:\\下載.wav",
    "ffmpeg_path": "D:\\Code\\ffmpeg\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe",
    "anki_media_path": "C:\\Users\\Admin\\AppData\\Roaming\\Anki2\\使用者 1\\collection.media",
    "audio_format": "wav",
    "playback_speed": 1.0
}
```

## 檔案命名規則

處理後的音訊檔案會以下列格式命名：
```
gemini-20240812_174739.wav
```
格式：`gemini-年月日_時分秒.副檔名`

## 注意事項

1. 請確保 FFmpeg 已正確安裝並可在指定路徑執行
2. 確認 Anki 媒體資料夾路徑正確
3. 來源音訊檔案路徑需要存在且可讀取
4. 程式會自動刪除原始檔案（請先備份重要檔案）

## 故障排除

### 常見問題
- **FFmpeg 錯誤**：檢查 FFmpeg 路徑是否正確
- **檔案不存在**：確認來源檔案和 Anki 媒體資料夾路徑
- **權限錯誤**：確認有足夠的檔案讀寫權限

## 授權

本專案採用 MIT 授權條款。

