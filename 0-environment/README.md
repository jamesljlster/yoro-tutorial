# 環境建置

### 環境需求

-   Python > 3.5:

    ```bash
    sudo apt install python3 python3-dev python3-venv
    ```

-   Git:

    ```bash
    sudo apt install git
    ```

-   C++ 編譯器:

    ```bash
    sudo apt install g++
    ```

-   CMake > 3.17:

    安裝方法請參考：<https://apt.kitware.com/>

-   OpenCV > 4.0:

    Ubuntu 環境需要手動安裝，可至實驗室公用FTP下載對應版本：  
    <ftp://icalpublic@140.127.205.190/DevelopTools/API/OpenCV/4.5.0>

    或是自己編譯：  
    <https://gitlab.ical.tw/jamesljlster/cv-build>

    安裝方法：  

    ```bash
    sudo apt install --fix-broken ./libopencv4-4.5.0-dev.deb
    ```

### 環境建置

1.  選定安裝位置

    ```bash
    mkdir -p ~/api/yoro_deploy
    cd ~/api/yoro_deploy
    ```


2.  建立 Python 虛擬環境

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    ```


3.  預先安裝 PyTorch (視環境狀況而定)

    免此步驟的環境：

    需要此步驟的環境：

    -   Manjaro


4.  編譯、安裝套件

    ```bash
    git clone git@gitlab.ical.tw:jamesljlster/yoro.git
    cd yoro

    pip install . # -v for verbose
    ```


5.  測試環境

    ```bash
    python -c "import yoro"
    ```
