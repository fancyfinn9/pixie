# PIXIE for Mastodon
Python Interface for Cross-Instance Emojos

<img src="pixie-sticker.png" alt="PIXIE - Python Interface for Cross-Instance Emojos" width="200"/>

Sprinkle a little bit of magic on your Mastodon instance! With PIXIE you can now use custom emojis from other Mastodon instances!

---

### User's guide
1. Make sure your instance has PIXIE. If it doesn't, ask the instance owner to add it.
2. Find a custom emoji (emojo) you would like to use, and use the emoji in the `:emoji_name@instance.example:` format. For example, `:squirtle@donphan.social:`. If the emoji doesn't appear in your draft, don't worry. Just make sure the syntax is correct and everything will work. (If you want to search for custom emojis check out https://emojos.in)
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
2. Clone the repository into a folder where you can access the Mastodon CLI. Test it by going into the folder in the command line and running `tootctl --version`.
3. Create a folder named **downloaded_images** in the same directory, for example at `/repository/downloaded_images`.
4. Run pixie-tests.py with `python3 pixie-tests.py` to check everything works properly.
5. Open pixie-main.py and edit the variables at the top of the file. Change donphan.social to your instance's web address (*without* https:// or www.), and change 5 to how frequently your cronjob will run pixie-main.py
6. You can now create a cronjob in whatever way you like to run pixie-main.py every amount of minutes that you specified in the previous step. You may change the interval at any time, but make sure to edit the variable in pixie-main.py
7. Tell your users that you're using PIXIE! If you want to support us please include the following HTML in your instance's description:

``
<a href="https://github.com/fancyfinn9/pixie" target="_blank">
<img src="https://raw.githubusercontent.com/fancyfinn9/pixie/main/pixie-sticker.png" alt="This instance uses PIXIE, Python Interface for Cross-Instance Emojos" width="200">
</a>
``

---
#### Credits:

All code by [fancyfinn9](https://donphan.social/@fancyfinn9)

Fairy wand icon by [Lorc](https://lorcblog.blogspot.com/)
