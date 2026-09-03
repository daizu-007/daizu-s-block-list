# main.py

# 必要なライブラリをインポート
from operator import ge
from pathlib import Path

# スクリプトをインポート
from Twitter.generate_mute_users import GenerateMuteUsers

# パスを取得
REPO_ROOT = Path(__file__).resolve().parent.parent

def main():
    generate_mute_users = GenerateMuteUsers(REPO_ROOT)
    generate_mute_users.run()

if __name__ == "__main__":
    main()
