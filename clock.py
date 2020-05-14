#-*- coding:utf-8 -*-
import e32
import audio
import time
import appuifw
import sys
import os.path
import marshal
 
def say(oclock):
    """say the time in English"""
    c = oclock
    if c > 12:
        c -= 12
    cs = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'][c]
    audio.say("it's " + cs + " o'clock.")
    
def say_current():
    global Sayflags
    t = time.localtime()
    # say according to configuration
    if Sayflags[int(t[3])] == 1:
        say(t[3])
    
def on_oclock():
    """when an o'clock arrived"""
    say_current()
    start_timer()
    
def start_timer():
    """start a timer that will be reached at next o'clock"""
    global Timer
    lt = time.localtime()
    d = 60 * (59 - lt[4]) + 61 - lt[5]
    if d>2147:
        Timer.after(2147, lambda :  Timer.after(d-2147, on_oclock)) 
    else:
        Timer.after(d, on_oclock)
    
def clock_names():
    return [u'0:00', u'1:00', u'2:00', u'3:00', u'4:00', u'5:00', u'6:00', u'7:00', u'8:00', u'9:00', u'10:00', u'11:00', u'12:00', u'13:00', u'14:00', u'15:00', u'16:00', u'17:00', u'18:00', u'19:00', u'20:00', u'21:00', u'22:00', u'23:00']
    
def list_handler():
    """set flag and refresh the listbox"""
    global Lb
    global Sayflags
    c = Lb.current()
    Sayflags[c] = 1 - Sayflags[c]
    Lb.set_list(list_content(), c)
 
def list_content():
    global Sayflags
    icons = [appuifw.Icon(u"z:\\resource\\apps\\avkon2.mif", 16506, 16507), appuifw.Icon(u"z:\\resource\\apps\\avkon2.mif", 16504, 16505)] # unchecked, unchecked
    return map(lambda s, f: tuple([s, icons[f]]), clock_names(), Sayflags)
    
def exit_handler():
    global Lock
    global Timer
    global Standalone
    Timer.cancel()
    save_cfg()
    if not Standalone:
        Lock.signal()
    else:
        appuifw.app.set_exit()
 
def save_cfg():
    global Sayflags
    try:
        f = open(Configfile, 'wb')
        marshal.dump(Sayflags, f)
        f.close()
    except:
        pass
    
def load_cfg():
    global Sayflags
    try:
        f = open(Configfile, 'rb')
        Sayflags = marshal.load(f)
        f.close()
    except:
        pass
 
# Testing code
def test():
    say_current()
    #on_oclock()
    #for n in range(1,13):
    #    say(n)
#test()
 
def main():
    global Standalone
    appuifw.app.title = u'Audio Clock'
    appuifw.app.exit_key_handler = exit_handler
    appuifw.app.body = Lb
    if time.localtime()[4] == 0:
        say_current()
    start_timer()
    if not Standalone:
        Lock.wait()
    
Standalone = True
Timer = e32.Ao_timer()
Lock = e32.Ao_lock()
Configfile = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\audioclock.cfg'
Sayflags = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1] #24 clocks' flags
load_cfg()
Lb = appuifw.Listbox(list_content(), list_handler)
main()
