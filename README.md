# 🐭 貓捉老鼠：Tom and Jerry 追逐遊戲 (Python Turtle)

## 🎯 專案簡介 (About)

這是一個基於 Python 內建 `turtle` 繪圖模組開發的經典追逐遊戲。玩家控制 Jerry（傑利鼠），試圖逃離 Tom（湯姆貓）的追捕。

**遊戲特色：**
* 簡潔的圖形介面與開場動畫。
* Tom 會鎖定 Jerry 的位置並不斷追趕。
* **難度遞增機制：** 隨著遊戲進行，Tom 的移動速度會持續增加（`self.TomSpeed += 0.05`），挑戰玩家的反應速度和生存時間。

## 🚀 如何開始 (Getting Started)

### 1. 執行環境

本專案使用標準 Python 函式庫，不需要安裝額外的第三方套件。
* **Python 版本：** 建議 3.x
* **依賴模組：** `turtle`, `time`, `random` (皆為標準庫)

### 2. 檔案結構 (關鍵！解決圖片依賴問題)

在執行程式前，請確保你的專案目錄結構如下，**特別是圖片檔案必須存在：**
⚠️ **重要提示：** 程式碼中預設會從 `img/` 資料夾載入圖片。請自行準備或下載兩張 `GIF` 格式的圖片，並分別命名為 `Tom.gif` 和 `Jerry.gif` 放置於 `img` 資料夾中。

### 3. 執行指令

在專案根目錄下，執行 `main.py` 檔案：

    ```bash
    python main.py

## 🕹️遊戲玩法
| 角色 | 控制者 | 目標 |
| :--- | :--- | :--- |
| **Jerry** | 玩家 | 使用鍵盤的**方向鍵** (Up, Down, Left, Right) 移動，盡可能存活更久。 |
| **Tom** | AI | 自動追逐 Jerry，速度會持續加快。Tom 移動時會在畫布上留下**藍色軌跡**。 |

* **遊戲結束條件：** 當 Tom 和 Jerry 的距離小於 10 像素時，遊戲結束。
* **結果：** 畫面將顯示 "GAME OVER" 以及你的存活時間（精確到小數後一位）。


## ⚙️ 程式碼結構解析 (Code Overview)

### `main.py`

作為專案的啟動入口點，只負責引入 `TomAndJerry_Login` 模組並啟動遊戲主類別。

    ```python
    # 僅用於啟動 TomAndJerry_Login.MainClass
    import TomAndJerry_Login

    class MainClass:
        def main():
            TomAndJerry_Login.MainClass()
        main()

### `TomAndJerry_Login.py`

包含遊戲的核心邏輯，MainClass 負責整個遊戲流程的控制。

| 方法名稱 | 職責 |
| :--- | :--- |
| `__init__` | 遊戲初始化，依序執行創建畫布、登入畫面、角色生成、按鍵綁定和開始主迴圈。 |
| `CreatePlayGround` | 創建 `turtle.Screen()` 遊戲視窗。 |
| `CreateLogInWord` | 顯示 "TOM and JERRY" 開場文字，並暫停 3 秒後清空畫面。 |
| `Tom_Jerry_Generate` | 初始化 Tom 和 Jerry 兩個 `turtle.Turtle` 物件，隨機設置初始位置，並註冊和設置 GIF 圖片。 |
| `BundleDirKey` | 綁定鍵盤的方向鍵到 Jerry 的移動方法，並設置 Tom 的軌跡。 |
| `Jerry_Up/Down/Left/Right` | 處理 Jerry 的移動邏輯（轉向並前進 20 單位）。 |
| `KeepGoing` | 遊戲主迴圈。計算 Tom 追逐 Jerry 的角度，加速 Tom 的移動，並檢查兩者距離是否小於 10 像素以觸發遊戲結束。 |
| `GameOver_ShowSecond` | 處理遊戲結束後的畫面顯示，計算並呈現玩家的存活時間。 |
