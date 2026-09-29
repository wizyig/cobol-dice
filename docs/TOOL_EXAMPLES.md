# Tool examples

## Dice

```json
{"request_id":"REQ-1001","tool":"dice","sides":6}
{"request_id":"REQ-1001","status":"OK","result":4}
```

## Coin

```json
{"request_id":"REQ-2001","tool":"coin"}
{"request_id":"REQ-2001","status":"OK","result":"heads"}
```

## Timestamp

```json
{"request_id":"REQ-3001","tool":"timestamp"}
{"request_id":"REQ-3001","status":"OK","result":"20260929T11253012"}
```

## Echo

```json
{"request_id":"REQ-4001","tool":"echo","payload":"HELLO"}
{"request_id":"REQ-4001","status":"OK","result":"HELLO"}
```
