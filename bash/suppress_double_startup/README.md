# shellで2重起動を抑制する方法

## 参考情報

https://intellectual-curiosity.tokyo/2020/09/05/shell%E3%81%A72%E9%87%8D%E8%B5%B7%E5%8B%95%E3%82%92%E6%8A%91%E5%88%B6%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/
shellで2重起動を抑制する方法

## 実験1

プロセスを1個起動する。

```
$ ./example_1001.sh
[26587] before sleep
[26587] after sleep
```
## 実験2

プロセスを2個起動する。

```
$ ./example_1001.sh & ./example_1001.sh
[1] 26864
既に起動しています!
[26864] before sleep
[26864] after sleep
[1]+  Done                    ./example_1001.sh
```
