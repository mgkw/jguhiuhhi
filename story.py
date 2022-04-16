import os

import shutil


try:
    shutil.rmtree("config")
except Exception as e:
    print(e)
    
    
try:
    import sys
    import time
    import random
    import argparse
    from random import choice
    from threading import Thread
    from instabot import Bot
     
except ModuleNotFoundError:
    os.system('python pip install instabot')
    os.system('python pip install requests_toolbelt')
    os.system('python pip install tqdm')
    os.system('python pip install urllib3==1.25.11')
    print('\n[+] Done')



sys.path.append(os.path.join(sys.path[0], '../../'))


users = ['quickpizza.karbala', 'al_hussein_resort', 'almayalisweets', 'charles_1chaplin', 'shawerma.karam', 'moodcafe.karbala', 'hungry__break', 'simsim.rest', 'tootfresh1', 'genius_burger_', 'lafleur_iq', 'kentucky_king_', 'freshmagic.karbala', 'banshee.res', 'durnsrawy', 'churro_station', 'karamna.iq', 'jumaar_resturant', 'kookhdajaj.karbala', 'chocolate__land', 'waraq.ennab', 'alagh2015', 'halwaal_shaam', 'nay.cafe_', 'milano_karbala', 'firefly_iq', 'eat_and_go_karbala', 'candys.lady', 'kentuckyhouse.karbala', 'caramel_karbala', 'novacafe.1', 'robochefsmart', 'lokma.super.star', 'pizzahouse.karbala', 'bait_faruge_iq', 'humam_cake', 'x.burger_', 'roknsultan', 'fire.fire.burger.karbala', 'pizzamaster_karbalaa', 'shaghf.karbala', 'food.fort.iq', 'maali244', 'cha_11a', 'mazayarestaurant_baghdad', 'alfaqma', 'am2o2o1111', 'mohammed___hisham', 'ridhaalwancoffee', 'yalanji.resturant', '_honey.bee.99_', 'lemoniraq', 'guevara_steakhouse', 'dawa.baghdad', 'barley_almansoor', 'shakespeare_baghdad', 'samadrestaurant', 'hardeesbaghdad', 'narabaghdad', 'habaibnaresturant', 'ortakchocolate', 'mandiplate_cafe_and_restaurant', 'beethoven.iraq', 'khan.mandi', 'manwella.rest', 'zaytoun_sweets', 'chesters.restaurant', 'royalgalaxygroup', 'shawarma.aldimashqi', 'icepack.iraq', 'na3na3rest', 'alareesharestaurant', 'shawrmarest', 'aghsan_alzaitoun', 'hookah.syria', 'chocolate.sarayi.iraq', 'yalanji_rest', 'rokn_almandi', 'westburgeriraq', 'madoiraq', 'haifa_hassony', 'manarfarress', 'yunusdiyebirisi0', 'eng_iraqe', 'saifcoloer', 'maya.ahmed97', 'model_haidy', 'sollaf5', 'shahadalshemari', 'a_y_a94', 'ghada.baseel', 'raneen.tapony', 'raidafade', 'halaalkaser', 'helee.bamarni', 'dalisalih', 'nareeman_alqaisi', 'model_marem', 'zainab_rabee_tv', 'mays.gumir', 'marina_alobaidi', 'baraa_ataallah', 'shaymaaraad.official', 'tamara_jammal', 'tayser_aliraqi12', 'jumana.karim.official', 'z44d4', 'nabaahali93', 'hibaazizaziz', 'alaabualshemlat', 'anne_salah_official', 'sabah.aldolaimi', 'zinah_ahmed_official', 'adam_rafet', 'habbawe81', 'ahmedalbaharr', 'magazine_baghdad', 'azal_alsayab', 'hamsa.majed1986', 'mahmoodalghiath', 'junaed_98', 'r_anooz', 'qn_iraq', 'enaastaleb', 'nadamodel', 'aseel_al_bayati', 'shamss_model', 'hasnaa.alshojeri', 'marammarooo_official', 'rafeef_alhafedh', 'shireensoliman_official', 'funon.tv', 'basra.qi', 'iraqi.artmag', 'mehdi.hjerank', 'ma.fn_', 'hayfaa_al_husseini', 'zahraa_alm93', 'ghazal_asady', 'sara_alrubaie.official', 'ashteaqadil', 'du_ali89', 'fatima_alhathal_', 'sajad_algarip', 'omar_mohamed_official', '43zl', 'maymu_88', 'noor.almajed.official', 'noor_almajid397', 'khatab_alqaisi', 'abojana_alselawi', 'sima_jaff', 'nareeman_alqaisi0', 'enas_haleem_', 'roaa_altalabani', 'ci_5m', 'anchors_iraq', 'haneenayad94', 'celebrities_sumer', '_m.a.m_6', 'bero_alazawi', 'dana_hussein86', 'danokhalil2020', 'vean123', 'noor_alarady', 'iraqstars.mag', 'yaqeen.samir', 'dalia_naim1', 'shyma_alshmary', 'saja.aldulaimy', 'raghad_khatoun', 'asawer.ezit', 'mera_taleb', 'dream_magazine.91', 'welyanalbaiaty94', 'rashaalaghafit', 'mashahirnamagazine', 'shahad_eidd', 'qasim.alhjamii', 'iraqs.tyle', 'aseel_naseh', 'farah.ahmad.8', 'rehamfouad95', 'farah.abdulhamed', 'iwjf_org', 'zhwr80', 'amal_ali_90', 'baghdad_famous', 'e.3j6', 'noor_jubouri_', 'bos_phor', 'shams_altmim', 'ishtariqmagazine', 'ahlame_hajji', 'dodo.8606', 'zena_iq2', 'wahaj_ali_ghaidan', 'nejoomelfan', 'noor_al_jawahery', 'dema.ahmad.4', 'raedabufatean', 'bakr_khald', 'alialkalede', 'celebrities_iqmag', 'husamalrassam', 'actress_alaa_hussein']



