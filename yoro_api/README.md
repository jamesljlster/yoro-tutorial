# YORO API

### C++ API

YORO C++ API 支援 CMake find_package 功能，
但由於套件安裝位置不在 CMake 預設模組搜尋路徑中，
因此需要設定環境編變數輔助尋找套件。  
在此提供 `export_yoro_dir.py` 協助設定環境變數：

```bash
python export_yoro_dir.py  # 將 yoro_api_DIR 環境變數寫入 ~/.bashrc
source ~/.bashrc           # 重新載入 ~/.bashrc
```

##### CMake 整合

這部份可能需要一些 CMake 的先備知識。

1.  載入 YORO API 與 OpenCV (相依套件)

    ```cmake
    # Find OpenCV
    find_package(OpenCV REQUIRED)
    include_directories(${OpenCV_INCLUDE_DIRS})

    # Find YORO C++ API
    find_package(yoro_api REQUIRED)
    include_directories(${yoro_api_INCLUDE_DIRS})
    ```

2.  鍊結函式庫

    假設有一個執行檔的 CMake Target 名稱為 my_program：

    ```cmake
    target_link_libraries(my_program yoro_api ${OpenCV_LIBS})
    ```

##### 載入 YORO Detector

### Python API
