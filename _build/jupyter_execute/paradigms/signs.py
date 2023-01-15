#!/usr/bin/env python
# coding: utf-8

# # Signs
# 
# | MZL   | Sign                      | Sign's Nmae | Phonetic Value |  Logogram |
# | :---  | ------------------------- | ----------- | -------------- | --------- |
# | 1	    | <font size="11">𒀸</font>  | AŠ          |*aš, rum*       |
# | 3	    | <font size="11">𒄬</font>  | HAL         | *hal*         |
# | 14	| <font size="11">𒁀</font> | BA         |*ba*            |
# | 15	| <font size="11">𒍪</font> | ZU          | *zu, su₂, ṣu₂* | ZU = *edûm* "to know", *lamādum* "learn"|
# | 16	| <font size="11">𒋢</font> | SU         | *su*           | KUŠ = *maškum* "skin, leather"|
# | 10	| <font size="11">𒀭</font> | AN          | *an*           | AN = *Anum*, *šamû* "heaven", DINGIR = *ilum* "Gott" determinative ᵈ |
# | 24	| <font size="11">𒅗</font> | KA         | *ka*           | (KA = *pûm* "mouth", DUG₄/DU₁₁  = *qabûm*, "to say", INIM = *awātum* "word", ZU₂ = *šinnum* "teeth")|
# | 71	| <font size="11">𒌷</font> | URU        | *ri₂, re₂*      | URU = *ālum* "cuty"|
# | 18	| <font size="11">𒀴</font> | ARAD        | *ir₃, er₃*     | NITA₂ = *zikarum* "man" (IR₃= *wardum*)
# | 19	| <font size="11">𒀵</font> | ARAD₂, (= ARAD×KUR) |(only until OB!)| ARAD₂, IR₁₁ = *wardum* "slave"|
# | 89	| <font size="11">𒆷</font> | LA           | *la*          |
# | 91    | <font size="11">𒈤</font> | MAH         | *mah*          |
# | 86	| <font size="11">𒌅</font> | TU          | *tu, ṭu₂*      |
# | 85    | <font size="11">𒇷</font> | LI          | *li, le*       |
# | 98	| <font size="11">𒈬</font> | MU           | *mu*           | (MU = *šumum* "name", MU = *šattum* "year")|
# | 111	| <font size="11">𒊒</font> | RU            | *ru*          |
# | 113	| <font size="11">𒁁</font> | BE            | *be, bad/t/ṭ* |
# | 110	| <font size="11">𒈾</font> | NA           | *na*           |
# | 118	| <font size="11">𒋾</font> | TI             | *ti, ṭi₃*     |
# | 112	| <font size="11">𒉡</font> | NU             | *nu*          |
# | 132	| <font size="11">𒄷</font> | HU            | *hu*          | MUŠEN = *iṣṣūrum* "bird"|
# | 136	| <font size="11">𒅅</font> | IG           | *ig, ik, iq*, *eg, ek, eq*| IG = *daltum*  "door"; GAL₂ = *bašûm* "to be""|
# | 140	| <font size="11">𒍣</font> | ZI            | *zi, si₂, ṣi₂, ze, se₂, ṣe₂* |
# | 141	| <font size="11">𒄀</font> | GI            | *gi, ge*       |GI = *qanûm* "reed, cane"|
# | 142	| <font size="11">𒊑</font> | RI            | *ri, re* (*dal, tal, ṭal*) | 
# | 167   | <font size="11">𒁴</font> | TIM            | *tim, dim*    |
# | 126	| <font size="11">𒀝</font> | AG             | *ag, ak, aq* |
# | 164	| <font size="11">𒂗</font> | EN             | *en*          | EN = *bēlum* "lord", ᵈEN.ZU = ᵈ*Suen*, ᵈ*Sîn* (Mondgott) ᵈEN.LIL₂ = ᵈ*Ellil*"|
# | 181	| <font size="11">𒋛</font> | SI             | *si, se*      |
# | 209	| <font size="11">𒋰</font> | TAB            | *tab, tap*     |
# | 221	| <font size="11">𒋳</font> | TAG            | *šum* (*tag, tak, taq*)|
# | 223	| <font size="11">𒀊</font> | AB             | *ab, ap*      |
# | 296   | <font size="11">𒊌</font> | UG             | *ug, uk, uq* |
# | 297   | <font size="11">𒊍</font> | AZ             | *as, az, aṣ* |
# | 222	| <font size="11">𒆍</font> | KA₂            | KA₂ = *bābum* "gate, door" |
# | 238	| <font size="11">𒌝</font> | UM             | *um*          |
# | 248	| <font size="11">𒋫</font> | TA             | *ta, ṭa₂*     |
# | 252	| <font size="11">𒄿</font> | I               | *i*          |
# | 260	| <font size="11">𒅀</font> | IA             | *ia*          |
# | 255	| <font size="11">𒌉</font> | TUR             | DUMU = *mārum* "son", TUR = *ṣehrum* "small"|
# | 258	| <font size="11">𒀜</font> | AD             | *ad, at, aṭ* | (AD = *abum* "father")
# | 259	| <font size="11">𒍢</font> | ZE₂            | *ṣi, ṣe, zi₂, ze₂* |
# | 261   | <font size="11">𒅔</font> | IN            | *in*  |
# | 266   | <font size="11">𒈗</font> | LUGAL          | LUGAL = *šarrum* "king"|
# | 309	| <font size="11">𒄠</font> | AM             | *am*  |
# | 313   | <font size="11">𒉈</font> | NE            | *ne, bil, pil, bi₂,* *ṭe₃* | 
# | 341   | <font size="11">𒌫</font> | UR₂           | *ur₂*  |
# | 348   | <font size="11">𒅋</font> | IL            | *il*   |
# | 350	| <font size="11">𒁺</font> | DU             | *du, ṭu₃* |
# | 354	| <font size="11">𒌈</font> | TUM            | *tum, dum, ṭum* |
# | 381	| <font size="11">𒍑</font> | UŠ             | *uš, us₂* | NITA = *zik(a)rum* "male, virile"|
# | 357	| <font size="11">𒅖</font> | IŠ             | *iš,* (*mil*) |
# | 358	| <font size="11">𒁉</font> | BI             | *bi, be₂, pi₂, pe₂* | KAŠ =  *šikarum* "beer"|
# | 380	| <font size="11">𒉌</font> | NI             | *ni, ne₂, i₃, li₂, zal* | I₃ = *šamnum* "oil"|
# | 437	| <font size="11">𒅕</font> | IR             | *ir, er *|
# | 464	| <font size="11">𒉺</font> | PA             | *pa*  | UGULA = *waklum* "overseer, inspector"|
# | 469	| <font size="11">𒄑</font> | GIŠ            | *iz, is, iṣ, ez, es, eṣ* | GIŠ = *iṣum* "tree; wood", Det. <sup>giš</sup> vor trees and wooden objects |
# | 472	| <font size="11">𒄞</font> |GUD             | *gud, gu₄*      | GU4/GUD = *alpum* "bull, ox" |
# | 474   | <font size="11">𒀠</font> | AL            | *al*  |
# | 483	| <font size="11">𒈥</font> | MAR            | *mar* |
# | 498	| <font size="11">𒂊</font> | E              | *e*  |
# | 490	| <font size="11">𒌑</font> | U₂             | *u₂*, (*šam*) | U₂ = *šammum* "grass, herb", KUŠ₃ = *ammatum* "forearm; cubit"|
# | 491	| <font size="11">𒂵</font> | GA             | *ga, qa₂* |(GA = *šizbum* "milk")|
# | 496	| <font size="11">𒆗</font> |KAL             | *dan, kal, rab*   |KALA(G) = *dannum* "mighty", KALAM = *mātum* land |
# | 495	| <font size="11">𒂍</font> | E₂             | *bid/t/ṭ*   | E₂ = *bītum* "house", E₂.GAL = *ekallum* "palace"|
# | 504	| <font size="11">𒌒</font> | UB             | *ub, up, ar₂* |
# | 511	| <font size="11">𒊏</font> | RA             | *ra*  |
# | 514	| <font size="11">𒇽</font> | LU₂            | | LU₂ = *awīlum* "man"|
# | 541	| <font size="11">𒊬</font> |SAR             | *sar, šar*    |
# | 543	| <font size="11">𒃼</font> | GAR₃            | *qar, gar₃, kar₃* |
# | 548	| <font size="11">𒀾</font> | AŠ₂             | *aš₂,* (*as₂, az₂, aṣ₂*) |
# | 560	| <font size="11">𒀉</font> | A₂             | *id, it, iṭ, ed, et, eṭ* | A₂ = *idum* "side" 
# | 561	| <font size="11">𒁕</font> | DA             | *da, ṭa*  |
# | 552	| <font size="11">𒈠</font> | MA             | *ma*      | MA.NA = *manûm* "mina"|
# | 553	| <font size="11">𒃲</font> |GAL             | *gal*, (*qal*) | GAL = *rabûm* "big" |
# | 566	| <font size="11">𒊭</font> | ŠA             | *ša*      |
# | 567	| <font size="11">𒋗</font> | ŠU             | *šu*      | ŠU = *qātum* "hand"|
# | 670   | <font size="11">𒀹𒁯</font> | *iš₈-tar₂* (*ištar₂*) | = GN Ištar, also with "ᵈ"|
# | 578	| <font size="11">𒆳</font> | KUR             | KUR = *mātum* "land"|
# | 579	| <font size="11">𒊺</font> | ŠE              | *še*     | ŠE = ŠE*-um* "barley; grain"|
# | 580	| <font size="11">𒁍</font> | BU             | *bu, pu* (*gid₂, qid₂, sir₂, šir₂*) |
# | 583   | <font size="11">𒊻</font> | UZ             | *uz, us, uṣ* |
# | 589	| <font size="11">𒋼</font> | TE             | *te, ṭe₄* |
# | 590	| <font size="11">𒀬</font> | KAR            | *kar*     |
# | 596	| <font size="11">𒌓</font> | UD              | *ud, ut, uṭ, tam, pir*   | UD, U₄ = *ūmum* "day", ᵈUTU = *Šamaš*, BABBAR = *peṣûm* "white""|
# | 598	| <font size="11">𒉿</font> | PI             | *wa/e/i/u, pi, pe*        |
# | 599	| <font size="11">𒊮</font> | ŠA₃            | *lib₃, ša₃*               | ŠA₃ = *libbum* "inner body, heart", cf. A.ŠA₃ |
# | 611   | <font size="11">𒌔</font> | UH₂            | *uh₂*                     |
# | 631	| <font size="11">𒄭</font> | HI               | *hi, he*                 | DUG₃/DU₁₀  = *ṭābum* "sweet", HI.A plural signs (after things) |
# | 636	| <font size="11">𒄴</font> | AH             | *ah, eh, ih, uh*          |
# | 641	| <font size="11">𒅎</font> | IM             | *im, em*                  | IM = *ṭīdum* "clay", *šārum* "wind", ᵈIŠKUR = Adad (weather god)|
# | 640	| <font size="11">𒄭𒁁</font> | KAM           | *kam, gam, qam₂*          | KAM after ordinals |
# | 681	| <font size="11">𒈪</font> | MI             | *mi, me₂, ṣil₂*           |
# | 686	| <font size="11">𒁶</font> | DIM₂           | *gim, gen₇*              | ŠIDIM = *itinnu* "builder" , GIM = *kīma* "like; when, as, that", DIM₂ = *banû* "build"
# | 690	| <font size="11">𒉏</font> | NIM            | *nim, num*                |
# | 693	| <font size="11">𒇴</font> | LAM            | *lam*                     |
# | 695	| <font size="11">𒀫</font> | AMAR           | *ṣur*                     | ᵈAMAR.UTU = Marduk    |
# | 698	| <font size="11">𒌌</font> | UL             | *ul*                      |
# | 724	| <font size="11">𒅆</font> | IGI            | *ši, lim, lem*            | IGI = *īnum* "eye", *pānum* "front"|
# | 726   | <font size="11">𒅈</font> | AR            | *ar*                       |
# | 731   | <font size="11">𒅇</font> | U₃            | *u₃*                       |
# | 736	| <font size="11">𒁲</font> | DI             | *di, ṭi, de, ṭe*          | SILIM = *šulmum* "completeness; well-being"|
# | 737	| <font size="11">𒆠</font> | KI             | *ki, ke, qi₂, qe₂*        | KI = *erṣetum* "earth", *ašrum* "place, site", Det. <sup>ki</sup> (after place names)|
# | 745	| <font size="11">𒆬</font> | KUG              | *kug, ku₃*               | KU₃ = *ellum* "pure, clean", KU₃.BABBAR = *kaspum* "silver", KU₃.SIG₁₇(GI) = *hurāṣum* "gold""|
# | 711	| <font size="11">𒌍</font> | EŠ              | *eš*, (*Sin*)             | (ᵈ)XXX/(ᵈ)30 = (ᵈ)Sîn (moon god)|
# | 753	| <font size="11">𒈨</font> | ME              | *me*                     | ME = plural sign (cf. MEŠ)|
# | 754	| <font size="11">𒈨𒌍</font> |MEŠ            | *meš*                     | MEŠ = plural sign; transliteration also <sup>pl</sup> or <sup>meš</sup>)|
# | 807	| <font size="11">𒅁</font> | IB             | *ib, ip, eb, ep*          |
# | 808	| <font size="11">𒆪</font> | KU             | *ku, qu₂*                 |
# | 812	| <font size="11">𒇻</font> | LU             | *lu*                      | UDU = *immerum* "sheep"|
# | 883	| <font size="11">𒊩</font> | MUNUS           | *sal,* (*šal*)           | MUNUS (also MI₂) = *sinništum* "woman"|
# | 884	| <font size="11">𒍮</font> | ZUM            | *zum, ṣum, ṣu, sum₂*      |
# | 887   | <font size="11">𒊩𒈠</font> | NIN           | *nin*                     | NIN = *bēltum* "lady"|
# | 889   | <font size="11">𒁮</font> | DAM            | *dam, ṭam*                | DAM.GAR₃ = *tamkārum* "merchant"|
# | 890	| <font size="11">𒊩𒆳</font> | GEME₂         | *ge₁₂*                      | GEME₂ = *amtum* "maid, female slave"|
# | 899	| <font size="11">𒂖</font> | EL             | *el, il₅*                 | SIKIL = ellum "rein"|
# | 900	| <font size="11">𒈝</font> | LUM            | *lum, num₂* (*hum, gum*)  | 
# | 828	| <font size="11">𒌨</font> | UR             | *ur, lig/lik/liq, taš*    |
# | 839	| <font size="11">𒀀</font> | A                | *a, a-a* (= *ajja*)      | A.(MEŠ) = *mû* "water", A.ŠA₃ = *eqlum* "field"|
# | 851	| <font size="11">𒍝</font> | ZA              | *za, sa₃, ṣa*             |
# | 856	| <font size="11">𒄩</font> | HA              | *ha                       | KU₆  = *nūnum* "fish"
# | 836	| <font size="11">𒂆</font> | GIN₂           | gin₂                      | GIN₂ = *šiqlum* "shekel"
