#-*- coding:utf-8 -*-
# C盘要有个wav文件，内含报时音频
import wx              
import time# 获取时间
import wave# 波形处理
import pyaudio# 播放器

class MyFrame(wx.Frame):
 def __init__(self,parent,id):
  wx.Frame.__init__(self,parent,id,title="整点报时",size=(410,150),style=wx.SYSTEM_MENU|wx.MINIMIZE_BOX|wx.CLOSE_BOX|wx.CAPTION)
  self.Center()
  self.InitUI()
  
 def InitUI(self):
  panel = wx.Panel(self)
  panel.SetBackgroundColour("green")
  t = time.strftime("%H:%M:%S",time.localtime())# 设置初始值
  self.text = wx.StaticText(panel,-1,t)
  font = wx.Font(72,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL,faceName="黑体")
  self.text.SetFont(font)
  self.text.SetForegroundColour("red")
  self.timer = wx.Timer(self)# 创建一个计时器对象
  self.Bind(wx.EVT_TIMER,self.Time,self.timer)# 绑定计时器事件
  self.timer.Start(1000)# 计时器计时1秒
  
 def Time(self,event):
  t = time.strftime("%H:%M:%S",time.localtime())
  self.text.SetLabel(t)# 刷新显示
  for i in range(0,24):
   temp = "{:0>2d}:00:00".format(i)
   if t == temp:# 判断是否为整点
    filename = "C:\\wav\\"+"{:0>2d}.wav".format(i)# 找到对应的wav文件路径
    self.Sound(filename)# 播放声音
    break
   
 def Sound(self,filename):
  f = wave.open(filename,'rb')# 加载音频文件（wav）
  pms = f.getparams()# 获取音频的属性参数
  nchannels, sampwidth, framerate, nframes = pms[:4]# 单独提取出各参数的值，并加以定义
  p = pyaudio.PyAudio()# 创建一个播放器
  s = p.open(format = p.get_format_from_width(sampwidth),channels = nchannels,rate = framerate,output = True)# 将音频转换为音频流
  while True:
   data = f.readframes(1024)# 按照1024大小的块，读取音频数据，得到一系列二进制编码
   if data == b'':
    break
   s.write(data)# 开始按照音频的参数，播放音频
  s.close()
  p.terminate()
   
if __name__ == '__main__':
 app = wx.App()           # 初始化wx.App类
 frame = MyFrame(parent=None, id=-1) # 实例MyFrame类，并传递参数
 frame.Show()            # 显示窗口
 app.MainLoop()           # 调用App类的MainLoop()主循环方法
