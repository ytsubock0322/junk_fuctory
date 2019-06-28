import requests
import argparse
###### setting #######
VT_APIKEY_01=e16a1cbb0bb4d55a47685d9235f6cdc840370a22a4d96107134fbc92f90a9a48
VT_APIKEY_02=ee0334db42285bd7236252015c24a1e947a78d23a411a1b638000b07dbc572ed
VT_APIKEY_03=4c9840e93fbc0abfaf82938db1f3ed325850e7004f7e9ebdced892bfc3ead094
VT_APIKEY_04=4ce49569e30eb05fc2c25cea04e34dbb82a4484be62213f5eae1f1a3991208c3
VT_APIKEY_05=10a210dd6996f3263f57cdd77660cce72ad72b900d583354632b9fd3213180c2
VT_APIKEY_06=59836533695f830b0de29f1e444cb76b245853645ddc926d6391ab5f11f0d039
VT_APIKEY_07=3fdcdb2befa67ef9ef8d487916f4835bcd16d363aff7ddd6a04a45fc0a53ac35
VT_APIKEY_08=1981fd7493205d2730e35cf87e57b567afe7eddafb55646492bbb6d7b920100b
VT_APIKEY_09=f55352fdf1fe3a7df7fff9ae74f903e8cea9aac764fa2ecba17ca973bb238dd5
VT_APIKEY_10=d598ee61a63fd4bfbe27e12aa6bdde8e45ae207c305b20c5ecbbd6c149071a54
VT_APIKEY_11=3584fd64ab8820f918398080c3a1b9e01de17383b78d165d5a610ab20fc810d6
VT_APIKEY_12=e170f03e8184a5978b41b1f065932e9494c19d5865eafdd844788c5317069f4b
VT_APIKEY_13=4089979baed233a43b652dc06393eb2efcc0966869e29e4e4a316e6434144ac9
VT_APIKEY_14=c3a0ee271b028e71af31d25531b7046ffc3caa9c702858fff583931aa038d4c0
VT_APIKEY_15=1542597099577c373c859f3ce53a212ed30e96f0e1100c2a7d99a0e9e3c681ea

# XXX:
def connect_database():
  pass

# XXX:
def regist_malicius_info():
  pass

def vt_file_result():
  url = 'https://www.virustotal.com/vtapi/v2/file/report'
  params = {'apikey': '<apikey>', 'resource': '<resource>'}
  response = requests.get(url, params=params)
  return response.json()
  
def vt_url_result():
  url = 'https://www.virustotal.com/vtapi/v2/url/report'
  params = {'apikey': '<apikey>', 'resource':'<resource>'}
  response = requests.get(url, params=params)
  return response.json()

def read_apikey():
  pass

def args_check():
  pass

def main():
    # XXX:引数のチェック
    # XXX: -h : HASHチェック
    # XXX: -f : fileチェック（HASH計算をしてvt_file_resultを叩く）
    # XXX:APIKEYの適用
    # XXX:VirusTotalから結果取得
    # XXX:ローカルDB登録
    pass

if __name__ == "__main__":
    main()


