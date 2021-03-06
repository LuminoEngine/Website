入力を受け取る
==========

この章では、キーボード、マウス、ゲームパッドといた様々なデバイスからの入力を、透過的に扱う方法を学びます。

方向キーでオブジェクトを移動する
--------------------

ボタンが押されているかどうか、といった入力を確認するには、 `Input` を使います。

次のプログラムは、キーボードの上下左右キーで Box を移動します。また、Z キーで位置をリセットします。

<!-- -------------------------------------------------------------------------------- -->
# [C++](#tab/lang-cpp)
```cpp
#include <Lumino.hpp>

class App : public Application
{
    Ref<BoxMesh> box;
    float posX = 0.0;
    float posY = 0.0;

    void onInit() override
    {
        box = BoxMesh::With().buildInto();
    }

    void onUpdate() override
    {
        if (Input::isPressed(u"left")) {
            posX -= 0.1;
        }

        if (Input::isPressed(u"right")) {
            posX += 0.1;
        }

        if (Input::isPressed(u"up")) {
            posY += 0.1;
        }

        if (Input::isPressed(u"down")) {
            posY -= 0.1;
        }

        // Z key, reset position
        if (Input::isTriggered(u"submit")) {
            posX = 0.0;
            posY = 0.0;
        }

        box->setPosition(posX, posY, 0.0);
    }
};

LUMINO_APP(App);
```
# [Ruby](#tab/lang-ruby)
```ruby
require "lumino"

class App < Application
  def on_init
    @box = BoxMesh.new
    @box.add_into
    @pos_x = 0.0
    @pos_y = 0.0
  end
  
  def on_update
    @pos_x -= 0.1 if Input.pressed?("left")
    @pos_x += 0.1 if Input.pressed?("right")
    @pos_y += 0.1 if Input.pressed?("up")
    @pos_y -= 0.1 if Input.pressed?("down")

    # Z key, reset position
    if Input.triggered?("submit")
      @pos_x = 0.0
      @pos_y = 0.0
    end

    @box.set_position(@pos_x, @pos_y, 0.0)
  end
end

App.new.run
```
# [HSP3](#tab/lang-hsp3)
```c
#include "lumino.as"
LUMINO_APP

*on_init
	LNBoxMesh_Create box
	LNWorldObject_AddInto box
	pos_x = 0.0
	pos_y = 0.0
	return

*on_update
	LNInput_IsPressed "left", a
	if a : pos_x -= 0.1
	LNInput_IsPressed "right", a
	if a : pos_x += 0.1
	LNInput_IsPressed "up", a
	if a : pos_y += 0.1
	LNInput_IsPressed "down", a
	if a : pos_y -= 0.1
	
	LNInput_IsTriggered "submit", a
	if a {
		pos_x = 0.0
		pos_y = 0.0
	}

	LNWorldObject_SetPositionXYZ box, pos_x, pos_y, 0
	return
```
---
<!-- -------------------------------------------------------------------------------- -->


![](img/input-1.gif)

`pressed` はキーが押されている間は true を返し、 `triggered` はキーが押された瞬間だけ true を返します。（これ以外にも離された瞬間を判定する `triggeredOff`、押している間は定期的に true を返す `repeated` が定義されています）

さて、それぞれ引数には `left` や `up` のように判定したいキーの名前を指定していますが、`submit` とはなんでしょうか。


仮想ボタンという考え方
----------

多くのコンシューマ機ではコントローラが1種類で、タイトルごとに「○ボタンは決定や攻撃」、「×ボタンはキャンセルやジャンプ」、のように役割が決まっています。

しかし様々なプラットフォームでの動作を想定する場合、キーボード、マウス、ゲームパッドやそれ以外のデバイスを接続されることを考えなければなりません。

またユーザーによってはゲームパッドで操作するよりもマウスとキーボードを組み合わせたプレイスタイルを好むこともあり、使いやすさのためにキーコンフィグを実装する必要も出てきます。

これらを全てカバーするようなプログラムを書くことは容易ではありませんが、Lumino ではこのような様々なケースへの対応負担を軽減するため、入力を抽象化して扱う機能を提供しています。


Input の動きを確認する
----------

`Input` では、 "キーボードの Z キー" 、や "ゲームパッドの1ボタン" といった具体的な物理ボタンを指定するのではなく、`ボタンの役割` を指定することで入力を判定します。

別途、この役割に物理ボタンを割り当てることで、入力を透過的に扱います。

