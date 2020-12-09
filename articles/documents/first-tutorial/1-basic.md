Lumino の基本
==========

この章では、Lumino を使ってアプリケーションを作成するための最も基本的な流れについて学びます。

基本的なプログラムの構造
----------

「最初のプログラム」で見たように、Lumino でアプリを開発するには Application クラスの実装から始めます。

空のウィンドウを表示するだけの最小限のプログラムは、次のようになります。

# [C++](#tab/lang-cpp)

```cpp
#include <Lumino.hpp>

void Main()
{
    // Lumino を初期化します。
    Engine::init();

    // メインループ。
    while (Engine::update())
    {
        // ここに処理を書きます。
    }
}
```

# [HSP3](#tab/lang-hsp3)

```hsp
#include "lumino.as"

// Lumino を初期化します
LNEngine_Init

// メインループ
repeat
    LNEngine_Update
    // ここに処理を書きます。
loop
```

# [Ruby](#tab/lang-ruby)

```ruby
require "lumino"

# Lumino を初期化します。
Engine.init

# メインループ。
while Engine.update do
    # ここに処理を書きます。
end
```

----------------------------------------

### 初期化

プログラムがスタートした後、Lumino の機能を使う前に、必ず初期化用の処理を呼び出す必要があります。

この中でウィンドウの作成やグラフィックスの初期化処理が行われ、すぐにゲームの処理を書き始められるようになります。

### メインループ

リアルタイムで動くゲームを作るためには **メインループ** を実装する必要があります。

メインループはその言葉通り、ユーザー操作によってウィンドウが閉じられたりするまで継続的に処理を繰り返し、通常は次の処理を行います。

- プレイヤーからの入力を確認する。
- ゲーム状態 (キャラクターの位置など) を進めます。
- それをもとに、グラフィックを表示します。

> [!Note]
> このループ 1 回分の実行単位を `フレーム` と呼びます。（「1 秒間は 60 フレーム」といったように使います）

# [C++](#tab/lang-cpp)

`Engine::update()` は画面の表示や音楽・入力デバイスの情報を更新します。
さらにメインループが 1 秒間に 60 回の周期で実行され続けるように、必要に応じて待機時間の調整を行います。

また通常は true を返しますが、ウィンドウが閉じられる等アプリケーションを終了するべきイベントが発生すると、false を返すようになります。

# [Ruby](#tab/lang-ruby)

`Engine.update` は画面の表示や音楽・入力デバイスの情報を更新します。
さらにメインループが 1 秒間に 60 回の周期で実行され続けるように、必要に応じて待機時間の調整を行います。

また通常は true を返しますが、ウィンドウが閉じられる等アプリケーションを終了するべきイベントが発生すると、false を返すようになります。

# [HSP3](#tab/lang-hsp3)

`LNEngine_Update` は画面の表示や音楽・入力デバイスの情報を更新します。
さらにメインループが 1 秒間に 60 回の周期で実行され続けるように、必要に応じて待機時間の調整を行います。

----------

Hello, Lumino!
----------

ウィンドウに文字列を表示してみましょう。

テキストや数値を画面に表示するには、Lumino の デバッグようの機能である、Debug クラスの print() メソッドを使うと簡単にできます。

# [C++](#tab/lang-cpp)

```cpp
#include <Lumino.hpp>

class App : public Application
{
    void onInit() override
    {
        Debug::print(u"Hello, Lumino!");
    }

    void onUpdate() override
    {
    }
};

LUMINO_APP(App);
```

# [Ruby](#tab/lang-ruby)

```ruby
require "lumino"

class App < Application
  def on_init
    Debug.print("Hello, Lumino!")
  end

  def on_update
  end
end

App.new.run
```

# [HSP](#tab/lang-hsp3)

```hsp
#include "lumino.as"

LNEngine_Init

LNDebug_Print "Hello, Lumino!"

repeat
	LNEngine_Update
loop
```

----------

文字列がウィンドウ上に表示されます。（その後、しばらくすると消えます）

![](img/basic-2.png)


文字列を表示し続ける
----------

次は onUpdate で文字列を表示してみます。

# [C++](#tab/lang-cpp)
```cpp
#include <Lumino.hpp>

class App : public Application
{
    void onInit() override
    {
    }

    void onUpdate() override
    {
        Debug::print(String::format(u"Time: {0}", Engine::time()));
    }
};

LUMINO_APP(App);
```
# [Ruby](#tab/lang-ruby)
```ruby
require "lumino"

class App < Application
  def on_init
  end

  def on_update
    Debug.print("Time: %f" % Engine.time)
  end
end

App.new.run
```

# [HSP](#tab/lang-hsp3)
```hsp
#include "lumino.as"

LNEngine_Init

repeat
	LNEngine_Update

	LNEngine_GetTime time
	LNDebug_Print "Time: " + time
loop
```

----------

`Engine::time()` は アプリケーションの起動からの経過時間を返します。これを利用して、onUpdate() がどのくらいの頻度で実行されているのかを確認してみます。

![](img/basic-3.png)

実行してみると、画面からあふれるほどのテキストが表示されてしまいました。

繰り返し実行されているのはわかりましたが、今は過去の情報は不要です。

`Debug::print()` は第一引数に数値を指定することで、テキストの表示時間をコントロールできます。次のように 0 を指定することで、テキストは 1 フレームの間だけ表示されるようになります。

# [C++](#tab/lang-cpp)
```cpp
#include <Lumino.hpp>

class App : public Application
{
    void onInit() override
    {
    }

    void onUpdate() override
    {
        Debug::print(0, String::format(u"Time: {0}", Engine::time()));
    }
};

LUMINO_APP(App);
```
# [Ruby](#tab/lang-ruby)
```ruby
require "lumino"

class App < Application
  def on_init
  end

  def on_update
    Debug.print(0, "Time: %f" % Engine.time)
  end
end

App.new.run
```

# [HSP](#tab/lang-hsp3)
```hsp
#include "lumino.as"

LNEngine_Init

repeat
	LNEngine_Update

	LNEngine_GetTime time
	LNDebug_PrintWithTime 0, "Time: " + time
loop
```
----------

修正したら、実行してみましょう。

![](img/basic-4.gif)

シンプルなタイマーができました！

テキストは 1 秒間に 60 回、表示と消去を繰り返すことで、リアルタイムに変化しているように見えます。
