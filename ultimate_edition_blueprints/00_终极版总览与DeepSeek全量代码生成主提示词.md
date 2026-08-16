# 《白岭防线：终极版》底层架构全景与 DeepSeek 主提示词

> 本文档用于向 **DeepSeek** 发送系统级提示词，用于直接生成《白岭防线 3D 坦克大战》终极版的底层完整核心代码框架与数据结构。

---

## 🎯 终极版核心目标

将现有的 3D 坦克大战全面进化为**作品级、全功能、极具打击感与深度**的 3D 装甲战术射击游戏：
1. **真实物理后坐力与悬挂俯仰**：开火车体后仰、刹车点头、行进颠簸；
2. **移动端细腻马达触觉反馈（Haptic Vibration）**：分级振动模拟；
3. **后处理轻量化辉光（Bloom）**：穿甲弹曳光、炮口焰、爆炸烈焰发光；
4. **战场动态交互道具**：可引爆柴油油桶堆、缓降伞降空投箱、可碾碎掩体；
5. **四大特化主炮流派**：APFSDS穿甲重炮、双联防空速射炮、重型攻城臼炮、电磁穿甲狙击炮；
6. **钢铁利维坦 BOSS 多部位破坏**：独立副炮塔、防空导弹发射架、履带总成可分别击破；
7. **程序化动态引擎声效**：随转速变调的柴油引擎、履带金属挤压转向音；
8. **无尽生存模式与本地战绩排行榜**：持久化保存高分与勋章。

---

## 🤖 发送给 DeepSeek 的提示词（可以直接复制以下内容）

```text
你是一位顶级的 3D 网页游戏架构师与 WebGL / Three.js 资深引擎专家。
请根据以下设计规范，为单文件 3D 坦克射击游戏《白岭防线：终极版》构建底层完整、高性能、无 Bug 的核心引擎与系统模块：

### 一、技术栈与运行环境
1. 核心渲染：Three.js (WebGLRenderer, 采用 PCFSoftShadowMap, ACESFilmicToneMapping)
2. 音频合成：Web Audio API (完全基于程序化振荡器与滤波噪声合成，无外部音频依赖或提供高保真本地回退)
3. 触觉反馈：Web Vibration API (区分轻/中/重/爆发 4 级振动)
4. 数据存储：HTML5 LocalStorage (本地排行榜、勋章、改装进度持久化)
5. 架构模式：面向对象实体组件系统（ECS）与有限状态机（FSM）

### 二、核心系统实现清单
1. TankPhysicsSystem（底盘物理与悬挂系统）：
   - 具备开火反作用力车体俯仰（Recoil Pitch）、制动点头（Braking Pitch）、履带转弯差速与抓地力计算。
2. WeaponSystem（多主炮流派与弹道物理）：
   - 支持 4 种主炮模式（标准重炮/双联速射/曲射臼炮/电磁贯穿），独立计算重力下坠、初速、散射角与破甲深度。
3. EnvironmentInteractionSystem（战场可破坏道具）：
   - 包含油桶（Barrel）、空投箱（AirDrop）、木质掩体（Barricade），支持碰撞物理、链式殉爆与范围伤害。
4. BossMultiPartSystem（利维坦 BOSS 部位破坏系统）：
   - 将 BOSS 拆解为 Hull, LeftTurret, RightTurret, MissilePod, LeftTrack, RightTrack, Bridge 7 个独立判定部位，各自拥有独立碰撞盒、血量与破坏残骸/瘫痪逻辑。
5. ProceduralAudioEngine（动态音频与引擎声效）：
   - 实现随战车速度动态调制 Pitch/Gain 的双振荡器柴油机声、履带挤压摩擦声、远景炮火回声。
6. HapticFeedbackEngine（触觉振动引擎）：
   - 封装轻量振动序列（Fire: 15ms, Hit: 40ms, Crit: [30ms, 20ms, 50ms], Storm: [80ms, 40ms, 120ms]）。
7. GameLoop & StateManager：
   - 管理波次进度（1~6波标准战役 + 无尽防线模式）、战术支援、加点改装、本地排行榜记录。

请输出模块化、高内聚、易于挂载的 JavaScript 核心架构代码与初始化入口。
```
