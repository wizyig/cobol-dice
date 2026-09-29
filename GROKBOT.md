# GrokBot 指示 — cobol-dice v0.3.1

対象: GitHub 面のみ。個人情報・他アカウント・X投稿・PAT本文は触るな。

状態:

```text
契約 v0.3 FROZEN
CI最小修正 = v0.3.1（本ファイルと同梱ソース）
COBOL観測源化 = 別トラック。勝手に着手するな
```

オペレータが「公開」と言うまで push / release をしない。

## 公開時の主張

README の3行を崩さない。

```text
モデル不要
推測禁止
観測列が教材
```

書いてよい: Python Adapter Reference / COBOL準拠 Adapter
書いてはいけない: COBOL が観測の出どころ（未証明）

## やってよいこと（公開指示後）

1. オペレータ指定の新規 public repo にこのディレクトリを載せる
2. ソースのみ。`__pycache__` / `.pytest_cache` / `htmlcov` / `coverage.xml` / 秘密を入れない
3. タグは `v0.3.1`。v0.4 を勝手に付けない
4. LICENSE は指定が来るまで作らない

## やってはいけないこと

- COBOL に神社語彙を入れる
- Adapter が result を生成する
- Recovery を「モデルが直した」と書く
- Debug Shrine xlsx を混ぜる
- 別監査 repo へ混ぜる / force push
- 手元パスを README に書く
- 68 passed を README の実測として固定する

## 手元確認

```text
cd cobol-dice
python scripts/verify.py
```

verify.py はリポジトリ直下を sys.path に足す。PYTHONPATH 必須ではない。
実測の passed / mypy / coverage はオペレータ記録が正。

## 公開単位

| 単位 | 中身 |
|---|---|
| 本repo | 契約・adapter・tests・example JSON・COBOL実験ソース |
| 別 | Debug Shrine workbook |
| 別 | キャラ／Grokシェア文 |
