import facebook

def main():
 
	cfg = {
	"page_id":"100009785912178",
	"access_token":"EAAIgAv82iY0BANlo0AKWGbGNHIUp2GTbCm1ruMKGq4JKzdKZC4ZBhvgGFvIkfTJYpt0zbBiAS5zMUFjErzQ7iKDFNZC8EJiKvUgpPDavXiBjZC8ZAbjtxVmZBMaor5ZCAbhJuDBy3vda0fxl9w6ZCB7Ml5bPp24tYbln6Qjjd4OBPrd63gi0keLA"
	}

	api = get_api(cfg)
	msg = "Hello, World!"
	status = api.put_wall_post(msg)

def get_api(cfg):
	graph = facebook.GraphAPI(cfg['access_token'])

if __name__== "__main__":
  main()
