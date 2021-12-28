# -*- coding: utf-8 -*-
import socket
import time
# import picamera
import subprocess
import random
import jtalk
# from voice_lab import app

host = 'localhost'
port = 10500

# Juliusに接続する準備
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

res = ''
while True:
    # 音声認識の区切りである「改行+.」がくるまで待つ
    while (res.find('\n.') == -1):
        # Juliusから取得した値を格納していく
        res += sock.recv(1024)

    word = ''
    for line in res.split('\n'):
        # Juliusから取得した値から認識文字列の行を探す
        index = line.find('WORD=')
        # 認識文字列があったら...
        if index != -1:
            # 認識文字列部分だけを抜き取る
            line = line[index + 6 : line.find('"', index + 6)]
            # 文字列の開始記号以外を格納していく
            if line != '[s]':
                word = word + line
                print('word：' + word)
        # 文字列を認識したら...
        if word == 'おはよう':
            # voice_message = app.lambda_handler()
            scp = subprocess.Popen("scp ec2-user@ip-10-20-0-158:/home/ec2-user/speechbot/voice_lab/todo.db /home/pi/speechbot/voice_lab/", shell=True, stdout=subprocess.PIPE)
            scp.wait()

            voice_message = subprocess.Popen("python3 /home/pi/speechbot/voice_lab/app.py", shell=True, stdout=subprocess.PIPE)
            voice_message.wait()
            word = voice_message.communicate()[0]
            jtalk.jtalk(word.decode(u"utf-8"))
            # sleepしないと喋ってるときに中断されるからプロセスの終了を待つとかのコードを書かないといけないかも
            time.sleep(10)

        if word == 'おやすみ':
            # jtalk = ['python3', '/home/pi/speechbot/jtalk.py', word] 
            # voice = subprocess.Popen(jtalk)
        # elif word == 'おやすみ':
            jtalk.jtalk(word.decode(u'utf-8'))
            # jtalk.jtalk(u'おやすみまる') 
        res = ''
    