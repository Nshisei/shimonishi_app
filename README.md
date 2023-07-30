# shimonishi_app
これは、2023年春・夏学期の情報ネットワーク学演習Iで下西研2で作成したプログラムである。

## 概要
気温と持っている服装に合わせて、その日の適切な服装を提案するアプリケーション

## 実行方法
### センサー側
```
$ cd shimonishi_app
$ python3 connection/server.py
```
### AP側
```
$ cd shimonishi_app
$ python3 slack.py
```
### slack側
DBから<name>の服装情報を取り出し、その日の温度に合わせて服装を提案する
```
服装予報
<name>
```
DBから<name>の服装情報を取り出し、その日の温度に合わせて、プロンプトと合わせて服装を提案する
```
服装予報 with list
<name>
```
DBに服装情報を登録する
```
insert clothes
<user_id>,<color>,<type>,<season>
```
DBに服装情報を削除する
```
delete clothes
<clothes_id>
```
DBにユーザを登録する
```
insert user
<id>,<name>,<gender>
```
DBにユーザを削除する
```
delete user
<id>
```