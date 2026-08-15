# 模块一：第 6 战区终局巨型要塞 BOSS 战开发方案

## 🎯 模块设计目标
在第 6 战区（Wave 6，最终防线）打破常规杂兵刷新逻辑，改为生成一辆巨大的**【超重型陆地巡洋要塞 · 钢铁利维坦】**。拥有独立血条、多炮塔独立索敌、分阶段战斗形态与召唤僚机机制。

---

## 🛠️ 底层数据结构设计

```javascript
/* BOSS 实体对象结构 */
const boss = {
  active: false,
  o: THREE.Group,           // BOSS 整体 3D 根节点（尺寸约为普通坦克 3.5 倍）
  hp: 60,                   // BOSS 总血量
  maxHp: 60,
  phase: 1,                 // 当前阶段 (1: 巡航炮击 -> 2: 狂暴机枪阵列 -> 3: 绝境全弹齐射)
  speed: 0.38,              // 缓慢压进的沉重移动速度
  lastPos: new THREE.Vector3(),
  turrets: [
    {
      id: 'main_heavy',     // 主炮塔（超重型 152mm 主炮）
      group: THREE.Group,
      barrel: THREE.Mesh,
      recoilVal: 0,
      reload: 2.2,
      maxReload: 2.2,
      damage: 3,
      offset: { x: 0, y: 1.8, z: 0.4 }
    },
    {
      id: 'sub_left',       // 左副炮塔（速射穿甲炮）
      group: THREE.Group,
      barrel: THREE.Mesh,
      recoilVal: 0,
      reload: 1.0,
      maxReload: 1.0,
      damage: 1,
      offset: { x: -1.8, y: 1.2, z: -1.6 }
    },
    {
      id: 'sub_right',      // 右副炮塔（速射穿甲炮）
      group: THREE.Group,
      barrel: THREE.Mesh,
      recoilVal: 0,
      reload: 1.0,
      maxReload: 1.0,
      damage: 1,
      offset: { x: 1.8, y: 1.2, z: -1.6 }
    }
  ],
  weakpoints: [             // 弱点系统（攻击弱点受到 2.5 倍伤害）
    { id: 'rear_engine', x: 0, y: 1.2, z: 3.2, r: 1.4, destroyed: false }
  ]
};
```

---

## ⚙️ 核心逻辑流程与状态机

### 1. 生成与阶段转换判定 (Phase Logic)
```javascript
function updateBossPhase() {
  const hpRatio = boss.hp / boss.maxHp;
  
  if (hpRatio > 0.65) {
    boss.phase = 1; // 阶段一：标准多炮塔轮番索敌
  } else if (hpRatio > 0.30 && boss.phase === 1) {
    boss.phase = 2; // 阶段二：狂暴提速 + 召唤 2 辆轻型侦察僚机
    boss.speed = 0.52;
    spawnEnemy('scout');
    spawnEnemy('scout');
    pushCombatFeed('⚠️ 警告：要塞装甲外壳剥落！进入狂暴突进阶段！');
  } else if (hpRatio <= 0.30 && boss.phase === 2) {
    boss.phase = 3; // 阶段三：绝境全弹齐射，主副炮装填时间缩短 50%
    boss.turrets.forEach(t => t.maxReload *= 0.6);
    pushCombatFeed('🚨 紧急战报：要塞主发电机超载！启动全域毁灭齐射！');
  }
}
```

### 2. 多炮塔独立旋转与射击 (Multi-Turret Aiming)
- **主炮塔**：始终以平稳角速度追踪玩家坐标，射程极远，命中造成 3 点破甲伤害；
- **左右副炮**：分别锁定玩家左右微偏角度，形成封锁交叉火力。

---

## 🎨 视觉与 UI 表现需求 (待美化接入)
1. **顶部专属巨型 BOSS 血条**：带有分段标记（3 个阶段刻度线）与装甲金边；
2. **重型履带泥雪飞溅与履带压痕**；
3. **分部位起火与断裂黑烟**（血量低于 50% 引擎冒火，血量为 0 时发生多重连续大爆炸）。
