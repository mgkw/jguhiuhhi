from instagrapi import Client
import random
import threading

cl = Client()
cl.login("ngmw2", "Mm11223344",relogin=True)
users = ['mem9.5w', 'ali_musadaq', '2ss___s', 'sar_._19', 'ramezgalalac', 'kh_alhaneen', 'singeramar', 'heba_saad99', 'merna_alismael', 'omar_mohamed_official', 'sollaf5', 'mariya.kozad', 'iraqait', 'h.aldirawy', 'university_of_baghdad1', 'm.norhene', 'rawan', 'reta.mohamad1', 'jehan.hashim', 'mustafa_alzubayd', 'model_sand', 'cznburak', 'hud_a96', 'alooosh_markae', 'critic_iq', 'asawer.ezit', 'alkhafajitv', 'poet_aboalhassan', 'banat_styel', 'taifofficial', 'jalila_official', 'saadoun_al_saadi', '28.dv', 'nazaralfares', 'sambosa.iraqia', 'iq.turkey', 'aloosh_al_ameer', 'welyanalbaiaty94', 'teba_khalil', 'elena_akbik', 'kamilyaward', 'snara_2', 'elissardancer', 'falafel.iraqia', 'instagram', 'abbas_shibani', 'basma_baghdad', 'ghada.baseel', 'shahnda.al_musawi', 'saja.aldulaimy', 'ali_athab9', 'daliatahastar', 'basmanalkateab_', 'vean123', 'iraq_keekers', 'm.u_r', 'hayarbaraouch', 'hebanourr', 'shurooqalhassen', 'haifa_hassony', 'mahmoodalghiath', 'mustafa_agha1', 'rahmariadh', 'anne_salah_official', 'rehamalbayati', 'iqiq.5', 'sattarsaad', 'aya_alzedan', 'hamo_beka_official', 'hindnizar', 'moatasemalnahar', 'nancyajram', 'd.qasim', 'haifawehbe', 'hassan.shakosh', 'actress_alaa_hussein', '_nabaaofficial_', '3anqene', 'hanadymehanna', 'evannaji', 'jumana.karim.official', 'nadeen_alfahd', 'zinah_ahmed_official', 'mohamedalsalim', 'mayadiab', 'humam_hassan', 'mohammadayad7', 'ashty_hadid', 'alwassef.official', 'dazdamonakh', 'angiekhouryme', 'stars_casablanca', 'shahadalshemari', 'aseelhameem', 'ehab_alatea', 'mays.gumir', 'mzajeat', 'haibat_adel', 'hannahelzahed', 'maher_ahmed76', 'ameer_alabadi94', 'sary_hussam', 'ghassan_esmaeel', 'husamalrassam', 'ahmed_almaslawi', 'nesreentafesh', '313_yousef', 'iraq.marka', 'batoul_official_', 'alaa_alebrahimi', 'raidafade', 'junaed_98', 'ali_jaber35', 'ali_almansory', 'shimaa_qasim', 'bessan.lsmail', 'malayeenkarim', 'souhair', 'zahra_ben_mime', 'aboody_kareem', 'ahlamalshamsi', 'husamalmajidofficial', 'marina_alobaidi', 'alsulltan', 'raedabufatean', 'tayseer_alsafeer', 'ruslan.hadad.offical', 'nadine.nassib.njeim', 'natachasinger', 'mzijeat', 'dalya.khaled', 'mashaheerfun', 'noorstars', 'jaafar_alghazal', 'dr_clean2020', 'hatem_aliraqii', 'amanialaa11', 'alaa_batti', 'omarkamal.official', 'mohammedfares84', 'kashkoolatheer', 'hurramm_khan', 'alijasimm', 'shahla_blogger', 'esra_alaseil', 'dr_kholodiii', 'chayma.allam', 'mustafaalabdullaah', 'asiakamal12', 'mohamedalsallm', 'alialkalede', 'aghar_fb', 'adam_rafet', 'm.khumra', 'hala.al.adil', 'hussamkamil', 'itsdjnemo', 'saifalbasha', 'saifamer_official', 'muhammadalhalfi.off', 'mohamedramadanws', 'ali.alsalem82', 'jalalalzain84', 'ahmed_almuhandes', 'muhaned_azawy', 'kinsey', 'muradturkk', 'yaserabdalwahab', 'ali.samir1', 'amerhussen1', 'cristiano', 'zaid.almallak', 'maysanber', 'ali.saber.official', 'mustafa_alrubayie', 'nooralzain.official', 'aboalhel', 'hybat_albadr', 'husham.althahabi', 'raneen.tapony', 'celebrities_iqmag', 'anne_salah_fans', 'cyrineanour', 'yara', 'qusayessa_off', 'elissazkh', 'ali_fadil', 'sahar_abas_jamil', 'mazajeat', 'nsr_degla', 'dumooa_tahseen', 'ahmed_sattar6', 'ziaedalhabib82', 'anghamtalib89', 'nasratalbader', 'saifnabeell', 'mahmod.alturky', 'rafatalbadr', 'minaalsheikhly', 'hamsa.majed1986', 'dadoo_hn', 'hfalat_vip1', 'ali_altolqanee', 'halamalturk', 'alnjomia', 'albasheershow', 'carmenfragoso.dancer', 'ahmedjwadofficial', 'kasimalsultan', 'fahdnori_official', 'myriamfares', 'oras_sattar', 'awosalhlfe', 'shamsofficial_', 'mbciraqtv', 'dhiya.almyali', 'yousif.alsudani', 'tamerhosny', 'majidalmohandis', 'alialfredawy']