例えば、先ほどの `submit` は「決定ボタン」を意味し、デフォルトでは `Zキー` と `Enterキー`、そして `ゲームパッドの1番ボタン` が割り当てられています。

次の表は、初期状態の割り当て一覧です。

| 名前 | キーボード | マウス | ゲームパッド  |
|------------------|------------|--------|---------------|
| left             | ← | -      | POV左, 第1軸- |
| right            | → | -      | POV右, 第1軸+ |
| up               | ↑ | -      | POV上, 第2軸- |
| down             | ↓ | -      | POV下, 第2軸+ |
| submit           | Z, Enter     | -      | 1 番ボタン    |
| cancel           | X, Esc | -      | 2 番ボタン    |
| menu             | X, Esc | -      | 3 番ボタン    |
| shift            | Shift | -      | 4 番ボタン    |
| pageup           | Q | -      | 5 番ボタン    |
| pagedown         | W | -      | 6 番ボタン    |
| any              | ※ | ※     | ※            |

※: any は割り当てられている全てのボタンに対応します。

次のプログラムで、押されたボタンに対応する文字列が表示されることを確認してみましょう。

<!-- -------------------------------------------------------------------------------- -->
# [C++](#tab/lang-cpp)
```cpp
#include <Lumino.hpp>

class App : public Application
{
    virtual void onUpdate() override
    {
        if (Input::isPressed(u"left")) Debug::print(0, u"left");
        if (Input::isPressed(u"right")) Debug::print(0, u"right");
        if (Input::isPressed(u"up")) Debug::print(0, u"up");
        if (Input::isPressed(u"down")) Debug::print(0, u"down");
        if (Input::isPressed(u"submit")) Debug::print(0, u"submit");
        if (Input::isPressed(u"cancel")) Debug::print(0, u"cancel");
        if (Input::isPressed(u"menu")) Debug::print(0, u"menu");
        if (Input::isPressed(u"shift")) Debug::print(0, u"shift");
        if (Input::isPressed(u"pageup")) Debug::print(0, u"pageup");
        if (Input::isPressed(u"pagedown")) Debug::print(0, u"pagedown");
        if (Input::isPressed(u"any")) Debug::print(0, u"any");
    }
};

LUMINO_APP(App);
```
# [Ruby](#tab/lang-ruby)
```ruby
require "lumino"

class App < Application
  def on_update
    Debug.print(0, "left") if Input.pressed?("left")
    Debug.print(0, "right") if Input.pressed?("right")
    Debug.print(0, "up") if Input.pressed?("up")
    Debug.print(0, "down") if Input.pressed?("down")
    Debug.print(0, "submit") if Input.pressed?("submit")
    Debug.print(0, "cancel") if Input.pressed?("cancel")
    Debug.print(0, "menu") if Input.pressed?("menu")
    Debug.print(0, "shift") if Input.pressed?("shift")
    Debug.print(0, "pageup") if Input.pressed?("pageup")
    Debug.print(0, "pagedown") if Input.pressed?("pagedown")
    Debug.print(0, "any") if Input.pressed?("any")
  end
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
	LNInput_IsPressed "left", a
	if a : LNDebug_PrintWithTime 0, strf("left")
	LNInput_IsPressed "right", a
	if a : LNDebug_PrintWithTime 0, strf("right")
	LNInput_IsPressed "up", a
	if a : LNDebug_PrintWithTime 0, strf("up")
	LNInput_IsPressed "down", a
	if a : LNDebug_PrintWithTime 0, strf("down")
	LNInput_IsPressed "submit", a
	if a : LNDebug_PrintWithTime 0, strf("submit")
	LNInput_IsPressed "cancel", a
	if a : LNDebug_PrintWithTime 0, strf("cancel")
	LNInput_IsPressed "menu", a
	if a : LNDebug_PrintWithTime 0, strf("menu")
	LNInput_IsPressed "shift", a
	if a : LNDebug_PrintWithTime 0, strf("shift")
	LNInput_IsPressed "pageup", a
	if a : LNDebug_PrintWithTime 0, strf("pageup")
	LNInput_IsPressed "pagedown", a
	if a : LNDebug_PrintWithTime 0, strf("pagedown")
	LNInput_IsPressed "any", a
	if a : LNDebug_PrintWithTime 0, strf("any")
	return
```
---
<!-- -------------------------------------------------------------------------------- -->

![](img/input-2.gif)


ボタンの割り当てを変更する
----------

TODO:

