from googlesearch import search
query =input("Enter your query here:")
for i in search(query,tld="com",num=5,stop=10,pause=2):
    print(i)
