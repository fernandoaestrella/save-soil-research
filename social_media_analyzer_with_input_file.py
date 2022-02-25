# remove my username as default user
# see if youtube subscriber count query will be possible
# make sure follower counts are not looked for if the url found is not for that social media
# find out why is it stopping after a certain amount of time
import time
import facebooklikes
import requests
from bs4 import BeautifulSoup
from instaloader import Instaloader, Profile
import tweepy
try:
    import requests
    from googlesearch import search, lucky
except ImportError:
    print("No module named 'google' found")

# to search
company_name_list = ''

with open('input.txt', encoding="utf8") as f:
    company_name_list = f.read()

search_params = ["Instagram", "Facebook",
                 "Twitter", "LinkedIn", "Youtube", "TikTok", "Contact", ""]
current_line = ''
output_text = ''

# instagram_login_name = input("Enter your instagram username: ")
instagram_login_name = 'fernandoaestrella'
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
    if input_profile_URL != '' and 'instagram' in input_profile_URL:
        try:
            return str(Profile.from_username(instaloader_instance.context, input_profile_URL.split("/")[3]).followers / 1000)
        except:
            return ''
    else:
        return ''


def get_facebook_likes_count(input_profile_URL):
    if input_profile_URL != '' and 'facebook' in input_profile_URL:
        try:
            return str(facebooklikes.get_facebook_likes_from_facebook_url(input_profile_URL) / 1000)
        except:
            return ''
    else:
        return ''
    return ''


def get_twitter_followers_count(input_profile_URL):
    if input_profile_URL != '' and 'twitter' in input_profile_URL:
        try:
            return str(twitter_api.get_user(screen_name=input_profile_URL.split("?")[0].split("/")[3]).followers_count / 1000)
        except:
            return ''
    else:
        return ''


def get_linkedin_followers_count(input_profile_URL):
    # very hard right now, they are very secretive after another company was making a business from scraping their data
    return ''


def get_youtube_followers_count(input_profile_URL):
    return ''


def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0


def get_tiktok_followers_count(input_profile_URL):
    if input_profile_URL != '' and 'tiktok' in input_profile_URL:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0"
            }
            soup = BeautifulSoup(requests.get(
                input_profile_URL, headers=headers).content, "html.parser")

            return str(value_to_float(soup.select_one('[title="Followers"]').text) / 1000)
        except:
            return ''
    else:
        return ''


def get_following_count(input_profile_URL, social_media_platform):
    if input_profile_URL != '':
        try:
            match social_media_platform:
                case 'instagram':
                    return str(Profile.from_username(instaloader_instance.context, input_profile_URL.split("/")[3]).followers / 1000)
                case 'facebook':
                    return str(facebooklikes.get_facebook_likes_from_facebook_url(input_profile_URL) / 1000)
                case 'twitter':
                    return str(twitter_api.get_user(screen_name=input_profile_URL.split("?")[0].split("/")[3]).followers_count / 1000)
                case 'LinkedIn':
                    return ''
                case 'Youtube':
                    return ''
                case 'TikTok':
                    return ''
                case _:
                    return ''
        except:
            return ''
    else:
        return ''


functions_list = [get_instagram_followers_count, get_facebook_likes_count,
                  get_twitter_followers_count, get_linkedin_followers_count, get_youtube_followers_count, get_tiktok_followers_count, None, None]


for company_name in company_name_list.splitlines():
    current_line = company_name + ",,,,,"

    if company_name == '':
        current_line = current_line + ',,,,,,,,,,,,,,,,,,,,'
    else:
        for i in range(8):
            current_URL = lucky(company_name + " " + search_params[i])
            current_line = current_line + current_URL + ","

            if functions_list[i] != None:
                current_line = current_line + \
                    functions_list[i](current_URL) + ','
            else:
                current_line = current_line + ','

            time.sleep(0.11)

    print(current_line)

    with open('output.csv', 'a') as fd:
        fd.write(f'\n{current_line}')

    output_text = current_line + "\n"

print(output_text)
