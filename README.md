# AdTEC: A Unified Benchmark for Evaluating Text Quality in Search Engine Advertising

The AdTEC dataset is designed to evaluate the quality of ad texts from multiple aspects, considering practical advertising operations.

> [!NOTE]
> The dataset and code will be made available after the paper is accepted.

## Experiments and Tasks Considered in the Paper

This dataset includes five tasks:
- **Ad Acceptability**: Given a text, predict the acceptance of overall quality with binary labels: `acceptable`/`unacceptable`.
- **Ad Consistency**: Given a pair of ad text and landing page (LP) text, predict the consistency between the ad and LP text with binary labels: `consistent`/`inconsistent`.
- **Ad Performance Estimation**: Given ad texts, keywords, and industry type, predict the overall performance with a score ranging from 0 to 100.
- **A3 Recognition**: Given a text, predict all possible aspects of advertising appeals (A3). The comprehensive list of A3 can be found in [[Murakami et al., 2022](https://aclanthology.org/2022.naacl-industry.9/)].
- **Ad Similarity**: Given a pair of ad texts, predict their similarity with a score ranging from 1 to 5.

## Languages
The dataset contains Japanese text only.

## Domain
Online advertisement (Search engine advertisement).

## Dataset Curators
The dataset was created by Peinan Zhang, Yusuke Sakai, Masato Mita, Hiroki Ouchi, and Taro Watanabe.

## Dataset Structure
All tasks are defined in TSV format and split into train, dev, and test sets.
The number of instances for each task in each split is shown in the table below.

| Task | Train | Dev | Test |
|------|------:|----:|-----:|
| Ad Acceptability | 13,265 | 970 | 980 |
| Ad Consistency   | 10,635 | 945 | 970 |
| Ad Performance Estimation | 125,087 | 965 | 965 |
| A3 Recognition | 1,856 | 465 | 410 |
| Ad Similarity | 4,980 | 623 | 629 |

Detailed examples of each task are provided below.

### Ad Acceptability

```tsv
label  title
acceptable  最新のビデオキャプチャー年間ランキングをご紹介・会員ランクに応じてポイント獲得がお得に。
unacceptable	茨城県アパート以上
acceptable	気になる保障をカンタン見積り
...
```

### Ad Consistency

```tsv
label	lp_text	title
consistent	介護の転職サポート登録のページ。介護の求人・転職なら介護ワーカー。介護福祉士、ホームヘルパー、ケアマネ、社会福祉士などの求人情報がどこよりも詳しくわかる！あなたの理想の職場がきっと見つかる！	介護職の求人なら【名古屋市】
inconsistent	手ぶらで体験レッスンが0円！上下ウェア・バスタオル・フェイスタオル・ヨガマット無料レンタルだから、手ぶらでOK！さらにお水（550ml×2本）をプレゼント！	ヨガ大分スタジオ「ロイブ」
consistent	ホーム コース ゲーム総合科 ゲーム総合科	プロの講師陣があなたのなりゲームクリエイターになるにはを全力サポート！資料請求はこちらから
...
```

### Ad Performance Estimation

```tsv
industry_type	keyword	title_1	title_2	title_3	description_1	description_2	score
EC	hunter	【公式】[MASK_2]（[MASK_8]）	《MAX50% OFF》AUTUMN SALE	人気＆注目アイテムはこちらから	人気商品がMAX50%OFF！機能性抜群の[MASK_8]アイテムで秋を楽しく過ごそう	機能的でスタイリッシュなデザイン。創業当初から愛される「機能美」をあなたへ。	55.90851442
金融	かしつけ	急ぎでお金の貸付受けたい方必見	免許証だけで最短1時間貸付可能		≪最短1h融資可能≫ローン貸付ランキング24hスマホ完結申込。融資可能か1秒診断		79.01220606
...
```

### A3 Recognition

```tsv
title  labels
THE THOUSAND KYOTO（ザ・サウザンド京都）の最寄駅は京都駅。THE THOUSAND KYOTO。ブライダルフェア情報、おトクな割引特典、フォトギャラリー、口コミ、見積もり例が充実！結婚式場探しはハナユメ！	商品/サービス特徴|オファー|アクセス
鳥取ガス enetopia	
ジャニーズ屈指のダンス力を誇る7人組グループ「Travis Japan」を全4週にわたって特集！	商品/サービス特徴
...
```

### Ad Similarity

```tsv
text1	text2	score
３月３１日まで実施中	山口トヨタ／お客様大感謝祭	2.67
春得キャンペーン第1弾	春得キャンペーン	4.33
...
```

## License
AdTEC dataset is released under the [CreativeCommons Attribution-NonCommercial-ShareAlike 4.0 International license](./LICENSE).

## Citation

```latex
@misc{zhang-2024-adtec,
  title = {{AdTEC}: A Unified Benchmark for Evaluating Text Quality in Search Engine Advertising},
  author = {Zhang, Peinan and Sakai, Yusuke and Mita, Masato and Ouchi, Hiroki and Watanabe, Taro},
  year = {2024}
}
```
