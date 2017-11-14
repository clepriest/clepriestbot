# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,requests,urllib
import re,string,os,shutil,urllib2,urllib3,subprocess
from urllib import urlopen
import requests,tempfile

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token='Emi2ooEATC1trHm9eQm8.92N3yOZyjP470D+f5mMOca.sQQ+hKVTqqvC6P2/fSK/XbHRjDLv9BOx8XQ0ZfPAjQE=')
cl.loginResult()
print "Cl-Login Success\n"

ki = LINETCR.LINE()
#ki.login(qr=True)
ki.login(token='EmFJApEIKLgndBfbA5Ic.ngZouQ5JCl1yyqkwKV5yla.j0IZD6onn8nX0xDnTlHro2TPktbwxOGxhhl/TFwb9wM=')
ki.loginResult()
print "Ki-Login Success\n"

kk = LINETCR.LINE()
#kk.login(qr=True)
kk.login(token='EmvtO0yqAf5pQfQ6TYb6.G9zI9TLx+k0yHOWQsyE/5G.Ut/7qTkiX3sJKNE7wet8Medp8PXPCDO94Vggrt8hNhc=')
kk.loginResult()
print "Kk-Login Success\n"

kc = LINETCR.LINE()
#kc.login(qr=True)
kc.login(token='EmWmh5ec63BWTgfjiP12.RX11XkH7n9co3xJN2vQHuG.dWGgky7Vmi5dhFYBVfMGebGn9U1/kKcsglBy6Lt1rUI=')
kc.loginResult()
print "Kc-Login Success\n\n=====[All Bot Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" TEST BOT
[Join︎ on/off]
[Group cancelalll︎]
[Leave︎ on/off]
[Add on/off]
[Share on/off]
[Message change:「text」]
[Message check]
[Confirm]
[Jam on/off]
[Change clock:「name」]
[Up]
[Cv join]

[*] Command in the groups [*]

[Curl]
[Ourl]
[url]
[url:「Group ID」]
[Invite：「mid」]
[Kick：「mid」]
[Ginfo]
[jointicket]
[Cancel]
[Gn 「group name」]
[Nk 「name」]

[*] Command kicker only [*]

