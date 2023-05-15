"""This program helps to create a link between the Google Sheets Database and the App"""

#Import Required Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']

def decrypt(encrypt_text):
    orig_text = []
    b = int(len(encrypt_text)/2)
    key = encrypt_text[b:]
    encrypt_text = encrypt_text[:b-1]
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) -ord(key[i]) - 1000)
        orig_text.append(chr(x))
    orig_text = ("" . join(orig_text))
    return orig_text

creds = {'type': 'ևւֈ֎ջպ\u058bքտպֆօևօ֚ԴĬĵĮİĪįľĽĶįĻĮĪįľĬ', 'project_id': 'յֆՃչօ֊֏֘֒ո֑֊ԿՊ՞ՇՓՇՍԲĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪ', 'private_key_id': 'ՇՏՆՌյՌ՛\u0558տՐքՎՂՏ\u0558յտՈՌՃո՟ևՎՇ\u0557ՈնՏ\u0558ՊւՊՌՂՌՖՕՏՐՃĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻ', 'private_key': 'ՁՊՃՅԿՙիլէեՃզդՠռՕձ՛Ը՝՜տՒՋՄՐՃԜդկ՝բ\u058c֏՛ՙէթ՟եեսսֈ֎տֆ՝Ց։Շըզկ՜թ\u0557ՓժթՖըց֏չվչ֑՟վը\u0557ՓֆկՖ՞է՛դՂըֈ֖ՍևխցէղՌֈԠՈյ֏էծձ՚չՁ՛ֆխ\u058c՞ՠդշպն֘լիճՍՙ֍ՖսյքաքՏ֏֒֘ՉՙբՖ՛ևգՠդփնջտՙՐ՝՚՛ՄՌ֜վ՟ՠՊփս՚ԯՐքի՟քջռեթՋ֒՝Ո֎ղքՊ\u058bլՉջոյֈՍց՛Տ֝հՎբն՝սլչժծՌէն֊խ\u058b֗ՇծֈդՌ֕իլ՚ղՉՈհև֒Ռ֒ծԜօ\u0558ՖմրՏւց֊ֆց՚լդռխ֑֍֎պֆՆ՞֍֗ՖՆ֒֊՚օչր֕\u058bժդՋ\u058c֛ՠռխՍզ՛էփժժֈ՝Ռ֚պոթՕ՚օդֈօՈԠ\u0590՛հէծՖքՕ\u0558ջփ՟ՉթՋլւՏռ֓քՏշ՚թվ՟զֈզՃ՟Շր\u0557֍լ\u058bՆԽՂիՅՒՅջ՞֏ֈըոխ֎Յ֊՞ո\u058cիխռպվ֗ԯկՋՙզ՛բ֍ց՞քցմքժռօծչՙ՝ւղ՚\u058cը՛ւդչ֔\u0557լխզ՟ց֜ծՏՙիռժ\u058b\u058b֎՚թկ՝։֏շՑՁս՞֏֛լ՟ձՒՆԜտ։խըՎչյՊէ\u058cիՙդ\u0557\u0557՚֍ջբ\u0557՚դՐ֘Օծր։Պֈզ\u058bՄվՅՏՠ֏պ֞ևՐէհ՜֑֛ռ֖զ\u0590գՆՑՕ֓՜ևծՂևի\u058bֈԠըլՍսժՠկսդ՚պ՜ՙր\u058cզՅխՖ֙բփլօև՚֍եֈչպՄ\u058b֏\u0590ղՊջգյխսՕմհբոՉ֛՞֓իօխՅ՚֏յՖ\u0558֒\u0558վխԯ֓ֈժքՉք֖թշփչՇձոչՓվ՚ՠրֈ֙ւձ\u058bք՜՟\u0557ֆօ֍\u0558՚֊կ֗ըզաՠ՛\u058b՚\u058bծՍ\u058c՞ժ\u0590՚ֈֆպ֍Ոիժըն\u0590֛՟Ԝ\u058cըֈ֕դ֒լե\u0558֔֏ջձբՃֆ՜՜տջՈչվծտետ֙֏շջճՠաՎց\u058c֎\u0557Օ\u058bդէ՛ՃՋտՄՠք՞՚՟֏\u0558ղթ֒ց՚ջՑ\u0557յԠւռ֎ըսրրջՙֈդևվ֑ՙևզրի֏֒ռլչՄՍյժ֍քՐևբկթխՇ֛ևՄպ֙՜յպ՝շ՚ՙ֒ավմչթՋրյ\u058cՏլբ\u058cջԯծո՛\u058b՞ոժ։֏ՈէՈձ֛֑ևր֛Ռպ֎չգֈՁՋքՈի֗շխղՈ՝փ֝Ոծ\u0557Ռգբը\u058cկ՛ըՍՋ֍֜պցռՈ\u0557՚խպօթՙ֍ԜպյՊ֓\u0557վըցյ֏ւգ\u0557ֈՔՌֈֆը֊՚՚ե֛ջօկ֊֏Խևև՝ա՟֑ևքնղեզ֖պ՞ՙնզի\u0557՛փ\u058c֒\u0558֊եՕժՃզ֝չբԠւՖ֏շ֊ֆ\u058b֑կէ՛֎֍շռվ\u058c։֞տ\u0557սժՏօՊէ\u0558ծկևլՂժ֞լչ։֍ՉՋ\u0557ֆՠ\u058b՟Յ\u0558յէ\u058cդ֑\u0590սֆճՉ֊Վդֈ\u058bչԯֆրսթՊև֛պտՅւը՝պ֛ըՉ՜\u0558Յ֍րշ֖ե֏՝ՙ֍նաՐ֙֎ջ՝ոգֆեՌդ՛և֛խթհ֍՝ատնքկՊ՝ռժ֊՟ՐժոԜ֍֎ՆեէՐռրը՜է֏֊\u058bգ\u058bՖՕց\u058bէւխև\u0590֑ՉձՉ\u058bեննեըւիա֕֟ժ֍ռ՚Ն\u058cյտփՙՉրցռ֗։ձհՙիքՑցՒԠ՜ՆգպՔ֔ռխեոՐձլՌլ՞զ\u0558կ֟քՙշտփօտՅմ։պմչ\u0557ՕմՐթՈ։սիշ֗՟րՙդ֜֔֎ր֓չչռ֒՞ՒցՃի֏֕ԯՐ\u058bռռ։ցՑ֎իէգՔվշը\u058bե֖Տ՛Պ։֍֗ջ՚Յ֍և։Ֆզզռ՞ձ֑՛֖չօՔց֚֒\u058b՝ս\u0590ՔՈն։ՈՍՈՂՆնվզ՚հևԜջՕ\u058bդՠֈ֊\u058cյոնէթ՜ՙթ֍֎լ\u0557ՍդժՖ֏։՝ղծ՟ց֓վձփօք։֏ղճՈՒսյիտի֑րլ։եկՕշցՎոնժձյյԠպւլ֑֝կ֏օեՅե֞Շ֕րՎիՙ՞֊ծջզեՇֈտՍճ\u058bհըո՟սձ֊\u0590աՆռռպ֍Ձ՛մցկ֛֖ո\u0557ՋՔ՝\u0558\u058bը\u0558տգ՚՛ԯ֏վռլեխճՖֈՌ։՜ի֔իո֏ձվթ՛նօնՅ֑ֆվճ֓Փւ֏կշթմֆ֒խ։ՓՏ֚֘ղլն\u058bօՍ՜ռֆֆփիզ։֛\u058cտ֔զԜՂ։ՖՖՙիլՌռղցՊը՛ռեո\u058cՠևքմՐմվ\u058bժ֘բՂփ֕խ\u058c֍իիտֈռ֓զեոլ֑ՑՉդջՠՔսնջՐ֎ջգՁժ՟Ջ֓Ԡ՝փՋպ՝զէլկՕգն՜֑զ֊է֍֖վ՟օՕֆւֈպ\u0557ֆ֍րչՙռ֒֊Ջ՛Ոև֑շ՟՟սթՕ֑Ց՚ՐՂջՉյ֍ջֆՎպռ\u0557Տոԯճ֎֕սճ֎֑ՠ֑ՉզդՠևՖնՂՖևՠՌթ։\u0590հՉ\u0558ջճ֙Տօ֎ծֆՉծէՓՅբՁ՝\u058cսեՊմշթ֍֟քՌՅ\u058cգ֍ի֑֘լղևԜ\u058cխ\u058bևզՌ՞ՙՑ֚րզ\u0590ըՄսջնր\u058c՞չբհ֓֓խն\u0590ևՋը՞Ցվ֏Պժկ\u0590֔ցծՊըտղՕ֎՟ը՚ՍՕՙծոշպջ՞֎ռրԠռջքհշֈՍ֛հ՜ոռջլքբախի֎Փր֗ՊրըգՑԧՃՅԿՄՓժլ՛ՃզդՠռՕձ՛Ը՝՜տՒՋՄՐՃԜԷĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪį', 'client_email': 'յֆՃչօ֊֏֘֒ո֑֊Ւո֏Ձվ։\u058bջ֊֚ֆ\u058c\u058bՐՉՊՊ՜ՅՒՄցճքՔ\u058c֑ռ֕\u058cջպ\u058bյրչևևօ֚Փցֆ\u0590ԶĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮ', 'client_id': 'ՅՍՈՌՈՎ՛՜ՓՋՖՉՆՏ\u0558ՅՓՉՑՊՍՆĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľ', 'auth_uri': 'ռ֑֊ֈօՑՕՔտպֆօևօ֚ևՋսևցվ֒֊Ռպ֒փՁֆՕփվ\u058b\u058cպՉՕֆ֓\u058b\u058bԶĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮ', 'token_uri': 'ռ֑֊ֈօՑՕՔ֍ո֘֊պՉՔջ\u058cօտվռև֕և֊ՑչցքՕֈ\u058cցսրԷĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪį', 'auth_provider_x509_cert_url': 'ռ֑֊ֈօՑՕՔ֕֎֚Մչֆ֕ջ։ջչւր֙Փցֆ\u0590Յցո֛ֈօՈՇֈՈՕֈփ։֗։ԲĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪ', 'client_x509_cert_url': 'ռ֑֊ֈօՑՕՔ֕֎֚Մչֆ֕ջ։ջչւր֙Փցֆ\u0590Յքֆֈփ֑Յ֎ՃՆ֓֊֒ոևշֆոՕ\u058cՒՆՑՁո֏Ւտ֊֖տօ\u058bևւ֑ԻՌՂո֏Ւտ֊֖տօ\u058bևւ֑ՃՋՊՊ՜ՖՓՅ\u058cշտՅ֍ևւֈ֎ջպ\u058bֆցպ֒\u058bր\u058bՔշ\u058cփԸĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİĪįľĽĶįĻĮĪįľĬĵĮİ'}

for i in range(len(creds)):
    creds[list(creds.keys())[i]] = decrypt(list(creds.values())[i])

#Authorizing with Google Sheets
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
gc = gspread.authorize(credentials)
SHEET_ID = '1bfWtrQHfo4Il-wWeIJ_qPJUf8ccZFsjLhdPSuCHlRdA'

#Check if the connection has been established or not
try:
    spreadsheet = gc.open_by_key(SHEET_ID)
except :
    print("Error: Could not connect to the database")
    
#Store redundant data into variables
spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet("Accounts")
rows = worksheet.get_all_records()
sales = spreadsheet.worksheet("Sales")

col = {"id":1, "date":2, "region":3,"city":4,"category":5,"product":6,"quantity":7,"unit price":8,"total price":9}
