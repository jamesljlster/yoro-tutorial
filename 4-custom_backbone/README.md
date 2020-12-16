# 自訂 Backbone

此章節將介紹如何使用自訂的 Backbone 訓練 YORO 以及角度偵測器。  

### 通則

透過設定檔中的 construct / backbone 欄位可以指定該模型使用的 backbone，
其中 name 為 backbone 模組的完整路徑，args 則是初始化該模組的所有參數。  
舉例來說，如果希望使用 torchvision 的 resnet18 作為 backbone，
且希望網路輸出節點數有 20 個，設定檔範例如下：

```yaml
construct:
  backbone:
    name: 'torchvision.models.resnet18'  # Backbone 物件完整路徑
    args: {num_classes: 20}  # 初始化參數，需要依據指定的物件自訂，無法通用
```

trainer 在讀取設定檔時，會自動將當前執行目錄加入 Python Path 中，
作為模組載入的搜尋路徑之一。  
因此自訂的 Backbone 可以不需要實際安裝到環境中，
只需要在模組目錄中執行訓練即可。

> 注意：自訂的 Backbone 需要相容於 TorchScript，否則會無法順利匯出模型。

### 範例簡介

-   `demo_backbone.py`  
    此檔案內含自訂的 CNN 與 FCN 網路（基於 AlexNet 修改而來），
    僅提供 Demo 用途，不建議真的拿來當 Backbone。

-   `yoro_custom_bbone.yaml`  
    使用 demo_backbone 模組自訂的 FCN 網路作為 Backbone 訓練 YORO 模型：

    ```bash
    trainer ./yoro_custom_bbone.yaml
    ```

-   `rotanc_custom_bbone.yaml`  
    使用 demo_backbone 模組自訂的 CNN 網路作為 Backbone，
    訓練使用 Anchor 為編碼方式的角度偵測器：

    ```bash
    trainer rotanc_custom_bbone.yaml
    ```