[Bye]
[Kill ban]
[Kill 「@」]
[Ban 「@」] By Tag
[Unban 「@」] By Tag
[Ban︎] Share Contact
[Unban︎] Share Contact
[Banlist︎]
[Cek ban]
[Cv mid]
[Cv ︎invite:「mid」]
[Cv ︎rename:「name」]
[Cv ︎gift]
[Respo︎n]
[Bot cancel]
[Title:]
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["","ue11fc7860247c63bd3da149613a793f6"]
admsa=["ue11fc7860247c63bd3da149613a793f6"]
pro=[]
linkpr=[]
cancl=[]
canclpr=[]
guard=[]

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    "lang":"JP",
    "comment":"Auto Like by Karen\nhttp://line.me/ti/p/~_mashirochan",
    "commentOn":True,
    "likeOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "cName":"",
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
		if op.type == 32:
		  if op.param1 in canclpr or guard:
			if wait["cancelprotect"] == True:
				if op.param2 in Bots + admin:
					pass
				else:
					ki.findAndAddContactByMid(op.param3)
					ki.inviteIntoGroup(op.param1,[op.param3])
					ki.kickoutFromGroup(op.param1,[op.param2])
			else:
				if op.param2 in Bots + admin:
					pass
				else:
					ki.findAndAddContactByMid(op.param3)
					ki.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 11:
		  if op.param1 in linkpr or guard:
			if wait["linkprotect"] == True:
				if ki.getGroup(op.param1).preventJoinByTicket == False:
					if op.param2 in Bots + admin:
						pass
					else:
						ki.kickoutFromGroup(op.param1,[op.param2])
						wait["blacklist"][op.param2] = True
						ki.reissueGroupTicket(op.param1)
						X = ki.getGroup(op.param1)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						print "[autokick] qr/link open"
        if op.type == 11:
			if op.param1 in pro or guard:
				  if wait["protect"] == True:
					ki.getGroup(op.param1)
					if op.param2 in Bots + admin:
						pass
					else:
						ki.kickoutFromGroup(op.param1,[op.param2])
						wait["blacklist"][op.param2] = True
						print "[autokick] random group update"
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
        if op.type == 13:
			if op.param2 in Bots + admin:
				pass
			else:
			 if op.param1 in cancl or guard:
				if wait["inviteprotect"] == True:
					cl.cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if op.param3 in admin + admsa:
                  if op.param2 in Bots or admsa:
                    pass
                  wait["blacklist"][op.param2] = True
                  print "Admin kicked."
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  ki.inviteIntoGroup(op.param1,[op.param3])
                  print "[Autokick] kicker kicked, admin invited back."
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                else:
                  if op.param1 in pro or guard:
                   wait["blacklist"][op.param2] = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   ki.inviteIntoGroup(op.param1,[op.param3])
				
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
#------------------------------------------------------------------------------
               elif wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cl.sendText(msg.to,"-> " + _name + "\nSudah didalam grup")
                            break
                        elif invite in wait["blacklist"]:
                            ki.sendText(msg.to,"Maaf, " + _name + " di Blacklist")
                            cl.sendText(msg.to,"Hubungi admin untuk Unban")
                            break                             
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(msg.to,[target])
                                wait["invite"] = False
                                break
                            except:
                                try:
                                    ki.findAndAddContactsByMid(invite)
                                    ki.inviteIntoGroup(op.param1,[invite])
                                    wait["invite"] = False
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(invite)
                                        cl.inviteIntoGroup(op.param1,[invite])
                                        wait["invite"] = False
                                        cl.sendText(msg.to,"Done" + _name)
                                        break
                                    except:
                                        try:
                                            kk.findAndAddContactsByMid(invite)
                                            kk.inviteIntoGroup(op.param1,[invite])
                                            wait["invite"] = False
                                            kk.sendText(msg.to,"Done" + _name)
                                            break
                                        except:
                                            cl.sendText(msg.to,"Error")
                                            wait["invite"] = False
                                            break
#----------------------------------------------------------END-----------------
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            
            elif msg.text.lower() == 'help':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
