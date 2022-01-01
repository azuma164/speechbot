import subprocess
import time

cmd = "mplayer siren.mp3"
p = subprocess.Popen("exec " + cmd, shell=True)
time.sleep(10)
p.kill()
subprocess.Popen("aplay open_jtalk.wav", shell=True)