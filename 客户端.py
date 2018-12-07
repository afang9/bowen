# import socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# soc.connect(('192.168.0.24',200))
# aaa='nihao'
# soc.send(aaa.encode('utf-8'))
# msg=soc.recv(1024)
# print(msg.decode('utf-8'))

# import socket                             #UDP
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送请求数据
# a=('192.168.0.24',200)
# while True:
#     reg=input('来吧！')
#     soc.sendto(reg.encode('utf-8'),a)
#     #接收相应
#     c=soc.recv(1024)
#     print(c.decode('utf-8'))
# import socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# soc.connect(('192.168.0.24',200))
# aaa='无敌最是寂寞，可耐一代红粉佳人！'
# soc.send(aaa.encode('utf-8'))
# msg=soc.recv(1024)
# print(msg.decode('utf-8'))


# import socket
# # soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # soc.connect(('192.168.0.53',200))
# # aaa='这你都知道？果然和他是同道中人！'
# # soc.send(aaa.encode('utf-8'))
# # mes=soc.recv(1024)
# # print(mes.decode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.62',200))
# aaa='继续看书！'
# s.send(aaa.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

# import socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# soc.connect(('192.168.0.62',200))
# reg='五心！'
# soc.send(reg.encode('utf-8'))
# msg=soc.recv(1024)
# print(msg.decode('utf-8'))

# import socket
# # soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # soc.connect(('127.0.0.1',200))
# # reg='有些饿！'
# # soc.send(reg.encode('utf-8'))
# # msg=soc.recv(1024)
# # print(msg.decode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('127.0.0.1',200)
# reg='wuyan'
# s.sendto(reg.encode('utf-8'),a)
# recv=s.recv(1024)
# print(recv.decode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.91',200))
# reg='执子之手，相濡以沫！'
# s.send(reg.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.91',200))
# aa='劝君一杯酒，事后莫强求'
# s.send(aa.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('192.168.0.91',100)
# reg='事事有心，却始终不及别人的一刹！'
# s.sendto(reg.encode('utf-8'),a)
# msg=s.recv(1024)
# print(msg.decode('utf-8'))


# import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # a=('192.168.0.91',100)
# # aa='细心懦弱之人，狠劲必然更胜一层！'
# # s.sendto(aa.encode('utf-8'),a)
# # msg=s.recv(1024)
# # print(msg.decode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('192.168.0.91',100)
# reg='事无伦常，初心已改，再过往，寥寥几笔而已！'
# s.sendto(reg.encode('utf-8'),a)
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.91',100))
# reg='唱首歌给你听！'
# s.send(reg.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

# import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # a=('192.168.0.91',100)
# # reg='有趣的灵魂万里挑一！'
# # s.sendto(reg.encode('utf-8'),a)
# # meg=s.recv(1024)
# # print(meg.decode('utf-8'))


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('0.0.0.0',100)
# s.bind(a)
# s.listen(4)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='dada'
#     a.send(reg.encode('utf-8'))

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('192.168.0.91',100)
# reg='世事无常，岂能无心！'
# s.sendto(reg.encode('utf-8'),a)
# msg=s.recv(1024)
# print(msg.decode('utf-8'))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.22',200))
# reg='...'
# s.send(reg.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('192.168.0.39',100)
# reg='gg'
# s.send(reg.encode('utf-8'),a)
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

# if __name__!='__main__':
#     脚本联系.zhishu()
# import os
# # print(os.listdir(r'E:\QQ\1241378256\FileRecv'))
# # pu_tong=0
# # for i in os.listdir():
# #     # print(type(i))
# #     if os.path.splitext(i)[-1]=='.py':
# #         # print(len(i))
# #     #     break
# #     # else:
# #         pu_tong+=1
# # print(pu_tong)
# # print(os.path.splitext(r'e:\gh.py'))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.32',100))
# reg='dfd'
# s.send(reg.encode('utf-8'))
# msg=s.recv(1024)
# print(msg.decode('utf-8'))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('192.168.0.32',100)
# reg='dgd'
# s.sendto(reg.encode('utf-8'),a)
# msg=s.recv(1024)
# print(msg.decode('utf-8'))

