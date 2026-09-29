# SHRINE_ADAPTER v0.1

Observe(JSON) を Shrine Narrative へ変換する。

語彙は OBSERVATION / ANOMALY / RECOVERY のみ。

## Rules

- 新しい事実を生成しない
- 原因を推測しない
- 実装内部を語らない
- 観測値を改変しない
- Event Log 以上の情報を作らない
- Recovery 判定は観測列からのみ行う

## Mapping

status=OK            → OBSERVATION
status=ERROR         → ANOMALY
ERROR…OK 同一 id     → RECOVERY（transform_sequence）

Recovery:

recovered = (error_count > 0) and (final_status == OK)
recovery_count = ERROR→OK 遷移の回数

中間 OK は正規ケース。現在 Recovered と recovery_count は分離する。
