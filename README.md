# COBOL Tools + SHRINE_ADAPTER v0.3.1

モデル不要
推測禁止
観測列が教材

```text
v0.3.1 = Python Adapter Reference
COBOL  = experimental / not yet validated
```

主張は観測済み事実だけ。

```text
言える:     COBOL準拠 Adapter（契約と example JSON）
まだ言えない: COBOL が観測の出どころ
```

神社を COBOL に入れない。LICENSE は未決定（捏造しない）。

## Available Tools

| Tool | Input | Output |
|---|---|---|
| dice | sides=2..1000 | 1..sides |
| coin | none | heads or tails |
| timestamp | none | YYYYMMDDThhmmsscc |
| echo | payload=1..80 | payload |

## Error Vocabulary

```text
invalid sides
invalid payload
invalid tool
invalid request
```

Recovery は観測列から定義する。LLM 内部状態は使わない。
