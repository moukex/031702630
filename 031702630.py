#-*- coding: utf-8 -*-
import re
import json
address=input()
if address.endswith("."):
    address=address[:-1]
level=int(address[:1])
address=address[2:]
def get_Answer(adate:str):
    jsonstr='{"台湾省":["台北市","新北市","桃园市","台中市","台南市","高雄市","基隆市","新竹市","嘉义市"],"澳门特别行政区":["花地玛堂区","圣安多尼堂区","大堂区","望德堂区","风顺堂区","嘉模堂区","圣方济各堂区"],"香港特别行政区":["九龙城区","北区","中西区","东区","南区","湾仔区","观塘区","深水埗区","黄大仙区","油尖旺区","离岛区","葵青区","西贡区","西贡区","沙田区","大埔区","荃湾区","屯门区","元朗区"],"北京市":["东城区","西城区","朝阳区","丰台区","石景山区","海淀区","门头沟区","房山区","通州区","顺义区","昌平区","大兴区","怀柔区","平谷区","密云区","延庆区"],"天津市":["和平区","河东区","河西区","南开区","河北区","红桥区","东丽区","西青区","津南区","北辰区","武清区","宝坻区","滨海新区","宁河区","静海区","蓟州区"],"河北省":["石家庄市","唐山市","秦皇岛市","邯郸市","邢台市","保定市","张家口市","承德市","沧州市","廊坊市","衡水市"],"山西省":["太原市","大同市","阳泉市","长治市","晋城市","朔州市","晋中市","运城市","忻州市","临汾市","吕梁市"],"内蒙古自治区":["呼和浩特市","包头市","乌海市","赤峰市","通辽市","鄂尔多斯市","呼伦贝尔市","巴彦淖尔市","乌兰察布市","兴安盟","锡林郭勒盟","阿拉善盟"],"辽宁省":["沈阳市","大连市","鞍山市","抚顺市","本溪市","丹东市","锦州市","营口市","阜新市","辽阳市","盘锦市","铁岭市","朝阳市","葫芦岛市"],"吉林省":["长春市","吉林市","四平市","辽源市","通化市","白山市","松原市","白城市","延边朝鲜族自治州"],"黑龙江省":["哈尔滨市","齐齐哈尔市","鸡西市","鹤岗市","双鸭山市","大庆市","伊春市","佳木斯市","七台河市","牡丹江市","黑河市","绥化市","大兴安岭地区"],"上海市":["黄浦区","徐汇区","长宁区","静安区","普陀区","虹口区","杨浦区","闵行区","宝山区","嘉定区","浦东新区","金山区","松江区","青浦区","奉贤区","崇明区"],"江苏省":["南京市","无锡市","徐州市","常州市","苏州市","南通市","连云港市","淮安市","盐城市","扬州市","镇江市","泰州市","宿迁市"],"浙江省":["杭州市","宁波市","温州市","嘉兴市","湖州市","绍兴市","金华市","衢州市","舟山市","台州市","丽水市"],"安徽省":["合肥市","芜湖市","蚌埠市","淮南市","马鞍山市","淮北市","铜陵市","安庆市","黄山市","滁州市","阜阳市","宿州市","六安市","亳州市","池州市","宣城市"],"福建省":["福州市","厦门市","莆田市","三明市","泉州市","漳州市","南平市","龙岩市","宁德市"],"江西省":["南昌市","景德镇市","萍乡市","九江市","新余市","鹰潭市","赣州市","吉安市","宜春市","抚州市","上饶市"],"山东省":["济南市","青岛市","淄博市","枣庄市","东营市","烟台市","潍坊市","济宁市","泰安市","威海市","日照市","莱芜市","临沂市","德州市","聊城市","滨州市","菏泽市"],"河南省":["郑州市","开封市","洛阳市","平顶山市","安阳市","鹤壁市","新乡市","焦作市","濮阳市","许昌市","漯河市","三门峡市","南阳市","商丘市","信阳市","周口市","驻马店市","济源市"],"湖北省":["武汉市","黄石市","十堰市","宜昌市","襄阳市","鄂州市","荆门市","孝感市","荆州市","黄冈市","咸宁市","随州市","恩施土家族苗族自治州","仙桃市","潜江市","天门市","神农架林区"],"湖南省":["长沙市","株洲市","湘潭市","衡阳市","邵阳市","岳阳市","常德市","张家界市","益阳市","郴州市","永州市","怀化市","娄底市","湘西土家族苗族自治州"],"广东省":["广州市","韶关市","深圳市","珠海市","汕头市","佛山市","江门市","湛江市","茂名市","肇庆市","惠州市","梅州市","汕尾市","河源市","阳江市","清远市","东莞市","中山市","潮州市","揭阳市","云浮市"],"广西壮族自治区":["南宁市","柳州市","桂林市","梧州市","北海市","防城港市","钦州市","贵港市","玉林市","百色市","贺州市","河池市","来宾市","崇左市"],"海南省":["海口市","三亚市","三沙市","儋州市","五指山市","琼海市","文昌市","万宁市","东方市","定安县","屯昌县","澄迈县","临高县","白沙黎族自治县","昌江黎族自治县","乐东黎族自治县","陵水黎族自治县","保亭黎族苗族自治县","琼中黎族苗族自治县"],"重庆市":["万州区","涪陵区","渝中区","大渡口区","江北区","沙坪坝区","九龙坡区","南岸区","北碚区","綦江区","大足区","渝北区","巴南区","黔江区","长寿区","江津区","合川区","永川区","南川区","璧山区","铜梁区","潼南区","荣昌区","开州区","梁平区","武隆区","城口县","丰都县","垫江县","忠县","云阳县","奉节县","巫山县","巫溪县","石柱土家族自治县","秀山土家族苗族自治县","酉阳土家族苗族自治县","彭水苗族土家族自治县"],"四川省":["成都市","自贡市","攀枝花市","泸州市","德阳市","绵阳市","广元市","遂宁市","内江市","乐山市","南充市","眉山市","宜宾市","广安市","达州市","雅安市","巴中市","资阳市","阿坝藏族羌族自治州","甘孜藏族自治州","凉山彝族自治州"],"贵州省":["贵阳市","六盘水市","遵义市","安顺市","毕节市","铜仁市","黔西南布依族苗族自治州","黔东南苗族侗族自治州","黔南布依族苗族自治州"],"云南省":["昆明市","曲靖市","玉溪市","保山市","昭通市","丽江市","普洱市","临沧市","楚雄彝族自治州","红河哈尼族彝族自治州","文山壮族苗族自治州","西双版纳傣族自治州","大理白族自治州","德宏傣族景颇族自治州","怒江傈僳族自治州","迪庆藏族自治州"],"西藏自治区":["拉萨市","日喀则市","昌都市","林芝市","山南市","那曲市","阿里地区"],"陕西省":["西安市","铜川市","宝鸡市","咸阳市","渭南市","延安市","汉中市","榆林市","安康市","商洛市"],"甘肃省":["兰州市","嘉峪关市","金昌市","白银市","天水市","武威市","张掖市","平凉市","酒泉市","庆阳市","定西市","陇南市","临夏回族自治州","甘南藏族自治州"],"青海省":["西宁市","海东市","海北藏族自治州","黄南藏族自治州","海南藏族自治州","果洛藏族自治州","玉树藏族自治州","海西蒙古族藏族自治州"],"宁夏回族自治区":["银川市","石嘴山市","吴忠市","固原市","中卫市"],"新疆维吾尔自治区":["乌鲁木齐市","克拉玛依市","吐鲁番市","哈密市","昌吉回族自治州","博尔塔拉蒙古自治州","巴音郭楞蒙古自治州","阿克苏地区","克孜勒苏柯尔克孜自治州","喀什地区","和田地区","伊犁哈萨克自治州","塔城地区","阿勒泰地区","石河子市","阿拉尔市","图木舒克市","五家渠市","铁门关市"]}'
    table=json.loads(jsonstr)
    zhixiashi=['北京市','上海市','重庆市','天津市']
    def Cut_Name(s:str):
        name=s[:s.index(',')]#切割逗号前的字符为姓名
        leftaddress=s[s.index(',')+1:]#逗号后的留下处理
        return name ,leftaddress
    def Cut_phone(s:str):
        phone=re.findall('\d{11}',s)
        aphone=phone[0]
        nextaddress=re.sub(phone[0],"",s)
        return aphone , nextaddress
    def find_Province(s:str):
        for sheng in table.keys():
            if s[:2] in sheng:
                return sheng
        return -1
    def find_city(s:str):
        for sheng in table.keys():
            if s[:2] in sheng:
                for cheng in table[sheng]:
                    if cheng[:2] in s:
                        return cheng
                return -1
    def solve_address(s:str):
        flag_sheng=s.find("省")
        pos_zizhiqu=s.find("自治区")
        if flag_sheng!=-1:
            address=s[flag_sheng+1:]
        else:
            lenth_sheng=len(sheng)
            if pos_zizhiqu==-1:
                address=s[lenth_sheng-1:]
            else:
                address=s[lenth_sheng:]
        return address
    def solve_1address(s:str):
        zifu=0;
        flag_cheng = s.find("地区")
        if flag_cheng != -1:
            zifu=1
        if flag_cheng == -1:
            flag_cheng=s.find("盟")
        if flag_cheng == -1:
            flag_cheng=s.find("自治州")
            if flag_cheng !=-1:
                zifu=2
        if flag_cheng == -1:
            flag_cheng = s.find("市")
        if flag_cheng!=-1:
            address1=s[flag_cheng+1+zifu:]
        if flag_cheng==-1:
            lenth_cheng=len(cheng)
            address1=s[lenth_cheng-1:]
        #print(flag_cheng)
        #print(cheng)
        #print(zifu)
        return address1
    def solve_2address(s:str):
        address2=s
        zifu=0
        flag_xian = s.find("岛")
        if flag_xian == -1:
            flag_xian=s.find("自治县")
            if flag_xian !=-1:
                zifu=2
        if flag_xian == -1:
            flag_xian = s.find("县")
        if flag_xian == -1:
            flag_xian = s.find("区")
        if flag_xian == -1:
            flag_xian = s.find("旗")
        if flag_xian == -1:
            flag_xian = s.find("市")
        if flag_xian!=-1:
            address2=s[flag_xian+1+zifu:]
            xian=s[:flag_xian+1+zifu]
        if flag_xian==-1:
            xian=""
        #print(flag_xian)
        #print(xian)
        return address2,xian
    def solve_3address(s:str):
        address3=s
        double=0 #判断为街道时为2个字符长度
        flag_country=s.find("镇")
        if flag_country == -1:
            flag_country = s.find("乡")
        if flag_country == -1:
            double=s.find("街道")
            flag_country = double
            if double!=-1:
                double=1
        if flag_country!= -1:
            address3=s[flag_country+1+double:]
            country=s[:flag_country+1+double]
        if flag_country==-1:
            country=""
        #print(flag_country)
        return address3,country
    def solve_4address(s:str):
        address4=s
        flag_cun = s.find("路")
        if flag_cun == -1:
            flag_cun = s.find("街")
        if flag_cun == -1:
            flag_cun = s.find("村")
        if flag_cun ==-1:
            flag_cun = s.find("巷")
        if flag_cun != -1:
            address4 = s[flag_cun + 1:]
            cun = s[:flag_cun + 1]
        if flag_cun==-1:
            cun = ""
        #print(flag_cun)
        return address4, cun
    def solve_5address(s:str):
        address5 = s
        flag_hao = s.find("号")
        if flag_hao != -1:
            address5 = s[flag_hao + 1:]
            hao = s[:flag_hao + 1]
        else:
            hao = ""
        #print(flag_hao)
        return address5, hao
    name, leftaddress = Cut_Name(adate)
    phone, nextaddress = Cut_phone(leftaddress)
    sheng=find_Province(nextaddress)
    cheng=find_city(nextaddress)
    if sheng in zhixiashi:
        cheng=sheng
        sheng=sheng[:2]
    address=solve_address(nextaddress)
    if cheng==-1:
        cheng=""
        address1=address
    else:
        address1=solve_1address(address)
    address2,xian=solve_2address(address1)
    address3,country=solve_3address(address2)
    if level == 1:
        answer = [sheng, cheng, xian, country,address3]
    if level == 2:
        address4, cun = solve_4address(address3)
        address5, hao = solve_5address(address4)
        answer = [sheng, cheng, xian, country, cun,hao,address5]
    if level == 3:
        address4, cun = solve_4address(address3)
        address5, hao = solve_5address(address4)
        answer = [sheng, cheng, xian, country, cun, hao, address5]
    final = {
        "姓名": name,
        "手机": phone,
        "地址": answer
    }
    return json.dumps(final,ensure_ascii=False)
finalanswer=get_Answer(address)
print (finalanswer)
#1!卜畸,18974264425天津市东丽区丰年村街道丰年村街道办事处常熟里社区居民委员会