posts = []
storyes = []
usered = []
nn = 0
stl = []
tottel_storyes = 0
dict = {"conunt":0}



def mihan1(n):
    tottel_storyes = 0
    nn = 0
    n = 0
    while True:
        n += 1
        usered.clear()
        posts.clear()
        if n == 10:
            print("done")
            break

        try:

            choses = random.choice(users)
            pk = cl.user_id_from_username(choses)
            post = cl.user_medias(pk, 100)
            for x in post:
                posts.append(x.pk)
            chosespost = random.choice(posts)
            getuser = cl.media_likers(chosespost)

            liker = [str(u.pk) for u in getuser if not u.is_private]
            for i in liker:


                story = cl.user_stories(i)
                if story == []:
                    continue
                usered.append(i)
                for x in story:
                    None
                stl.append(x.pk)
                to = len(stl)
                nn += 1
                tottel_storyes += to
                cl.story_seen(stl)
                np = dict["conunt"]
                if np == 5000:
                    break
                np += 1
                internal_marks = {'conunt': np}
                dict.update(internal_marks)
                ki = len(usered)
                print("user = {} , person: {}".format(ki,dict["conunt"]))

                stl.clear()


        except Exception as e:
            None


def mihan2(n):
    tottel_storyes = 0
    nn = 0
    n = 0
    while True:
        n += 1
        usered.clear()
        posts.clear()
        if n == 10:
            print("done")
            break

        try:

            choses = random.choice(users)
            pk = cl.user_id_from_username(choses)
            post = cl.user_medias(pk, 100)
            for x in post:
                posts.append(x.pk)
            chosespost = random.choice(posts)
            getuser = cl.media_likers(chosespost)

            liker = [str(u.pk) for u in getuser if not u.is_private]
            for i in liker:

                story = cl.user_stories(i)
                if story == []:
                    continue
                usered.append(i)
                for x in story:
                    None
                stl.append(x.pk)
                to = len(stl)
                nn += 1
                tottel_storyes += to
                cl.story_seen(stl)
                np = dict["conunt"]
                if np == 500:
                    break
                np += 1
                internal_marks = {'conunt': np}
                dict.update(internal_marks)
                ki = len(usered)
                stl.clear()


        except Exception as e:
            None


def mihan3(n):

    tottel_storyes = 0
    nn = 0
    n = 0
    while True:
        n += 1
        posts.clear()
        usered.clear()

        if n == 10:
            print("done")
            break

        try:

            choses = random.choice(users)
            pk = cl.user_id_from_username(choses)
            post = cl.user_medias(pk, 100)
            for x in post:
                posts.append(x.pk)
            chosespost = random.choice(posts)
            getuser = cl.media_likers(chosespost)

            liker = [str(u.pk) for u in getuser if not u.is_private]
            for i in liker:

                story = cl.user_stories(i)

                if story == []:
                    continue
                usered.append(i)
                for x in story:
                    None
                stl.append(x.pk)
                to = len(stl)
                nn += 1
                tottel_storyes += 1
                cl.story_seen(stl)
                np = dict["conunt"]
                if np == 500:
                    break
                np += 1
                internal_marks = {'conunt': np}
                dict.update(internal_marks)

                stl.clear()

        except Exception as e:
            None


def mihan4(n):
    tottel_storyes = 0
    nn = 0
    n = 0
    while True:
        n += 2
        posts.clear()
        usered.clear()

        if n == 10:
            print("done")
            break

        try:

            choses = random.choice(users)
            pk = cl.user_id_from_username(choses)
            post = cl.user_medias(pk, 100)
            for x in post:
                posts.append(x.pk)
            chosespost = random.choice(posts)
            getuser = cl.media_likers(chosespost)

            liker = [str(u.pk) for u in getuser if not u.is_private]
            for i in liker:

                story = cl.user_stories(i)

                if story == []:
                    continue
                usered.append(i)
                for x in story:
                    None
                stl.append(x.pk)
                to = len(stl)
                nn += 1
                tottel_storyes += 1
                cl.story_seen(stl)
                np = dict["conunt"]
                if np == 500:
                    break
                np += 1
                internal_marks = {'conunt': np}
                dict.update(internal_marks)

                stl.clear()

        except Exception as e:
            None



x = threading.Thread(target=mihan1, args=(1,))
b = threading.Thread(target=mihan2, args=(1,))
c = threading.Thread(target=mihan3, args=(1,))
d = threading.Thread(target=mihan4, args=(1,))

x.start()
b.start()
c.start()
d.start()
