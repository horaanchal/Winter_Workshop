import urllib3
import requests
import facebook
token = 'EAAWelqEYbEkBACmgVpAzBpBUGgaaJVC0KW5wbyLRS1dCO0zaCAL9UAlVQHdCB3xxo6tkq4WE9QZCtYHSVQPewmJXbsMgqvZBHJ3YUhlGZAK6uE0pw9kvbcZBvRXjiLZA9tAZCS7vfn7SDf6ZAknZABrpbvS1mpvbGuuVNAMs5gn0mwZDZD'
graph = facebook.GraphAPI(access_token = token, version = 2.7)
#mydetails = graph.request('/me?fields=id,name,age_range,about,friends, posts')
posts = graph.request('/me?fields=posts')
print (posts)
#myid = mydetails['id']
#print(myid)

##In v2.0 of the Graph API, calling /me/friends returns the person's friends who also use the app. In addition, in v2.0, you must request the user_friends permission from each user. user_friends is no longer included by default in every login. Each user must grant the user_friends permission in order to appear in the response to /me/friends

friends = graph.get_object("/me/friends")
print(friends)
