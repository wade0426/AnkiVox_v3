import json
import os
import shutil
import subprocess
import pyperclip
from datetime import datetime
import sys


class GeminiAnkiTTS:
    def __init__(self):
        self.config_file = "config.json"
        self.default_config = {
            "source_path": "D:\\下載.wav",
            "ffmpeg_path": "D:\\Code\\ffmpeg\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe",
            "anki_media_path": "C:\\Users\\Admin\\AppData\\Roaming\\Anki2\\使用者 1\\collection.media",
            "audio_format": "wav",
            "playback_speed": 1.0
        }
        
    def load_config(self):
        """載入設定檔"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # 如果檔案不存在，建立預設設定檔
            self.save_config(self.default_config)
            return self.default_config.copy()
    
    def save_config(self, config):
        """儲存設定檔"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    
    def show_menu(self):
        """顯示主選單"""
        print("\n--- Gemini Anki TTS ---")
        print("按 Enter 將檔案移動到Anki資料夾，'s' 進入設定，'c'複製 Prompt，'q' 退出。")
    
    def show_config_menu(self, config):
        """顯示設定選單"""
        print("\n=== 設定頁面 ===")
        print("目前設定：")
        print(f"1. 來源檔案路徑：{config.get('source_path', self.default_config['source_path'])}")
        print(f"2. FFmpeg 執行檔路徑：{config.get('ffmpeg_path', self.default_config['ffmpeg_path'])}")
        print(f"3. Anki 媒體資料夾路徑：{config.get('anki_media_path', self.default_config['anki_media_path'])}")
        print(f"4. 音訊格式：{config.get('audio_format', self.default_config['audio_format'])}")
        print(f"5. 播放速度：{config.get('playback_speed', self.default_config['playback_speed'])}")
        print("\n請輸入數字選擇要修改的設定，或按 'b' 返回主頁面")
    
    def modify_setting(self, config, setting_number):
        """修改特定設定項目"""
        if setting_number == 1:
            # 來源檔案路徑
            current_value = config.get("source_path", self.default_config["source_path"])
            print(f"\n修改來源檔案路徑")
            print(f"目前值：{current_value}")
            new_value = input("請輸入新的來源檔案路徑（留空保持不變）: ").strip()
            if new_value:
                config["source_path"] = new_value
                print("✅ 來源檔案路徑已更新")
            else:
                print("保持原設定不變")
                
        elif setting_number == 2:
            # FFmpeg 執行檔路徑
            current_value = config.get("ffmpeg_path", self.default_config["ffmpeg_path"])
            print(f"\n修改 FFmpeg 執行檔路徑")
            print(f"目前值：{current_value}")
            new_value = input("請輸入新的 FFmpeg 執行檔路徑（留空保持不變）: ").strip()
            if new_value:
                config["ffmpeg_path"] = new_value
                print("✅ FFmpeg 執行檔路徑已更新")
            else:
                print("保持原設定不變")
                
        elif setting_number == 3:
            # Anki 媒體資料夾路徑
            current_value = config.get("anki_media_path", self.default_config["anki_media_path"])
            print(f"\n修改 Anki 媒體資料夾路徑")
            print(f"目前值：{current_value}")
            new_value = input("請輸入新的 Anki 媒體資料夾路徑（留空保持不變）: ").strip()
            if new_value:
                config["anki_media_path"] = new_value
                print("✅ Anki 媒體資料夾路徑已更新")
            else:
                print("保持原設定不變")
                
        elif setting_number == 4:
            # 音訊格式
            current_value = config.get("audio_format", self.default_config["audio_format"])
            print(f"\n修改音訊格式")
            print(f"目前值：{current_value}")
            while True:
                new_value = input("請輸入新的音訊格式 (mp3/wav，留空保持不變): ").strip().lower()
                if not new_value:
                    print("保持原設定不變")
                    break
                if new_value in ["mp3", "wav"]:
                    config["audio_format"] = new_value
                    print("✅ 音訊格式已更新")
                    break
                else:
                    print("❌ 請輸入 'mp3' 或 'wav'")
                    
        elif setting_number == 5:
            # 播放速度
            current_value = config.get("playback_speed", self.default_config["playback_speed"])
            print(f"\n修改播放速度")
            print(f"目前值：{current_value}")
            print("說明：1.0=原速, 1.2=加速20%, 0.8=減速20%")
            while True:
                speed_input = input("請輸入新的播放速度 (0.1-3.0，留空保持不變): ").strip()
                if not speed_input:
                    print("保持原設定不變")
                    break
                try:
                    new_speed = float(speed_input)
                    if 0.1 <= new_speed <= 3.0:
                        config["playback_speed"] = new_speed
                        print("✅ 播放速度已更新")
                        break
                    else:
                        print("❌ 播放速度請設定在 0.1 到 3.0 之間")
                except ValueError:
                    print("❌ 請輸入有效的數字")
    
    def setup_config(self):
        """設定模式 - 新的互動式設定介面"""
        config = self.load_config()
        
        while True:
            self.show_config_menu(config)
            
            try:
                user_choice = input("請選擇: ").strip().lower()
                
                if user_choice == 'b':
                    # 儲存設定並返回主頁面
                    self.save_config(config)
                    print("設定已儲存，返回主頁面")
                    break
                elif user_choice.isdigit():
                    choice_num = int(user_choice)
                    if 1 <= choice_num <= 5:
                        self.modify_setting(config, choice_num)
                        # 修改完成後暫停一下讓使用者看到確認訊息
                        input("\n按 Enter 繼續...")
                    else:
                        print("❌ 請輸入 1-5 的數字或 'b'")
                        input("按 Enter 繼續...")
                else:
                    print("❌ 請輸入 1-5 的數字或 'b'")
                    input("按 Enter 繼續...")
                    
            except ValueError:
                print("❌ 輸入格式錯誤，請重新輸入")
                input("按 Enter 繼續...")
            except KeyboardInterrupt:
                print("\n設定已取消，返回主頁面")
                break
    
    def generate_filename(self, audio_format):
        """生成帶時間戳記的檔名"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"gemini-{timestamp}.{audio_format}"
    
    def process_audio(self):
        """處理音訊檔案的主要功能"""
        print("\n=== 處理音訊檔案 ===")
        config = self.load_config()
        
        # 檢查來源檔案是否存在
        source_path = config["source_path"]
        if not os.path.exists(source_path):
            print(f"錯誤：來源檔案不存在 - {source_path}")
            return
        
        # 檢查 Anki 媒體資料夾是否存在
        anki_media_path = config["anki_media_path"]
        if not os.path.exists(anki_media_path):
            print(f"錯誤：Anki 媒體資料夾不存在 - {anki_media_path}")
            return
        
        # 生成新檔名
        audio_format = config["audio_format"]
        new_filename = self.generate_filename(audio_format)
        target_path = os.path.join(anki_media_path, new_filename)
        
        # 取得來源檔案的副檔名
        source_ext = os.path.splitext(source_path)[1][1:].lower()  # 去掉點號並轉小寫
        
        playback_speed = config.get("playback_speed", 1.0)
        ffmpeg_path = config["ffmpeg_path"]
        
        try:
            # 判斷是否需要使用 FFmpeg
            if playback_speed != 1.0:
                # 需要變速處理，必須使用 FFmpeg
                print(f"正在處理音訊 (變速: {playback_speed}x)...")
                cmd = [
                    ffmpeg_path,
                    "-i", source_path,
                    "-filter:a", f"atempo={playback_speed}",
                    "-y",  # 覆寫輸出檔案
                    target_path
                ]
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"FFmpeg 錯誤：{result.stderr}")
                    return
                
                # 刪除原始檔案
                os.remove(source_path)
                print(f"檔案已處理並移動至：{target_path}")
                
            elif source_ext != audio_format:
                # 格式不同，需要轉換
                print(f"正在轉換格式 ({source_ext} -> {audio_format})...")
                cmd = [
                    ffmpeg_path,
                    "-i", source_path,
                    "-y",  # 覆寫輸出檔案
                    target_path
                ]
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"FFmpeg 錯誤：{result.stderr}")
                    return
                
                # 刪除原始檔案
                os.remove(source_path)
                print(f"檔案已轉換並移動至：{target_path}")
                
            else:
                # 格式相同且不需變速，直接移動
                print("正在移動檔案...")
                shutil.move(source_path, target_path)
                print(f"檔案已移動至：{target_path}")
            
            # 生成 Anki 音訊標籤並複製到剪貼簿
            anki_tag = f"[sound:{new_filename}]"
            pyperclip.copy(anki_tag)
            print(f"Anki 標籤已複製到剪貼簿：{anki_tag}")
            print("✅ 處理完成！")
            
        except Exception as e:
            print(f"處理過程中發生錯誤：{str(e)}")
    
    def copy_prompt(self):
        """複製 Prompt 功能"""
        prompt_file = "Prompt.txt"
        try:
            if os.path.exists(prompt_file):
                with open(prompt_file, 'r', encoding='utf-8') as f:
                    prompt_content = f.read()
                pyperclip.copy(prompt_content)
                print("Prompt 已複製到剪貼簿！")
            else:
                # 如果沒有 Prompt.txt，使用預設的提示詞
                default_prompt = "請為以下文字生成自然的語音朗讀："
                pyperclip.copy(default_prompt)
                print("預設 Prompt 已複製到剪貼簿！")
        except Exception as e:
            print(f"複製 Prompt 時發生錯誤：{str(e)}")
    
    def run(self):
        """主程式執行"""
        print("歡迎使用 Gemini Anki TTS！")
        
        while True:
            self.show_menu()
            try:
                user_input = input().strip().lower()
                
                if user_input == '':  # Enter 鍵
                    self.process_audio()
                elif user_input == 's':
                    self.setup_config()
                elif user_input == 'c':
                    self.copy_prompt()
                elif user_input == 'q':
                    print("感謝使用 Gemini Anki TTS，再見！")
                    break
                else:
                    print("無效的輸入，請按 Enter、's'、'c' 或 'q'")
                    
            except KeyboardInterrupt:
                print("\n程式已中斷")
                break
            except Exception as e:
                print(f"發生未預期的錯誤：{str(e)}")


if __name__ == "__main__":
    app = GeminiAnkiTTS()
    app.run() 