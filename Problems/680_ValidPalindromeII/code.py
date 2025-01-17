from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        validFlag: bool = True # only change to true if palindrome is found
        invalidStrings: dict[str, bool] = {}

        '''
        Try using just a while loop. If they don't match, try the next index for l.
        If that doesn't match, push l back and try the next index for r. If they both don't 
        match, it's not a palindrome. Track the number of skips. If it's greater than 1, 
        the algorithm should return false.
        '''

        l: int = 0
        r: int = len(s) - 1
        skipAlternateRoute: List[int] = []
        indexesReset: bool = False
        skipCount: int = 0

        print("---------------------------------------------------")
        while l <= r:
            if skipCount > 1 and indexesReset == False:
                skipCount -= 1
                # reset indexes to try other route
                # print("[{}] Resetting indexes l: {} -> {} r: {} -> {}".format(skipCount, l, skipAlternateRoute[0], r, skipAlternateRoute[1]))
                l = skipAlternateRoute[0]
                r = skipAlternateRoute[1]
                indexesReset = True
                continue
            elif skipCount > 1 and indexesReset == True:
                return False
            
            # print("[{}] Checking l[{}]: {} and r[{}]: {}".format(skipCount, l, s[l], r, s[r]))
            
            if s[l] != s[r]:
                # try increasing l first
                if s[l+1] == s[r]: # abcdefgci l=b, l+1=c, l+2=d, r=c, r+1=g
                    # print("[{}] Checking l+1[{}]: {} and r[{}]: {}".format(skipCount, l+1, s[l+1], r, s[r]))
                    skipCount += 1
                    skipAlternateRoute = [l+1, r-2]
                    l += 2
                    r -= 1
                    continue
                elif s[r-1] == s[l]: # def
                    # print("[{}] Checking s[{}]: {} and r-1[{}]: {}".format(skipCount, l, s[l], r-1, s[r-1]))
                    skipCount += 1
                    skipAlternateRoute = [l+2, r-1]
                    l += 1
                    r -= 2
                    continue
                else:
                    return False
                        
                
            l += 1
            r -= 1
                
        if skipCount < 2:
            return True
        else:
            return False
                

                # then try increasing r

        # for i in range(len(s)):
        #     l: int = 0
        #     r: int = len(s) - 2
        #     tempString: str = s[:i] + s[i+1:]
        #     tempStringIsPalindome: bool = True
        #     # print("Testing: {} ...".format(tempString))

        #     while l <= r:
        #         if tempString in invalidStrings:
        #             tempStringIsPalindome = False
        #             break

        #         if tempString[l].isalnum() == False:
        #             l += 1
        #             continue

        #         if tempString[r].isalnum() == False:
        #             r -= 1
        #             continue

        #         if str.lower(tempString[l]) != str.lower(tempString[r]):
        #             tempStringIsPalindome = False
        #             invalidStrings[tempString] = False
        #             break
                
        #         l += 1
        #         r -= 1

        #     print(len(invalidStrings.keys()))

        #     if tempStringIsPalindome == True:
        #         return True


        return validFlag
    
