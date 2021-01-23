# 環境建置

此章節將介紹如何建立 YORO 專案所需要的執行環境。

## 環境需求

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
    <https://developer.nvidia.com/CUDA-TOOLKIT-ARCHIVE>

-   cuDNN:
    <https://developer.nvidia.com/CUDNN>

-   CMake > 3.17:

    安裝方法請參考：<https://apt.kitware.com/>

-   OpenCV > 4.0:

    編譯安裝方法請參考：  
    <https://docs.opencv.org/4.5.0/d7/d9f/tutorial_linux_install.html>

## 環境建置

> 註1：Manjaro 使用者可直接使用 Native 環境，
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
    pip install wheel
    ```

3.  預先安裝 PyTorch

    由於 PyTorch 官方提供的套件使用舊的 C++ ABI，
    因此需要自行編譯相容於系統環境的 PyTorch。  
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

              請參考 <http://icl.cs.utk.edu/magma/software/>

        -   Manjaro:

            ```bash
            sudo pacman -S magma
            ```

    2.  編譯、安裝 PyTorch

        使用 Git Clone 指定版本的 PyTorch 專案，在此以 v1.7.0 為例：

        ```bash
        cd ~/api/yoro_deploy  # 回到工作根目錄

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
        python setup.py build
        python setup.py install
        ```

    3.  安裝 Torchvision

        使用 Git Clone 指定版本的 Torchvision 專案，在此以 v0.8.1 為例：

        ```bash
        cd ~/api/yoro_deploy  # 回到工作根目錄

        git clone --depth 1 --branch v0.8.1 https://github.com/pytorch/vision
        cd vision
        ```

        編譯安裝套件：

        ```bash
        python setup.py install
        ```

4.  編譯、安裝 YORO 套件

    ```bash
    cd ~/api/yoro_deploy  # 回到工作根目錄

    git clone https://github.com/jamesljlster/yoro.git
    cd yoro

    pip install -v .
    ```

5.  測試環境

    ```bash
    cd ~                     # 離開 YORO 套件目錄
    python -c "import yoro"  # 測試載入套件是否會出現異常狀況
    ```
