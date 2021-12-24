#coding: utf-8
import subprocess
from datetime import datetime
import sys

def jtalk(t):
    # 合成音声の作成
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
    # 音声の読み上げ
    aplay = ['aplay','-q','-D', 'plughw:3,0','open_jtalk.wav'] #-Dhw:{カード番号},{デバイス番号}
    # aplay = ['aplay','-q','-D', 'plughw:3,0','futta-amorous.wav'] #-Dhw:{カード番号},{デバイス番号}
    wr = subprocess.Popen(aplay)

def main():
    text = 'テストだよー'
    jtalk(text)

if __name__ == '__main__':
    args = sys.argv
    word = args[1]
    jtalk(word)
    
