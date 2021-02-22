HSP3 で Lumino をはじめる
==========

必要な環境
----------

- Windows 10 (64bit)
- HSP 3.5.1+

開発環境の準備を行う
----------
### HSP3 をインストールする

1. [HSPTV] (https://hsp.tv/index2.html) にアクセスし、最新の HSP3 開発環境をダウンロードしてインストールしてください。

### Lumino をインストールする

1. [LuminoHSP3 のパッケージ](http://nnmy.sakura.ne.jp/archive/lumino/v0.10.0/Lumino-v0.10.0-HSP3.zip) をダウンロードし、展開してください。
2. "LuminoHSP3.dll" を HSP3 のエディタ (hsed3.exe) と同じフォルダにコピーします。
3. "lumino.as" を 2 のフォルダにある "common" フォルダにコピーします。
4. "lumino.hs" を 2 のフォルダにある "hsphelp" フォルダにコピーします。

最初のプログラム
----------

HSPスクリプトエディタを開き、次のプログラムを入力してみましょう。

```hsp
#include "lumino.as"
LUMINO_APP

*on_init
	LNUIText_CreateWithText "Hello, Lumino!", text
	LNUIElement_AddInto text
    return

*on_update
    return
```

続いてプログラムを実行してみます。

![](img/first-program.png)

中央に "Hello, Lumino!" と書かれたウィンドウが表示されましたか？

これで Lumino を使うための準備が整いました。次は [チュートリアル](../first-tutorial/1-basic.md) に進みましょう！
