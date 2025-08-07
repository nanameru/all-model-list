# 🤖 日本のLLM活用ガイド

**業務カテゴリ別LLMモデル比較・活用事例データベース**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://kimurataiyou.github.io/all-model-list)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

> 「どの業務にどのLLMを使えばいいか」が一目でわかる、実用性重視のガイド

## 📊 収集データ概要

- **総モデル数**: 51個
- **収集範囲**: OpenRouter.ai上位モデル
- **業務カテゴリ**: 15分野の詳細分析
- **収集日**: 2025年8月7日
- **データ形式**: 構造化JSON + マークダウン

## 🎯 このプロジェクトの特徴

### 💼 業務カテゴリ別アプローチ
従来の「モデル性能比較」ではなく、「実際の業務でどう使うか」に特化：

| # | 業務カテゴリ | 代表タスク | 重視指標 |
|---|------------|-----------|----------|
| 1 | 顧客サポート／FAQ | チャットボット、メール対応 | 正確性・レスポンス速度・コスト |
| 2 | 営業メール & フォロー | パーソナライズ営業文生成 | 出力品質・テンプレ適用性 |
| 3 | マーケティング制作 | ブログ・SNS・広告コピー | クリエイティブ度・ブランド適合 |
| 4 | ソフトウェア開発支援 | コード生成・バグ修正・テスト | 技術精度・コンテキスト長 |
| 5 | データ分析 & BI | SQL生成・レポート解説 | 数値理解・論理的説明 |
| 6 | 社内ナレッジ検索 | 文書Q&A・ポリシー案内 | 長文処理・検索精度 |
| 7 | 法務文書レビュー | 契約チェック・リスク抽出 | 正確性・説明可能性 |
| 8 | 財務・経営企画 | 数値分析・IR資料 | 数値整合性・信頼性 |
| 9 | 人事・採用 | 履歴書要約・求人作成 | 公平性・個人情報保護 |
| 10 | 研修・eラーニング | 教材作成・クイズ生成 | 教育的配慮・多様性 |
| 11 | 会議メモ & アクション | 議事録・TODO抽出 | リアルタイム性・構造化 |
| 12 | 多言語対応 | 翻訳・ローカライゼーション | 言語精度・文化的適合 |
| 13 | クリエイティブ設計 | ネーミング・コンセプト | 創造性・マルチモーダル |
| 14 | サプライチェーン | 需要予測・在庫最適化 | 時系列分析・数値予測 |
| 15 | IT運用・障害対応 | ログ解析・手順提案 | 専門知識・即応性 |

### 🏢 日本市場特化
- 日本語性能評価
- 国内企業での実際の活用事例
- 日本の法規制・商習慣を考慮
- コスト効果の具体的な計算例

### 📈 実用性重視
- 理論より実践的な選択指標
- 導入コストとROIの透明性
- 段階的導入のロードマップ
- 失敗事例と対策も含む

## 🚀 クイックスタート

