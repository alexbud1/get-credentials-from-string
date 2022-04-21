import re

##### get nth occurence of substring in string
##### returns index of substring
def get_index(string, substring, n):
		list1 = re.finditer(substring,string)
		matches_positions = [match.start() for match in list1]
		return matches_positions[n]


##### class which represents credentials in database
class Credentials:
		def __init__(self, engine, name, user, password, host, port):
				self.engine = engine
				self.name = name
				self.user = user
				self.password = password
				self.host = host
				self.port = port


##### fetch credentials from string
##### returns object 
def get_credentials(s):
		index1 = s.index('//') + 2
		index2 = get_index(s,":",1)
		user = s[index1:index2]

		engine = 'django.db.backends.postgresql_psycopg2'

		index1 = get_index(s,":",1)+1
		index2 = get_index(s,"@",0)
		password = s[index1:index2]

		index1 = index2 +1
		index2 = get_index(s,":",2)
		host = s[index1:index2]

		index1 = index2 + 1
		index2 = get_index(s,"/",2)
		port = s[index1:index2]

		index2 +=1
		name = s[index2:]
		creds = Credentials(engine, name, user, password, host, port)
		return creds


print(get_credentials("your_string"))



