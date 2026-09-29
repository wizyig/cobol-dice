# Audit layers（オペレータ実測 2026-09-29）

```text
Layer A 契約     PASS（推測禁止 / 神社分離 / 秘密0）
Layer B 再現     PASS（68/68）
Layer C 配布     v0.3.1 で CI体裁を対象
Layer D Origin   FAIL（COBOL未接続）— 別トラック
```

観測線の現状:

```text
User → Python Adapter → Tests(68)
COBOL 未接続
```

68 passed は adapter 正しさだけを示す。
