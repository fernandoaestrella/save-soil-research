from asyncio.windows_events import NULL
from operator import eq
from instaloader import Instaloader, Profile
import tweepy
try:
    import requests
    from googlesearch import search, lucky
except ImportError:
    print("No module named 'google' found")

search_params = ["Instagram", "Facebook",
                 "Twitter", "LinkedIn", "Youtube", "Contact", ""]
current_line = ''
output_text = ''

instagram_login_name = 'fernandoaestrella_savesoil'

instaloader_instance = Instaloader()
twitter_auth = tweepy.OAuth2BearerHandler(
    "AAAAAAAAAAAAAAAAAAAAAJS4ZAEAAAAAx5jXU42rUN3kThXshHj0HOH8tbU%3DRg06IEV8puXluNiCAij5iRCGYeuONbBduouJHtNd3wSOAEhCm5")
twitter_api = tweepy.API(twitter_auth)

# login
try:
    instaloader_instance.load_session_from_file(instagram_login_name)
except FileNotFoundError:
    instaloader_instance.context.log(
        "Session file does not exist yet - Logging in.")

if not instaloader_instance.context.is_logged_in:
    instaloader_instance.interactive_login(instagram_login_name)
    instaloader_instance.save_session_to_file()

def get_instagram_followers_count(input_profile_URL):
    if input_profile_URL != '':
        try:
            return str(Profile.from_username(instaloader_instance.context, input_profile_URL.split("/")[3]).followers / 1000)
        except:
            return ''
    else:
        return ''

def get_facebook_likes_count(input_profile_URL):
    return ''

def get_twitter_followers_count(input_profile_URL):
    if input_profile_URL != '':
        try:
            return str(twitter_api.get_user(screen_name=input_profile_URL.split("?")[0].split("/")[3]).followers_count / 1000)
        except:
            return ''
    else:
        return ''

functions_list = [get_instagram_followers_count, get_facebook_likes_count,
                  get_twitter_followers_count, NULL, NULL, NULL, NULL]

print(get_instagram_followers_count("https://www.instagram.com/fernandoaestrella_savesoil/"))

"""
for company_name in company_name_list.splitlines():
    current_line = company_name + ",,,,,"

    if company_name == '':
        current_line = current_line + ',,,,,,,,,,,,,,,,,,,,'
    else:
        for i in range(7):
            current_URL = lucky(company_name + " " + search_params[i])
            current_line = current_line + current_URL + ","

            if functions_list[i] != NULL:
                current_line = current_line + \
                    functions_list[i](current_URL) + ','
            else:
                current_line = current_line + ','

        print(current_line)

    output_text = current_line + "\n"
"""

# print(output_text)

"""
text_file = open("output.csv", "w")
n = text_file.write(output_text)
text_file.close()"""

# print("Instagram\n")
# for target_profile in instagram_URL_list.splitlines():
#     if target_profile != '':
#         profile = Profile.from_username(
#             instaloader_instance.context, target_profile.split("/")[3])
#         followers = profile.get_followers()
#         instaloader_instance.context.log('{}'.format(profile.followers / 1000))
#     else:
#         print()

# print("Twitter:")
# for target_profile in twitter_URL_list.splitlines():
#     if target_profile != '':
#         print(twitter_api.get_user(
#             screen_name=target_profile.split("?")[0].split("/")[3]).followers_count / 1000)
#     else:
#         print()
