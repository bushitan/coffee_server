#coding:utf-8
'''
	图片转pdf操作
	需要安装 reportlab，安装地址如下
	pip install reportlab -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
'''
from PIL import Image,ImageDraw,ImageFont
import os
import re
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import shutil
import time

class QRPrint():
	def __init__(self):
		self.base_path = r"image/"
		self.card_width = 591
		self.card_height = 1063
		self.space = 20 #20
		self.space_left = 28 #基础28   # 广电打印机23
		self.space_top = 128

		# #普通版本
		# self.qr_x = 145
		# self.qr_y = 643  # 原有的位置
		# # self.qr_y = 590
		# self.qr_width = 300 # 二维码宽度
		# self.qr_height = 300 # 二维码高度


		#新版设计稿 current
		# self.qr_x = 145
		# self.qr_y = 290  # 原有的位置
		# self.qr_width = 300 # 二维码宽度
		# self.qr_height = 300 # 二维码高度

		# 白日梦想家专属
		self.qr_x = 165
		self.qr_y = 725
		self.qr_width = 260 # 二维码宽度
		self.qr_height = 260 # 二维码高度






		# 竖直图的位置
		# self.qr_x = 263
		# self.qr_y = 684
		# self.qr_width = 280 # 二维码宽度
		# self.qr_height = 280 # 二维码高度

		# 魏阿未版本
		# self.qr_x = 105
		# self.qr_y = 480
		# self.qr_width = 380 # 二维码宽度
		# self.qr_height = 380 # 二维码高度


		self.sn_space = 20 # SN序列号的空白位置

	# 获取打印的背景图
	# 不包含二维码
	# @param
	# 	bg_white	 A4空白背景
	# 	card_path 	 名片模板地址
	# 	template_out  A4模板输出地址
	def print_a4_template(self ,bg_white,card_path,template_out):
		bg_path = bg_white
		_card_path = card_path
		out = template_out
		im_bg = Image.open(bg_path)
		card = Image.open(_card_path)

		for i in range(0,4):
			_bx = (self.card_width + self.space) * i + self.space_left
			for j in range(0,3):
				_by = (self.card_height + self.space) * j + self.space_top
				im_bg.paste(card, (_bx, _by))
		im_bg.save(out)

	# 在已经打好的背景图上
	# 打印最终的二维码
	# @param
	# 	bg_path	 A4模板背景
	# 	qr_list  二维码列表
	# 	out_path 最终打印图片地址
	def print_a4_qr(self,bg_path,qr_list,out_path,page_index):
		bg = Image.open(bg_path)


		# 页面序号
		draw = ImageDraw.Draw(bg)
		ttfont = ImageFont.truetype("C:\\Windows\\Fonts\\STXINGKA.TTF",30)
		draw.text((10,10), str(page_index), fill=(0,0,0),font=ttfont)


		for i in range(0,5):
			_bx = (self.card_width + self.space  ) * i + self.space_left - self.space
			for j in range(0,4):
				_by = (self.card_height + self.space ) * j + self.space_top - self.space * 1.5
				# 取消中间的标记点
				# if i==1 and j==1:
				# 	continue
				# if i==1 and j==2:
				# 	continue
				# if i==2 and j==1:
				# 	continue
				# if i==2 and j==2:
				# 	continue
				# if i==3 and j==1:
				# 	continue
				# if i==3 and j==2:
				# 	continue
				draw.text((_bx,_by), str('-'), fill=(0,0,0),font=ttfont)
				# draw.arc((_bx, _by, 2, 2), 0, 360, 'black')

		# 粘贴二维码
		for i in range(0,4):

			_bx = (self.card_width + self.space) * i + self.space_left
			for j in range(0,3):
				_by = (self.card_height + self.space) * j + self.space_top

				if len(qr_list) <= 0 :
					break

				# 粘贴二维码
				qr_path = qr_list.pop(0)  # 从第一个拿数据
				qr = Image.open(qr_path)  # 画qr
				qr = qr.resize((self.qr_width ,self.qr_height)) # 重新设置二维码大小
				bg.paste(qr, (_bx  + self.qr_x , _by + self.qr_y ), mask=qr)

				# 写SN 序列号
				sn = qr_path.split("\\")[-1].split(".")[0]
				draw.text((_bx + self.sn_space * 1.5  ,_by + self.sn_space), str("SN:" + sn), fill=(64,56,65 , 120),font=ttfont)


		bg.save(out_path)


	# 数组拆分
	def arr_size(self,arr,size):
		s=[]
		for i in range(0,int(len(arr))+1,size):
			c=arr[i:i+size]
			s.append(c)
		return s


	def print_back(self,org_path,out_path):
		shutil.copyfile(org_path,out_path )


