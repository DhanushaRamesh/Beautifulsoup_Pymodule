from bs4 import BeautifulSoup

html = open("home.html").read()
soup = BeautifulSoup(html,'html.parser')

#print(soup.find('tr',id="Prod_Build").find('th',id="Prod_Build").string)

if soup.find('tr',id="Prod_Build").find('th',id="Prod_Build"):
    soup.find('tr', id="Prod_Build").find('td',id="status").string = "updated_status"
    soup.find('tr', id="Prod_Build").find('td',id="time").string = "updated_time"
    style_th = soup.find('tr', id="Prod_Build").find('th', id="lets_style")
    style_th['style'] = "background-color:#4CAF50;color: black;"


html = soup.prettify("utf-8")
with open("output.html", "wb") as file:   #All the changes r saved in a new html file 
    file.write(html)
