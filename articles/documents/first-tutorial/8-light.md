ライトを設定する
==========

この章では、ワールド内のオブジェクトに陰影をつけるためライティングについて学びます。

ライトの基本操作
----------

ライトを移動して、光の当たり方を変えてみます。

カメラと同じく、初期状態ではひとつのライトがワールドに配置されています。

このライトは、最も一般的に使用される `DirectionalLight` と呼ばれるものです。DirectionalLight は、太陽のように一定方向から均一に、ワールド全体を照らします。

次のコードで、カメラと同じように向きを変え、中天から直下を照らすようにしてみます。

<!-- -------------------------------------------------------------------------------- -->
# [C++](#tab/lang-cpp)
```cpp
#include <Lumino.hpp>

class App : public Application
{
    void onInit() override
    {
        auto box = BoxMesh::With().buildInto();

        auto camera = Engine::camera();
        camera->setPosition(5, 5, -5);
        camera->lookAt(0, 0, 0);

        auto light = Engine::mainLight();
        light->lookAt(0, -1, 0);
    }
};

LUMINO_APP(App);
```
# [Ruby](#tab/lang-ruby)
```ruby
require "lumino"

class App < Application
    def on_init
        box = BoxMesh.new
        box.add_into

        camera = Engine.camera
        camera.set_position(5, 5, -5)
        camera.look_at(0, 0, 0)

        light = Engine.main_light
        light.look_at(0, -1, 0);
    end
end

App.new.run
```
# [HSP3](#tab/lang-hsp3)
```c
#include "lumino.as"
LUMINO_APP

*on_init
    LNBoxMesh_CreateWithSize 1, 1, 1, box
    LNWorldObject_AddInto box

    LNEngine_GetMainCamera camera
    LNWorldObject_SetPositionXYZ camera, 5, 5, -5
    LNWorldObject_LookAtXYZ camera, 0, 0, 0

    LNEngine_GetMainLight light
    LNWorldObject_LookAtXYZ light, 0, -1, 0
    return

*on_update
    return
```
---
<!-- -------------------------------------------------------------------------------- -->

![](img/graphics-basic-7.png)

ボックスが真上から照らされるようになるため、上面が明るくなり、他の面は暗くなりました。


ライトの種類
----------

TODO:

### DirectionalLight

### AmbientLight

### PointLight

### SpotLight
