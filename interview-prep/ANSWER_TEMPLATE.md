# Answer Template

## Question

`<Ghi lai cau hoi>`

## Short Answer

Tra loi 2-4 cau, du de interviewer thay ban nam concept chinh.

## Deep Explanation

Giai thich co cau truc:

- No la gi.
- Giai quyet van de nao.
- Hoat dong nhu the nao.
- Khi nao dung va khi nao khong dung.

## Production Example

Mo ta mot tinh huong that:

- Source system.
- Data volume/frequency.
- Pipeline/tool.
- Failure mode.
- Cach monitor va recover.

## Common Mistakes

- Nham lan concept.
- Bo qua idempotency/retry/backfill.
- Toi uu sai cho data size.
- Khong tinh schema evolution, late data, duplicates.

## Trade-offs

- Performance vs cost.
- Freshness vs consistency.
- Simplicity vs flexibility.
- Batch reliability vs streaming latency.

## Follow-up Questions

- Interviewer co the hoi gi tiep?
- Ban se defend design nhu the nao?
- Neu scale tang 10x thi doi gi?

## SQL Example

```sql
-- Them SQL neu phu hop
SELECT 1;
```

## Spark/Python Example

```python
# Them Spark/Python neu phu hop
print("example")
```

## Performance Notes

Noi ve partitioning, indexing, shuffle, file size, concurrency, cache, query plan.

## Cost Notes

Noi ve storage, compute, scan bytes, cluster sizing, serverless billing, retention.

## Monitoring Notes

Noi ve row count, freshness, null rate, duplicate rate, latency, SLA, error budget, alert.

## Interview Tips

Tra loi theo format: definition -> example -> risk -> trade-off -> monitoring.

