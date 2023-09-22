import requests as r

searchURL = 'http://drd.ba.ttu.edu/isqs6339/ex/l1.2/search.php'
actionURL = 'http://drd.ba.ttu.edu/isqs6339/ex/l1.2/search_post.php?method=GET&searchInput=asdf&ddlRandomness=NES'
action_postURL = 'http://drd.ba.ttu.edu/isqs6339/ex/l1.2/search_post.php'

res = r.get(searchURL)

res.status_code
res.headers['content-type']
res.encoding
res.text
res.content


###############################################
#          Let's play with the get            #
###############################################
#notes:  Notice the action url and method
#modify url

res_get = r.get(actionURL)

res_get.status_code
res_get.content

##############################################
#  Issue, site is expecting a cookie         #
##############################################

res.cookies
res_get.cookies

#Get the Cookies
search_cookies = res.cookies

#set cookies for call
res_get = r.get(actionURL, cookies=search_cookies)

res_get.content

##############################################
#               Let's try the post           #
##############################################

post_data = {'method':'POST','searchInput':'asdf','ddlRandomness':'NES'}

res_post = r.post(action_postURL, data=post_data, cookies=search_cookies )

res_post.content

############################################
#     Note the header                      #
############################################

#Let's pass a real browser header

headers = {'user-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}

res_post = r.post(action_postURL, data=post_data, cookies=search_cookies, headers=headers)

res_post.content

#also works on get
res_get = r.get(actionURL, cookies=search_cookies, headers=headers)

res_get.content


