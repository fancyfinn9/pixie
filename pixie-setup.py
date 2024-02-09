import tarfile                  # Used for compressing emojis into .tar.gz
import subprocess               # Used for adding emojis to instance through command line
import urllib.request           # Used for internet access

class Error(Exception): pass # Used for stopping the program if one of the tests fail

# Startup text
print("\nPIXIE by fancyfinn9")
print("Python Interface for Cross-Instance Emojos")
print("Use custom emojis from any other Mastodon instance!")

# Test Mastodon CLI
print("\n[1/4] Testing Mastodon CLI...")
subprocess.run(["tootctl", "--version"])
success = input("Did you a version number appear? [Y/n] ").lower()
if success == "y":
    print("Test 1/4 completed")
else:
    print("\n[!] Whoops! PIXIE needs access to the Mastodon CLI to work, but was unable to run a command in the command line. Make sure you're running this script in a place on your machine where you can access the Mastodon CLI.")
    Error()

# Test internet access and image downloading
print("\n[2/4] Testing internet access...")
urllib.request.urlretrieve("https://pool.jortage.com/donphansocial/custom_emojis/images/000/044/619/static/masto_ball.png", "downloaded_images/masto_ball@donphan.social.png")
success = input("Check the \"downloaded_images\" directory. Is there a file called \"masto_ball@donphan.social.png\"? [Y/n] ").lower()
if success == "y":
    print("Test 2/4 completed")
else:
    print("\n[!] Whoops! For some reason downloading the image didn't work. Are you sure that this script can access the internet?")
    Error()

# Test .tar.gz compression
print("\n[3/4] Testing .tar.gz compression...")

# Open the .tar.gz file
with tarfile.open("emojos.tar.gz", "w:gz") as tar:
    
    # Add each file individually
    for file in ["downloaded_images/masto_ball@donphan.social.png"]:
        tar.add(file)
        
    # Save the .tar.gz file
    tar.close()

success = input("Is there an archive called \"emojos.tar.gz\" in the same directory as this script? It should contain \"masto_ball@donphan.social.png\" [Y/n] ").lower()
if success == "y":
    print("Test 3/4 completed")
else:
    print("\n[!] Whoops! For some reason creating the archive didn't work.")
    Error()
    
# Test adding emojis to instance
print("\n[4/4] Testing adding emoji to instance...")
subprocess.run(["tootctl", "emoji", "import", "emojos.tar.gz", "--unlisted"])
success = input("Start writing a Mastodon post and try use the emoji :masto_ball@donphan.social:. Does it work? [Y/n] ").lower()
if success == "y":
    print("Test 4/4 completed")
else:
    print("\n[!] Whoops! For some reason the emoji didn't import. Try again in a few minutes.")
    Error()

print("\nEverything works perfectly, PIXIE will work on this machine.")
