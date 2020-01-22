import stackapi
from stackapi import StackAPI 
site = StackAPI('stackoverflow')
site.page_size = 1
site.max_pages = 1
try:	
	#query = input("enter:")
	answers = site.fetch('answers') 
	id = answers['items'][0]['question_id']
	print(id)
	question = site.fetch('questions/%s'%(id))
	print(question)
	#print(question['items'][0]['link'])
	#answer = site.fetch(id)

except stackapi.StackAPIError as e:
    print("   Error URL: {}".format(e.url))
    print("   Error Code: {}".format(e.code))
    print("   Error Error: {}".format(e.error))
    print("   Error Message: {}".format(e.message))