# YORO API

YORO C++ API 支援 CMake find_package 功能，
但由於套件安裝位置不在 CMake 預設模組搜尋路徑中，
因此需要設定環境編變數輔助尋找套件。  
在此提供 `export_yoro_dir.py` 協助設定環境變數：

```bash
python export_yoro_dir.py  # 將 yoro_api_DIR 環境變數寫入 ~/.bashrc
source ~/.bashrc           # 重新載入 ~/.bashrc
```

### 編譯範例檔案

在終端機中切換至此 README.md 所在的資料夾，並執行：

```bash
mkdir build && cd build
cmake ..
cmake --build . --target install
```

編譯好的範例執行檔會出現在 install 資料夾中。

### CMake 整合

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

> 註：YORO API 採用 Shared Library 的方式發布，
> 透過 RPATH 設定可以免去在系統中指定 LD_LIBRARY_PATH 的問題，
> 可參考本單元 CMakeLists.txt 中
> Initialize RPATH settings for shared library loading 的寫法。
> 更詳細的相關資訊請參考：
> <https://gitlab.kitware.com/cmake/community/-/wikis/doc/cmake/RPATH-handling>

### API 使用方式

Python API 需要在事先設定的虛擬環境中執行，C++ 則無此限制。

##### 引入 API

```cpp
#include <yoro_api.hpp>
```

```python
from yoro import api
```

##### DeviceType

在後續載入 Detector 時，可以透過參數指定模型要載入在那一種裝置上：

-   預設裝置

    使用預設裝置，程式會自動偵測系統是否有 CUDA 資源可以使用，
    若否則會使用 CPU 資源。

    ```cpp
    yoro_api::DeviceType::Auto
    ```

    ```python
    api.DeviceType.Auto
    ```

-   CPU

    強制使用 CPU 資源。

    ```cpp
    yoro_api::DeviceType::CPU
    ```

    ```python
    api.DeviceType.CPU
    ```

-   CUDA

    強制使用 CUDA 資源，如果 CUDA 資源不可用會丟 Exception。

    ```cpp
    yoro_api::DeviceType::CUDA
    ```

    ```python
    api.DeviceType.CUDA
    ```