#===CHANGE NAME===================================================================                    
            elif ("gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
#===============================================================================
            elif msg.text.lower() in ["invite"]:
              if msg.from_ in admin:
                    wait["invite"] = True
                    cl.sendText(msg.to,"Send contact")
#===GIFT=========================================================================
            elif msg.text in ["gift","Gift"]:
             if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
#===============================================================================
            elif msg.text in ["cancel","Cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"Undangan dibersihkan")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak ada undangan")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#===MEMBUKA ATAU MENUTUP LINK===================================================
            elif msg.text in ["link on","Link on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
                        
            elif msg.text in ["link off","Link off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#===GROUP INFO===================================================================
            elif msg.text in ["ginfo"]:
              if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "Nama Grup : " + group.name + "\nId Grup : " + group.id + "\nPembuat Grup :" + gCreator + "\nGambar Grup : http://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
#================================================================================

#====BOT RESPON==================================================================
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                

#===GANTI NAMA BOT================================================================                
            elif "cnmain " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("cnmain ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")
                    cl.sendText(msg.to,"My name is " + string + ".")
            elif "bot1cn " in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("bot1cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"Done")
                    ki.sendText(msg.to,"My name is " + string + ".")
            elif "bot2cn " in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("bot2cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.sendText(msg.to,"Done")
                    kk.sendText(msg.to,"My name is " + string + ".")
            elif "bot3cn " in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("bot3cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kc.getProfile()
                    profile_B.displayName = string
                    cl.sendText(msg.to,"Done")
                    kc.sendText(msg.to,"My name is " + string + ".")
#====CEK KONTAK MENGGUNAKAN MID=================================================
            elif "show " in msg.text:
                midd = msg.text.replace("show ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":midd}
                cl.sendMessage(msg)
#===COMMAND PROTECT, PANICK, DLL================================================                
            elif msg.text.lower() == 'contact on':
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already on")
                        
            elif msg.text.lower() == 'contact off':
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Off")
                    else:
                        cl.sendText(msg.to,"It is already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Off")
                    else:
                        cl.sendText(msg.to,"It is already off")
                        
            elif msg.text.lower() == 'protect on':
              if msg.from_ in admin:
                if wait["protect"] == True:
                    if msg.to in pro:
                        cl.sendText(msg.to,"protection already on")
                    else:
                        pro.append(msg.to)
                        cl.sendText(msg.to,"protection on")
                else:
                    wait["protect"] = True
                    pro.append(msg.to)
                    cl.sendText(msg.to,"protection on")
                        
            elif msg.text.lower() == 'qrprotect on':
              if msg.from_ in admin:
                if wait["linkprotect"] == True:
                    if msg.to in linkpr:
                        cl.sendText(msg.to,"protection already on")
                    else:
                        linkpr.append(msg.to)
                        cl.sendText(msg.to,"protection on")
                else:
                    wait["linkprotect"] = True
                    linkpr.append(msg.to)
                    cl.sendText(msg.to,"protection on")
                        
            elif msg.text.lower() == 'inviteprotect on':
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if msg.to in cancl:
                        cl.sendText(msg.to,"protection already on")
                    else:
                        cancl.append(msg.to)
                        cl.sendText(msg.to,"protection on")
                else:
                    wait["inviteprotect"] = True
                    cancl.append(msg.to)
                    cl.sendText(msg.to,"protection on")
                        
            elif msg.text.lower() == 'cancelprotect on':
              if msg.from_ in admin:
                if wait["cancelprotect"] == True:
                    if msg.to in canclpr:
                        cl.sendText(msg.to,"protection already on")
                    else:
                        canclpr.append(msg.to)
                        cl.sendText(msg.to,"protection on")
                else:
                    wait["cancelprotect"] = True
                    canclpr.append(msg.to)
                    cl.sendText(msg.to,"protection on")
                        
            elif msg.text.lower() == 'auto join on':
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already on")
						
            elif msg.text.lower() == "guard:list":
			  if msg.from_ in admin:
				if guard == []:
					cl.sendText(msg.to,"No one groups accepted.")
				else:
					mc = ""
					for gid in guard:
						mc += "\n- " + cl.getGroup(gid).name
					cl.sendText(msg.to, "protected groups :\n" + mc)
						
            elif "guard:on" in msg.text.lower():
              if msg.from_ in admin:
                if msg.to in guard:
                    cl.sendText(msg.to,"Guard already on.")
                else:
                    guard.append(msg.to)
                    cancl.append(msg.to)
                    pro.append(msg.to)
                    canclpr.append(msg.to)
                    linkpr.append(msg.to)
                    wait["inviteprotect"] = True
                    wait["cancelprotect"] = True
                    wait["protect"] = True
                    wait["linkprotect"] = True
                    cl.sendText(msg.to,"Bots will protect this group.")
                        
            elif "guard:off" in msg.text.lower():
              if msg.from_ in admin:
                if msg.to not in guard:
                    cl.sendText(msg.to,"Guard already off.")
                else:
                    guard.remove(msg.to)
                    cancl.remove(msg.to)
                    pro.remove(msg.to)
                    canclpr.remove(msg.to)
                    linkpr.remove(msg.to)
                    wait["inviteprotect"] = False
                    wait["cancelprotect"] = False
                    wait["protect"] = False
                    wait["linkprotect"] = False
                    cl.sendText(msg.to,"Bots will unprotect this group.")
                        
            elif msg.text.lower() == 'auto join off':
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Off")
                    else:
                        cl.sendText(msg.to,"It is already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Off")
                    else:
                        cl.sendText(msg.to,"It is already off")
                        
            elif msg.text.lower() == "protect off":
              if msg.from_ in admin:
                if wait["protect"] == False:
                    if msg.to not in pro:
                        cl.sendText(msg.to,"protection already off")
                    else:
                        pro.remove(msg.to)
                        cl.sendText(msg.to,"protection off")
                        guard.remove(msg.to)
                else:
                    wait["protect"] = False
                    pro.remove(msg.to)
                    cl.sendText(msg.to,"protection off")
                    guard.remove(msg.to)
                        
            elif msg.text.lower() == "qrprotect off":
              if msg.from_ in admin:
                if wait["linkprotect"] == False:
                    if msg.to not in linkpr:
                        cl.sendText(msg.to,"protection already off")
                    else:
                        linkpr.remove(msg.to)
                        cl.sendText(msg.to,"protection off")
                        guard.remove(msg.to)
                else:
                    wait["linkprotect"] = False
                    linkpr.remove(msg.to)
                    cl.sendText(msg.to,"protection off")
                    guard.remove(msg.to)
                        
            elif msg.text.lower() == "inviteprotect off":
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if msg.to not in cancl:
                        cl.sendText(msg.to,"protection already off")
                    else:
                        cancl.remove(msg.to)
                        cl.sendText(msg.to,"protection off")
                        guard.remove(msg.to)
                else:
                    wait["inviteprotect"] = False
                    cancl.remove(msg.to)
                    cl.sendText(msg.to,"protection off")
                    guard.remove(msg.to)
                        
            elif msg.text.lower() == "cancelprotect off":
              if msg.from_ in admin:
                if wait["cancelprotect"] == False:
                    if msg.to not in canclpr:
                        cl.sendText(msg.to,"protection already off")
                    else:
                        canclpr.remove(msg.to)
                        cl.sendText(msg.to,"protection off")
                        guard.remove(msg.to)
                else:
                    wait["cancelprotect"] = False
                    cancl.remove(msg.to)
                    cl.sendText(msg.to,"protection off")
                    guard.remove(msg.to)
                        
            elif msg.text in ["Leave on","Auto leave: on"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already on")
                        
            elif msg.text in ["Leave off","Auto leave: off"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already off")
                        
            elif msg.text in ["Share on","share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already on")
                        
            elif msg.text in ["Share off","share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
#===COMMAND BUAT MY SET (LIHAT SET GROUP)=======================================                        
            elif msg.text.lower() == 'myset':
             if msg.from_ in admin:
                md = ""
                if wait["contact"] == True: md+="☞ Contact → ✔\n"
                else: md+="☞ Contact → ❌\n"
                if wait["autoJoin"] == True: md+="☞ Auto Join → ✔\n"
                else: md+="☞ Auto Join → ❌\n"
                if wait["autoCancel"]["on"] == True:md+="☞ Auto cancel: " + str(wait["autoCancel"]["members"]) + " → ✔\n"
                else: md+="☞ Group cancel → ❌\n"
                if wait["leaveRoom"] == True: md+="☞ Auto leave → ✔\n"
                else: md+="☞ Auto leave → ❌\n"
                if wait["timeline"] == True: md+="☞ share → ✔\n"
                else:md+="☞ Share → ❌\n"
                if wait["autoAdd"] == True: md+="☞ Auto add → ✔\n"
                else:md+="☞ Auto add → ❌\n"
                if wait["commentOn"] == True: md+="☞ Auto komentar → ✔\n"
                else:md+="☞ Auto komentar → ❌\n"
                if msg.to in pro: md+="☞ Protect → ✔\n"
                if msg.to not in pro: md+="☞ Protect → ❌\n"
                if msg.to in linkpr: md+="☞ Link Protect → ✔\n"
                if msg.to not in linkpr: md+="☞ Link Protect → ❌\n"
                if msg.to in cancl: md+="☞ Invitation Protect → ✔\n"
                if msg.to not in cancl: md+="☞ Invitation Protect → ❌\n"
                if msg.to in canclpr: md+="☞ Cancel Protect → ✔\n"
                if msg.to not in canclpr: md+="☞ Cancel Protect → ❌\n"
                if wait["likeOn"] == True: md+="☞ Auto like → ✔\n"
                else:md+="☞ Auto like → ❌\n" 
                cl.sendText(msg.to,md)
#===COMMAND BUAT LIKE ON ATAU OFF===============================================                
            elif msg.text in ["Like:on","like:on"]:
              if msg.from_ in admin:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
                        
            elif msg.text in ["like:off","Like:off"]:
              if msg.from_ in admin:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
#===============================================================================
            elif msg.text in ["Add on","Add auto on"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                        
            elif msg.text in ["Add off","Add auto off"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
#===============================================================================
            elif msg.text in ["comment on"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
                        
            elif msg.text in ["comment off"]:
              if msg.from_ in admin:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
#===============================================================================
            elif msg.text in ["Gurl","gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#==========CEK SIDER============================================================
            elif msg.text.lower() == 'setpoint':
                    cl.sendText(msg.to, "Setpoint ditambahkan")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
                    
            elif msg.text.lower() == 'viewsider':
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "Siders:\n%s\nDate and time:\n[%s]"  % (chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Setpoint belum terpasang")
#------------------------------------------------------------------------------------

#-----------------------------------------------
            elif msg.text.lower() in ["alljoin"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text.lower() in ["Cv1 join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text.lower() in ["Cv2 join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text.lower() in ["Cv3 join"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Bye all"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "code27" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("code27","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                         if target not in Bots:
                          if target not in admin:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
							    pass

            elif "kick " in msg.text:
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")
#================================================================================
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes")
                            except:
                                ki.sendText(msg.to,"Error")
                                
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes")
                            except:
                                ki.sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
            elif msg.text in ["Test"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                kk.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                kc.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
#-----------------------------------------------
            elif "Bc " in msg.text:
              if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Cv say hi"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Cv say hinata pekok"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Selamat datang di Chivas Family Room")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text.lower() in ["respon","resp"]:
			  if msg.from_ in admin:
				cl.sendText(msg.to,"Shiina on")
				ki.sendText(msg.to,"Sorata on")
				kk.sendText(msg.to,"Nanami on")
				kc.sendText(msg.to,"Ryunosuke on")
#-----------------------------------------------

            elif msg.text in ["Creator","creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ue11fc7860247c63bd3da149613a793f6'}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': 'u238c8b46c8c4a80504f6eafdf45fcb5f'}
                cl.sendMessage(msg)

            elif msg.text in ["Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Tunggu...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s detik" % (elapsed_time))

            elif msg.text in ["botcall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
#------------------------------------------------------------------	
            elif "cover " in msg.text:
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendText(msg.to,"Cover " + contact.displayName)
                            cl.sendImageWithURL(msg.to,path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "cover group" in msg.text:
              if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(msg.to, path)
#------------------------------------------------------------------
            elif ("pp " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                            cl.sendImageWithURL(msg.to,image)
                        except:
                            pas
                print "[Command]dp executed"		
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim kontak")

            elif msg.text in ["Unban"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim kontak")

            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak ada user terbanned")
                else:
                    cl.sendText(msg.to,"User terbanned:")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak ada user terblacklist")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"User terblacklist telah dikeluarkan")
#===============================================================================
#==============OP TYPE CEK SIDER===========================
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = cl.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n- " + Name
						wait2['ROM'][op.param1][op.param2] = "- " + Name
				else:
					cl.sendText
            except:
                pass
				
			
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
#===DEF AUTO LIKE======================================================================
def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#======================================================================================
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
