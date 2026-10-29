# 龙虾工作台

打开preview.svg看设计，修改scene.json的配色和镜头。使用Blender 4.5 LTS，在本目录运行：

```bash
blender --background --python build_scene.py -- --output-dir ./output
```

输出front.png、side.png和scene.blend。打开工程可继续调整材质、物件和镜头。

先用低分辨率检查构图，再提高resolution；Cycles渲染较慢可把samples降到8。bpy脚本使用Blender内置Python执行。