s = Solution()
# true
print(s.validPalindrome("aba"))
# true
print(s.validPalindrome("abca"))
# false
print(s.validPalindrome("abc"))
# true
print(s.validPalindrome("lyjcyxwvartqrbmqpddmushqkalgywgsialtbfysqkmbobaujedobhsmauazbhdsilqkkjuzoqimfqwmfoqeiovstodqqsiyjbkbtshhjsalmbxqaacjmnijyfrwtvqfischpkcrwtozbiwrfvuggqdcinfhhyohizalbzjppztabikdnznbhyolevzutydrbxirjzltcpdglzjtyblflqjkolxymkvdfyqrfbhgwqsnzhuqxfcttlwjigbtennfvbxplzmxdheiaulyhzztwbhtsemruznnqzborldvdfpfjyraxuhceuklfxilxtljyytriyhezhjklykkkijjzquapufkrlsiovnkozlxkjnahpiulsrmykcqavrlriknuoxtdzpzddukfqmyvppndgjvcbuaskqsppsxbhchmtgxqklivlqbmscowxndgxcubnvymipsxohtrmtjyexbmslhhmqklrfvrdimcxykvgvkfocigjimkafxeevdetqjscgqewhaukixtxiivzsklpzcscxgzdlfqjmpkxegtbejckitubhugylihvoqximedxuujhsyzclyyrnvzptfrdhdmocxhgpwjxpxkbougrwwwhkfddyxnvawdirsrydkqstalyqpokivlcwxtmviakkwaqmwguasmmujfrxbhmckhgfwcsghuxcprqawxggdfpegfvolhenffubhsprjbpzkoxzksdyrajrtzmqwvcjvdzthzhwrmdqdmbnqxqibnfwpqbouophshrrbytfaroltdsfrmrnzrtlxskwfbxmieqyrlnpluohqafnfpfgrwjmmnzrgzdlzannsjxvoaxanzlldbrivsesecrdfttvaxsplisqjrsrklmfbtfejpftfxkdgvvdowlpwcafjzxsiwwgbtiphyrqbnjhyrioyaxucxndjwjhjjozdplbljuoizgxwzrydoptnwfminobnwhnearuhhommwxfnzvymbupowhsvvxsyxfldgwheacxksspkeiyrdlwrbktiwuydxqkfpdbsnggwuyfyigpbakxohotqbidrmjsldrpklozbifpcyxismcefvdwxunahkfujenaknczawlcvdfeazizsfzunozorctpdrzczwwdwcdmfhjsmfwjfqihwslydaghcccxvbntdrxkzyohrpgxcjxixdhpkjzsrqwsquauoqdtprdqrfajaqtzyzpussttzfaepgmgjvjvoopvntctdrddsaammvgcehmprmtzumifgjbzvpzprlepczdmwwdrrtvwhhnjatzswboekiajtspxcjgcgviewevutoxvrybxknptsnuysvwccdfmrxjuvptyamcckubbdptpzgaysbzsztjzwtcloqeyvosgmbpfgzbcdouiqfffwfuiawkzkodgckjwkvyuitmqixrjehzdksniqpsrigosupxkkluoiimdzyyhxvsffbkkhdaaxfoiatzsrtbnpgqnrfbosaymnpwmihoctrypveiuxcwtbodtggqxgyhhwtyknhruyhclssxlcmcabshajvtxurrrykkyalhdhbdwvjjhsejlqvnctixnzvukalkphvlwvmcqjeytpwbahfscydpjgcoxjcniptpobbuqirmhcjcesdhgwllnzyjrriduyyaogpqyxuhcvsvrxpvupmbczimxfggplguslywqjhyjyckwjbycbyhyaanuatlezcoiampqwtcgtrssnuhrzhlmuuczbernacccvtcjkzwhrptmzdxquqjvmxqzrvkluhrjekknzmqogbhzhzduvtndyqojylugcqnbjomsyiipsfhiflcnjzgfzkgsdbtqsuzdzjiykxfdjnzgdvcppiqlfmxurhldpcuhxbqytoizqdenexbtsztisrzsokuktzsqvooysvuqwijuxqyzguqnszumukgawzyogkxvkjsjttsjgnaftbgjqdwkjbrpqylyemnqcdllndevrcpmiwsuiipzjnipjbxfkdffmthhlkpqewukaxgworxcfwmlhothsgvhvwgfnpdvsxclprpnsnaiorttjfpiiufgagfbmiffgeikdarhubuaezjuqvgksbeiajjffbztzopyhvjoieduxqodqghkigskimdabcyhlqxxyaemhpriklpqmlbjocmklswahpwgwgzdludqvpiegwguznpclsucuqkvsawdbttfowetonjfjqnjvzdhfuqfpjmxynimnfxuygsztbortaxhxxwyzjwqszresyotfqdrcmwhrdsuelbxobqtnukazqikeijaispuhqpquexbwycxbzvbdbzczhdbrksibjikghthjjswuionrmarutnxqoserlkzioyssxpqhlqwztfvslsoaidgrahfvlvawegcajryevlqhapdfwyllaljqpzgqhjkozturndcksqieawyeazmmdxjcbfdobylfrudnxhlqvsmxyyiehauwvoqfpcuamknhbxgznwgnpggzkolpgfrcouxakuxyqbnzfwiiwdpqognpvksrfwajycyikjhharxlvummqjbduynuaghwvtdeqcbbexzmnyrzxorubfgcbzisaqnejyxxvaxrqxpfnyqyiqdwjaqobzthoxxvcjuwygbqjpaaverwmqmwcqkwrygapuiozsbkyeltsfbqylmbjeirpcmlwupdssmxvwadjxuwjoeeurakjeoqqosojuudzmclnskioxburoijftgbroznqplgddejuyrwcptkoyuqlecohsaftcgkorupqwvmadhemtgbqxwdcnoiobhtuffohsirgybmattgqkxdrtlssddwomxlxrpmsnhygfsyrjioxuurbkupzljrkgkytvzwpjvntqbzowctwjuhvsrzercfblafwcincdfucuwuynvwsxnxqdoqgskeujobuevkcsllfzcaypzfgrtzisouslkaohmoqzcmdzdrjcnasnazpaugxpmtaqewqxqwmqlqrmyyigqrlzczogzfaqnrgisnldfvhjvdpdlgjltsnfxopcluaqlplrdurnkffyfbyuaqwybeaebmhtlnordnvuuyjiukyknpxvamrqqqvlwzgouilfhhzekvgkqmsqhdqikddkwemlqfydfvkyicbmgnwxccmnbzphghoolhazupawvdwplphojedprkpmstcttuaqhxlxhyfziqwvnigwdmtuwutpfqbjmsqjzhomqltlrkavlvueusktbmmouqckzkejcyerrhjbodozzhdxtglaoptpchhdjnoyvtpdsumbrbppchssqbzbqqcsedqtqwhndxrgmyrhyfgzwkbgamfiqcmbcqqclrjvonrsobujtaoridmcrhowykivrhoywffjwpcohahixfwcqrgocsokorujsnveplxqksjytomxmxrlmtzbrjgmnmfzsziosxzhpkygfueazbfhypxqbssthyluexvwvprrickierqmatzimsvrppiibhiwfapptkwbcsjtzbsboabfvhyokdqsigfslwppaabuevsqqamshzzczhyipgiuitoluzgqwwcxnwquwumctqctkxvniathxwulblviimspakbsblgmfgnvxbnllpavkkckfjjlzolbizbigdbksujdsydphyuvzdlwpopwhfgajwmjubtufnbjakoftqftxrawpupkhmihoxqfgzxxdboyqgvolgecagnexhuuieizhlhxsrqefeikqcluzqzypsmkgkmzdrpsilgudqvbbjceltfdbamirhykijczepbrswgmdbxujcbfotwmnjmdhualecpyzusyeetlroakadpxppupmhsmsppniaauwqdjznznqkbakgtyckoazajjgypvzenxapjdgasfjfuqejedtdkvsrtgvmfkwxgwywpbnwffjqkjrrvufvkysgdukmpzqsbflnymgzxktqucxsvhzzrxnjydqblluvegrplvokhxpordaokurylggxvvbiiszjnuqjreecvgegqkohxyvmzypavllhbsstdemtlzmdqhlwkgcyqnuedntoztrwftvldtkuvwmhrklmxyrcynjgcrizpccvevkwjngmwkyorortkaaiajhomskokyawycbqquqbvpzppxbemjnttcqiblschxiulckqhufeibxrblzemrmjrfnbeqadwaytsobfvzflyasevaygvywvvrcidowqfscgynwuesswbbeecdclxwfdcopctdcbzftwmqkdsfkgjmwciiymzhlmfyaqopxbpikxltckgvitxnxbfitzuusqjnhlynlgptejpgnwebjcsmluwrkmsotihynyuhmyzytzcszmfxwgsbyocxvovhigjdpnbiuoqpzxanqzpbosxagibrgkgexeqawxnmmcjwawzgmavjffautdzpxgyxurupaqcweqsvzynqlnjoevagatcrmfeokzpiijvgebridzpmwcfhnwclmggxdsffifmkwiondafvnenolwnezwyrhllslogyjcbtpbecikylqivhbrkistbpdfrqhldylbuqfifcbihnacybphorcbyiivhvttswzzfyqygcdqhnptbeystejhuiyvisgjerevxdgkmksicqeyniilobpxivmfhzilqjyekihpuzrferwodnhoxymzfeyphzmzwjuvfqfetxwovkdmwutckxlsrylqmtsvriaiuhnshiuhcvzyxxatmhazrytobddzfxbicwxxspwnsbgpdanmiepznyvrinotebesqtgwtseanobufqlqbzqlwzqvkonlnscoqofdcslyauaszvlstlnhzfjqvagxzntzjymlyofoleqphtvukpniawecbfltyxdtywwgigxsacfcydgkxolhoswbmbjistxsgdlodufbevixjjxivebfudoldgsxtsijbmbwsohloxkgdycfcasxgigwwytdxytlfbcewainpkuvthpqelofoylmyjztnzxgavqjfzhnltslvzsauaylscdfoqocsnlnokvqzwlqzbqlqfubonaestwgtqsebetonirvynzpeimnadpgbsnwpsxxwcibxfzddbotyrzahmtaxxyzvchuihsnhuiairvstmqlyrslxkctuwmdkvowxtefqfvujwzmzhpyefzmyxohndowrefrzuphikeyjqlizhfmvixpboliinyeqciskmkgdxverejgsivyiuhjetsyebtpnhqdcgyqyfzzwsttvhviiybcrohpbycanhibcfifqublydlhqrfdpbtsikrbhviqlykicebptbcjygolsllhrywzenwlonenvfadnoiwkmfiffsdxggmlcwnhfcwmpzdirbegvjiipzkoefmrctagaveojnlqnyvsqewcqapuruxygxpzdtuaffjvamgzwawjcmmnxwaqexegkgrbigaxsobpzqnaxzpqouibnpdjgihvovxcoybsgwxfmzscztyzymhuynyhitosmkrwulmscjbewngpjetpglnylhnjqsuuztifbxnxtivgkctlxkipbxpoqayfmlhzmyiicwmjgkfsdkqmwtfzbcdtcpocdfwxlcdceebbwsseuwnygcsfqwodicrvvwyvgyavesaylfzvfbostyawdaqebnfrjmrmezlbrxbiefuhqkcluixhcslbiqcttnjmebxppzpvbquqqbcywaykoksmohjaiaaktroroykwmgnjwkvevccpzircgjnycryxmlkrhmwvuktdlvtfwrtzotndeunqycgkwlhqdmzltmedtssbhllvapyzmvyxhokqgegvceerjqunjzsiibvvxgglyrukoadropxhkovlprgevullbqdyjnxrzzhvsxcuqtkxzgmynlfbsqzpmkudgsykvfuvrrjkqjffwnbpwywgxwkfmvgtrsvkdtdejequfjfsagdjpaxnezkvpygjjazaokcytgkabkqnznzjdqwuaainppsmshmpuppxpdakaorlteeysuzypcelauhdmjnmwtofbcjuxbdmgwsrbpezcjikyhrimabdftlecjbbvqduglisprdzmkgkmspyzqzulcqkiefeqrsxhlhzieiuuhxengaceglovgqyobdxxzgfqxohimhkpupwarxtfqtfokajbnfutbujmwjagfhwpopwldzvuyhpdysdjuskbdgibziblozljjfkckkvapllnbxvngfmglbsbkapsmiivlbluwxhtainvxktcqtcmuwuqwnxcwwqgzulotiuigpiyhzczzhsmaqqsveubaappwlsfgisqdkoyhvfbaobsbztjscbwktppafwihbiipprvsmiztamqreikcirrpvwvxeulyhtssbqxpyhfbzaeufgykphzxsoizszfmnmgjrbztmlrxmxmotyjskqxlpevnsjurokoscogrqcwfxihahocpwjffwyohrvikywohrcmdiroatjubosrnovjrlcqqcbmcqifmagbkwzgfyhrymgrxdnhwqtqdescqqbzbqsshcppbrbmusdptvyonjdhhcptpoalgtxdhzzodobjhrreycjekzkcquommbtksueuvlvakrltlqmohzjqsmjbqfptuwutmdwginvwqizfyhxlxhqauttctsmpkrpdejohplpwdvwapuzahloohghpzbnmccxwngmbciykvfdyfqlmewkddkiqdhqsmqkgvkezhhfliuogzwlvqqqrmavxpnkykuijyuuvndronlthmbeaebywqauybfyffknrudrlplqaulcpoxfnstljgldpdvjhvfdlnsigrnqafzgozczlrqgiyymrqlqmwqxqweqatmpxguapzansancjrdzdmczqomhoaklsuosiztrgfzpyaczfllsckveubojueksgqodqxnxswvnyuwucufdcnicwfalbfcrezrsvhujwtcwozbqtnvjpwzvtykgkrjlzpukbruuxoijrysfgyhnsmprxlxmowddssltrdxkqgttambygrishoffuthboioncdwxqbgtmehdamvwqpurokgctfashocelquyoktpcwryujeddglpqnzorbgtfjiorubxoiksnlcmzduujosoqqoejkarueeojwuxjdawvxmssdpuwlmcpriejbmlyqbfstleykbszoiupagyrwkqcwmqmwrevaapjqbgywujcvxxohtzboqajwdqiyqynfpxqrxavxxyjenqasizbcgfburoxzrynmzxebbcqedtvwhgaunyudbjqmmuvlxrahhjkiycyjawfrskvpngoqpdwiiwfznbqyxukaxuocrfgplokzggpngwnzgxbhnkmaucpfqovwuaheiyyxmsvqlhxndurflybodfbcjxdmmzaeywaeiqskcdnrutzokjhqgzpqjlallywfdpahqlveyrjacgewavlvfhargdiaoslsvftzwqlhqpxssyoizklresoqxnturamrnoiuwsjjhthgkijbiskrbdhzczbdbvzbxcywbxeuqpqhupsiajiekiqzakuntqboxbleusdrhwmcrdqftoyserzsqwjzywxxhxatrobtzsgyuxfnminyxmjpfqufhdzvjnqjfjnotewofttbdwasvkqucuslcpnzugwgeipvqduldzgwgwphawslkmcojblmqplkirphmeayxxqlhycbadmiksgikhgqdoqxudeiojvhypoztzbffjjaiebskgvqujzeaubuhradkiegffimbfgagfuiipfjttroiansnprplcxsvdpnfgwvhvgshtohlmwfcxrowgxakuweqpklhhtmffdkfxbjpinjzpiiuswimpcrvednlldcqnmeylyqprbjkwdqjgbtfangjsttjsjkvxkgoyzwagkumuzsnqugzyqxujiwquvsyoovqsztkukoszrsitzstbxenedqziotyqbxhucpdlhruxmflqippcvdgznjdfxkyijzdzusqtbdsgkzfgzjnclfihfspiiysmojbnqcgulyjoqydntvudzhzhbgoqmznkkejrhulkvrzqxmvjquqxdzmtprhwzkjctvcccanrebzcuumlhzrhunssrtgctwqpmaioczeltaunaayhybcybjwkcyjyhjqwylsuglpggfxmizcbmpuvpxrvsvchuxyqpgoayyudirrjyznllwghdsecjchmriqubboptpincjxocgjpdycsfhabwptyejqcmvwlvhpklakuvznxitcnvqljeshjjvwdbhdhlaykkyrrruxtvjahsbacmclxsslchyurhnkytwhhygxqggtdobtwcxuievpyrtcohimwpnmyasobfrnqgpnbtrsztaiofxaadhkkbffsvxhyyzdmiioulkkxpusogirspqinskdzhejrxiqmtiuyvkwjkcgdokzkwaiufwfffqiuodcbzgfpbmgsovyeqolctwzjtzszbsyagzptpdbbukccmaytpvujxrmfdccwvsyunstpnkxbyrvxotuveweivgcgjcxpstjaikeobwsztajnhhwvtrrdwwmdzcpelrpzpvzbjgfimuztmrpmhecgvmmaasddrdtctnvpoovjvjgmgpeafzttssupzyztqajafrqdrptdqouauqswqrszjkphdxixjcxgprhoyzkxrdtnbvxccchgadylswhiqfjwfmsjhfmdcwdwwzczrdptcrozonuzfszizaefdvclwazcnkanejufkhanuxwdvfecmsixycpfibzolkprdlsjmrdibqtohoxkabpgiyfyuwggnsbdpfkqxdyuwitkbrwldryiekpsskxcaehwgdlfxysxvvshwopubmyvznfxwmmohhuraenhwnbonimfwntpodyrzwxgzioujlblpdzojjhjwjdnxcuxayoiryhjnbqryhpitbgwwisxzjfacwplwodvvgdkxftfpjeftbfmlkrsrjqsilpsxavttfdrcesesvirbdllznaxaovxjsnnazldzgrznmmjwrgfpfnfaqhoulpnlryqeimxbfwksxltrznrmrfsdtloraftybrrhshpouobqpwfnbiqxqnbmdqdmrwhzhtzdvjcvwqmztrjarydskzxokzpbjrpshbuffnehlovfgepfdggxwaqrpcxuhgscwfghkcmhbxrfjummsaugwmqawkkaivmtxwclvikopqylatsqkdyrsridwavnxyddfkhwwwrguobkxpxjwpghxcomdhdrftpzvnryylczyshjuuxdemixqovhilyguhbutikcjebtgexkpmjqfldzgxcsczplkszviixtxikuahweqgcsjqtedveexfakmijgicofkvgvkyxcmidrvfrlkqmhhlsmbxeyjtmrthoxspimyvnbucxgdnxwocsmbqlvilkqxgtmhchbxsppsqksaubcvjgdnppvymqfkuddzpzdtxounkirlrvaqckymrsluiphanjkxlzoknvoislrkfupauqzjjikkkylkjhzehyirtyyjltxlixflkuechuxaryjfpfdvdlrobzqnnzurmesthbwtzzhyluaiehdxmzlpxbvfnnetbgijwlttcfxquhznsqwghbfrqyfdvkmyxlokjqlflbytjzlgdpctlzjrixbrdytuzveloyhbnzndkibatzppjzblazihoyhhfnicdqgguvfrwibzotwrckphcsifqvtwrfyjinmjcaaqxbmlasjhhstbkbjyisqqdotsvoieqofmwqfmiqozujkkqlisdhbzauamshbodejuabobmkqsyfbtlaisgwyglakqhsumddpqmbrqtravwxycjyl"))
# false
print(s.validPalindrome("eeccccbebaeeabebccceea"))
# false
print(s.validPalindrome("aabdeenddbaagbddeedbaa"))
# true
print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))