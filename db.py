import numpy as np
import matplotlib.pyplot as plt
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def decrypt(encrypt_text):
    orig_text = []
    b = int(len(encrypt_text)/2)
    key = encrypt_text[b:]
    encrypt_text = encrypt_text[:b-1]
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) -ord(key[i]))
        orig_text.append(chr(x))
    orig_text = ("" . join(orig_text))
    return orig_text

scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']
creds = {'type': 'æÉæïÑÆÓÔÚÖÉÑÜáé\x99sdtyhcnuysfbgsuy', 'project_id': 'ÔÍ¡ÚÛÖ×èíÔÔÖ\x94¦\xad¬¬\x94\x9b\x85sdtyhcnuysfbgsuyvcfe', 'private_key_id': '¦\x96¤\xadË\x98£¨Ú¬Ç\x9a\x97«§ÚØ\x95\x9a\x96É§È¥\x92\x99«×\x9c¦¯Í\x97¢¥®£\x96\x93\xa0\x93sdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgs', 'private_key': '\xa0\x91¡¦\x95¥³¼ÂÁ\x86²¹¼ËºÊ¨\x86°\xadÇ\x93¢\x8f\x92¦}±½Â\xadÙå¾»´ª£µµÜäçËÑÎ¯§Ý¥¤¦Ê¸ªµº»¦°ÀäêÍÉºß¶à»¤§Ô±°§Æ¥·¤µÇì¯ÌºÝÅÅ«Ñl\x97Öíº¿¶©»\x93·Õ¼Ú¦Ã¿É×ÉÛ±ÂÅ°ºÜ\x92ÐËãÂè\x9bÏÒâ\xa0\x9cÁ¦©ÚÂ§ÂäÌÇÇ©«¹\x9d§\x99¨ëã¸\xad\x98ÖÎ¢p§Ï\xadÂåÈÊÊ´\x98èÀªÛ³È\x9aÛË°ÚµÇÐ\x9f×¯\xadÙ°©¾·»ä½¶ÄÆ¯ÂÊÕ®Ùî©ÁÕ¸\x9a×Åµ¹¼\x9cª½Æè®×»xã«µ½Ì\x9eãßÝ×Æ©®¶Ø¼àÛÖÝá\x98»àÚ\x9b\x9däí»ÔµÓëêËÈ\x97ÌÛªÓ°¬¶©ºâ±Èé³\x98âÊÓÅ\x98¦ÚÀ×ê¡mÞ®Á¯¯\xadÏ\x97»ÜÐ\xad®´\x98Âå±ÉÔÈ\x9fÇ¹ÐÝ\x9c¸Ð¸\x99³¥¼\x97èÈÌ¤¤\x93¨\x9fª¨Ö²ÚÉ¶ÏÏá\x92Þ¬ºæ´ÌÆÍàänÅ\xad\x9e³·Ààà§ÐÐÕâ½ÍÊ½»«¹ÑÁ¨ÔË¶ÔÁÌ×\x9cÃ¿ÉÀÐØÁ¥¸Ìà¶ËËØ±¬Î\xad×âÖ\x98\x9fÞ´Ûã¼ºÍ\x95\x92qÛØÒÁ\x9bÇÈ\x9b¯ÍÂ¤¦º¸§Ûà\xad¤°Ç²å\x96²ÐÙ©ïÅÈ\x96Æ\x97¥´í¶Þâ¬¨ÎÃâØÖîÉë·\x91\x92£ê¾Ú»\x96Õ\xadåÑ\x7f²¿¯Ê©¶ÑÂ±¶Ø¯¸ÉØµ¦Ë©ê§Ò®×ã©Ü³ÐÜÕ\x96èâÓ·¡ÍÆÖ¼¹¨ÊÏÃÜ\x95Û\x9eÝÂÈÌ\x95¨âÔ\x9d¶ó®Êµ\x7fîä\xadÐ\x9eàåÎÐÐÇ\x9aÂÀºªÉ\x9cÃáÕçç¼ØÚ¿Á¤ÇÉÝ¨¹ñÎÔº®³¶¯é\x96ËÉ©Í¼Ñá\x97âÞÝè\x9c¶«¶Íòî¬pÚªâÞÃÜ¿Ç¥ÓåÝ¶¯\x9fä¯»ÈÇ\x97ÚÜÁÐªÎÛáÓÊÂ®©±ÜÞëª\x98Ð»¹¾¤\x9a»\x97¶ã¿¾«Ï\x98¼ÀÕàªÉ¤¶¼~ãÒÚ°ÍÛÜ¾¥ÝÀÖãê¦Õ¹Ñ³ÐéÇ®Ü¥\x9aÃÏØÑ¦êÄ¼ª±\x97ëæ«ÙÖ®½Ì³Ë¸\x95Ò¼Úµ×Ð\x9c½Ïä²Ç¶×¼}ÅÚ®Ø²Æ¬ãØ§±\x9bÓèÐÝâà\x99ÖìÌÂÑ\x8d\x9aå¦¾è¼¼´\x9a¹Òì\x96¶º§µ¿»Ï´²º°¬ÜØÍ×Û©»¦\xadºÏÀ\x9cìlÈÈ©Úµß¾Í½ßÝ¿\x9aÔ©¨×ëÁ×¨\xad¶ã¼ÜºÌò\x9eÔÕÂ¬¬çêæÃ³©¶æÙÅ¸³¸³©±×êÎ\x98åÁ\x96Èª·ÚÓº\x83ÝªÚ¸ØÝíä¼»©ÐçÀÛÈßëë¾\xadß¯\x9cá¨º··»ÖÍ\xa0½ï±ÈËß¥\x9a¦Ô¨îº\x97µÈªÑ»ãóÞÕ¯\x9cà\xadÅì×¹oÐ×ÀÈ\x9aÕîÙÆ£ã¾©ÂëÃ¥\x9f¤\x9aéÏÜï²Ý°ªÕ·¸\x9bÛñÜªÆÈÑ²¢Ç½ÔÜ±¹ÀìÄÀ¼ÈÌÁ\xa0±Ú¦Êº¬«Ö\x83ÞË\xa0½Ê«ÐË©ª¾ñÝØ·Ù\x98¯Êê±ÕÏÔÏç«¶\x96çÃÉÕ®´ÑÌ¿èð¯Ü¾¬¢ÛÄÍË¼¤ÒÞÏÚÎÈÂ¼ÌÓ\x8dÔ¨\x7f½ª¯º\x94ÞÓ°ÄÈ\x9eÄË\x93Ê¿¼¤·ïßµºËØáÎªÍÖÈÇÊ\x9f\x96Ë\x9b««êÊ¹Üâ¬Ö¼ÆéÕÒÐãØàÛÏ°\x9aÓ\x99¿íÑo«ç½ÚðÒ\x8eèÃÊ¾¨É¸¶âÇé\x9c¯\x98ËçàÚ¤\x98ïÔÈ¬È«ÉºÏäºßÅÔµßíãÐ¬¿â°\x97Å×\x90°£\x94£ÉÁ«±Âê}Ê\x91Þº¿éîØµ¸À¾¬»©·àí³µ®º¶\x9eßä¹µº´ÝâãÊÐÓ×Ú×³Ê\x93\x94àÖ¸ÍÐÜÍÂìÇ¼\x96»Ñ\x9e×ÝÉ®Ç½rÐÖÊÍÝÊëÆÃ¬¶Û¡íã©¿¤\x9fØÅÝ¹²\x9bÖÁ§¼êº»Ú¬¼ÇìÕ®¢ÚÏÙÖ\x8dªÕßÂìÛÇ\x99\x9d°¬§Ù°»Úµ·®rÔÕÎÏÆ¼¯©Þ«êÀ·Ô«Âæ´Ý¹©Éä½£òÜÊ»ã®ÞÒ»ÌÅÃëëº×¦\xa0âÙÉ·¸îæ\x9aªáÑÓÙÎÈÖÜÐÏäÅ\x83¡Æ¨\x9e«ÁÀª¸²Ü¦©¹ã¶µæ¸êßÈ\x9bµÌâÌë¯\x96Ñ×ÇÕìµ¾áÕ»éÈªÅÈï¤¨\xadÇ¯µÛÉÌ\x95Ý½µ\x9d¹®\x99Û\x83¸Õ¨Í\xa0«¾¾Ò¶²²¯çÅëËÙÖ¾©Ü\x98åÒÖÍ¶ÍëáÏ¥Äâå§\x9e\x94ÜíÆÄ¸Ê·¨â\x99\x9b§\x8d½¬ÖÚÉë\x99ÇÒº±Åp·ÞåÜÚíÎ²Ù\x9b¼¸¾Ã\x96Ñ\x9e\x97åÇ\x9d¦ãèÓ¤¬Æ´ç¦çá»Ú\x97°Á\x9c¤¬\x94¿Ù¼»¬¹ÄÅëòã\x95\x91ÛÄë¾éÖ»´ÙxÛ¼ÙÏÉ§°¶¤ÝÅ½âË¥Ì·ÉÖë¿Ý®°ÓÝÄ¹ï×\x99»½\x98Üð\xa0¶·àïÝ±\x96½ÛÁºç¬¶\xad\x9e\x9d\x9aÅÃ¹ÝÜ«ÜáËmÒÞæ½¸Ì\x9dëÏÃ×¹Í´Ö¸µË§Î®ÜØ¨ç¹\xa0«\x7f¦\xa0\x93\x8f\x94¸Ã½\x96³¸®¾¯ºº\x82°¾Ì\x91¡¦\x95\x90x\x95sdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnu', 'client_email': 'ÔÍ¡ÚÛÖ×èíÔÔÖ§ÔÞ¦×ÖÙÎÛâÇãÖ\x92¬«\x97ªª\x9d\x91×Öæ¡ÍÕÌåëâÙÈÇÈËÝÛãÖ\x93ÜâÑ\x94sdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdt', 'client_id': '¤\x94¦\xad\x9e\x9a£¬®§\x99\x95\x9b«§ª¬\x96\x9f\x9d\x9e\x8esdtyhcnuysfbgsuyvcfehn', 'auth_uri': 'ÛØèéÛ\x9d\x9d¤ÚÖÉÑÜáéì¤ÊÕÔÏÚË£ÅÔæ¢Ó£èÉØâÝ«¢Ç×ÛÛ\x95sdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsu', 'token_uri': 'ÛØèéÛ\x9d\x9d¤èÔÛÖÏ¥£àåÒÍÑÍÏÖÞÕ\x93ÜâÑ£í×ÎÓã\x99sdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuy', 'auth_provider_x509_cert_url': 'ÛØèéÛ\x9d\x9d¤ðêÝ\x90ÎâäàâÈÇÕÑá\x94ØÑÒ¨âÅéíÐ\x95\x9dëª¢ÉÇÙçè\x99sdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuy', 'client_x509_cert_url': 'ÛØèéÛ\x9d\x9d¤ðêÝ\x90ÎâäàâÈÇÕÑá\x94ØÑÒ¨åÓÖèÜ\x92ä¦¨àËÖÈ×Öí×\x92Þ\x9a\x98§\x95ÖË\x92Úæ×ÝìÜÄÜé\x9e§\x96ÃÐ\xa0ÖìéÌÙÙÉÜÚ¢\x95\x9d¬©\x95©§ÑÄÛ£àæËÔÝÜØÞ×ÆÉÔÝÜÚ£ÅÔæ\x93sdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeysdtyhcnuysfbgsuyvcfehnfubeys'}
for i in range(len(creds)):
    creds[list(creds.keys())[i]] = decrypt(list(creds.values())[i])
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
gc = gspread.authorize(credentials)
SHEET_ID = '1bfWtrQHfo4Il-wWeIJ_qPJUf8ccZFsjLhdPSuCHlRdA'
try:
    spreadsheet = gc.open_by_key(SHEET_ID)
    
except gspread.exceptions.APIError or ConnectionError as e:
    print("Error: Could not connect to the database. Reason:", e)

spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet("Accounts")
rows = worksheet.get_all_records()

sales = spreadsheet.worksheet("Sales")

col = {"id":1, "date":2, "region":3,"city":4,"category":5,"product":6,"quantity":7,"unit price":8,"total price":9}
