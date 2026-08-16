# 模块三：战车主炮特化流派与 Roguelike 深度改装系统

---

## 🎯 四大主炮特化流派（Weapon Archetypes）

| 流派名称 | 射速 / 装填 | 弹道特性 | 单发伤害 | 战术定位与打击风格 |
| :--- | :--- | :--- | :--- | :--- |
| **1. 125mm APFSDS 脱壳重穿甲炮** | 中等（1.2s） | 高速平直、穿透多辆敌车 | **18 基础 / 36 暴击** | **经典重炮**：远程点杀重型目标，直线穿刺 |
| **2. 35mm 双联装防空速射炮** | 极快（0.12s） | 双管交替开火、轻微弹道散射 | **4 基础 x 2 管** | **弹幕压制**：近距离疯狂扫射，割草轻坦群 |
| **3. 203mm 重型攻城曲射臼炮** | 较慢（2.8s） | 抛物线高抛曲射、超大爆破圈 | **45 溅射范围伤害** | **攻坚轰炸**：越过工事掩体打击掩体后敌人 |
| **4. 电磁轨道穿甲狙击炮 (Railgun)** | 慢速（2.2s） | 瞬间光束贯穿、附带 EMP 麻痹 | **30 贯通 + 2s 瘫痪** | **战术控制**：瘫痪重甲敌车并贯穿全场 |

---

## 🛠️ Roguelike 武器模块改装树

在每波战斗结束后的战地改装界面中，玩家不仅可以获得常规数值强化，还可以随时**升级或切换主炮形态**：

```javascript
const WeaponModules = {
  standard: {
    name: '125mm 滑膛坦克炮',
    fireInterval: 1.1,
    bulletSpeed: 52,
    damage: 10,
    recoil: 0.12,
    bulletType: 'ap'
  },
  autocannon: {
    name: '35mm 双联防空速射炮',
    fireInterval: 0.12,
    bulletSpeed: 64,
    damage: 3.5,
    recoil: 0.04,
    bulletType: 'rapid'
  },
  mortar: {
    name: '203mm 攻城曲射臼炮',
    fireInterval: 2.8,
    bulletSpeed: 28,
    damage: 48,
    recoil: 0.24,
    bulletType: 'mortar_lob'
  },
  railgun: {
    name: '电磁轨道穿甲狙击炮',
    fireInterval: 2.2,
    bulletSpeed: 140,
    damage: 32,
    recoil: 0.18,
    bulletType: 'rail_beam'
  }
};
```
