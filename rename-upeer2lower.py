# -*- coding: utf-8 -*-

# 参考: https://www.hobochuritsu.com/entry/2019/02/16/220000

import glob
import os
import sys
import re

"""
ディレクトリ内のファイルの大文字を小文字に再帰的にリネーム
"""

# 引数の指定がない場合はカレントディレクトリを対象とする
if len(sys.argv) > 1:
    src_dir = sys.argv[1]
else:
    src_dir = "./"
# ディレクトリ内のファイル名を再帰的に取得する
path = os.path.join(src_dir, "**/*.*")
files = glob.glob(path, recursive=True)
for fi in files:
    # 元のディレクトリ構造とファイル名、拡張子を取得する
    org_dir, org_name = os.path.split(fi)
    filename, suffix = os.path.splitext(org_name)
    # 自分自身はリネームしない
    if org_name == __file__:
        continue
    # 名前に大文字英字を含まないファイルは処理しない
    if not re.search('[A-Z]', org_name):
        continue
    #
    new_name = "{0}{1}".format(filename.lower(), suffix)
    new_path = os.path.join(org_dir, new_name)
    # リネーム
    os.rename(fi, new_path)
    print("{0} -> {1}".format(org_name, new_name))
