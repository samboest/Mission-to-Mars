# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
img_url_soup = soup(html,'html.parser')

image_url_rel = img_url_soup.find_all('div', class_ = 'collapsible results')

for i in range(2):
    source = image_url_rel.find_all('div')[2 * i] 
    url = source.find('img', class_='thumb').get('src')
    img_url = f'https://marshemispheres.com/{url}'
    title = img_url_soup.find('h3').get_text()
    hemisphere_image_urls = [{"image_url":img_url,"title":title}]
    hemisphere_image_urls.append(hemisphere_image_urls)
print(len(hemisphere_image_urls))