bot = Bot()
bot.login()

    
def story(n):
	
	n = 500
	print('1')
	while True:
	    user_to_get_likers_of = bot.get_user_id_from_username(choice(users))
	    current_user_id = user_to_get_likers_of
	    print(choice(users))
	
	      
		
	    try:
	        # GET USER FEE
	        
	        if not bot.api.get_user_feed(current_user_id):
	            print("Can't get feed of user_id=%s" % current_user_id)
	
	        # GET MEDIA LIKERS
	        user_media = random.choice(bot.api.last_json["items"])
	        if not bot.api.get_media_likers(media_id=user_media["pk"]):
	            print(
	                "Can't get media likers of media_id='%s' by user_id='%s'" % (user_media["pk"], current_user_id)
	            )
	
	        likers = bot.api.last_json["users"]
	        liker_ids = [
	            str(u["pk"]) for u in likers if not u["is_private"] and "latest_reel_media" in u
	        ]
	
	        # WATCH USERS STORIES
	        if bot.watch_users_reels(liker_ids[:20]):
	            print("Total stories viewed: %d" % bot.total["stories_viewed"])
	        if bot.total["stories_viewed"] >= n:
	        	break
	        
	            
	
	        # CHOOSE RANDOM LIKER TO GRAB HIS LIKERS AND REPEAT
	        current_user_id = random.choice(liker_ids)
	
	        if random.random() < 0.05:
	            current_user_id = user_to_get_likers_of
	            print("Sleeping and returning back to original user_id=%s" % current_user_id)
	            
	
	    except Exception as e:
	        # If something went wrong - sleep long and start again
	        print("Exception:", str(e))
	        current_user_id = user_to_get_likers_of
	        

def story_viwe1(n):
	
	n = 500
	print('2')
	while True:
	    user_to_get_likers_of = bot.get_user_id_from_username(choice(users))
	    current_user_id = user_to_get_likers_of
	    print(choice(users))
	
	      
		
	    try:
	        # GET USER FEE
	        
	        if not bot.api.get_user_feed(current_user_id):
	            print("Can't get feed of user_id=%s" % current_user_id)
	
	        # GET MEDIA LIKERS
	        user_media = random.choice(bot.api.last_json["items"])
	        if not bot.api.get_media_likers(media_id=user_media["pk"]):
	            print(
	                "Can't get media likers of media_id='%s' by user_id='%s'" % (user_media["pk"], current_user_id)
	            )
	
	        likers = bot.api.last_json["users"]
	        liker_ids = [
	            str(u["pk"]) for u in likers if not u["is_private"] and "latest_reel_media" in u
	        ]
	
	        # WATCH USERS STORIES
	        if bot.watch_users_reels(liker_ids[:20]):
	            print("Total stories viewed: %d" % bot.total["stories_viewed"])
	        if bot.total["stories_viewed"] >= n:
	        	break
	        
	            
	
	        # CHOOSE RANDOM LIKER TO GRAB HIS LIKERS AND REPEAT
	        current_user_id = random.choice(liker_ids)
	
	        if random.random() < 0.05:
	            current_user_id = user_to_get_likers_of
	            print("Sleeping and returning back to original user_id=%s" % current_user_id)
	            
	
	    except Exception as e:
	        # If something went wrong - sleep long and start again
	        print("Exception:", str(e))
	        current_user_id = user_to_get_likers_of


