# 訓練模型

此部份需要在預先建置好的 Python 虛擬環境中執行。

### 訓練 YORO

接下來介紹的是 YORO 模型的訓練流程：

1.  使用 anchor_cluster 協助決定 Anchor

    anchor_cluster 會將資料集中的物件寬度、高度依據指定的尺度進行縮放之後，
    進行 K-Means 分群。  
    跳過這個步驟使用人工指定好的 Anchor 也行，訓練效果不見得會比較差。

    程式用法請參考：

    ```bash
    anchor_cluster -h
    ```

    範例：

    ```bash
    anchor_cluster ~/dataset/coating/train 2 --width 224 --height 224
    ```

    範例輸出：

        Iter 1. Average moving distance: 0.415559
        Iter 2. Average moving distance: 0.002135
        Iter 3. Average moving distance: 0.000012

        anchor:
          - [49.36836242675781, 34.85364532470703]
          - [42.48030090332031, 42.5048828125]

    請將程式輸出的 anchor 列表記下，以利後續配置設定檔。

2.  配置訓練設定檔

    上一步所取得的 Anchor 資訊可套用在 contruct / anchor 設定中，
    查看 [coating.yaml](coating.yaml) 以了解詳細配置。

3.  訓練模型

    trainer 可搭配指定的設定檔以及 Command Line 參數進行模型訓練，
    程式用法請參考：

    ```bash
    trainer -h
    ```

    訓練過程中產生的備份檔會包含目前訓練的狀態以及最佳網路權重，
    因此不必擔心訓練中途停止會丟失最佳權重，
    在訓練結束之後，
    trainer 會自動以最佳權重匯出 TorchScript Model。

    範例：

    ```bash
    trainer coating.yaml
    ```

##### 從 Backup 匯出模型

使用 backup_exporter 可從 trainer 產生的備份檔中匯出當下最佳權重的模型，
需要以 Command Line 參數依序帶入訓練設定檔以及模型備份檔，
程式用法請參考：

```bash
backup_exporter -h
```

範例：

```bash
backup_exporter coating.yaml coating.backup/epoch_30000.sdict
```

##### 匯出 Pretrained Weight

pretrain_exporter 可自訓練備份檔或者 TorchScript Model 匯出 Pretrained Weight，
程式用法請參考：

```bash
pretrain_exporter -h
```

範例：

```bash
# 自 TorchScript Model 匯出
pretrain_exporter coating_epoch_30000.zip coating_pretrain.pth

# 自 Backup 匯出
pretrain_exporter coating.backup/epoch_30000.sdict coating_bak_pretrain.pth
```

匯出預訓練權重之後，可在訓練階段使用 --pretrain 參數指定給 trainer 使用，
範例如下：

```bash
trainer coating.yaml --pretrain coating_pretrain.pth
```

### 訓練角度偵測器

trainer 也提供角度偵測器訓練的功能，設定檔請參考：

-   [rotation_anchor.yaml](rotation_anchor.yaml): 使用 Anchor 編碼訓練角度辨識模型
-   [rotation_classifier.yaml](rotation_classifier.yaml): 使用分類法訓練角度辨識模型
-   [rotation_regressor.yaml](rotation_regressor.yaml): 使用 Anchor 編碼訓練角度辨識模型

設定檔內容除了不需要 Anchor 資訊，以及角度編碼設定有所不同之外，
其餘內容皆與 YORO 訓練設定相同。

### 測試模型效果

匯出 TorchScript Model 之後，可使用 recaller 快速檢視模型訓練效果，
程式用法請參考：

```bash
recaller -h
```

程式的第一個參數為模型的處理問題，選轉物件偵測填入 yoro，
旋轉角度偵測則使用 rot 作為參數；
第二個參數為 TorchScript Model 的檔案路徑；
第三個參數則是輸入來源的類型，可使用 image 或 video 作為影像輸入來源，
最後再填入影像路徑或是攝影機裝置路徑。  
使用範例如下：

```bash
# 使用影像作為輸入
recaller yoro coating_epoch_30000.zip image ~/dataset/coating/valid/CamToolbox_20200121_153827_1.jpg
recaller rot rotation_anchor_epoch_500.zip image ~/dataset/PlateShelf/valid/0.jpg

# 使用攝影機作為輸入
recaller yoro coating_epoch_30000.zip video /dev/video0
```

在使用 yoro 模式下，
recaller 可再帶入 `--conf 過濾門檻` 以及 `--nms 合併門檻` 進行測試。
