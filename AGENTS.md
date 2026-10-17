# Fixture rules
Use Python standard library only. All data is synthetic. Keep policy.py and summary.py independent; server.py is existing local test UI.
Gate: python3 -m unittest discover -s tests -v
Do not deploy, access secrets, or change repository settings. For delegated work, use the explicit Worktree absolute path for every command.
