# Contract v0.3

Request → COBOL → Response → SHRINE_ADAPTER → Narrative

Response:
- OK: request_id + status + result。message 禁止
- ERROR: request_id + status + message。result 禁止
- message は語彙固定

Narrative:
- class_name: OBSERVATION | ANOMALY | RECOVERY
- request_id 保持
- text 非空
- 推測語禁止

RecoveryReport:
- recovered / steps / error_count / ok_count / recovery_count / final_status
- mixed request_id は拒否
