import subprocess
import time

cmd = "mplayer -ao alsa:device=hw=2.0 siren.mp3"
p = subprocess.Popen("exec " + cmd, shell=True)
time.sleep(5)
p.kill()
wav = subprocess.Popen("aplay -D plughw:2,0 open_jtalk.wav", shell=True)
wav.wait()
wav.kill()