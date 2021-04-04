import string

with open("key.txt", "r") as f:
    shift = int(f.readline())
    key = f.readline()

with open("flag.txt", "r") as f:
    flag = f.read()

stdalph = string.ascii_lowercase
rkey = ""

for i in key:
    if i not in rkey:
        rkey += i
for i in stdalph:
    if i not in rkey:
        rkey += i
rkey = rkey[-shift:] + rkey[:-shift]

enc = ""
for a in flag:
    if a in stdalph:
        enc += rkey[stdalph.index(a)]
    else:
        enc += a

print(enc)

# quutcvbmy ft qii amtkm iqkd tx qjbqfbtm, fzwcw bd mt kqo q sww dztgiv sw qsiw ft xio. 
# bfd kbmyd qcw ftt drqii ft ywf bfd xqf ibffiw stvo txx fzw yctgmv. fzw sww, tx utgcdw, 
# xibwd qmokqo swuqgdw swwd vtm'f uqcw kzqf zgrqmd fzbma bd brhtddbsiw. owiitk, siqua. 
# owiitk, siqua. owiitk, siqua. owiitk, siqua. ttz, siqua qmv owiitk! iwf'd dzqaw bf gh q 
# ibffiw. sqcco! scwqaxqdf bd cwqvo! utrbmy! zqmy tm q dwutmv. zwiit? sqcco? qvqr? uqm otg 
# swibwjw fzbd bd zqhhwmbmy? b uqm'f. b'ii hbua otg gh. ittabmy dzqch. gdw fzw dfqbcd. otgc 
# xqfzwc hqbv yttv rtmwo xtc fztdw. dtcco. b'r wnubfwv. zwcw'd fzw ycqvgqfw. kw'cw jwco hctgv 
# tx otg, dtm. q hwcxwuf cwhtcf uqcv, qii s'd. jwco hctgv. rq! b ytf q fzbmy ytbmy zwcw. otg
#  ytf ibmf tm otgc xgpp. tk! fzqf'd rw! kqjw ft gd! kw'ii sw bm ctk 118,000. sow! sqcco, b 
# ftiv otg, dfth xiobmy bm fzw ztgdw! zwo, qvqr. zwo, sqcco. bd fzqf xgpp ywi? q ibffiw. 
# dhwubqi vqo, ycqvgqfbtm. mwjwc fztgyzf b'v rqaw bf. fzcww vqod ycqvw duztti, fzcww vqod 
# zbyz duztti. fztdw kwcw qkakqcv. fzcww vqod utiiwyw. b'r yiqv b ftta q vqo qmv zbfuzzbawv 
# qctgmv fzw zbjw. otg vbv utrw squa vbxxwcwmf. zb, sqcco. qcfbw, yctkbmy q rgdfquzw? ittad 
# yttv. zwqc qstgf xcqmabw? owqz. otg ytbmy ft fzw xgmwcqi? mt, b'r mtf ytbmy. wjwcostvo amtkd, 
# dfbmy dtrwtmw, otg vbw. vtm'f kqdfw bf tm q degbccwi. dguz q ztfzwqv. b ygwdd zw utgiv zqjw 
# lgdf ytffwm tgf tx fzw kqo. b itjw fzbd bmutchtcqfbmy qm qrgdwrwmf hqca bmft tgc vqo. fzqf
# 'd kzo kw vtm'f mwwv jquqfbtmd. sto, egbfw q sbf tx htrh... gmvwc fzw ubcugrdfqmuwd. kwii, 
# qvqr, ftvqo kw qcw rwm. kw qcw! sww-rwm. qrwm! zqiiwiglqz! dfgvwmfd, xqugifo, vbdfbmygbdzwv
#  swwd, hiwqdw kwiutrw vwqm sgppkwii. kwiutrw, mwk zbjw ubfo ycqvgqfbmy uiqdd tx... ...9:15
# . fzqf utmuigvwd tgc uwcwrtmbwd. qmv swybmd otgc uqcwwc qf ztmwn bmvgdfcbwd! kbii kw hbua t
# gclts ftvqo? b zwqcv bf'd lgdf tcbwmfqfbtm. zwqvd gh! zwcw kw yt. awwh otgc zqmvd qmv qmfwm
# mqd bmdbvw fzw fcqr qf qii fbrwd. ktmvwc kzqf bf'ii sw ibaw? q ibffiw duqco. kwiutrw ft ztm
# wn, q vbjbdbtm tx ztmwdut qmv q hqcf tx fzw zwnqytm yctgh. fzbd bd bf! ktk. ktk. kw amtk fz
# qf otg, qd q sww, zqjw ktcawv otgc kztiw ibxw ft ywf ft fzw htbmf kzwcw otg uqm ktca xtc ot
# gc kztiw ibxw. ztmwo swybmd kzwm tgc jqibqmf htiiwm ltuad scbmy fzw mwufqc ft fzw zbjw. tgc
#  fth-dwucwf xtcrgiq bd qgftrqfbuqiio utitc-utccwufwv, duwmf-qvlgdfwv qmv sgssiw-utmftgcwv bmft
#  fzbd dttfzbmy dkwwf docgh kbfz bfd vbdfbmufbjw ytivwm yitk otg amtk qd... ztmwo! fzqf ybci kqd
#  ztf. dzw'd ro utgdbm! dzw bd? owd, kw'cw qii utgdbmd. cbyzf. otg'cw cbyzf. qf ztmwn, kw utmdfqm
# fio dfcbjw ft brhctjw wjwco qdhwuf tx sww wnbdfwmuw. fzwdw swwd qcw dfcwdd-fwdfbmy q mwk zwirwf 
# fwuzmtityo. kzqf vt otg fzbma zw rqawd? mtf wmtgyz. zwcw kw zqjw tgc iqfwdf qvjqmuwrwmf, fzw a
# cwirqm. qufx{awowvuqwdqcrtcwibawdgsdfbfgfbtm}