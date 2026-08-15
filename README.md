# 🇨🇳 3D 抗战装甲防线：钢铁风暴 (Tank Battle 3D)

> **纪念中国人民抗日战争暨世界反法西斯战争胜利 81 周年** 专属定制作品级 3D 沉浸式装甲战争网页游戏。

---

## 🎮 游戏核心特色与架构

- **3D 战场物理与真实装甲渲染**：采用 Three.js 构建 3D 战场、动态风雪/夜战照明弹、独立炮塔俯仰瞄准与战车动态悬挂系统；
- **历史战地广播与真实抗战冲锋号**：
  - 5 套随机战前动员开场白（延安新华广播电台、八路军前敌总指挥部、新华社前线特刊等）；
  - 100% 真实军乐冲锋号现场实录（通过 Web Audio 2.4x 高动态增益节点与铜管高频泛音增强播放）；
- **沉浸重装甲声学引擎**：无缝消除尖锐激光音，全频换装 105mm/122mm 重炮次低频火药爆轰、48Hz 装甲钢板钝击与跳弹偏折；
- **Roguelike 战地军功改装**：穿甲脱壳翼稳弹 (APFSDS)、高爆碎甲弹 (HE)、复合披挂装甲、涡轮增压引擎等；
- **终极战术技能**：`E` 键 360° 环形歼灭风暴、`Q` 键战术烟幕抢修、空中补给空投箱。

---

## 🚀 部署至 Netlify 步骤指南

本游戏为纯静态架构（Pure Static Web Application），原生支持一键部署到 Netlify。

### 方式一：Git 仓库自动持续部署（推荐）
1. 在 [GitHub](https://github.com/new) 或 [Gitee](https://gitee.com/projects/new) 上创建一个新仓库（例如 `tank-battle-3d`）；
2. 在本地执行推送（见下方 Git 指令）；
3. 打开 [Netlify 控制台](https://app.netlify.com/) -> 点击 **"Add new site"** -> **"Import an existing project"**；
4. 选择您的 GitHub / Gitee 仓库，构建设置（Build Settings）默认留空（Publish directory 填 `.`），点击 **"Deploy site"**；
5. Netlify 将在 15 秒内自动生成一个全球 CDN 加速的在线访问链接（例如 `https://your-tank-game.netlify.app`）。

### 方式二：Netlify Drop 一键拖拽部署（免命令行）
1. 访问 [https://app.netlify.com/drop](https://app.netlify.com/drop)；
2. 直接将包含 `index.html` 的本项目整个文件夹拖入网页框中；
3. 网页将瞬间完成上传并直接生成在线游戏链接！

---

## 💻 本地运行方法

可以使用任意静态 HTTP 服务器进行本地运行与测试：

```bash
# 使用 Python 启动本地服务
python -m http.server 8080

# 然后在浏览器打开
http://localhost:8080/index.html
```

---

## 📁 目录结构概览

```text
├── index.html                  # 核心 3D 游戏主程序与 UI 界面
├── netlify.toml                # Netlify 静态部署与媒体缓存策略
├── _redirects                  # 单页路由重定向规则
├── three.module.js             # Three.js 3D 渲染核心库
├── victory.jpg                 # 革命胜利纪念主题海报
├── dongfanghong_short.mp3      # 精炼版《东方红》开场进行曲
├── audio/                      # 战地广播语音与真实冲锋号音频库
│   ├── charge_bugle.mp3        # 真实军号冲锋号实录音频
│   ├── broadcast_intro_1~5.mp3 # 5 组随机战前开场白播音
│   ├── broadcast_mobilize_1~3  # 3 组战中动员与战术口令
│   ├── broadcast_boss.mp3      # 要塞 BOSS 突入军情广播
│   ├── broadcast_victory.mp3   # 伟大胜利大捷特刊
│   └── broadcast_defeat.mp3    # 战地重整号召
└── game_upgrade_plan/          # 8 大模块升级方案与设计文档
```
