# 原始二进制资料校验清单

此清单用于核对已形成的**本地Git原始档案**。截至本次GitHub连接器上传，远端只同步了文本版手册和衍生数据；下列原始DOCX/XLSX暂未作为二进制对象导入GitHub，请不要将它们视为已经在远端完整备份。

| 离线Git相对路径 | SHA-256 |
|---|---|
| `docs/manuals/政府韧性信息人工标注手册（V1.2）.docx` | `761d4d741093803bac090dc6ad10abcea25fa4192340a085a5856a0b98f84058` |
| `docs/manuals/政府韧性信息人工标注手册（V1.3.1）.docx` | `0dc5eb8cc779a8e0d72ccc1ca160d534a3e2a9ee4966dcdb71f82733f8ad55cd` |
| `data/pilot/武汉公文首批试标.xlsx` | `81b150ecf767819ce5719c87bff8e7177392f0a10194ed29acb3bdcf1079d5f3` |
| `data/audit/随机审计盲表.xlsx` | `d3637b1692db2b3a17e95cefefc985b55f935768ccc1f54052438b6cba835f4a` |

## 离线包（2026-11-22）
- `government-resilience-git-archive.zip` SHA-256：`65abc93983201696805c80b6b7e883dd58db507d82f5d17facaed25c328df199`
- `government-resilience-measurement.bundle` SHA-256：`b2e8d48615230a76b2913b8b2faea4b0f33de9108c4b9c135712bccb699d2db1`

## 原始五条本地Git提交
```text
d5d8bad chore(repo): initialize private research archive and safety rules
dd4a041 docs(research): archive original project brief and methodological references
9c1729e docs(annotation): preserve V1.2 and V1.3.1 manuals with revision history
3185d8c data(pilot): archive 17-document index, 160 weak labels, and blind review forms
22f440c docs(process): document AI-first review, provenance gaps, and reproducibility plan
```

本次GitHub连接器上传产生的是**另一条真实的Git提交历史**，并未伪造相同SHA或日期。欲完整保存本地原历史与DOCX/XLSX，应将离线包原Git分支作为GitHub独立备份分支上传（参见`docs/RESTORE_ORIGINAL_GIT_HISTORY.md`）。

`data/pilot/武汉公文首批公文索引.csv` 是17篇公文元数据的派生版。 `data/pilot/weak_labels_160.csv.gz.base64` 可通过 `python scripts/decode_weak_labels.py` 解码为CSV，但只包含10列核心ID/AI标签，不包含完整正文、AI证据、人工盲审表。
