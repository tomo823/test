import numpy as np
import librosa
import scipy
from pydub import AudioSegment
import matplotlib.pyplot as plt

# mp3ファイルの読み込み
def load_audio(file_path):
    audio = AudioSegment.from_file(file_path, format="mp3")
    audio = audio.set_channels(1)  # モノラル変換
    audio_samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
    return audio_samples, audio.frame_rate

# 短時間フーリエ変換 (STFT)
def stft(audio_samples, sample_rate):
    return librosa.stft(audio_samples)

# ノイズ除去処理
def noise_reduction(stft_data, threshold=0.1):
    magnitude, phase = librosa.magphase(stft_data)
    magnitude[magnitude < threshold] = 0  # 閾値以下を0にする
    return magnitude * phase

# 逆STFT
def istft(stft_data):
    return librosa.istft(stft_data)

# 音声の保存
def save_audio(audio_samples, sample_rate, output_path):
    audio_segment = AudioSegment(
        audio_samples.tobytes(),
        frame_rate=sample_rate,
        sample_width=audio_samples.dtype.itemsize,
        channels=1
    )
    audio_segment.export(output_path, format="mp3")

# メイン処理
def process_audio(input_file, output_file):
    # 音声の読み込み
    audio_samples, sample_rate = load_audio(input_file)

    # 周波数解析 (STFT)
    stft_data = stft(audio_samples, sample_rate)

    # ノイズ除去
    stft_clean = noise_reduction(stft_data)

    # 時間領域に戻す
    cleaned_audio = istft(stft_clean)

    # 音声を保存
    save_audio(cleaned_audio, sample_rate, output_file)

    # 結果の表示
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.title("Original Audio")
    librosa.display.specshow(librosa.amplitude_to_db(np.abs(stft_data), ref=np.max), sr=sample_rate, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')

    plt.subplot(2, 1, 2)
    plt.title("Cleaned Audio")
    librosa.display.specshow(librosa.amplitude_to_db(np.abs(stft_clean), ref=np.max), sr=sample_rate, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    
    plt.tight_layout()
    plt.show()

# ファイルパスを指定
input_file = "./split_1.mp3"
output_file = "output_cleaned.mp3"

process_audio(input_file, output_file)
