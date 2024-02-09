
instance_url = "donphan.social" # Change to your instance's URL!

frequency_minutes = 30 # How often you run this script in minutes

#======================================================#

import tarfile                  # Used for compressing emojis into .tar.gz
import subprocess               # Used for adding emojis to instance through command line
import urllib.request           # Used for internet access
import json                     # Used for parsing JSON from API
from pathlib import Path        # Used for accessing files in downloaded_images/
import re                       # Used for searching posts for any custom emoji references
import datetime                 # Used for checking current time and when posts were published

def log(text):
    logtxt = "["+datetime.datetime.now().isoformat()+"] "+text
    with open("log.txt", "a") as f:
        f.write("\n"+logtxt)
        f.close()
    print(logtxt)
        
log("======== NEW RUN ========")
log("PIXIE started. Running on "+instance_url)

# For later
filenames = []

# Get posts from API
req = urllib.request.urlopen("https://"+instance_url+"/api/v1/timelines/public?local=True") 
response = json.loads(req.read())

log("Recieved public timeline")

# Set variables for next step
current_time = datetime.datetime.now()
threshold_time = current_time - datetime.timedelta(minutes=(frequency_minutes + 1))

log("Set time variables")

# Loop through all posts
for post in response:
    created_at = datetime.datetime.fromisoformat(post["created_at"]).replace(tzinfo=None) # This little .replace() is just to fix a bug with timezones
    if created_at > threshold_time: # Checking if the post was created since the last run.

        # First, we'll extract the attached emoji data
        existing_emojis = [] # Create a new list
        if post["emojis"] != []:
            for emoji in post["emojis"]:
                existing_emojis.append(emoji["shortcode"])
        
        # Some cool regex to find any emoji mentions in the post
        matches = re.findall(r':(\S+?)@(\S+?):', post["content"])
        
        for emoji in matches: # Loop through all emojis
            log("Post id "+post["id"]+" contains emojis. Checking")
            emoji_name = emoji[0]+"@"+emoji[1] # Set a variable to the shortcode for easy access later
            if emoji[1] != instance_url: # Just making sure the user didn't try use an emoji that's on the same instance as them
                if emoji_name not in existing_emojis: # Mastodon attaches the emoji details to the post's data by default. Of course, it can't do this for non-existent emojis, so this is a quick way of checking if an emoji already exists on the instance or not
                    if emoji_name not in filenames: # Have we already checked this emoji during this run?
                        log(f"Emoji {emoji_name} is being fetched")
                        instance_domain = emoji[1]
                        try:
                            req = urllib.request.urlopen("https://"+instance_domain + "/api/v1/custom_emojis") # Get the list of custom emojis from the instance the user is trying to get it from
                            response = json.loads(req.read())
                            
                            dict_of_emojis = {d["shortcode"]: d for d in response} # Quickly parse the custom emojis for quicker run times. This way, instead of looping through every custom emoji the instance has, we can just check if any of the emojis have the shortcode we're looking for
                            custom_emoji = dict_of_emojis.get(emoji[0]) # Search for the shortcode in our parsed dictonary. If it doesn't exist it will throw an error and the script will move on to the next emoji
                            
                            urllib.request.urlretrieve(custom_emoji["url"], "downloaded_images/"+emoji[0]+"@"+emoji[1]+custom_emoji["url"][-4:]) # Download the emoji and save it in the downloaded_images directory with the correct filename
                            filenames.append(emoji[0]+"@"+emoji[1]+custom_emoji["url"][-4:]) # Add the emoji to our list of checked emojis so we don't search for the emoji again during this run if the emoji appears again
                            
                            log("Fetched "+emoji_name)
                        except Exception as e:
                            log("An error occurred. Info:\n"+str(e))

log("Looped through posts")

# Open the .tar.gz file
with tarfile.open("emojos.tar.gz", "w:gz") as tar:
    
    # Iterate through all .png files and add them to the archive
    pathlist = Path("/downloaded_images").glob('**/*.png')
    for path in pathlist:
        tar.add(str(path))
    
    # Iterate through all .gif files and add them to the archive
    pathlist = Path("/downloaded_images").glob('**/*.gif')
    for path in pathlist:
        tar.add(str(path))
        
    # Save the .tar.gz file
    tar.close()
    
log("Created .tar.gz archive")

subprocess.run(["tootctl", "emoji", "import", "emojos.tar.gz", "--unlisted"])

log("Added emojis to instance. Have a nice day!")
