import instaloader
ig=instaloader.Instaloader()
dp=input("enter un insta:")
ig.download_profile(dp,profile_pic_only=True)
