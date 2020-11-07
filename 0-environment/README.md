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

-   CUDA Toolkit:

    需要與後續 PyTorch 安裝版本所對應的一致：  
    <https://developer.nvidia.com/CUDA-TOOLKIT-ARCHIVE>

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

> 註1：建議 Manjaro 使用者直接使用 Native 環境，
> 使用 pacman 安裝 python-pytorch-opt-cuda 套件，
> 並直接跳到第 4 步驟。

> 註2：請不要使用 sudo 執行任何 pip 指令！！

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

    此步驟需要在 Python 虛擬環境中執行，可參考官方作法：  
    <https://github.com/pytorch/pytorch>

    1.  安裝相依套件

        共同相依套件：

        ```bash
        pip install \
            numpy ninja pyyaml mkl mkl-include setuptools cffi \
            typing-extensions future six requests dataclasses
        ```

        Magma:

        -   Ubuntu:

              請參考<http://icl.cs.utk.edu/magma/software/>

        -   Manjaro:

            ```bash
            sudo pacman -S magma
            ```

    2.  編譯、安裝 PyTorch

        使用 Git Clone 指定版本的 PyTorch 專案，在此以 v1.7.0 為例：

        ```bash
        git clone --depth 1 --branch v1.7.0 https://github.com/pytorch/pytorch.git
        cd pytorch

        git submodule sync
        git submodule update --init --recursive --depth 1
        ```

        如果需要，安裝並指定相容於 CUDA 安裝版本的編譯器：

        ```bash
        export CC=$(which gcc-9)
        export CXX=$(which g++-9)
        ```

        編譯及安裝：

        ```bash
        pip install . # -v for verbose
        ```

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
