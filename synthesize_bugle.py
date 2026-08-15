import wave
import math
import struct
import os

def generate_charge_bugle(output_file="audio/charge_bugle.wav"):
    os.makedirs("audio", exist_ok=True)
    sample_rate = 44100
    
    # 经典中国抗战军号冲锋号谱 (Standard Chinese Military Charge Bugle)
    # (freq_hz, duration_sec, is_accent, pause_after)
    G3 = 392.00
    C4 = 523.25
    E4 = 659.25
    G4 = 783.99
    C5 = 1046.50
    E5 = 1318.51

    score = [
        # 第一句: 嘀嘀哒嘀哒——
        (G3, 0.12, 0.8, 0.02),
        (C4, 0.14, 0.9, 0.02),
        (E4, 0.14, 0.9, 0.02),
        (G4, 0.18, 0.95, 0.02),
        (C5, 0.42, 1.0, 0.08),

        # 第二句: 哒哒哒 嘀哒——
        (C5, 0.09, 0.95, 0.02),
        (C5, 0.09, 0.95, 0.02),
        (C5, 0.12, 1.0, 0.03),
        (G4, 0.14, 0.85, 0.02),
        (E4, 0.14, 0.85, 0.02),
        (C4, 0.38, 0.9, 0.08),

        # 第三句（冲锋高潮）: 嘀— 嘀哒嘀哒 嘀哒————！
        (G3, 0.16, 0.85, 0.03),
        (G3, 0.09, 0.8, 0.02),
        (C4, 0.11, 0.9, 0.02),
        (E4, 0.11, 0.9, 0.02),
        (G4, 0.15, 0.95, 0.02),
        (C5, 0.22, 1.0, 0.02),
        (G4, 0.18, 0.95, 0.02),
        (C5, 1.15, 1.0, 0.45) # 激昂拖长音
    ]

    total_samples = int(sample_rate * (sum(d + p for _, d, _, p in score) + 0.8))
    buffer = [0.0] * total_samples

    cursor = 0
    for freq, duration, accent, pause in score:
        note_samples = int(sample_rate * duration)
        for i in range(note_samples):
            t = i / sample_rate
            # 军号唇簧振动与泛音列 (Brass Harmonic Series Formulation)
            # 铜管乐器具有丰富的 1~6 次谐波与共鸣峰
            vibrato = 1.0 + 0.015 * math.sin(2 * math.pi * 5.5 * t) if t > 0.2 else 1.0
            cur_freq = freq * vibrato
            
            # 谐波叠加 (Odd and even brass overtones)
            h1 = math.sin(2 * math.pi * cur_freq * t)
            h2 = 0.65 * math.sin(2 * math.pi * cur_freq * 2 * t)
            h3 = 0.45 * math.sin(2 * math.pi * cur_freq * 3 * t)
            h4 = 0.30 * math.sin(2 * math.pi * cur_freq * 4 * t)
            h5 = 0.20 * math.sin(2 * math.pi * cur_freq * 5 * t)
            h6 = 0.12 * math.sin(2 * math.pi * cur_freq * 6 * t)
            
            raw_sample = h1 + h2 + h3 + h4 + h5 + h6
            # 铜管物理共振与软削峰饱和 (Tube non-linear brass projection)
            raw_sample = math.tanh(raw_sample * 1.35)

            # 吹奏起音与释音包络 (ADSR Envelope)
            attack_time = 0.025
            release_time = 0.045
            if t < attack_time:
                env = (t / attack_time) ** 1.3
            elif t > duration - release_time:
                env = (duration - t) / release_time
            else:
                env = 1.0

            val = raw_sample * env * accent * 0.55
            if cursor + i < total_samples:
                buffer[cursor + i] += val

        cursor += note_samples + int(sample_rate * pause)

    # 添加山谷战场远景混响 (Battlefield Valley Echo / Reverb Tail)
    reverb_delay1 = int(sample_rate * 0.18)
    reverb_delay2 = int(sample_rate * 0.36)
    reverb_delay3 = int(sample_rate * 0.54)
    for i in range(total_samples):
        if i >= reverb_delay1:
            buffer[i] += buffer[i - reverb_delay1] * 0.26
        if i >= reverb_delay2:
            buffer[i] += buffer[i - reverb_delay2] * 0.14
        if i >= reverb_delay3:
            buffer[i] += buffer[i - reverb_delay3] * 0.07

    # 归一化与 16-bit PCM 输出
    max_val = max(abs(s) for s in buffer) or 1.0
    with wave.open(output_file, 'wb') as wav_out:
        wav_out.setnchannels(1)
        wav_out.setsampwidth(2)
        wav_out.setframerate(sample_rate)
        
        frames = bytearray()
        for sample in buffer:
            norm = (sample / max_val) * 0.92
            int_sample = int(norm * 32767.0)
            int_sample = max(-32768, min(32767, int_sample))
            frames.extend(struct.pack('<h', int_sample))
        
        wav_out.writeframes(frames)
    
    print(f"Generated {output_file}, size: {os.path.getsize(output_file)} bytes")

if __name__ == "__main__":
    generate_charge_bugle()
