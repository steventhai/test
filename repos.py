import sys, argparse, requests, json

def main(argv):
   keyword = ''
   limit = ''
   
   # Setting command line input parameters.
   parser = argparse.ArgumentParser(description="Get repositories info based on keyword and limit (number of repositories returned)")
   parser.add_argument('keyword', help='The string keyword to search repositories for, e.g: "search abc"')
   parser.add_argument('limit', type=int, help='Number of repositories returned ( 1 <= limit <= 100)')
   args = parser.parse_args()
   
   keyword = args.keyword
   limit = args.limit

   # Execute GET request with specified keyword and limit
   get(keyword, limit)

# Helper to submit the GET request.
def get(keyword, limit):
      
      # Build the request URI.
      uri = "https://api.github.com/search/repositories?q={0}&sort=forks&order=desc&per_page={1}".format(keyword, limit)

      # Set the json result.
      jsonResult = {}
      
      # Submit request if limit is valid.
      if (limit <= 0 or limit > 100):
         jsonResult['error'] = 'Limit must be between 1 and 100!'
      else:
         getResult = requests.get(uri).json()
         
         # Build the json result
         jsonResult['keyword'] = keyword
         jsonResult['desired_repositories_number'] = limit
         
         # Get all the repository items.
         items = getResult["items"]
         
         jsonResult['returned_repositories_number'] = len(items)
         repos = []
         # Build details for each item.
         for item in items:
            details = {}
            details["id"] = item["id"]
            details["name"] = item["name"]
            details["description"] = item["description"]
            details["language"] = item["language"]
            details["created_date"] = item["created_at"]
            details["html_url"] = item["html_url"]
            details["watchers"] = item["watchers_count"]
            details["forks"] = item["forks_count"]
            details["owner_username"] = item["owner"]["login"]
            details["owner_id"] = item["owner"]["id"]
            details["owner_html_url"] = item["owner"]["html_url"]
            repos.append(details)
         
         jsonResult["repositories"] = repos
      
      print (json.dumps(jsonResult, indent = 3))

if __name__ == "__main__":
   main(sys.argv[1:])