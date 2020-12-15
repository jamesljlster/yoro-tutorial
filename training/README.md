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

-   `backup_exporter`

##### 匯出 Pretrained Weight

-   `pretrain_exporter`

##### 簡易 Recall 模型

-   `recaller`

### Notes
