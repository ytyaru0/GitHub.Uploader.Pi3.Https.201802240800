#!/bin/bash
user=ytyaru0
desc="GitHubアップロードツール。Databaseクラスをシングルトンにした（未テスト）"
url=http://ytyaru.hatenablog.com/entry/2019/01/27/000000
target=$(cd $(dirname $0) && pwd)

. /home/pi/root/script/sh/pyenv.sh
. /home/pi/root/env/py/auto_github/bin/activate

#script=/media/mint/85f78c06-a96e-4020-ac36-9419b7e456db/mint/root/pj/auto/GitHub/python/v3.1/GitHubUploader.py
script=/tmp/work/GitHub.Uploader.Pi3.Https.201802210700/src/Uploader.py
python3 ${script} "${target}" -u  "${user}" -d "${desc}" -l "${url}"

