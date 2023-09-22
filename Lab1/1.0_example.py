import requests as r
res = r.get("https://www.depts.ttu.edu/rawlsbusiness/")

#Check the text is available
res.text
#check the content is available
res.content
#check the HTML response code
res.status_code
#to know how long does it take to be connected to the web
res.elapsed
res.elapsed.microseconds
#Check the encoding type
res.encoding
#Check the header and see the content type
res.headers

new_res=r.get("https://en.wikipedia.org/wiki/Lubbock,_Texas")
new_res.headers


new_res=r.get("https://www.southplainsmall.com/")
new_res.headers

new_res=r.get("http://www.southplainsmall.com/")
new_res.history
new_res.url

#check ssl when redirection is not allowed
new_res=r.get("http://www.southplainsmall.com/", allow_redirects=False)
new_res.history
new_res.status_code
new_res.url

#302 : moved temporarily
new_res.is_redirect
new_res.is_permanent_redirect

img_res = r.get("https://www.depts.ttu.edu/rawlsbusiness/about/images/WilliamsDeanPortrait2.jpg")
img_res.headers

json_res = r.get("http://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json?accessType=DOWNLOAD")
json_res.headers
