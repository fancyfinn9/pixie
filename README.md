# PIXIE for Mastodon
Python Interface for Cross-Instance Emojos

With PIXIE you can now use custom emojis from other Mastodon instances! No more restrictions to the emojis your instance has!

---

### User's guide
1. Make sure your server has PIXIE. If it doesn't, ask the instance owner to add it.
2. Find a custom emoji (emojo) you would like to use, and use the emoji in the `:emoji_name@instance.example:` format. For example, `:squirtle@donphan.social:`. If the emoji doesn't appear in your draft, don't worry. Just make sure the syntax is correct and everything will work.
3. Publish your post!

Please note that if it is the first time someone on the instance uses any given emoji, it may take a couple of minutes for the emoji to display.

>**If the given emoji has not been used on the instance before, it will not display unless you use it in a public post.**
>
>This means it will not display if you use it in:
>- Your display name
>- The information fields on your profile
>- A post only visible to mentioned users
>- A post only visible to followers
>
>If you would like to use an emoji from another instance in any of the cases above, make a post visible to everyone with that emoji in it. You may delete that post once the emoji displays.

---

### Admin's guide
1. Make sure Python 3 is installed on your machine. Test it by running `python3 --version` in the command line.
2. Clone **the entire repository** into a folder in a place where you can access the Mastodon CLI. Test it by going into the folder in the command line and running `tootctl --version`.
3. Run pixie-tests.py with `python3 pixie-tests.py` to check everything works properly.
4.
