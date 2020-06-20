import requests
from webbot import Browser
from Keys import *
#Execute at registration time, using a scheduling app or batch file
#MUST HAVE PLAN PREPARED AND TERM ADJUSTED
TERM = 'Fall Semester 2020'

web = Browser()
web.go_to('https://esther.rice.edu/selfserve/twbkwbis.P_WWWLogin')
web.type(USERNAME, id='UserID')
web.type(PASSWORD, id='PIN')
web.click('Login')
web.click('Register or Add/Drop Classes')
web.switch_to_tab(2)
web.click(text = 'Register for Classes')
web.type(NET_ID, id='username')
web.type(NET_PASS, id='password')
web.click('Login')
web.click(id = 's2id_txt_term')
web.click('Fall Semester 2020')
web.click('Continue')
web.click('Ok')
web.click('Plans')
web.click('Add All')
web.click('Submit')