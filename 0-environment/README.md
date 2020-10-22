# 環境建置

選定安裝位置

```bash
mkdir -p ~/api/yoro_deploy
cd ~/api/yoro_deploy
```

Clone YORO 專案

```bash
git clone git@gitlab.ical.tw:jamesljlster/yoro.git
```

建立 Python 虛擬環境

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

安裝套件

```bash
cd yoro
pip install -r requirements.txt
pip install . # -v for verbose
```
