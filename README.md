# GitHub auto-committer

Makes one small commit every day, so the contribution graph stays green.

## How it works

- `.github/workflows/daily-commit.yml` runs every day at 06:17 UTC and on manual dispatch.
- `scripts/daily_commit.py` appends today's date to `activity.log` and commits it as `log: YYYY-MM-DD`.
- The workflow pushes the commit with the built-in `GITHUB_TOKEN`.

## Setup

1. Create an empty repo on GitHub (no README, no .gitignore).
2. Push this repo:

   ```sh
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin master
   ```

3. In the repo, open **Settings > Actions > General** and make sure **Workflow permissions** allows read and write access. The workflow's `permissions: contents: write` normally covers this.

## Test it

Run it from the Actions tab: **Daily commit > Run workflow**. Or locally:

```sh
python scripts/daily_commit.py
git push
```

## Notes

- Commit messages are `log: 2026-11-14` style: short and tied to the actual change.
- GitHub disables scheduled workflows after 60 days without repository activity. Daily bot commits count as activity, so this keeps itself alive.
- Pushes made with `GITHUB_TOKEN` do not trigger other workflows.
- To change the time, edit the `cron` line. It is UTC.
