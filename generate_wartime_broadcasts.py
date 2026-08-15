import asyncio
import edge_tts
import os

BROADCASTS = {
    "broadcast_intro.mp3": {
        "voice": "zh-CN-YunjianNeural",  # 沉稳雄浑、极具历史感与动员力的男声播音员
        "rate": "+5%",
        "pitch": "-2Hz",
        "text": "延安新华广播电台，陕北新华广播电台！全线装甲部队指战员注意：白岭防线阻击战正式打响！为了民族独立与和平，全线出击，坚决粉碎敌人进犯！"
    },
    "broadcast_mobilize.mp3": {
        "voice": "zh-CN-YunxiNeural",
        "rate": "+8%",
        "pitch": "+0Hz",
        "text": "战地紧急动员号召：同志们，我们身后就是祖国和人民，寸土不让！瞄准敌方重装甲目标，坚决开火！"
    },
    "broadcast_boss.mp3": {
        "voice": "zh-CN-YunjianNeural",
        "rate": "+10%",
        "pitch": "+0Hz",
        "text": "紧急战报！敌军超重型陆地巡洋要塞突破前沿防线！全体车组立即集中所有重炮火力，实施饱和打击！"
    },
    "broadcast_victory.mp3": {
        "voice": "zh-CN-YunjianNeural",
        "rate": "+6%",
        "pitch": "-1Hz",
        "text": "中央人民广播电台，新华社前线急电：白岭战区敌军主力已被全线歼灭！抗日战争取得伟大胜利！正义必胜！和平必胜！人民必胜！"
    },
    "broadcast_defeat.mp3": {
        "voice": "zh-CN-YunjianNeural",
        "rate": "+4%",
        "pitch": "-2Hz",
        "text": "革命尚未成功，同志仍需努力！全体指战员，重整装甲战车，誓死保卫阵地，准备再次出击！"
    }
}

async def generate():
    os.makedirs("audio", exist_ok=True)
    for filename, item in BROADCASTS.items():
        out_path = os.path.join("audio", filename)
        print(f"Generating {out_path}...")
        communicate = edge_tts.Communicate(item["text"], item["voice"], rate=item["rate"], pitch=item["pitch"])
        await communicate.save(out_path)
        print(f"Saved {out_path}, size: {os.path.getsize(out_path)} bytes")

if __name__ == "__main__":
    asyncio.run(generate())
