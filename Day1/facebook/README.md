Files: 
	fbmycontent.py

````````
the program outputs my own(or any specified user's) public feed. 
attempted to list friends, but nothing more than the number of friends are listed. A possible reason:
In v2.0 of the Graph API, calling /me/friends returns the person's friends who also use the app. In addition, in v2.0, you must request the user_friends permission from each user. user_friends is no longer included by default in every login. Each user must grant the user_friends permission in order to appear in the response to /me/friends
````````
