## ゲート
- `python3 -m unittest discover -s tests -v`

## 動作確認
- 起動: `python3 -c "print('synthetic data; no emulator required')"`
- seed: `python3 -c "print('alice and bob are synthetic query values')"`
- ログイン: 不要。alice/bob はローカルの合成入力値
- 開発サーバー: `python3 server.py --port 8765`
- e2e: `python3 e2e.py`

## 境界の候補
- パス: `policy.py`
- 文字列: `can_cancel`