def story3(n):
	
	n = 500
	print('3')
	while True:
	    user_to_get_likers_of = bot.get_user_id_from_username(choice(users))
	    current_user_id = user_to_get_likers_of
	    print(choice(users))
	
	      
		
	    try:
	        # GET USER FEE
	        
	        if not bot.api.get_user_feed(current_user_id):
	            print("Can't get feed of user_id=%s" % current_user_id)
	
	        # GET MEDIA LIKERS
	        user_media = random.choice(bot.api.last_json["items"])
	        if not bot.api.get_media_likers(media_id=user_media["pk"]):
	            print(
	                "Can't get media likers of media_id='%s' by user_id='%s'" % (user_media["pk"], current_user_id)
	            )
	
	        likers = bot.api.last_json["users"]
	        liker_ids = [
	            str(u["pk"]) for u in likers if not u["is_private"] and "latest_reel_media" in u
	        ]
	
	        # WATCH USERS STORIES
	        if bot.watch_users_reels(liker_ids[:20]):
	            print("Total stories viewed: %d" % bot.total["stories_viewed"])
	        if bot.total["stories_viewed"] >= n:
	        	break
	        
	            
	
	        # CHOOSE RANDOM LIKER TO GRAB HIS LIKERS AND REPEAT
	        current_user_id = random.choice(liker_ids)
	
	        if random.random() < 0.05:
	            current_user_id = user_to_get_likers_of
	            print("Sleeping and returning back to original user_id=%s" % current_user_id)
	            
	
	    except Exception as e:
	        # If something went wrong - sleep long and start again
	        print("Exception:", str(e))


def story4(n):
	
	n = 500
	print('4')
	while True:
	    user_to_get_likers_of = bot.get_user_id_from_username(choice(users))
	    current_user_id = user_to_get_likers_of
	    print(choice(users))
	
	      
		
	    try:
	        # GET USER FEE
	        
	        if not bot.api.get_user_feed(current_user_id):
	            print("Can't get feed of user_id=%s" % current_user_id)
	
	        # GET MEDIA LIKERS
	        user_media = random.choice(bot.api.last_json["items"])
	        if not bot.api.get_media_likers(media_id=user_media["pk"]):
	            print(
	                "Can't get media likers of media_id='%s' by user_id='%s'" % (user_media["pk"], current_user_id)
	            )
	
	        likers = bot.api.last_json["users"]
	        liker_ids = [
	            str(u["pk"]) for u in likers if not u["is_private"] and "latest_reel_media" in u
	        ]
	
	        # WATCH USERS STORIES
	        if bot.watch_users_reels(liker_ids[:20]):
	            print("Total stories viewed: %d" % bot.total["stories_viewed"])
	        if bot.total["stories_viewed"] >= n:
	        	break
	        
	            
	
	        # CHOOSE RANDOM LIKER TO GRAB HIS LIKERS AND REPEAT
	        current_user_id = random.choice(liker_ids)
	
	        if random.random() < 0.05:
	            current_user_id = user_to_get_likers_of
	            print("Sleeping and returning back to original user_id=%s" % current_user_id)
	            
	
	    except Exception as e:
	        # If something went wrong - sleep long and start again
	        print("Exception:", str(e))
	        
x = Thread(target=story, args=(0,))
x.start()

x = Thread(target=story_viwe1, args=(0,))
x.start()

x = Thread(target=story3, args=(0,))
x.start()

x = Thread(target=story4, args=(0,))
x.start()
