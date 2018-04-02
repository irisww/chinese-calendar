# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime

import chinese_calendar

constants_template = """# -*- coding: utf-8 -*-
# this file is generated by chinese_calendar.scripts.generate_constants
from __future__ import absolute_import, unicode_literals

import datetime
from enum import Enum


class Holiday(Enum):
    def __new__(cls, english, chinese, days):
        obj = object.__new__(cls)
        obj._value_ = english

        obj.chinese = chinese
        obj.days = days
        return obj

    new_years_day = 'New Year\\'s Day', '元旦', 1
    spring_festival = 'Spring Festival', '春节', 3
    tomb_sweeping_day = 'Tomb-sweeping Day', '清明', 1
    labour_day = 'Labour Day', '劳动节', 1
    dragon_boat_festival = 'Dragon Boat Festival', '端午', 1
    national_day = 'National Day', '国庆节', 3
    mid_autumn_festival = 'Mid-autumn Festival', '中秋', 1

    # special holidays
    anti_fascist_70th_day = 'Anti-Fascist 70th Day', '中国人民抗日战争暨世界反法西斯战争胜利70周年纪念日', 1


holidays = {}

workdays = {}
"""


class Arrangement(object):
    def __init__(self):
        self.holidays = {}
        self.workdays = {}

        self.year = None
        self.month = None
        self.day = None
        self.holiday = None
        self.is_working = None

        for method in dir(self):
            try:
                int(method[1:])
                getattr(self, method)()
            except ValueError:
                pass

    def _2018(self):
        """ http://www.gov.cn/zhengce/content/2017-11/30/content_5243579.htm
一、元旦：1月1日放假，与周末连休。
二、春节：2月15日至21日放假调休，共7天。2月11日（星期日）、2月24日（星期六）上班。
三、清明节：4月5日至7日放假调休，共3天。4月8日（星期日）上班。
四、劳动节：4月29日至5月1日放假调休，共3天。4月28日（星期六）上班。
五、端午节：6月18日放假，与周末连休。
六、中秋节：9月24日放假，与周末连休。
七、国庆节：10月1日至7日放假调休，共7天。9月29日（星期六）、9月30日（星期日）上班。
        """
        self.year_at(2018) \
            .nyd().rest(1, 1) \
            .sf().rest(2, 15).to(2, 21).work(2, 11).work(2, 24) \
            .tsd().rest(4, 5).to(4, 7).work(4, 8) \
            .ld().rest(4, 29).to(5, 1).work(4, 28) \
            .dbf().rest(6, 18) \
            .nd().rest(10, 1).to(10, 7).work(9, 29).work(9, 30) \
            .maf().rest(9, 24)

    def _2017(self):
        """ http://www.gov.cn/zhengce/content/2016-12/01/content_5141603.htm
一、元旦：1月1日放假，1月2日（星期一）补休。
二、春节：1月27日至2月2日放假调休，共7天。1月22日（星期日）、2月4日（星期六）上班。
三、清明节：4月2日至4日放假调休，共3天。4月1日（星期六）上班。
四、劳动节：5月1日放假，与周末连休。
五、端午节：5月28日至30日放假调休，共3天。5月27日（星期六）上班。
六、中秋节、国庆节：10月1日至8日放假调休，共8天。9月30日（星期六）上班。
        """
        self.year_at(2017) \
            .nyd().rest(1, 1).to(1, 2) \
            .sf().rest(1, 27).to(2, 2).work(1, 22).work(2, 4) \
            .tsd().rest(4, 2).to(4, 4).work(4, 1) \
            .ld().rest(5, 1) \
            .dbf().rest(5, 28).to(5, 30).work(5, 27) \
            .nd().rest(10, 1).to(10, 8).work(9, 30) \
            .maf().rest(10, 4)  # 国庆中秋相连，经查证10月4日为中秋

    def _2016(self):
        """ http://www.gov.cn/zhengce/content/2015-12/10/content_10394.htm
一、元旦：1月1日放假，与周末连休。
二、春节：2月7日至13日放假调休，共7天。2月6日（星期六）、2月14日（星期日）上班。
三、清明节：4月4日放假，与周末连休。
四、劳动节：5月1日放假，5月2日（星期一）补休。
五、端午节：6月9日至11日放假调休，共3天。6月12日（星期日）上班。
六、中秋节：9月15日至17日放假调休，共3天。9月18日（星期日）上班。
七、国庆节：10月1日至7日放假调休，共7天。10月8日（星期六）、10月9日（星期日）上班。
        """
        self.year_at(2016) \
            .nyd().rest(1, 1) \
            .sf().rest(2, 7).to(2, 13).work(2, 6).work(2, 14) \
            .tsd().rest(4, 4) \
            .ld().rest(5, 1).to(5, 2) \
            .dbf().rest(6, 9).to(6, 11).work(6, 12) \
            .maf().rest(9, 15).to(9, 17).work(9, 18) \
            .nd().rest(10, 1).to(10, 7).work(10, 8).to(10, 9)

    def _2015(self):
        """ http://www.gov.cn/zhengce/content/2014-12/16/content_9302.htm
一、元旦：1月1日至3日放假调休，共3天。1月4日（星期日）上班。
二、春节：2月18日至24日放假调休，共7天。2月15日（星期日）、2月28日（星期六）上班。
三、清明节：4月5日放假，4月6日（星期一）补休。
四、劳动节：5月1日放假，与周末连休。
五、端午节：6月20日放假，6月22日（星期一）补休。
六、中秋节：9月27日放假。
七、国庆节：10月1日至7日放假调休，共7天。10月10日（星期六）上班。

        注意：参见《国务院关于中国人民抗日战争暨世界反法西斯战争胜利70周年纪念日调休放假的通知》
        http://www.gov.cn/zhengce/content/2015-05/13/content_9742.htm
        额外的放假安排如下：
        9月3日至5日调休放假，共3天。其中9月3日（星期四）放假，9月4日（星期五）调休，9月6日（星期日）上班。
        """
        self.year_at(2015) \
            .nyd().rest(1, 1).to(1, 3).work(1, 4) \
            .sf().rest(2, 18).to(2, 24).work(2, 15).work(2, 28) \
            .tsd().rest(4, 5).to(4, 6) \
            .ld().rest(5, 1) \
            .dbf().rest(6, 20).rest(6, 22) \
            .maf().rest(9, 27) \
            .nd().rest(10, 1).to(10, 7).work(10, 10) \
            .afd().rest(9, 3).to(9, 4).work(9, 6)

    def _2014(self):
        """ http://www.gov.cn/zwgk/2013-12/11/content_2546204.htm
一、元旦：1月1日放假1天。
二、春节：1月31日至2月6日放假调休，共7天。1月26日（星期日）、2月8日（星期六）上班。
三、清明节：4月5日放假，4月7日（星期一）补休。
四、劳动节：5月1日至3日放假调休，共3天。5月4日（星期日）上班。
五、端午节：6月2日放假，与周末连休。
六、中秋节：9月8日放假，与周末连休。
七、国庆节：10月1日至7日放假调休，共7天。9月28日（星期日）、10月11日（星期六）上班。
        """
        self.year_at(2014) \
            .nyd().rest(1, 1) \
            .sf().rest(1, 31).to(2, 6).work(1, 26).work(2, 8) \
            .tsd().rest(4, 5).to(4, 7) \
            .ld().rest(5, 1).to(5, 3).work(5, 4) \
            .dbf().rest(6, 2) \
            .maf().rest(9, 8) \
            .nd().rest(10, 1).to(10, 7).work(9, 28).work(10, 11)

    def _2013(self):
        """ http://www.gov.cn/zwgk/2012-12/10/content_2286598.htm
一、元旦：1月1日至3日放假调休，共3天。1月5日（星期六）、1月6日（星期日）上班。
二、春节：2月9日至15日放假调休，共7天。2月16日（星期六）、2月17日（星期日）上班。
三、清明节：4月4日至6日放假调休，共3天。4月7日（星期日）上班。
四、劳动节：4月29日至5月1日放假调休，共3天。4月27日（星期六）、4月28日（星期日）上班。
五、端午节：6月10日至12日放假调休，共3天。6月8日（星期六）、6月9日（星期日）上班。
六、中秋节：9月19日至21日放假调休，共3天。9月22日（星期日）上班。
七、国庆节：10月1日至7日放假调休，共7天。9月29日（星期日）、10月12日（星期六）上班。
        """
        self.year_at(2013) \
            .nyd().rest(1, 1).to(1, 3).work(1, 5).to(1, 6) \
            .sf().rest(2, 9).to(2, 15).work(2, 16).work(2, 17) \
            .tsd().rest(4, 4).to(4, 6).work(4, 7) \
            .ld().rest(4, 29).to(5, 1).work(4, 27).work(4, 28) \
            .dbf().rest(6, 10).to(6, 12).work(6, 8).work(6, 9) \
            .maf().rest(9, 19).to(9, 21).work(9, 22) \
            .nd().rest(10, 1).to(10, 7).work(9, 29).work(10, 12)

    def _2012(self):
        """ http://www.gov.cn/zwgk/2011-12/06/content_2012097.htm
一、元旦：2012年1月1日至3日放假调休，共3天。2011年12月31日（星期六）上班。
二、春节：1月22日至28日放假调休，共7天。1月21日（星期六）、1月29日（星期日）上班。
三、清明节：4月2日至4日放假调休，共3天。3月31日（星期六）、4月1日（星期日）上班。
四、劳动节：4月29日至5月1日放假调休，共3天。4月28日（星期六）上班。
五、端午节：6月22日至24日放假公休，共3天。
六、中秋节、国庆节：9月30日至10月7日放假调休，共8天。9月29日（星期六）上班。

        注意：今年元旦特殊处理，去年上班 Σ( ° △ °|||)︴
        """
        self.year_at(2012) \
            .nyd().rest(1, 1).to(1, 3) \
            .sf().rest(1, 22).to(1, 28).work(1, 21).work(1, 29) \
            .tsd().rest(4, 2).to(4, 4).work(3, 31).work(4, 1) \
            .ld().rest(4, 29).to(5, 1).work(4, 28) \
            .dbf().rest(6, 22).rest(6, 24) \
            .maf().rest(9, 30) \
            .nd().rest(10, 1).to(10, 7).work(9, 29)

    def _2011(self):
        """ http://www.gov.cn/zwgk/2010-12/10/content_1762643.htm
一、元旦：1月1日至3日放假公休，共3天。
二、春节：2月2日（农历除夕）至8日放假调休，共7天。1月30日（星期日）、2月12日（星期六）上班。
三、清明节：4月3日至5日放假调休，共3天。4月2日（星期六）上班。
四、劳动节：4月30日至5月2日放假公休，共3天。
五、端午节：6月4日至6日放假公休，共3天。
六、中秋节：9月10日至12日放假公休，共3天。
七、国庆节：10月1日至7日放假调休，共7天。10月8日（星期六）、10月9日（星期日）上班。

        注意：明年元旦特殊处理，放到今年上班了 Σ( ° △ °|||)︴
        """
        self.year_at(2011) \
            .nyd().rest(1, 1).to(1, 3) \
            .sf().rest(2, 2).to(2, 8).work(1, 30).work(2, 12) \
            .tsd().rest(4, 3).to(4, 5).work(4, 2) \
            .ld().rest(4, 30).to(5, 2) \
            .dbf().rest(6, 4).rest(6, 6) \
            .maf().rest(9, 10).to(9, 12) \
            .nd().rest(10, 1).to(10, 7).work(10, 8).work(10, 9) \
            .nyd().work(12, 31)

    def _2010(self):
        """ http://www.gov.cn/zwgk/2009-12/08/content_1482691.htm
一、元旦：1月1日至3日放假公休，共3天。
二、春节：2月13日至19日放假调休，共7天。2月20日（星期六）、21日（星期日）上班。
三、清明节：4月3日至5日放假公休，共3天。
四、劳动节：5月1日至3日放假公休，共3天。
五、端午节：6月14日至16日放假调休，共3天。6月12日（星期六）、13日（星期日）上班。
六、中秋节：9月22日至24日放假调休，共3天。9月19日（星期日）、25日（星期六）上班。
七、国庆节：10月1日至7日放假调休，共7天。9月26日（星期日）、10月9日（星期六）上班。
        """
        self.year_at(2010) \
            .nyd().rest(1, 1).to(1, 3) \
            .sf().rest(2, 13).to(2, 19).work(2, 20).work(2, 21) \
            .tsd().rest(4, 3).to(4, 5) \
            .ld().rest(5, 1).to(5, 3) \
            .dbf().rest(6, 14).to(6, 16).work(6, 12).work(6, 13) \
            .maf().rest(9, 22).to(9, 24).work(9, 19).work(9, 25) \
            .nd().rest(10, 1).to(10, 7).work(9, 26).work(10, 9)

    def _2009(self):
        """ http://www.gov.cn/zwgk/2008-12/10/content_1174014.htm
一、元旦：1月1日至3日放假，共3天。
其中，1月1日（星期四、新年）为法定节假日，1月3日（星期六）为公休日。
1月4日（星期日）公休日调至1月2日（星期五）。
1月4日（星期日）上班。
二、春节：1月25日至31日放假，共7天。
其中，1月25日（星期日、农历除夕）、1月26日（星期一、农历正月初一）、1月27日（星期二、农历正月初二）为法定节假日，1月31日（星期六）照常公休；1月25日（星期日）公休日调至1月28日（星期三），1月24日（星期六）、2月1
日（星期日）两个公休日调至1月29日（星期四）、1月30日（星期五）。
1月24日（星期六）、2月1日（星期日）上班。
三、清明节：4月4日至6日放假，共3天。
其中，4月4日（星期六、农历清明当日）为法定节假日，4月5日（星期日）照常公休。
4月4日（星期六）公休日调至4月6日（星期一）。
四、劳动节：5月1日至3日放假，共3天。
其中，5月1日（星期五、“五一”国际劳动节）为法定节假日，5月2日（星期六）、5月3日（星期日）照常公休。
五、端午节：5月28日至30日放假，共3天。
其中，5月28日（星期四、农历端午当日）为法定节假日，5月30日（星期六）照常公休；5月31日（星期日）公休日调至5月29日（星期五）。
5月31日（星期日）上班。
六、国庆节、中秋节：10月1日至8日放假，共8天。
其中，10月1日（星期四）、10月2日（星期五）、10月3日（星期六）为国庆节法定节假日，10月4日（星期日）照常公休；10月3日（星期六）公休日及中秋节分别调至10月5日（星期一）、10月6日（星期二），9月27日（星期日）、10
月10日（星期六）公休日调至10月7日（星期三）、10月8日（星期四）。
9月27日（星期日）、10月10日（星期六）上班。
        """
        self.year_at(2009) \
            .nyd().rest(1, 1).to(1, 3).work(1, 4) \
            .sf().rest(1, 25).to(1, 31).work(1, 24).work(2, 1) \
            .tsd().rest(4, 4).to(4, 6) \
            .ld().rest(5, 1).to(5, 3) \
            .dbf().rest(5, 28).to(5, 30).work(5, 31) \
            .nd().rest(10, 1).to(10, 8).work(9, 27).work(10, 10) \
            .maf().rest(10, 3)  # 国庆中秋相连，经查证10月3日为中秋

    def _2008(self):
        """ http://www.gov.cn/zwgk/2007-12/18/content_837184.htm
一、元旦：2007年12月30日—2008年1月1日放假，共3天。
其中，1月1日（星期二）为法定节假日，12月30日（星期日）为公休日，12月29日（星期六）公休日调至12月31日（星期一），12月29日（星期六）上班。
二、春节：2月6日—12日（农历除夕至正月初六）放假，共7天。
其中，2月6日（除夕）、2月7日（春节）、2月8日（正月初二）为法定节假日，2月9日（星期六）、2月10日（星期日）照常公休，2月2日（星期六）、2月3日（星期日）两个公休日调至2月11日（星期一）、2月12日（星期二），2月2
日（星期六）、2月3日（星期日）上班。
三、清明节：4月4日—6日放假，共3天。
其中，4月4日（清明节）为法定节假日，4月5日（星期六）、4月6日（星期日）照常公休。
四、“五一”国际劳动节：5月1日—3日放假，共3天。
其中，5月1日为法定节假日，5月3日（星期六）为公休日，5月4日（星期日）公休日调至5月2日（星期五），5月4日（星期日）上班。
五、端午节：6月7日—9日放假，共3天。
其中，6月7日（星期六）照常公休，6月8日（农历五月初五，端午节）为法定节假日，6月8日（星期日）公休日调至6月9日（星期一）。
六、中秋节：9月13日—15日放假，共3天。
其中，9月13日（星期六）为公休日，9月14日（农历八月十五，中秋节）为法定节假日，9月14日（星期日）公休日调至9月15日（星期一）。
七、国庆节：9月29日—10月5日放假，共7天。
其中，10月1日、2日、3日为法定节假日，9月27日（星期六）、9月28日（星期日）两个公休日调至9月29日（星期一）、30日（星期二），10月4日（星期六）、5日（星期日）照常公休。

        注意：今年元旦假期，去年年尾要上班。
        """
        self.year_at(2008) \
            .nyd().rest(1, 1) \
            .sf().rest(2, 6).to(2, 12).work(2, 2).work(2, 3) \
            .tsd().rest(4, 4).to(4, 6) \
            .ld().rest(5, 1).to(5, 3).work(5, 4) \
            .dbf().rest(6, 7).to(6, 9) \
            .maf().rest(9, 13).to(9, 15) \
            .nd().rest(9, 29).to(10, 5)

    def _2007(self):
        """ http://www.gov.cn/fwxx/sh/2006-12/18/content_471877.htm
一、元旦： 1月1日－3日放假，共三天。
其中1月1日为法定假日，将2006年12月30日（星期六）、31日（星期日）两个公休日分别调至2007年1月2日、3日，2006年12月30日（星期六）、12月31日（星期日）上班。
二、春节：2月18日—24日（即农历初一至初七）放假，共7天。
其中18日、19日、20日为法定假日，将17日（星期六）、18日（星期日）、25日（星期日）三个公休日分别调至21日（星期三）、22日（星期四）、23日（星期五）；24日（星期六）照常公休，17日、25日上班。
三、“五一”：5月1日—7日放假，共7天。
其中，1日、2日、3日为法定假日，将4月28日（星期六）、29日（星期日）两个公休日调至5月4日（星期五）、7日（星期一）；5月5日（星期六）、6日（星期日）照常公休，4月28日、29日上班。
四、“十一”：10月1日—7日放假，共7天。
其中，1日、2日、3日为法定假日，将9月29日（星期六）、30日（星期日）两个公休日调至10月4日（星期四）、5日（星期五）；10月6日（星期六）、7日（星期日）照常公休，9月29日、30日上班。

        注意：明年元旦假期，今年年尾会放假。今年元旦假期，去年年尾要上班。
        """
        self.year_at(2007) \
            .nyd().rest(1, 1).to(1, 3) \
            .sf().rest(2, 18).to(2, 24).work(2, 17).work(2, 25) \
            .ld().rest(5, 1).to(5, 7).work(4, 28).work(4, 29) \
            .nd().rest(10, 1).to(10, 7).work(9, 29).work(9, 30) \
            .nyd().rest(12, 30).to(12, 31)

    def _2006(self):
        """ http://www.gov.cn/jrzg/2005-12/22/content_133837.htm
一、元旦：1月1日—3日放假，共3天。
其中1月1日为法定假日，将12月31日(星期六)、1月1日(星期日)两个公休日调至1月2日(星期一)、3日(星期二)，12月31日(星期六)上班。
二、春节：1月29日—2月4日(即农历大年初一至初七)放假，共7天。
其中，29日、30日、31日为法定假日，将1月28日(星期六)、29日(星期日)、2月5日(星期日)三个公休日调至2月1日(星期三)、2日(星期四)、3日(星期五)，2月4日(星期六)照常公休，1月28日、2月5日上班。
三、“五一”：5月1日—7日放假，共7天。
其中，1日、2日、3日为法定假日，将4月29日(星期六)、30日(星期日)两个公休日调至5月4日(星期四)、5日(星期五)，5月6日(星期六)、7日(星期日)照常公休，4月29日、30日上班。
四、“十一”：10月1日—7日放假，共7天。
其中，1日、2日、3日为法定假日，将9月30日(星期六)、10月1日(星期日)、8日(星期日)三个公休日调至10月4日(星期三)、5日(星期四)、6日(星期五)，10月7日(星期六)照常公休，9月30日、10月8日上班。

        注意：明年元旦假期，今年年尾要上班。今年元旦假期，去年年尾要上班。
        """
        self.year_at(2006) \
            .nyd().rest(1, 1).to(1, 3) \
            .sf().rest(1, 29).to(2, 4).work(1, 28).work(2, 5) \
            .ld().rest(5, 1).to(5, 7).work(4, 29).work(4, 30) \
            .nd().rest(10, 1).to(10, 7).work(9, 30).work(10, 8) \
            .nyd().work(12, 30).to(12, 31)

    def _2005(self):
        """
        https://zhidao.baidu.com/question/2299098.html
        国务院办公厅近日发出通知，2005年元旦、春节、“五一”、“十一”放假调休日期具体安排如下：
        一、元旦：1月1日～3日放假，共3天。其中1月1日为法定假日，将1月1日(星期六)公休日调至1月3日(星期一)，1月2日(星期日)照常公休。
        二、春节：2月9日～15日(农历大年初一至初七)放假，共7天。其中，9日、10日、11日为法定假日，
        2月12日(星期六)、13日(星期日)照常公休，将2月5日(星期六)、6日(星期日)两个公休日调至2月14日(星期一)、15日(星期二)，
        2月5日、6日上班。
        三、“五一”：5月1日～7日放假，共7天。其中，1日、2日、3日为法定假日，将4月30日(星期六)、5月1日(星期日)、8日(星期日)三个公休日
        调至5月4日(星期三)、5日(星期四)、6日(星期五)，5月7日(星期六)照常公休，4月30日、5月8日上班。
        四、“十一”：10月1日～7日放假，共7天。其中，1日、2日、3日为法定假日，将10月1日(星期六)、2日(星期日)两个公休日
        调至10月4日(星期二)、5日(星期三)，10月8日(星期六)、9日(星期日)两个公休日调至10月6日(星期四)、7日(星期五)，10月8日、9日上班。
        """
        self.year_at(2005) \
            .nyd().rest(1, 1).to(1, 3) \
            .sf().rest(2, 9).to(2, 15).work(2, 5).work(2, 6) \
            .ld().rest(5, 1).to(5, 7).work(4, 30).work(5, 8) \
            .nd().rest(10, 1).to(10, 7).work(10, 8).work(10, 9)

    def _2004(self):
        """
        https://zh.wikisource.org/zh-hans/国务院办公厅关于2004年部分节假日安排的通知
        各省、自治区、直辖市人民政府，国务院各部委、各直属机构：
            为便于各地区、各部门及早合理安排节假日旅游、交通运输、生产经营等有关工作，经国务院批准，现将2004年
        元旦、春节、“五一”、“十一”放假调休日期具体安排通知如下：
        一、元旦：1月1日放假。
        二、春节：1月22日———28日（即农历大年初一至初七）放假，共7天。
            其中，22日、23日、24日为法定假日，1月25日（星期日）照常公休，将1月17日（星期六）、18日（星期日）、24日（星期六）三个公休日
            调至1月26日（星期一）、27日（星期二）、28日（星期三），1月17日、18日上班。
        三、“五一”：5月1日———7日放假，共7天。
            其中，1日、2日、3日为法定假日，将5月1日（星期六）、2日（星期日）两个公休日调至5月4日（星期二）、5日（星期三），
            5月8日（星期六）、5月9日（星期日）两个公休日调至5月6日（星期四）、7日（星期五），5月8日、9日上班。
        四、“十一”：10月1日———7日放假，共7天。
            其中，1日、2日、3日为法定假日，将10月2日（星期六）、3日（星期日）两个公休日调至10月4日（星期一）、5日（星期二），
            10月9日（星期六）、10日（星期日）两个公休日调至10月6日（星期三）、7日（星期四），10月9日、10日上班。
        """
        self.year_at(2004) \
            .nyd().rest(1, 1) \
            .sf().rest(1, 22).to(1, 28).work(1, 17).work(1, 18) \
            .ld().rest(5, 1).to(5, 7).work(5, 8).work(5, 9) \
            .nd().rest(10, 1).to(10, 7).work(10, 9).work(10, 10)

    # 注：2003年及以前的安排就很凌乱了（其实06/07两年也是叫“部分节假日安排”）
    # 假如之后想要加的话可以参考以下地址：
    # 2003: https://zh.wikisource.org/zh-hans/国务院办公厅关于2003年部分节假日休息安排的通知
    # 2002: https://zh.wikisource.org/zh-hans/国务院办公厅关于2002年部分节假日休息安排的通知
    # 2001: https://zh.wikisource.org/zh-hans/国务院办公厅关于2001年春节、“五一”、“十一”放假安排的通知

    def year_at(self, number):
        self.year = number
        return self

    def nyd(self):
        """ 元旦 """
        return self.mark(chinese_calendar.Holiday.new_years_day)

    def sf(self):
        """ 春节 """
        return self.mark(chinese_calendar.Holiday.spring_festival)

    def tsd(self):
        """ 清明节 """
        return self.mark(chinese_calendar.Holiday.tomb_sweeping_day)

    def ld(self):
        """ 劳动节 """
        return self.mark(chinese_calendar.Holiday.labour_day)

    def dbf(self):
        """ 端午节 """
        return self.mark(chinese_calendar.Holiday.dragon_boat_festival)

    def nd(self):
        """ 国庆节 """
        return self.mark(chinese_calendar.Holiday.national_day)

    def maf(self):
        """ 中秋节 """
        return self.mark(chinese_calendar.Holiday.mid_autumn_festival)

    def afd(self):
        """ 中国人民抗日战争暨世界反法西斯战争胜利70周年纪念日 """
        return self.mark(chinese_calendar.Holiday.anti_fascist_70th_day)

    def mark(self, holiday):
        self.holiday = holiday
        return self

    def work(self, month, day):
        return self.save(month, day, is_working=True)

    def rest(self, month, day):
        return self.save(month, day, is_working=False)

    def save(self, month, day, is_working=True):
        if not self.year:
            raise ValueError('should set year before saving holiday')
        if not self.holiday:
            raise ValueError('should set holiday before saving holiday')
        self.is_working = is_working
        self.days[datetime.date(year=self.year, month=month, day=day)] = self.holiday
        self.month = month
        self.day = day
        return self

    def to(self, month, day):
        if not (self.year and self.month and self.day):
            raise ValueError('should set year/month/day before saving holiday range')
        start_date = datetime.date(year=self.year, month=self.month, day=self.day)
        end_date = datetime.date(year=self.year, month=month, day=day)
        if end_date <= start_date:
            raise ValueError('end date should be after start date')
        for i in range((end_date - start_date).days):
            the_date = start_date + datetime.timedelta(days=i + 1)
            self.days[the_date] = self.holiday
        return self

    @property
    def days(self):
        return self.workdays if self.is_working else self.holidays
