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

class App : public Application
{
};

LUMINO_APP(App);
```

# [Ruby](#tab/lang-ruby)

```ruby
require "lumino"

class App < Application
end

App.new.run
```

# [HSP3](#tab/lang-hsp3)

```c
#include "lumino.as"

LUMINO_APP

*on_init
    return

*on_update
    return
```

---

実行して、ウィンドウを表示してみましょう。

![](img/basic-1.png)

この時点でできることは、クローズボタンなどでウィンドウを閉じるだけです。

文字を表示したりユーザー入力を受けて動きを表現するためには、この App クラスにいくつかのメソッドを実装する必要があります。


初期化と更新
----------

小さな Lumino アプリケーションを作成するための基本的なタスクは次の2つです。

- プログラムの開始時に変数を初期化する
- プログラムが動き出したら、繰り返し変数を変更する

# [C++](#tab/lang-cpp)

これらの処理を行うために、次のように 2 つのメソッド定義を追加します。

```cpp
#include <Lumino.hpp>

class App : public Application
{
    void onInit() override
    {
    }

    void onUpdate() override
    {
    }
};

LUMINO_APP(App);
```

* `onInit` はアプリケーションの開始時に 1 回だけ呼び出されます。ここには変数などの初期化処理を書きます。
* `onUpdate` はアプリケーションの実行中、繰り返し呼び出されます。ここには変数などの更新処理を書きます。

# [Ruby](#tab/lang-ruby)

これらの処理を行うために、次のように 2 つのメソッド定義を追加します。

```ruby
require "lumino"

class App < Application
  def on_init
  end

  def on_update
  end
end

App.new.run
```

* `on_init` はアプリケーションの開始時に 1 回だけ呼び出されます。ここには変数などの初期化処理を書きます。
* `on_update` はアプリケーションの実行中、繰り返し呼び出されます。ここには変数などの更新処理を書きます。

# [HSP3](#tab/lang-hsp3)

これらの処理を行うための空のラベルが、先ほどのプログラムに書かれています。

```c
#include "lumino.as"

LUMINO_APP

*on_init    // 初期化
    return

*on_update  // 更新
    return
```

* `on_init` はアプリケーションの開始時に 1 回だけ呼び出されます。ここには変数などの初期化処理を書きます。
* `on_update` はアプリケーションの実行中、繰り返し呼び出されます。ここには変数などの更新処理を書きます。

---

処理内容は書かれていないため、実行するとウィンドウは表示できますが、動きに変わりはありません。

> [!Note]
> 更新処理は 1秒間に 60 回、繰り返し実行されます。
> この 1 回分の実行単位を `フレーム` と呼び、「1 秒間は 60 フレーム」といったように使います。


Hello, Lumino!
----------

ウィンドウに文字列を表示してみましょう。

テキストや数値を画面に表示するには、Lumino の デバッグ用の機能である、Debug クラスの機能を使うのが簡単です。

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

# [HSP3](#tab/lang-hsp3)

```c
#include "lumino.as"

LUMINO_APP

*on_init
    LNDebug_Print "Hello, Lumino!"
    return
	
*on_update
    return
```

---

文字列がウィンドウ上に表示されます。（その後、しばらくすると消えます）

![](img/basic-2.png)


文字列を表示し続ける
----------

次は更新処理の動作を確認してみます。

Lumino にはアプリケーションの起動からの経過時間を取得する機能がありますので、これを使って時間を表示し続けてみます。

# [C++](#tab/lang-cpp)

アプリケーションの起動からの経過時間を取得するには、`Engine::time()` を使います。

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

アプリケーションの起動からの経過時間を取得するには、`Engine.time` を使います。

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

# [HSP3](#tab/lang-hsp3)

アプリケーションの起動からの経過時間を取得するには、`LNEngine_GetTime` を使います。

```c
#include "lumino.as"

LUMINO_APP

*on_init
    return

*on_update
    time = 0
    LNEngine_GetTime time
    LNDebug_Print strf("Time: %f", time)
    return
```

---

![](img/basic-3.png)

実行してみると、画面からあふれるほどのテキストが表示されてしまいました。

繰り返し実行されているのはわかりましたが、今は過去の情報は不要です。

# [C++](#tab/lang-cpp)

`Debug::print()` は第一引数に数値を指定することで、テキストの表示時間をコントロールできます。次のように 0 を指定することで、テキストは 1 フレームの間だけ表示されるようになります。

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

`Debug.print()` は第一引数に数値を指定することで、テキストの表示時間をコントロールできます。次のように 0 を指定することで、テキストは 1 フレームの間だけ表示されるようになります。

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

# [HSP3](#tab/lang-hsp3)

`LNDebug_PrintWithTime` を使うことで、テキストの表示時間をコントロールできます。次のように第1引数に 0 を指定することで、テキストは 1 フレームの間だけ表示されるようになります。

```c
#include "lumino.as"

LUMINO_APP

*on_init
    return

*on_update
    time = 0
    LNEngine_GetTime time
    LNDebug_PrintWithTime 0, strf("Time: %f", time)
    return
```

---

修正したら、実行してみましょう。

![](img/basic-4.gif)

シンプルなタイマーができました！

テキストは 1 秒間に 60 回、表示と消去を繰り返すことで、リアルタイムに変化しているように見えます。
