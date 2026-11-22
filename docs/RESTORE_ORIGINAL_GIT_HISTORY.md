# 将原始离线Git五条提交完整保存在GitHub

**已知状态：** GitHub默认分支 `main` 通过连接器创建了文本研究记录的真实提交。先前离线Git归档则含有原始Word/Excel及另五条提交。两条提交历史不同，不能直接对 `main` 执行非快进覆盖或强推。

如需将全部原始文件连同原五条提交完整上传至同一个私有仓库，建议在自己的Mac终端运行以下命令，创建独立分支而不覆盖目前的 `main`：

```bash
# 解压从ChatGPT取得的 government-resilience-git-archive.zip
unzip government-resilience-git-archive.zip
cd government-resilience-measurement
git status --short
git log --oneline -5

# 用自己的GitHub登录或凭据认证（不要把令牌粘贴到聊天）
git remote add origin https://github.com/komaedazsy/government-resilience-measurement.git
git push -u origin main:refs/heads/archive/original-local-history
```

如果zip解压后目录层级有所不同，请进入包含 `.git` 的目录。若 `origin` 已存在，请用 `git remote -v` 检查并视情况 `git remote set-url origin ...`。**不要使用 `--force`。**

成功后，私有仓库将有：
- `main`：本次通过GitHub连接器提交的可检索研究说明及部分数据派生文本。
- `archive/original-local-history`：此前五条真实本地Git提交及原始DOCX/XLSX二进制文件。

也可通过 `.bundle` 恢复：`git clone government-resilience-measurement.bundle government-resilience-restored`，再按上面的方式新增远端并推送其main到归档分支。

完成推送后，请将仓库分支链接提供给对话以便核验文件SHA、commit ID、隐私状态。后续正式开发可以从 `main` 新建分支，并有选择地合并经核实的原件，而不是直接合并两个无共同祖先的Git历史。
