# 訓練模型

### 訓練 YORO

1.  使用 anchor_cluster 協助決定 Anchor

    anchor_cluster 會將資料集中的物件寬度、高度依據指定的尺度進行縮放之後，
    進行 K-Means 分群。

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

### Notes

-   `anchor_cluster`
-   `trainer`
-   `recaller`
-   `backup_exporter`
-   `pretrain_exporter`
