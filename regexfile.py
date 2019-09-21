import re 

email = 'chenguttuvan@dst.com'
exp = '[a-z\.]+'

match1 = re.findall(exp,email)

print(match1)