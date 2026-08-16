# 模块四：钢铁利维坦 BOSS 多部位破坏与阶段演进系统

---

## 🎯 BOSS 结构分拆与部位独立判定（Multi-Part Hierarchy）

巨型陆地巡洋要塞「钢铁利维坦」拥有 7 个独立的碰撞网格与生命判定部位：

```mermaid
graph TD
  LeviathanBoss["钢铁利维坦 (总指挥枢纽)"]
  LeviathanBoss --> MainHull["1. 重装甲主车体 (Core Hull - 60 HP)"]
  LeviathanBoss --> LeftTurret["2. 左翼 150mm 副炮塔 (Left Turret - 15 HP)"]
  LeviathanBoss --> RightTurret["3. 右翼 150mm 副炮塔 (Right Turret - 15 HP)"]
  LeviathanBoss --> MissilePod["4. 背部 6 联装战术火箭巢 (Missile Pod - 18 HP)"]
  LeviathanBoss --> LeftTrack["5. 左侧主驱动履带 (Left Track - 12 HP)"]
  LeviathanBoss --> RightTrack["6. 右侧主驱动履带 (Right Track - 12 HP)"]
  LeviathanBoss --> Bridge["7. 顶部雷达指挥塔 (Command Bridge - 10 HP)"]
```

---

## 💥 部位破坏与战术收益机制

1. **摧毁副炮塔（Left/Right Turret）**：
   - 局部引发强烈黑烟与火花大爆炸，该炮塔永久断裂垂落；
   - BOSS 永久失去该侧的持续火力压制能力。
2. **摧毁战术火箭巢（Missile Pod）**：
   - 触发内部火箭殉爆，并扣除 BOSS 总血量 10 点；
   - 彻底解除 BOSS 阶段二的「全屏火箭弹幕」威胁。
3. **摧毁履带总成（Left/Right Track）**：
   - 履带崩断散落一地，BOSS 移动速度直接下降 50%（若双侧皆被摧毁，则完全原地瘫痪无法转向）。
4. **摧毁指挥塔（Command Bridge）**：
   - BOSS 索敌准度大幅下降，且进入 4 秒过载硬直状态。
