import smtplib

try:
		msgFrom = "sereiavaa@gmail.com"
		smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		msgTo = "brunarupp@gmail.com"
		toPass = 'achtundzwanzig'
		smtpObj.login(msgTo, toPass)
		msg = '''
		teste do codigo da internet
		'''
		smtpObj.sendmail(msgTo,msgFrom,'Subject: Teste de envio de email\n{}'.format(msg))
		smtpObj.quit()
		print("Email enviado com sucesso!")
except:
		print("Erro ao enviar e-mail")