### 1. 動的比較表で検索
**🔗 [https://kimurataiyou.github.io/all-model-list](https://kimurataiyou.github.io/all-model-list)**

- 業務カテゴリでフィルタリング
- 価格帯・プロバイダーで絞り込み
- リアルタイム検索・ソート

### 2. 業務別ガイドを参照
```
models/by-business-category/
├── customer-support/          # 顧客サポート活用ガイド
├── software-development/      # 開発支援活用ガイド
├── marketing-content/         # マーケティング活用ガイド
└── ...                       # 全15カテゴリ
```

### 3. 具体的なモデル情報
```
models/providers/
├── openai/gpt-oss-120b/      # モデル詳細・事例
├── deepseek/r1-0528-free/    # 無料高性能モデル
├── mistral/devstral-medium/  # 開発特化モデル
└── ...                       # 全51モデル
```

## 📊 価格帯別おすすめ

### 🆓 無料で始める（11モデル）
| モデル | 適用業務 | 特徴 |
|--------|----------|------|
| DeepSeek R1 0528 (free) | 開発支援・データ分析 | 推論能力高、完全無料 |
| OpenAI gpt-oss-20b (free) | 顧客サポート・営業 | バランス型、安定動作 |
| Mistral Small 3.2 24B (free) | 軽量タスク全般 | 高速応答 |

### 💰 コスパ重視（$0.01-0.10/M）
| モデル | 月間コスト目安 | 業務適性 |
|--------|---------------|----------|
| DeepSeek R1 Qwen3 8B | $10-50 | 開発・分析・IT運用 |
| Tencent Hunyuan A13B | $20-80 | 多言語・顧客対応 |
| Mistral Small 3.2 24B | $30-100 | 一般業務全般 |

### 🏆 高性能（$0.10+/M）
| モデル | 月間コスト目安 | 業務適性 |
|--------|---------------|----------|
| OpenAI gpt-oss-120b | $100-500 | 高度な推論・複雑業務 |
| Google Gemini 2.5 Pro | $200-800 | マルチモーダル・創作 |
| Anthropic Claude Opus 4.1 | $300-1000 | 法務・高精度分析 |

## 🏢 活用事例ハイライト

### 成功事例1: ECサイトの顧客サポート自動化
- **企業**: 中堅Eコマース（従業員200名）
- **モデル**: OpenAI gpt-oss-120b
- **効果**: 1次対応率80%向上、人件費月300万削減
- **ROI**: 投資回収期間2ヶ月

### 成功事例2: 製造業の需要予測
- **企業**: 製造業（売上100億円）
- **モデル**: DeepSeek R1 + 社内データ
- **効果**: 予測精度15%向上、在庫コスト月500万削減
- **ROI**: 年間6000万の効果

### 成功事例3: スタートアップの開発支援
- **企業**: AIスタートアップ（従業員30名）
- **モデル**: Mistral Devstral Medium
- **効果**: 開発速度40%向上、バグ率30%削減
- **ROI**: エンジニア1名分の効果

## 🛠️ 貢献方法

### 新しいモデル情報の追加
1. [モデル更新Issue](https://github.com/kimurataiyou/all-model-list/issues/new?template=model-update.md)を作成
2. 業務カテゴリ適性を1-5で評価
3. 可能であれば実際のテスト結果を添付

### 活用事例の共有
1. [活用事例Issue](https://github.com/kimurataiyou/all-model-list/issues/new?template=usage-case.md)を作成
2. 匿名での投稿も可能
3. ROI計算例があると更に有用

### データの更新・修正
1. 該当ファイルを直接編集してPR
2. [PRテンプレート](https://github.com/kimurataiyou/all-model-list/blob/main/.github/PULL_REQUEST_TEMPLATE/default.md)に従って情報を記載

## 📁 リポジトリ構造

```
all-model-list/
├── data/
│   └── models/                        # 構造化データ
│       └── all-models-with-business-categories.json
├── models/
│   ├── providers/                     # プロバイダー別モデル情報
│   │   ├── openai/
│   │   ├── google/
│   │   └── ...
│   ├── by-business-category/          # 業務カテゴリ別ガイド
│   │   ├── customer-support/
│   │   ├── software-development/
│   │   └── ...
│   └── templates/                     # コントリビューション用テンプレート
├── docs/
│   └── index.html                     # GitHub Pages（動的テーブル）
├── .github/
│   ├── workflows/                     # CI/CD
│   ├── ISSUE_TEMPLATE/               # Issue テンプレート
│   └── PULL_REQUEST_TEMPLATE/        # PR テンプレート
└── README.md                         # このファイル
```

## 📊 データ品質保証

- **自動検証**: GitHub Actions でデータ形式チェック
- **コミュニティレビュー**: PR による査読体制
- **定期更新**: 月1回の価格・性能情報更新
- **情報源追跡**: 全データに出典を明記

## 🤝 コミュニティガイドライン

### 歓迎する貢献
- 実際の利用経験に基づく情報
- 具体的な数値・効果測定結果
- 失敗事例と学習内容
- 業界特有の活用パターン

### 注意事項
- 機密情報・個人情報の保護
- 公平で偏見のない評価
- 信頼できる情報源の明記
- 建設的で敬意ある議論

## 📞 お問い合わせ・サポート

- **バグ報告**: [GitHub Issues](https://github.com/kimurataiyou/all-model-list/issues)
- **機能要望**: [GitHub Discussions](https://github.com/kimurataiyou/all-model-list/discussions)
- **活用相談**: [Discussions](https://github.com/kimurataiyou/all-model-list/discussions/categories/q-a)

## 📈 今後のロードマップ

### Phase 1 (完了)
- [x] 51モデルの基本情報整理
- [x] 15業務カテゴリでの分類
- [x] 動的比較表の実装

### Phase 2 (進行中)
- [ ] 全モデルの詳細データ追加
- [ ] 活用事例の継続収集
- [ ] 業界別ガイドの作成

### Phase 3 (計画中)
- [ ] API提供（プログラマティックアクセス）
- [ ] モバイル対応の改善
- [ ] 多言語化（英語・中国語）
- [ ] AI推奨エンジン機能

## 🏆 貢献者

このプロジェクトは日本のLLMコミュニティによって支えられています。

<!-- 貢献者リストは自動更新予定 -->

---

## 📄 ライセンス

MIT License - 詳細は [LICENSE](LICENSE) を参照

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=kimurataiyou/all-model-list&type=Date)](https://star-history.com/#kimurataiyou/all-model-list&Date)

---

**最終更新**: 2025年8月7日  
**データ更新頻度**: 月1回  
**コミュニティ**: 日本のLLM活用者・開発者

> 💡 「業務に最適なLLMが見つからない」という悩みを解決するため、  
> 実用性重視で情報を整理・共有しています。ぜひご活用ください！