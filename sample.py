import subprocess
import time
import os
import signal

cmd = "mplayer -ao alsa:device=hw=3.0 siren.mp3"
p = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
cmd_display = "sudo /home/pi/rpi-rgb-led-matrix/examples-api-use/demo -D 1 --led-rows=32 --led-cols=64 --led-slowdown-gpio=4  /home/pi/rpi-rgb-led-matrix/ppm_samples/eva_warning.ppm"
display = subprocess.Popen(cmd_display, shell=True, preexec_fn=os.setsid)
time.sleep(5)
# p.kill()
os.killpg(os.getpgid(p.pid), signal.SIGTERM)
wav = subprocess.Popen("aplay -D plughw:3,0 open_jtalk.wav", shell=True)
wav.wait()
# wav.kill()
os.killpg(os.getpgid(display.pid), signal.SIGTERM)