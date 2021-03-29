"""
code by Luis Gonzaga Lara Gutierrez
"""

import os
import time
import subprocess
import sys
import logging

class testSystem:
	class fileList:
		def __init__(self,i):
			self.tc_id=i
			self.name=""
			i=i+1
		def prep():
			try:
				assert int(time.time()) % 2 == 0 , ("\033[1m" + "SystemTimeError:" + "Time value is not divisible by 2" + "\033[0m" )					
				return True			
			except AssertionError as txt:
				print(txt)
				return False		
		def run():
			lt=os.listdir("/home")
			return lt
		def clean_up():
			print("Clean_up done")
			return True

	class randomFile:
		def prep():
			ram=subprocess.getoutput("cat /proc/meminfo |grep MemTotal")
			ram=ram.split(" ")
			try:
				assert int(ram[8])/(1024*1024) > 1 , ("\033[1m" + "RAMAmountError: RAM for host is less than 1 GB"+ "\033[0m")			
				return True
			except AssertionError as txt:
				print(txt)
				return False	
		def run():
			try:
				f = open("test.txt" , "wb")
				f.write(os.urandom(1024*1024))
			except:
				print("ERROR: File test.txt could not be opened")
				return False
		def clean_up():
			if os.path.exists("test.txt"):
				os.remove("test.txt")
			else:
				print("No test file to delete")
			print("Clean_up done")

	def execute(self,testtype):
		p=None
		lt=[]
		logging.basicConfig(filename='tests.log',level=logging.DEBUG,)
		print("----------------------------------------------------")
		print(" ")
		if "fileList" in testtype:
			for i in range(0,4):
				sys.stdout.write("Running prep for fileTest {0}\r".format("."*i))
				sys.stdout.flush()
				time.sleep(0.125)
			print("")
			#print("Running prep for fileTest")
			p=test.fileList.prep()
			if p==False:
				logging.error("SystemTimeError:" + "Time value is not divisible by 2")
				logging.error("Test case fileList HALTED")				
				sys.exit()			
			print("Passed")
			logging.info("System prep for fileList successfully executed.") 
			for i in range(0,4):
				sys.stdout.write("Running run for fileTest {0}\r".format("."*i))
				sys.stdout.flush()
				time.sleep(0.075)
			print("")
			lt=test.fileList.run()
			for x in lt:
				print(x)
			logging.info("Run fileList successfully executed.") 
			print("Passed")
			for i in range(0,4):
				sys.stdout.write("Running clean_up for fileTest {0}\r".format("."*i))
				sys.stdout.flush()
				time.sleep(0.075)
			print("")		
			test.fileList.clean_up()
			logging.info("Clean_up for fileList successfully executed.") 
			print("Passed")
			logging.info("fileList Test case successfully executed")
			
		else:		
			for i in range(0,4):
				sys.stdout.write("Running prep for randomFile {0}\r".format("."*i))
				sys.stdout.flush()
				time.sleep(0.125)
			print("")			
			p=test.randomFile.prep()
			if p==False:
				logging.error("RAMAmountError: RAM for host is less than 1 GB")
				logging.error("Test case RandomFile HALTED")				
				sys.exit()
			logging.info("System prep for randomFile successfully executed.") 
			print("Passed")
			for i in range(0,4):
				sys.stdout.write("Running run for randomFile {0}\r".format("."*i))
				sys.stdout.flush()
				time.sleep(0.075)
			print("")
			test.randomFile.run()
			logging.info("Run randomFile successfully executed.") 
			print("Passed")
			for i in range(0,5):
				sys.stdout.write("Running clean_up for randomFile {0}\r".format("."*i))
				sys.stdout.flush()
				time.sleep(0.075)
			print("")
			test.randomFile.clean_up()
			logging.info("Clean_up for randomFile succesfully executed.") 
			logging.info("randomFile Test case successfully executed")

if __name__=="__main__":
	test=testSystem()
	test.execute("fileList")
	test.execute("randomFile")

