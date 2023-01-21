from bs4 import BeautifulSoup
import requests
import smtplib, ssl

url = 'https://www.computerworld.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

news = []

def scrape():
	for h3_tag in soup.find_all('h3'):
		for a_tag in h3_tag.find_all('a'):
			article_title = a_tag.get_text()
			article_url = a_tag.get('href')
			article_to_append = {"title": article_title, "url": f"https://www.computerworld.com{article_url}"}
			news.append(article_to_append)

	news_txt_format = ''
	for item in news:
		news_txt_format += f"Title: {item.get('title')}, url: {item.get('url')}\n"

	return news_txt_format


def send_email(msg):
	port = 465  
	smtp_server = "smtp.gmail.com"
	sender_email = ""  # Enter your email address
	receiver_email = ""  # Enter receiver address
	password = ""  #enter password you created for the gmail app 
	email_body = msg
	message = "Subject: News\n\n" + email_body

	
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)


def main():
	message = scrape()
	send_email(message)

if __name__ == '__main__':
	main()	


