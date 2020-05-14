#-*- coding:utf-8 -*-
class Person(object):
	"""人的类"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		self.gun = None#用来保存枪对象的引用
		self.hp = 100

	def install_bullet_to_gun(self, clip_temp, bullet_temp):
		"""把子弹装到弹夹中"""

		#弹夹.保存子弹(子弹)
		clip_temp.save_bullet(bullet_temp)

	def install_clip_to_gun(self, gun_temp, clip_temp):
		"""把弹夹安装到枪中"""

		#枪.保存弹夹(弹夹)
		gun_temp.save_clip(clip_temp)

	def naqiang(self, gun_temp):
		"""拿起一把枪"""
		self.gun = gun_temp

	def __str__(self):
		if self.gun:
			return "\033[0;30;40m%s的血量为:%d, 他有枪 %s\033[0m"%(self.name, self.hp, self.gun)
		else:
			if self.hp>0:
				return "\033[0;31;41m%s的血量为%d, 他没有枪\033[0m"%(self.name, self.hp)
			else:
				return "\033[0;32;42m%s 已挂....\033[0m"%self.name

	def shot(self, diren):
		"""让枪发射子弹去打敌人"""
		#枪.开火(敌人)

		self.gun.fire(diren)

	def blood_drop(self, damage_amount):
		"""根据杀伤力，掉相应的血量"""
		self.hp -= damage_amount

class Gun(object):
	"""枪类"""
	def __init__(self, name):
		super(Gun, self).__init__()
		self.name = name#用来记录枪的类型
		self.clip = None#用来记录弹夹对象的引用

	def save_clip(self, clip_temp):
		"""用一个属性来保存这个弹夹对象的引用"""
		self.clip = clip_temp

	def __str__(self):
		if self.clip:
			return "\033[0;33;43m枪的信息为:%s, %s\033[0m"%(self.name, self.clip)
		else:
			return "\033[0;34;44m枪的信息为:%s,这把枪中没有弹夹\033[0m"%(self.name)

	def fire(self, diren):
		"""枪从弹夹中获取一发子弹，然后让这发子弹去击中敌人"""

		#先从弹夹中取子弹
		#弹夹.弹出一发子弹()
		bullet_temp = self.clip.tanchu_bullet()

		#让这个子弹去伤害敌人
		if bullet_temp:
			#子弹.打中敌人(敌人)
			bullet_temp.dazhong(diren)
		else:
			print("\033[0;35;45m弹夹中没有子弹了。。。。\033[0m")



class Danjia(object):
	"""弹夹类"""
	def __init__(self, max_num):
		super(Danjia, self).__init__()
		self.max_num = max_num#用来记录弹夹的最大容量
		self.bullet_list = []#用来记录所有的子弹的引用

	def save_bullet(self, bullet_temp):
		"""将这颗子弹保存"""
		self.bullet_list.append(bullet_temp)

	def __str__(self):
		return "\033[0;36;46m弹夹的信息为:%d/%d\033[0m"%(len(self.bullet_list), self.max_num)

	def tanchu_bullet(self):
		"""弹出最上面的那颗子弹"""
		if self.bullet_list:
			return self.bullet_list.pop()
		else:
			return None

class Zidan(object):
	"""子弹类"""
	def __init__(self, damage_amount):
		super(Zidan, self).__init__()
		self.damage_amount = damage_amount#这颗子弹的威力

	def dazhong(self, diren):
		"""让敌人掉血"""

		#敌人.掉血(一颗子弹的威力)
		diren.blood_drop(self.damage_amount)


def main():
	"""用来控制整个程序的流程"""

	#1. 创建百里守约对象
	baili = Person("百里守约")

	#2. 创建一个枪对象
	m82a1 = Gun("m82a1")

	#3. 创建一个弹夹对象
	clip = Danjia(20)

	#4. 创建一些子弹
	for i in range(15):
		bullet = Zidan(10)

		#5. 百里守约把子弹安装到弹夹中
		#百里守约.安装子弹到弹夹中(弹夹，子弹)
		baili.install_bullet_to_gun(clip, bullet)

	#6. 百里守约把弹夹安装到枪中
	#百里守约.安装弹夹到枪中(枪，弹夹)
	baili.install_clip_to_gun(m82a1, clip)

	#test:测试弹夹的信息
	#print(clip)

	#test:测试枪的信息
	#print(m82a1)

	#7. 百里守约拿枪
	#百里守约.拿枪(枪)
	baili.naqiang(m82a1)

	#test:测试百里守约对象
	print('\033[0;37;47m baili\033[0m')

	#8. 创建一个敌人
	baronnash = Person("纳什男爵")
	print(baronnash)

	#9. 百里守约开枪打敌人
	#百里守约.扣扳机(纳什男爵)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)
	baili.shot(baronnash)
	print(baronnash)
	print(baili)

if __name__ == '__main__':
	main()
