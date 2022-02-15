from operator import eq
from instaloader import Instaloader, Profile
import tweepy

instagram_login_name = 'fernandoaestrella'
instagram_URL_list = """https://www.instagram.com/hrhcpuntacana/?hl=en
https://www.instagram.com/hardrockcasinopc/
https://www.instagram.com/ricacomunidad/?hl=en
https://www.instagram.com/ism_rd/?hl=en
https://www.instagram.com/dominicanwatchman/?hl=en
https://www.instagram.com/fundacionfarach/?hl=en

https://www.instagram.com/casamarti.rd/?hl=en
https://www.instagram.com/tropigasrd/?hl=en
https://www.instagram.com/sunixpetroleum/?hl=en
https://www.instagram.com/fundaciontropigas/
https://www.instagram.com/metrogasrd/?hl=en
https://www.instagram.com/metrogasrd/?hl=en
https://www.instagram.com/humanoseguros/?hl=en
https://www.instagram.com/ercbpodr/
https://www.instagram.com/cedimatdr/?hl=en
https://www.instagram.com/pepsird/?hl=en
https://www.instagram.com/harinablanquita/
https://www.instagram.com/bancoademi/?hl=en
https://www.instagram.com/asocpopular/?hl=en
https://www.instagram.com/maritimadominicana/?hl=en
https://www.instagram.com/dpworldcaucedo/?hl=en
https://www.instagram.com/amaditalab/?hl=en
https://www.instagram.com/diesco_mobiliario/?hl=en
https://www.instagram.com/universal_rd/?hl=en
https://www.instagram.com/qualadominicana/?hl=en
https://www.instagram.com/bancocariberd/?hl=en
https://www.instagram.com/nestle_rd/?hl=en
https://www.instagram.com/gerdaumetaldom/?hl=en
https://www.instagram.com/enoteca.do/?hl=en
https://www.instagram.com/mapfresaludars/?hl=en
https://www.instagram.com/ikeadominicana/?hl=en
https://www.instagram.com/hitpuerto/?hl=en
https://www.instagram.com/innovacentro/?hl=en
https://www.instagram.com/advensus/?hl=en
https://www.instagram.com/grupotherrestra/?hl=en


https://www.instagram.com/navierasrannik/
https://www.instagram.com/banescord/?hl=en
https://www.instagram.com/atreviacomunicacion/?hl=en
https://www.instagram.com/imcadom/?hl=en
https://www.instagram.com/cepmrd/?hl=en
https://www.instagram.com/mapfrebhd/?hl=en
https://www.instagram.com/farmaconal/?hl=en
https://www.instagram.com/hirehoratiord/?hl=en
https://www.instagram.com/acromaxrd/?hl=en
https://www.instagram.com/bancobdi/?hl=en
https://www.instagram.com/petroquimrd/?hl=en
https://www.instagram.com/cecomsard/?hl=en
https://www.instagram.com/segurossurard/
https://www.instagram.com/afpreservasrd/?hl=en
https://www.instagram.com/pedidosya.do/?hl=en
https://www.instagram.com/kpmgrd/


https://www.instagram.com/afpsiembra/?hl=en
https://www.instagram.com/reidyco/?hl=en
https://www.instagram.com/unitedbrandsdr/?hl=en
https://www.instagram.com/jmmbrd/?hl=en
https://www.instagram.com/pricewaterhousecoopers/?hl=en
https://www.instagram.com/feltrexrd/?hl=en
https://www.instagram.com/globalcompliancespecialty/
https://www.instagram.com/tpago/
https://www.instagram.com/mipuntord/
https://www.instagram.com/aesdominicana/?hl=en
https://www.instagram.com/bdodominicana/
https://www.instagram.com/arsyunenrd/?hl=en
https://www.instagram.com/loscastillos.com.do/?hl=en
https://www.instagram.com/avonrd/?hl=en
https://www.instagram.com/pagesbbdo/?hl=en

https://www.instagram.com/institutoomg/?hl=en

https://www.instagram.com/pelleranoherrera/?hl=en
https://www.instagram.com/alphainversiones/?hl=en
https://www.instagram.com/multicomputos/?hl=en

https://www.instagram.com/headricklaw/?hl=en

https://www.instagram.com/napdelcaribe/?hl=en
https://www.instagram.com/omddominicana/?hl=en
https://www.instagram.com/excel_rd/?hl=en
https://www.instagram.com/starbucksdo/?hl=en
https://www.instagram.com/viajesalkasa/?hl=en

https://www.instagram.com/cci_pb/?hl=en
https://www.instagram.com/linkpartnersrd/?hl=en
https://www.instagram.com/bolsard/?hl=en
https://www.instagram.com/Alburquerque.RD/
https://www.instagram.com/penaizquierdoseguros/
https://www.instagram.com/cunamutualgroup/?hl=en
https://www.instagram.com/aloricard/?hl=en"""
instaloader_instance = Instaloader()