# 二维码工具
class QRUtils():
	def __init__(self,bg_path = "",template_path = "",out_path = ""):
		self.qr_print = QRPrint()
		self.bg_path = bg_path
		self.template_path = template_path
		self.out_path = out_path

	# 输出打印模板
	# 可以正、反同时使用
	def create_bg(self):
		self.qr_print.print_a4_template(
			self.bg_path ,
			self.template_path ,
			self.out_path
		)

	# 开始打印图片
	def start(self,qr_list,final_path):
		self.create_bg()
		# self.create_print(qr_list,final_path)
		self.qr_print.print_a4_qr(self.out_path,qr_list,final_path)

	# 读取所有二维码地址
	# @param
	# 	all_qr_list 二维码地址数组
	# 	file_save 正面存储地址
	#	org_back 背面原始地址
	def create_img(self,all_qr_list,file_save,org_back):
		_list = self.qr_print.arr_size(all_qr_list,12) # #将数组拆分为12
		# 将数组拆分为12长度的子数组
		for i, sub_list in enumerate( _list ):
			print (i,sub_list)
			# self.start(sub_list , file_save + r"r_%s.jpg" % (i)) # 打印二维码
			self.create_bg()

			# 打印正面图片
			self.qr_print.print_a4_qr(self.out_path,sub_list , file_save + r"%s.jpg" % (i) , i)

			time.sleep(1)
			# 复制背面图片
			self.qr_print.print_back(  org_back, file_save + r"%sb.jpg" % (i) )
			time.sleep(1)

	# 读取所有二维码地址
	# @param
	# 	file_path 包含qr文件夹的地址
	def read_all_qr_path(self,file_path):
		qr_list = []
		for root, dirs, files in os.walk(file_path):
			files = sorted(files,key = lambda i:int(re.match(r'(\d+)',i).group())) #按名字排序
			for f in files:
				qr_list.append(root + f)
			return qr_list

if __name__ == "__main__":

	# 唯一输入的文件夹名字
	#17_92601_93200
	#17_93201_93800

	input_qr_file_name = "17_93801_94400" #seeking


	BASE  =  unicode( r"E:\CarcerWorld\方案策划\6 咖啡地图 2019-2-11\1 集点卡\外卖卡券\制作\\" ,"utf-8")
	# 模板
	IMAGE_A4 =  BASE + unicode( r"1 原材料\bg.jpg" ,"utf-8")
	IMAGE_FRONT = BASE +  unicode(r"1 原材料\\front.jpg","utf-8")
	IMAGE_BACK = BASE +  unicode(r"1 原材料\\back.jpg","utf-8")

	print (os.path.exists(IMAGE_FRONT))
	# 打印底稿
	PRINT_BG_FRONT = BASE +  unicode(r'2 合成底稿\r_card_front_template.jpg',"utf-8")
	PRINT_BG_BACK = BASE +  unicode(r'2 合成底稿\r_card_back_template.jpg',"utf-8")

	# 二维码文件夹
	FILE_QR = BASE +  unicode(r'3 二维码文件夹\%s\\' % (input_qr_file_name),"utf-8")
	# 结果图片文件夹
	FILE_SAVE =  BASE + unicode(r'4 生成结果\\',"utf-8")


	# 创建背面
	card_back =  QRUtils(
		bg_path = IMAGE_A4,
		template_path = IMAGE_BACK,
		out_path = PRINT_BG_BACK
	)
	card_back.create_bg()

	card_front =  QRUtils(
		bg_path =IMAGE_A4,
		template_path = IMAGE_FRONT,
		out_path = PRINT_BG_FRONT
	)
	card_front.create_bg()
	qr_list = card_front.read_all_qr_path(FILE_QR)
	# 创建图片
	card_front.create_img(qr_list,FILE_SAVE  , PRINT_BG_BACK  )



















	# print (qr_list)


	# print (card_front.create_pdf(qr_list))
	# card_front.start(qr_list , r"image/r_final1.jpg")




	# # 创建背面
	# card_back =  QRUtils(
	# 	bg_path = r"image/bg.jpg",
	# 	template_path = r"image/card_back.jpg",
	# 	out_path = r"image/r_card_back_template.jpg"
	# )
	# card_back.create_bg()
	#
	# # 创建正面模板
	# card_front =  QRUtils(
	# 	bg_path = r"image/bg.jpg",
	# 	template_path = r"image/card_front.jpg",
	# 	out_path = r"image/r_card_front_template.jpg"
	# )
	#
	# qr_list = []
	# for i in range(0,12):
	# 	qr_list.append( r"image/qr.png")
	# card_front.start(qr_list , r"image/r_final1.jpg")
