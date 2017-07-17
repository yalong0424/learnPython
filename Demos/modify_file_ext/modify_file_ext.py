#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getopt
import sys

class FileExtModification(object):
	def __init__(self, fileinfos):
		assert(len(fileinfos) == 3)
		self.__modifyPath = fileinfos[0] #需要修改文件后缀的路径
		self.__needModifyExt = fileinfos[1] #需要修改的后缀名
		self.__modifiedExt = fileinfos[2] #修改后的后缀名

	def __change_word_dir(self):
		os.chdir(self.__modifyPath)

	def __get_all_files(self):
		self.__change_word_dir()
		files = os.listdir(self.__modifyPath)
		return files
		
	def __find_files(self):
		files = []
		for file in self.__get_all_files():
			if file.split(".")[1] == self.__needModifyExt:
				files.append(file)
		return files
				
	def change_file_ext(self):
		try:
			for file in self.__find_files():
				os.renames(file, file.split(".")[0] + "." + self.__modifiedExt)
		except:
			pass
			
def parseCmdLine():
	#只输入脚本名称时的默认参数
	modifyPath = os.path.abspath("./files")  # 需要修改文件后缀的路径
	needModifyExt = "txt"  # 需要修改的后缀名
	modifiedExt = "bat"  # 修改后的后缀名
	#解析命令行参数，参数格式为 python modify_file_ext.py modify_path need_modify_file_ext modified_file_ext
	opts, args = getopt.getopt(sys.argv[1:], "")
	if len(args) == 1:
		modifyPath = os.path.abspath(args[0])
	elif len(args) == 2:
		modifyPath = os.path.abspath(args[0])
		needModifyExt = args[1]
	elif len(args) == 3:
		modifyPath = os.path.abspath(args[0])
		needModifyExt = args[1]
		modifiedExt = args[2]
	elif len(args) > 3:
		print("Too many argumens!!!")

	return [modifyPath, needModifyExt, modifiedExt]


if __name__ == "__main__":
	file_infos = parseCmdLine()
	file_ext_modification = FileExtModification(file_infos)
	file_ext_modification.change_file_ext()