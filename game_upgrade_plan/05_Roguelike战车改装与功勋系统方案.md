# 模块五：Roguelike 战车改装与抗战功勋勋章系统方案

- **文件绝对路径**：`d:\坦克大战\game_upgrade_plan\05_Roguelike战车改装与功勋系统方案.md`
- **模块职责**：战区通关 3 选 1 科技强化词条、属性倍率计算、8 大抗战胜利荣誉勋章与结算大屏。

---

## 🎯 模块设计目标
1. 每一战区结束并进入下一战区前，弹出**【战地整备车间 · 战术改装】**面板，提供 3 张随机战术卡牌；
2. 游戏结算（通关或阵亡）时，根据命中率、大招使用、无伤记录等给予对应的**【抗战功勋荣誉勋章】**。

---

## 🛠️ 底层数据结构设计

### 1. 战车改装词条库 (Upgrade Card Pool)
```javascript
const upgradePool = [
  {
    id: 'tungsten_ap',
    title: '钨合金穿甲弹芯',
    desc: '主炮基础穿透伤害提升 35%，对重装甲目标额外增伤 20%',
    rarity: 'rare',
    apply: (p) => { p.damageMultiplier = (p.damageMultiplier || 1) * 1.35; }
  },
  {
    id: 'turbo_diesel',
    title: '涡轮增压柴油机',
    desc: '战车最高行进时速 +25%，原地差速转向灵敏度 +30%',
    rarity: 'common',
    apply: (p) => { p.speedMultiplier = (p.speedMultiplier || 1) * 1.25; }
  },
  {
    id: 'composite_armor',
    title: '特种复合装甲板',
    desc: '战车最大生命上限 +3 点，并立即修补 3 点生命值',
    rarity: 'rare',
    apply: (p) => { p.maxHp += 3; p.hp = Math.min(p.maxHp, p.hp + 3); }
  },
  {
    id: 'rapid_loader',
    title: '半自动液压装弹机',
    desc: '主炮装填冷却时间缩短 25%',
    rarity: 'rare',
    apply: (p) => { p.reloadSpeedMultiplier = (p.reloadSpeedMultiplier || 1) * 1.25; }
  },
  {
    id: 'reactive_armor',
    title: '爆破反应装甲 (ERA)',
    desc: '免疫下一次受到的致命炮火打击，并产生震退冲击波',
    rarity: 'epic',
    apply: (p) => { p.hasReactiveArmor = true; }
  },
  {
    id: 'overcharge_dynamo',
    title: '发电机过载电容',
    desc: '击毁敌军获得的【全弹灭绝风暴】能量增加 50%',
    rarity: 'common',
    apply: (p) => { p.energyGainMultiplier = (p.energyGainMultiplier || 1) * 1.5; }
  }
];
```

### 2. 8 大抗战功勋勋章库 (Medal System)
```javascript
const medals = [
  {
    id: 'sniper',
    name: '百步穿杨勋章',
    desc: '主炮命中率高于 75%',
    check: (stats) => stats.shotsFired > 15 && (stats.shotsHit / stats.shotsFired) >= 0.75
  },
  {
    id: 'iron_wall',
    name: '钢铁长城勋章',
    desc: '至少在 1 个战区内实现无伤通关',
    check: (stats) => stats.flawlessWaves >= 1
  },
  {
    id: 'iron_fist',
    name: '铁拳突击勋章',
    desc: '使用全弹灭绝风暴单次击毁 4 辆以上敌方坦克',
    check: (stats) => stats.maxUltMultiKill >= 4
  },
  {
    id: 'hero_commander',
    name: '英雄车长勋章',
    desc: '成功击溃第 6 战区终局要塞 BOSS 取得最终胜利',
    check: (stats) => stats.gameWon === true
  }
];
```

---

## 🎨 视觉与 UI 表现需求 (待美化接入)
1. **战地整备卡牌面板**：采用磨砂玻璃质感、金铜边框、卡牌 Hover 微倾斜与发光粒子；
2. **结算大屏荣誉勋章墙**：金色立体金属勋章逐一盖章点亮，带有胜利军乐与礼炮声效。
