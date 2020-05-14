#-*- coding:utf-8 -*-

#创建一个英雄类
class Hero(object):
    def __init__(self, name):
        super(Hero, self).__init__()
        self.name = name
        self.gun = None #用来保存枪对象的引用
        self.hp = 600
    #将子弹安装到弹夹中
    def install_bullet_to_clip(self, clip_temp, bullet_temp):
        #弹夹.保存子弹(子弹)
        clip_temp.save_bullet(bullet_temp)

    #将弹夹安装到武器上
    def install_clip_to_gun(self, gun_temp, clip_temp):
        #枪.保存弹夹(弹夹)
        gun_temp.save_clip(clip_temp)
    #英雄拿起武器
    def armed(self, gun_temp):
        self.gun = gun_temp
    def __str__(self):
        if self.gun:
            return "\033[0;34;44m %s的血量:%d,已武装%s\033[0m"%(self.name, self.hp, self.gun)
        else:
            if self.hp > 0:
                return "\033[0;35;45m %s的血量:%d,没有武装\033[0m"%(self.name, self.hp)

            else:
                return "\033[0;36;46m %s挂了...game over~"%self.name

    def pull_trigger(self, enemy):
        #用一个属性来保存这个弹夹对象的引用
        self.gun.shot(enemy)
    #根据伤害量掉血
    def blood_drop(self, damage_amount):
        self.hp -= (damage_amount * 10)

#    def __str__(self):
#        if self.clip:
#            return "\033[0;36;46m 枪的信息:%s, %s"%(self.name, self.clip)
#        else:
#            return "\033[0;37;47m 枪的信息:%s,枪中没有弹夹"%(self.name)
#
#    def shot(self, enemy):
#        #枪从弹夹中获取一发子弹，然后让这发子弹集中怪兽
#        #先从弹夹中取子弹
#        clip_temp = self.clip.shot_out()
#
#        #让这颗子弹去伤害怪兽
#        if shot_temp:
#            #子弹打中怪兽
#            shot_temp.hit(enemy)
#        else:
#            print('\033[0;37;47m 弹夹中没有子弹...\033[0m')
#
#创建武器类
class Gun(object):
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name #用来记录枪的类型
        self.clip = None #用来记录弹夹对象的引用

    #用一个属性保存这个弹夹对象的引用
    def save_clip(self, clip_temp):
        self.clip = clip_temp

    def __str__(self):
        if self.clip:
            return "\033[0;30;40m枪的信息:%s,%s\033[0m"%(self.name, self.clip)
        else:
            return "\033[0;31;41m枪的信息:%s,枪没有弹夹\033[0m"%(self.name)

    def shot(self, enemy):
        # 枪从弹夹中获取一发子弹，然后让这发子弹去击中敌人
        #先从弹夹中获取子弹
        bullet_temp = self.clip.sub_bore()
        #让这颗子弹去伤害敌人
        if bullet_temp:
            bullet_temp.hit(enemy)
        else:
            print('\033[0;37;47m弹夹中没有子弹了...\033[0m')

#创建弹夹类
class Clip(object):
    def __init__(self, max_num):
        super(Clip, self).__init__()
        self.max_num = max_num #用来记录弹夹容量
        self.bullet_list = [] #记录所有的子弹的引用
    #将子弹保存到弹夹中
    def save_bullet(self, bullet_temp):
        #保存这颗子弹
        self.bullet_list.append(bullet_temp)

    def __str__(self):
        return "\033[0;32;42m 弹夹%d个，子弹%d颗\033[0m"%(len(self.bullet_list), self.max_num)
    #子弹出膛
    def sub_bore(self):
        #从弹夹中取出最上面的子弹
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None

#创建子弹类
class Bullet(object):
    def __init__(self, damage_amount):
        super(Bullet, self).__init__()
        self.damage_amount = damage_amount #子弹的伤害
    
    def hit(self, enemy):
        #是敌人血量减少
        enemy.blood_drop(self.damage_amount)

def main():
    '''控制整个程序的流程'''
    #1.创建百里守约对象
    baili = Hero('百里守约')
    #2.创建武器对象
    m82a1 = Gun("巴雷特")
    #3.创建弹夹对象
    clip = Clip(10)
    #4.创建子弹对象
    #bullet = Bullet(1600)
    for i in range(15):
        bullet = Bullet(10)
        #安装子弹到弹夹中
        baili.install_bullet_to_clip(clip, bullet)
    #5.创建怪兽对象
    
    #6.百里守约将子弹安装到弹夹中
   # baili.shangdan(clip, bullet)
    #7.百里守约将弹夹安装到武器上
    baili.install_clip_to_gun(m82a1, clip)
    print('\033[0;33;43m 弹夹信息:clip\033[0m')
    print('\033[0;34;44m 枪的信息:m82a1\033[0m')
    #8.百里守约拿起武器
    baili.armed(m82a1)
    #输出英雄的信息
   # print(baili)
    #9.创建一个怪兽
    BaronNash = Hero('纳什男爵')
    print('\033[0;35;45m BaronNash\033[0m')
    #10.百里守约使用武器射击怪兽
    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)

    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)

    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)
    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)
    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)
    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)
    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)
    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)
    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)
    baili.pull_trigger(BaronNash)
    print(BaronNash)
    print(baili)
if __name__ == '__main__':
    main()