twitter_auth = tweepy.OAuth2BearerHandler(
    "AAAAAAAAAAAAAAAAAAAAAJS4ZAEAAAAAx5jXU42rUN3kThXshHj0HOH8tbU%3DRg06IEV8puXluNiCAij5iRCGYeuONbBduouJHtNd3wSOAEhCm5")
twitter_api = tweepy.API(twitter_auth)
twitter_URL_list = """https://twitter.com/plazadelasalud
https://twitter.com/plazalama?lang=en
https://twitter.com/farmaciascarol?lang=en
https://twitter.com/barrickrd?lang=en
https://twitter.com/tiendascorripio?lang=en


https://twitter.com/HRHPuntaCana?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor

https://twitter.com/ricacomunidad?lang=en
https://mobile.twitter.com/ismrdo
https://twitter.com/dominicanwatch
https://twitter.com/grupofarach
https://twitter.com/altice_do?lang=en

https://twitter.com/tropigasrd
https://twitter.com/sunixpetroleum
https://twitter.com/ftropigas
https://twitter.com/metrogasrd
https://twitter.com/seguroshumano
https://twitter.com/ercbpodr?lang=en
https://twitter.com/cedimatrd
https://twitter.com/pepsird?lang=en


https://twitter.com/ademibanco
https://twitter.com/asocpopular?lang=en
https://twitter.com/dpworldcaucedo?lang=en
https://twitter.com/amaditalab?lang=en

https://twitter.com/universalrd
https://twitter.com/qualard
https://twitter.com/bancocariberd
https://twitter.com/nestlerd
https://twitter.com/gerdau_metaldom
https://twitter.com/casabrugal
https://twitter.com/mapfresaludars
https://twitter.com/ikeadominicana?lang=en
https://twitter.com/hitpuerto

https://twitter.com/advensus
https://twitter.com/grupotherrestra
https://twitter.com/egehaina

https://twitter.com/navierasrannik/with_replies
https://twitter.com/banescord?lang=en
https://twitter.com/atrevia
https://twitter.com/MobilRD
https://twitter.com/cepmrd?lang=en
https://twitter.com/mapfre_bhd?lang=en
https://twitter.com/farmaconal
https://twitter.com/hire_horatio
https://twitter.com/acromaxrd?lang=en
https://twitter.com/bancobdi?lang=en

https://twitter.com/cecomsard
https://twitter.com/segurossurard?lang=en
https://twitter.com/afpreservasrd
https://twitter.com/pedidosya?lang=en
https://twitter.com/kpmgd?lang=cs


https://twitter.com/afpsiembra?lang=en
https://twitter.com/reidyco?lang=en

https://twitter.com/jmmbrd

https://twitter.com/feltrexrd?lang=en

https://twitter.com/tpago

https://twitter.com/aesdominicana?lang=en
https://twitter.com/bdodominicana
https://twitter.com/arsyunenrd

https://twitter.com/avon_rd
https://twitter.com/pagesbbdo
https://twitter.com/GeneradoraItabo/with_replies


https://twitter.com/pelleranoh
https://twitter.com/alphainversion
https://twitter.com/multicomputos

https://twitter.com/headricklaw


https://twitter.com/omd_dominicana
https://twitter.com/excel_rd
https://twitter.com/starbucksdo?lang=en
https://twitter.com/viajesalkasa
https://twitter.com/spb_global
https://twitter.com/cci_pb

https://twitter.com/bolsard
https://twitter.com/alburquerquerd
https://twitter.com/lpenaizquierdo
https://twitter.com/cunamutualrd"""

# login
try:
    instaloader_instance.load_session_from_file(instagram_login_name)
except FileNotFoundError:
    instaloader_instance.context.log(
        "Session file does not exist yet - Logging in.")
if not instaloader_instance.context.is_logged_in:
    instaloader_instance.interactive_login(instagram_login_name)
    instaloader_instance.save_session_to_file()

# print("Instagram\n")
# for target_profile in instagram_URL_list.splitlines():
#     if target_profile != '':
#         profile = Profile.from_username(
#             instaloader_instance.context, target_profile.split("/")[3])
#         followers = profile.get_followers()
#         instaloader_instance.context.log('{}'.format(profile.followers / 1000))
#     else:
#         print()

print("Twitter:")
for target_profile in twitter_URL_list.splitlines():
    if target_profile != '':
        print(twitter_api.get_user(
            screen_name=target_profile.split("?")[0].split("/")[3]).followers_count / 1000)
    else:
        print()
