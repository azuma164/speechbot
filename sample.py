import subprocess
import time

cmd = "mplayer siren.mp3"
p = subprocess.Popen("exec " + cmd, shell=True)
time.sleep(1)
# p.kill()
wav = subprocess.Popen("aplay open_jtalk.wav", shell=True)
wav.wait()
p.kill()