# python 3.8+ required
# this is a calculate m program
import math

# 暗号化
# 1.巨大な素数p,qを用意しn=pqを計算
# 2.p-1とq-1の最小公倍数Lをもとめる
# 3.ed≡1(mod L) (ed-1がLの倍数である)となるようなedの組を求める
# 4.平文mを公開鍵(e,n)を使ってc = m^e mod n (mのe乗をnで割った余り)を計算して暗号化
# (n・e): 公開鍵
# (n・d): 秘密鍵


# 拡張ユークリッド互除法 x=e,y=L,gcd(x,y)=gcd(e,L)=1
def ex_euclid(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1

    while c1 != 0:
        m = c0 % c1
        q = c0 // c1

        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
    # return d
    return a0


# 復号化(mを求める)
# 1. n = pqを計算しておく
p = 34111525225922333955113751419357677129436029651245533697825114748126342624744832960936498161825269430327019858323450578875242014583535842110912370431931233957939950911741013017595977471949767235426490850284286661592357779825212265055931705799916913817655743434497422993498931394618832741336247426815710164342599150990608143637331068220244525541794855651643135012846039439355101027994945120698530177329829213208761057392236875366458197098507252851244132455996468628957560178868724310000317011912994632328371761486669358065577269198065792981537378448324923622959249447066754504943097391628716371245206444816309511381323
q = 44481453884385518268018625442920628989497457642625668259648790876723318635861137128631112417617317160816537010595885992856520476731882382742220627466006460645416066646852266992087386855491152795237153901319521506429873434336969666536995399866125781057768075533560120399184566956433129854995464893265403724034960689938351450709950699740508459206785093693277541785285699733873530541918483842122691276322286810422297015782658645129421043160749040846216892671031156465364652681036828461619272427318758098538927727392459501761203842363017121432657534770898181975532066012149902177196510416802134121754859407938165610800223
# 2. p-1とq-1の最小公倍数Lを求める L = lcm(a,b) = ab/gcd(a,b)
lcm = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
L = lcm
# 3. ed≡1(modL)(ed-1がLの倍数)となるedの組を求める
e = 65537
d = ex_euclid(e, L)
# 4. m = c^d mod n
c = 225549592628492616152632265482125315868911125659971085929712296366214355608049224179339757637982541542745010822022226409126123627804953064072055667012172681551500780763483172914389813057444669314726404135978565446282309019729994976815925850916487257699707478206132474710963752590399332920672607440793116387051071191919835316845827838287954541558777355864714782464299278036910958484272003656702623646042688124964364376687297742060363382322519436200343894901785951095760714894439233966409337996138592489997024933882003852590408577812535049335652212448474376457015077047529818315877549614859586475504070051201054704954654093482056493092930700787890579346065916834434739980791402216175555075896066616519150164831990626727591876115821219941268309678240872298029611746575376322733311657394502859852213595389607239431585120943268774679785316133478171225719729917877009624611286702010936951705160870997184123775488592130586606070277173392647225589257616518666852404878425355285270687131724258281902727717116041282358028398978152480549468694659695121115046850718180640407034795656480263573773381753855724693739080045739160297875306923958599742379878734638341856117533253251168244471273520476474579680250862738227337561115160603373096699944163
n = p * q
m = pow(c, d, n)

# to get the flag
# required python2
# print("%0512x" % m).decode("hex")
