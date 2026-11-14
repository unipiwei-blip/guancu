# -*- coding: utf-8 -*-
"""莞促集团官网静态站点生成器。运行后产出全部 HTML / SEO / 站点地图文件。"""
import os, json, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://www.guancu.com'
TODAY = datetime.date.today().isoformat()

NAV = [
    ('首页', 'index.html', 'index'),
    ('集团概览', 'about.html', 'about'),
    ('业务板块', 'services.html', 'services'),
    ('成员企业', 'companies.html', 'companies'),
    ('新闻资讯', 'news.html', 'news'),
    ('联系我们', 'contact.html', 'contact'),
    ('网站地图', 'sitemap.html', 'sitemap'),
]
FRIENDS = [
    ('广东省湖南攸县商会', 'https://www.zyyous.com/'),
    ('才猎天下大数据', 'https://www.91cailie.com/'),
    ('湾区（广东）数字经济研究院', 'https://www.baydea.com/'),
    ('东莞市常平个体私营企业协会', 'https://www.ichangping.cn/'),
    ('AI建站-跨境极站', 'https://www.gosite.com.cn/'),
    ('莞促集团', 'https://www.guancu.com/'),
]

CITY_SVG = '''<svg class="city" viewBox="0 0 1440 230" preserveAspectRatio="none" aria-hidden="true">
<defs><linearGradient id="bld" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="rgba(96,164,255,.34)"/><stop offset="1" stop-color="rgba(255,255,255,.02)"/></linearGradient></defs>
<g fill="url(#bld)">
<rect x="0" y="160" width="52" height="70" rx="3"/><rect x="60" y="112" width="68" height="118" rx="3"/><rect x="136" y="146" width="46" height="84" rx="3"/>
<rect x="192" y="72" width="82" height="158" rx="3"/><rect x="284" y="128" width="58" height="102" rx="3"/><rect x="352" y="96" width="74" height="134" rx="3"/>
<rect x="436" y="150" width="52" height="80" rx="3"/><rect x="498" y="58" width="88" height="172" rx="3"/><rect x="596" y="118" width="64" height="112" rx="3"/>
<rect x="670" y="86" width="76" height="144" rx="3"/><rect x="756" y="140" width="56" height="90" rx="3"/><rect x="822" y="48" width="92" height="182" rx="3"/>
<rect x="924" y="110" width="66" height="120" rx="3"/><rect x="1000" y="142" width="54" height="88" rx="3"/><rect x="1064" y="78" width="80" height="152" rx="3"/>
<rect x="1154" y="124" width="62" height="106" rx="3"/><rect x="1226" y="96" width="72" height="134" rx="3"/><rect x="1308" y="144" width="56" height="86" rx="3"/>
<rect x="1374" y="106" width="66" height="124" rx="3"/></g>
<g fill="rgba(255,255,255,.55)">
<rect x="72" y="132" width="8" height="3" rx="1.5"/><rect x="88" y="132" width="8" height="3" rx="1.5"/><rect x="72" y="152" width="8" height="3" rx="1.5"/><rect x="88" y="152" width="8" height="3" rx="1.5"/>
<rect x="206" y="96" width="10" height="3" rx="1.5"/><rect x="226" y="96" width="10" height="3" rx="1.5"/><rect x="246" y="96" width="10" height="3" rx="1.5"/><rect x="206" y="120" width="10" height="3" rx="1.5"/><rect x="226" y="120" width="10" height="3" rx="1.5"/>
<rect x="514" y="82" width="10" height="3" rx="1.5"/><rect x="536" y="82" width="10" height="3" rx="1.5"/><rect x="558" y="82" width="10" height="3" rx="1.5"/><rect x="514" y="108" width="10" height="3" rx="1.5"/><rect x="536" y="108" width="10" height="3" rx="1.5"/>
<rect x="838" y="72" width="10" height="3" rx="1.5"/><rect x="860" y="72" width="10" height="3" rx="1.5"/><rect x="882" y="72" width="10" height="3" rx="1.5"/><rect x="838" y="98" width="10" height="3" rx="1.5"/><rect x="860" y="98" width="10" height="3" rx="1.5"/>
<rect x="1080" y="102" width="10" height="3" rx="1.5"/><rect x="1102" y="102" width="10" height="3" rx="1.5"/><rect x="1124" y="102" width="10" height="3" rx="1.5"/><rect x="1080" y="128" width="10" height="3" rx="1.5"/>
</g></svg>'''


def T(text, **kw):
    for k, v in kw.items():
        text = text.replace('{{' + k + '}}', str(v))
    return text


# ---------------------------------------------------------------- 文章数据
ARTICLES = [
    dict(
        slug='ortur', file='news/ortur.html', date='2026-11-11', cat='集团动态',
        title='莞促集团赴投资企业昂图智能 ORTUR 学习交流纪实',
        cover='cover-ortur.jpg',
        excerpt='11月11日下午，莞促集团一行走进投资企业东莞市昂图智能科技有限公司，从产品培训到设备实操、从展厅参观到座谈交流，近距离感受桌面级数字创意设备的技术积累。',
        desc='2026年11月11日，莞促集团赴投资企业东莞市昂图智能科技有限公司（ORTUR）开展学习交流，内容涵盖产品知识培训、激光雕刻实操演示、产品展厅参观与座谈交流。',
        keywords='莞促集团,昂图智能,ORTUR,激光雕刻,产业投资,学习交流',
        body=[
            ('p', '11月11日下午，莞促集团一行走进投资企业东莞市昂图智能科技有限公司（ORTUR），开展学习交流活动。从产品知识培训到设备实操演示，从展厅参观到座谈交流，双方在轻松热烈的氛围中深入互动，收获满满。'),
            ('h2', '初识 ORTUR：桌面级数字创意设备'),
            ('p', '东莞市昂图智能科技有限公司成立于2016年，是一家专注于桌面级数字创意设备研发、生产和销售的企业，旗下产品涵盖激光雕刻机、3D打印机、CNC雕刻机等多个品类，产品远销海内外。品牌秉持「新、品质、服务、合作」的理念，致力于让每个人都能轻松实现自己的创意。'),
            ('p', '截至目前，昂图智能已累计获得发明专利30项、实用新型专利62项、外观专利72项，并拥有CE、RoHS、WEEE、FCC、FDA、CPC、IEC等欧盟及美国多项安全认证，以扎实的技术积累为产品品质保驾护航。'),
            ('h2', '产品知识培训与现场实操'),
            ('p', '交流伊始，昂图智能团队带来系统的产品知识培训，由曾伟旭董事长主讲，从激光雕刻的技术原理讲起，逐一介绍ORTUR各系列激光雕刻机、光斑技术、激光模组等核心技术要点，帮助来访人员建立完整的认知框架。'),
            ('p', '培训结束后，工作人员将设备搬上会议桌进行实际操作，完整呈现激光雕刻的全过程。光束起落之间，图案便精准呈现在板材之上。一枚在金属挂牌上雕刻出的图案，线条清晰锐利、细节毕现，直观呈现了激光雕刻的精细度。'),
            ('figure', ('ortur-laser.jpg', '激光雕刻设备实操演示现场')),
            ('h2', '展厅参观与座谈交流'),
            ('p', '在产品展厅，材料样品墙按树叶、亚克力、石头、玻璃、金属等材质分区陈列，同一束激光在不同材料上呈现出截然不同的雕刻效果。展厅中的木质立体房屋模型、雕花装饰画等作品，展现从平面切割到立体拼装、从实用器物到艺术创作的多种可能。'),
            ('p', '参观结束后，双方举行座谈交流。昂图智能分享了企业在品牌塑造、产品迭代、市场开拓等方面的经验与思考，莞促集团一行结合自身业务实际，就感兴趣的领域与对方深入探讨，现场气氛融洽、交流务实高效。'),
            ('figure', ('ortur-meeting.jpg', '双方围绕企业发展与产品体系座谈交流')),
            ('h2', '持续投资优秀智造企业'),
            ('p', '半天的走访，让集团近距离感受到一家掌握3D打印和激光雕刻前沿技术的智能制造企业专注产品、深耕技术的发展定力。未来，莞促集团将持续投资优秀智造业企业，互学互鉴、共同成长，全力为建设「智创优品、和美宜居」现代化东莞贡献力量。'),
        ],
    ),
    dict(
        slug='cloud-investment', file='news/cloud-investment.html', date='2026-11-02', cat='产业观察',
        title='2026 东莞全球云招商大会正式上线，产业服务迎来新机遇',
        cover='cover-invest.jpg',
        excerpt='大会以「链全球·看东莞——让世界看见东莞，让机遇时刻在线」为主题，不设主会场、不设人数上限、不以闭幕为终点，全网在线观看超750万人次。',
        desc='2026年11月2日，2026东莞全球云招商大会正式上线，发布东莞投资环境白皮书与产业机遇，介绍企莞家平台、有空间进莞来小程序与企业服务专员机制。',
        keywords='东莞,全球云招商大会,投资促进,产业服务,企莞家,营商环境',
        body=[
            ('p', '11月2日上午10时，2026东莞全球云招商大会正式上线。大会由东莞市人民政府主办、东莞市投资促进局承办，以「链全球·看东莞——让世界看见东莞，让机遇时刻在线」为主题。与往年不同，今年的大会不设主会场、不设人数上限、不以闭幕为终点，通过多个微信视频号同步直播，截至上午直播结束，全网在线观看超750万人次。'),
            ('h2', '一部手机进场，会场没有围墙'),
            ('p', '整场直播时长约50分钟，设置前景展望、招商寄语、圆桌对话、机遇发布、东莞投资环境白皮书解读、成果展示六个环节，直播信号同步连通海外，让身在东京、法兰克福、中东等地的海内外潜在投资商同步感受东莞的投资发展机遇。'),
            ('h2', '企业提问，部门作答，政策当场揭晓'),
            ('p', '圆桌对话环节搬进松山湖XbotPark机器人基地，围绕「企业落户东莞，竞争力从哪里来」展开交流，讨论聚焦产业链核心优势：一小时能配齐多少核心零部件、样机改模需要几天、工程师资源如何保障。'),
            ('p', '机遇发布环节采用「企业提问—部门作答—政策揭晓」的结构推进。市发展改革局、市自然资源局、市投资控股集团有关负责人，围绕场景机会、土地资源、资本支持逐一回应，清晰说明连片产业用地供给、「标准地」改革落地、「拿地即开工」实施、产业基金投向等事项，给出可落地、可操作的实施路径。'),
            ('h2', '从一天到一年，招商永不下线'),
            ('p', '大会同步发布由德勤编撰的《东莞投资环境》白皮书。白皮书指出，东莞已构建起完备的制造业体系，在电子信息、AI服务器、新能源等产业实现多领域超90%的本地配套率。一年以来，东莞市签约产业项目630宗，总金额2196.1亿元。'),
            ('p', '大会与东莞市持续推进的企业服务体系相衔接：全面升级的「企莞家」企业综合服务平台提供「一站式」集成服务；依托平台建设的「有空间进莞来」小程序，意向投资企业可快速查找土地、厂房资源和扶持政策，在线提交投资计划；企业落地后，近4000人的企业服务专员队伍提供「一对一」服务。今年9月投入运行的东莞企业出海服务中心线下服务大厅，首批开放商事认证、政策咨询、海外知识产权、跨境金融、国际保险等7个窗口。'),
            ('h2', '产业服务机构的观察'),
            ('p', '产业空间、资本支持与企业服务体系的持续完善，让企业从落地到成长的各个环节更加透明、可预期。对扎根东莞、面向中小企业提供企业服务与产业协同的机构而言，更完整的产业链配套与更高效的服务机制，也意味着更丰富的服务场景与更长期的合作空间。'),
        ],
    ),
    dict(
        slug='holiday-2026', file='news/holiday-2026.html', date='2026年9月', cat='通知公告',
        title='莞促集团 2026 年中秋国庆放假安排',
        cover='notice-autumn.jpg',
        excerpt='中秋节9月25日至9月27日放假3天，国庆节10月1日至10月7日放假7天，两段假期共10天，10月8日正常返岗。',
        desc='莞促集团2026年中秋、国庆放假通知：9月25日至27日、10月1日至7日放假，共10天；9月20日、10月10日补班；10月8日正常返岗。',
        keywords='莞促集团,放假通知,中秋,国庆,2026',
        body=[
            ('p', '集团各部门、各子公司：根据国务院办公厅关于2026年节假日安排的通知精神，结合集团实际经营情况，现将中秋节、国庆节放假安排通知如下。'),
            ('h2', '放假安排'),
            ('ul', [
                '中秋节：9月25日（星期五）至9月27日（星期日），放假3天。',
                '国庆节：10月1日（星期四）至10月7日（星期三），放假7天。',
                '两段假期共10天；9月28日（星期一）至9月30日（星期三）正常上班。',
                '调休补班：9月20日（星期日）、10月10日（星期六）正常上班。',
                '返岗时间：10月8日（星期四）正常上班。',
            ]),
            ('p', '请各部门提前做好节前工作收尾与节后工作衔接，妥善安排客户对接及项目进度，确保各项业务平稳有序运转。'),
            ('h2', '温馨提示'),
            ('ul', [
                '节前安全检查：请各部门分别于9月24日、9月30日下班前完成办公区域安全检查，切断电源、锁闭门窗，妥善保管重要文件与贵重物品。',
                '假期值班安排：假期期间集团实行领导带班值班制，值班人员须坚守岗位、保持通讯畅通，遇突发事件按流程及时上报处置。',
                '出行安全提示：节日期间出行请提前规划行程，注意交通与人身财产安全，尽量避开高峰时段及人员密集场所。',
                '工作联络畅通：请全体员工假期期间保持手机畅通，以便工作联络与应急调度；如遇紧急公务，请第一时间响应配合。',
            ]),
            ('p', '值此双节同庆之际，集团向辛勤工作在各个岗位上的全体同仁及家属致以诚挚的问候与美好的祝福，祝全体同仁及家人双节愉快、阖家幸福、平安顺遂。'),
        ],
    ),
    dict(
        slug='labor-day-2026', file='news/labor-day-2026.html', date='2026-04-30', cat='通知公告',
        title='莞促集团 2026 年五一劳动节放假通知',
        cover='cover-labor.jpg',
        excerpt='2026年5月1日至5月5日放假5天，5月9日调休上班，5月6日全员正常返岗，并同步发布假期安全与值班提示。',
        desc='莞促集团2026年五一劳动节放假通知：5月1日至5日放假5天，5月9日正常上班，5月6日复工，附假期温馨提示。',
        keywords='莞促集团,五一劳动节,放假通知,2026',
        body=[
            ('p', '尊敬的客户朋友及全体同事：根据国务院办公厅《关于2026年部分节假日安排的通知》（国办发明电〔2025〕7号）要求，结合集团实际运营情况，现将2026年五一劳动节放假安排通知如下。'),
            ('h2', '时间安排'),
            ('ul', [
                '放假时间：2026年5月1日（星期五）至5月5日（星期二），共放假5天。',
                '调休上班：2026年5月9日（星期六）正常上班。',
                '复工时间：2026年5月6日（星期三）全员正常返岗上班。',
            ]),
            ('h2', '假期温馨提示'),
            ('ul', [
                '放假前请各部门把办公区域打扫干净，关闭水电、门窗，妥善保管办公物资。',
                '假期出行请做好规划，注意人身、财产安全，遵守交通规则。',
                '值班人员请严格遵守值班制度，保持通讯畅通，妥善处理突发工作事宜。',
                '请合理安排假期，调整身心，度过一个平安、快乐、幸福的五一假期。',
            ]),
            ('p', '特此通知。莞促集团有限公司　2026年4月30日'),
        ],
    ),
    dict(
        slug='water-ai-park', file='news/water-ai-park.html', date='2025-04-01', cat='产业观察',
        title='东莞水乡人工智能产业园开园，科技教育赋能区域发展迈出新步伐',
        cover='cover-ai.jpg',
        excerpt='4月1日，东莞水乡人工智能产业园、东莞市水乡现代化产业创新创业社区同步揭牌，全市首个市—区域板块会商机制与教育扩优提质改革实验区落地。',
        desc='2025年4月1日东莞水乡人工智能产业园开园，布局「一基地一中心一平台N个应用场景」，百度智能云（东莞）AI人工智能产业基地已吸引10家人工智能企业入驻。',
        keywords='东莞水乡,人工智能产业园,数字经济,科技教育,产业园区',
        body=[
            ('p', '4月1日，东莞水乡人工智能产业园、东莞市水乡现代化产业创新创业社区同步揭牌，科技教育赋能水乡发展推进会同期举办，标志着水乡经济区在培育新质生产力方面迈出坚实一步。'),
            ('h2', '统筹机制创新，科创与教育双突破'),
            ('p', '活动当天，东莞市科技局、东莞市教育局分别与水乡经济区签约，谋划共同实施全市首个市—区域板块会商机制、建设全市首个教育扩优提质改革实验区，通过「市—经济区—镇」三级联动，进一步发挥水乡经济区的统筹机制效能。'),
            ('p', '在教育扩优提质方面，实验区将积极引入优质教育资源，推进东莞中学分别与洪梅中学、水乡未来学校开展集团化办学，设立水乡教育高层次人才基地、水乡区域教研基地，并率先推行改革试点，大力推进「人工智能+教育」实践。'),
            ('h2', '「一基地一中心一平台N个应用场景」'),
            ('p', '产业园选址水乡河西数字产业区一期，总建筑面积约2.6万平方米，功能布局包括「一基地一中心一平台N个应用场景」：一基地为百度智能云（东莞）AI人工智能产业基地，一中心为规划建设的水乡经济区智算中心，一平台为人工智能运营服务平台，N个应用场景涵盖智能驾驶、低空物流、智慧工厂等领域。'),
            ('p', '目前，百度智能云（东莞）AI人工智能产业基地已吸引10家人工智能企业入驻，加速构建产业生态圈。活动现场还启动了水乡五镇智能驾驶汽车、穗莞跨城保税低空物流航线共2个人工智能应用场景，其中穗莞跨城保税低空物流配送航线是两市在低空经济领域合作的首个示范项目。'),
            ('h2', '产业协同的新空间'),
            ('p', '2025年东莞市政府「一号文」明确提出深入实施「人工智能+」行动，全力推进人工智能和制造业深度融合，并将水乡经济区作为重点布局区域之一。产业园的开园与应用场景的持续落地，为本地企业服务、数字化服务与产业投资带来新的协同空间，也为区域经济培育新质生产力提供了载体支撑。'),
        ],
    ),
    dict(
        slug='solar-project', file='news/solar-project.html', date='2023-10-11', cat='产业投资',
        title='中核汇能·莞促新能源广东户用光伏项目启动大会顺利召开',
        cover='cover-solar.jpg',
        excerpt='2023年10月11日，中核汇能·莞促新能源广东户用光伏项目启动大会在惠州博罗项目部举行，央企与民企携手共同开发广东户用光伏市场。',
        desc='中核汇能·莞促新能源广东户用光伏项目启动大会在莞促新能源广东惠州博罗项目部召开，莞促集团董事长谭喜及中核汇能、中铁十一局集团电务工程等各方代表出席。',
        keywords='莞促集团,莞促新能源,中核汇能,户用光伏,EPC,新能源',
        body=[
            ('p', '2023年10月11日，中核汇能·莞促新能源广东户用光伏项目启动大会在莞促新能源广东惠州博罗项目部会议室举行。莞促集团董事长谭喜，中核汇能代表王总、章瑞，EPC总包中铁十一局集团电务工程有限公司华南区域王书记、施工负责人闵总，广东京源电力设计有限公司代表李总，以及莞促新能源（广东）有限公司运营团队出席启动大会。'),
            ('h2', '三方战略合作，共同开发广东户用光伏市场'),
            ('p', '谭喜对莞促新能源、中核汇能、中铁十一局集团电务工程三方达成战略合作、共同开发广东户用光伏市场表示感谢。他指出，在中核汇能、中铁十一局集团电务工程的重视支持和莞促新能源前期布局基础上，促成了项目启动；实施本项目可实现资源综合利用、改善环境，建设条件落实有保障、技术上可行、经济效益良好、社会效益显著，符合可持续发展的乡村振兴理念。'),
            ('h2', '把规模与质量、合规放在首位'),
            ('p', '中核汇能代表在会上表示，作为新能源行业的头部企业，央企有责任担当起户用光伏市场开发的托底重任，积极布局广东户用光伏市场，追求规模、追求质量，同时在把好规模的同时保证合法合规运作，把好质量关和审计关。'),
            ('p', '中铁十一局集团电务工程有限公司华南区域负责人表示，质量是兴国之道，也是企业立身之本，将充分发挥央企在质量管理模式上的先进优势，扎实进行质量培训，规范质量管理行为，严查质量隐患、严控工程风险，严格遵守户用光伏发电项目施工标准与安全文明施工要求。'),
            ('p', '莞促新能源运营团队代表对项目的最终敲定表示祝贺，并表达了央企与民企携手完成既定目标的信心，将把项目的流程和效率做好、把落地和交付做到全域最佳。'),
            ('figure', ('solar-meeting.jpg', '项目启动大会座谈现场')),
            ('h2', '关于莞促新能源'),
            ('p', '莞促新能源（广东）有限公司是专业从事太阳能光伏发电及储能电站等投资和建设的新能源综合性企业，拥有一支经过众多项目验证的项目开发和管理团队，业务涵盖光伏发电工程的开发、设计、采购、施工总承包（EPC）等服务。'),
            ('p', '下一步，莞促新能源、中核汇能、中铁十一局集团电务工程将紧密配合，统筹各地项目，全力以赴打造精品品质项目，加大规模推广应用力度，为广东省绿色能源高质量发展贡献力量。'),
        ],
    ),
    dict(
        slug='spring-2021', file='news/spring-2021.html', date='2021年2月', cat='通知公告',
        title='莞促集团 2021 年春节放假通知与集团服务概览',
        cover='cover-spring.jpg',
        excerpt='2021年春节放假日期为2月2日至2月18日共17天，2月19日正式上班；通知同时回顾了集团以商务服务代理为起点的业务体系。',
        desc='莞促集团2021年春节放假通知：2月2日至2月18日放假17天，2月19日正月初八正式上班，附春节防疫事项与集团业务介绍。',
        keywords='莞促集团,春节放假通知,2021,企业服务,财税,知识产权',
        body=[
            ('p', '新春佳节来临之际，莞促集团全体员工向您致以节日的问候，衷心感谢您一直以来对莞促集团工作的肯定与支持。2021年春节放假日期为2月2日至2月18日，放假17天，2月19日（正月初八）正式上班，请大家提前做好工作安排。'),
            ('h2', '放假前后注意事项'),
            ('ul', [
                '放假前需确保门窗落锁，关闭电源、水龙头等，做好防火防盗的预防措施，消除隐患。',
                '提前安排好工作生活，注意安全，减少外出，外出须佩戴口罩、做好防护、避免聚集。',
                '假期间返乡的员工要注意旅途人身、财产安全，假期结束后按时返回公司。',
            ]),
            ('h2', '春节期间防疫事项'),
            ('ul', [
                '需外出人员尽可能错峰出行，避开高峰期，全程做好个人防护。',
                '密切关注国内高、中风险地区动态变化与病例行动轨迹，如非必要不前往出现疫情的地区。',
                '养成良好卫生习惯，勤洗手、避免用手接触口鼻眼，咳嗽、打喷嚏时注意遮挡。',
                '保持家庭和工作场所环境卫生，勤通风、勤消毒、勤打扫。',
            ]),
            ('h2', '关于我们'),
            ('p', '莞促企业管理服务集团有限公司是莞促集团的母公司，控股股东是莞促（广东）企业事务代理有限公司，成立于2006年，从事商务服务代理服务，主要经营审计、税收筹划、代理记账、财税培训、商标注册、双软认定、专利申请、人力资源服务、环保项目咨询、代办各类许可证、申请高新技术企业、项目及科技申报等业务。'),
            ('p', '从企业事务代理起步，集团逐步把服务链条延伸至财税、知识产权、数字科技、产业投资与教育文旅等领域，形成多主体协同的业务格局，持续为东莞及周边地区的中小微企业提供专业支持。'),
        ],
    ),
    dict(
        slug='mentor', file='news/mentor.html', date='2019-12-17', cat='集团荣誉',
        title='集团董事长谭喜列入东莞市第五批科技企业创业导师备案名单',
        cover='cover-mentor.jpg',
        excerpt='东莞市科技企业孵化协会发布东孵协〔2019〕22号通知，经审核与社会公示，备案第五批科技企业创业导师名单，莞促企业管理服务集团有限公司总经理谭喜在列。',
        desc='2019年12月17日，东莞市科技企业孵化协会发布第五批科技企业创业导师备案通知，莞促集团董事长谭喜列入名单。',
        keywords='莞促集团,谭喜,创业导师,科技企业孵化,东莞',
        body=[
            ('p', '2019年12月17日，东莞市科技企业孵化协会发布《关于东莞市第五批科技企业创业导师的备案通知》（东孵协〔2019〕22号）。根据《东莞市科技企业创业导师认定和管理暂行办法》（东科〔2016〕93号）的有关规定，经协会审核、社会公示，第五批科技企业创业导师名单完成备案，莞促企业管理服务集团有限公司总经理谭喜列入名单。'),
            ('h2', '创业导师机制'),
            ('p', '创业导师备案旨在建立我市长效的导师工作机制，加强创业导师在科技企业孵化服务中的支撑作用。名单由各孵化器单位推荐、协会审核并面向社会公示后确定，成员来自产业投资、科技服务、企业管理、研究院所等不同领域。'),
            ('h2', '与集团服务能力的衔接'),
            ('p', '集团长期聚集了一批经验丰富、专业水平高、综合能力强的审计、项目申报、知识产权、财税咨询等方面的专业人才，服务中小微企业在创立、成长与规范化管理各阶段的实际需求。创业导师机制与集团既有的企业服务体系形成互补，为科技企业提供更贴近经营实际的咨询与辅导。'),
            ('h2', '持续服务本地企业'),
            ('p', '以专业服务支撑企业成长，是集团长期坚持的方向。集团将继续立足东莞，围绕企业合规经营、知识产权保护、科技项目申报与数字化升级等方向，与各类园区、商协会及专业机构保持协同，为本地企业提供更系统的支持。'),
        ],
    ),
    dict(
        slug='changping-visit', file='news/changping-visit.html', date='2019-01-10', cat='交流合作',
        title='常平个体私营企业协会走访莞促知识产权 共话商标品牌保护',
        cover='cover-changping.jpg',
        excerpt='2019年1月10日，常平个体私营企业协会开展新年企业走访活动，第三站来到莞促（广东）知识产权代理有限公司，围绕知识产权与商标品牌服务深入交流。',
        desc='常平个体私营企业协会走访莞促（广东）知识产权代理有限公司，公司总经理谭喜介绍知识产权业务，并就服务常平镇企业商标品牌提出工作计划。',
        keywords='莞促集团,知识产权,商标,常平,个体私营企业协会,交流',
        body=[
            ('p', '2019年1月10日，常平个体私营企业协会展开新一年的企业走访活动。协会会长黄建新、秘书长李达豪、理事会成员和常平工商分局李旭明副分局长共约20人参加此次活动，先后走访广东万恒通家居制品有限公司、东莞市仲邑五金制品有限公司，第三站来到莞促（广东）知识产权代理有限公司。'),
            ('h2', '聚焦知识产权与商标品牌'),
            ('p', '在莞促（广东）知识产权代理有限公司，总经理谭喜向大家介绍了公司的基本情况，讲述了知识产权、商标品牌对企业发展的重要性，并对服务常平镇企业知识产权、商标品牌方面提出了积极、全面的工作计划。走访活动在愉快的交流氛围中结束。'),
            ('h2', '集团知识产权服务能力'),
            ('p', '莞促（广东）知识产权代理有限公司是莞促集团旗下成员企业，成立于2008年，是国家商标局和国家知识产权局批准的备案代理机构，立足东莞、面向全国开展商标及其他知识产权业务代理。'),
            ('p', '公司为企业提供商标查询、商标注册、商标变更、商标续展、商标转让、商标补证、商标许可，以及专利申请、版权登记等知识产权代理服务，为企业量身打造专业的知识产权保护方案，助力中小微企业在知识经济时代以创新驱动发展。'),
            ('h2', '与产业共同成长'),
            ('p', '以走访交流为纽带，集团持续了解制造、贸易等不同行业企业在品牌保护与创新成果管理上的实际需求，并把这些需求反馈到服务设计中，让专业服务更贴近企业经营的一线。'),
        ],
    ),
]

# 2026-11-13 全网资料整理新增的资讯稿，独立维护在 news_data.py
from news_data import NEW_ARTICLES

# 补齐用于结构化数据与排序的 ISO 日期（旧稿中有中文月份写法）
_ISO_FIX = {'2026年9月': '2026-09', '2021年2月': '2021-02'}
for _a in ARTICLES:
    _a.setdefault('iso_date', _ISO_FIX.get(_a['date'], _a['date']))
for _a in NEW_ARTICLES:
    _a.setdefault('iso_date', _a.get('iso_date', _a['date']))
ARTICLES = NEW_ARTICLES + ARTICLES
ARTICLES.sort(key=lambda a: a['iso_date'], reverse=True)

ART_BY_SLUG = {a['slug']: a for a in ARTICLES}

PER_PAGE = 6
NEWS_PAGES = (len(ARTICLES) + PER_PAGE - 1) // PER_PAGE


def news_filename(idx):
    return 'news.html' if idx == 1 else f'news-{idx}.html'


# 文章分类：每个分类对应一个可点击、可被搜索引擎收录的独立页面
CATEGORIES = [
    ('集团动态', 'group-news', '集团会议、业务部署与走访交流等动态资讯'),
    ('集团档案', 'group-archive', '集团发展脉络、工商沿革与人物档案'),
    ('集团荣誉', 'group-honor', '资质备案、导师聘任与行业认可'),
    ('成员企业', 'member-companies', '控股企业、成员企业与投资企业的最新动态'),
    ('产业投资', 'industry-investment', '新能源项目与产业投资合作进展'),
    ('产业观察', 'industry-insight', '东莞及粤港澳大湾区的产业环境与政策动态'),
    ('交流合作', 'exchange', '商协会走访、校企合作与交流活动'),
    ('通知公告', 'announcements', '节假日安排与集团对外通知'),
]
CAT_SLUG = {name: slug for name, slug, _ in CATEGORIES}


def cat_file(slug):
    return f'category/{slug}.html'


def cat_count(name):
    return sum(1 for a in ARTICLES if a['cat'] == name)


def category_tags(active=None, base=''):
    """可点击的分类标签；active 为当前分类名，None 表示「全部」页。"""
    all_cls = 'pill active' if active is None else 'pill'
    out = [f'<a class="{all_cls}" href="{base}news.html">全部 <i class="cnt">{len(ARTICLES)}</i></a>']
    for name, slug, _ in CATEGORIES:
        cls = 'pill active' if active == name else 'pill'
        out.append(f'<a class="{cls}" href="{base}{cat_file(slug)}">{name} <i class="cnt">{cat_count(name)}</i></a>')
    return ''.join(out)


# ---------------------------------------------------------------- 业务板块
SERVICES = [
    dict(num='01', ico='企', name='企业总部管理与咨询', desc='集团管控、组织设计与经营顾问', img='biz-hq.jpg',
         points=['企业总部管理与集团化管控', '企业管理咨询与信息咨询', '组织设计、流程梳理与经营诊断'],
         detail='以集团总部管理为主线，为成员企业与合作伙伴提供组织架构设计、经营诊断、管理流程梳理与信息咨询服务，帮助企业在扩张阶段建立清晰、可执行的管理机制。'),
    dict(num='02', ico='财', name='财税与工商服务', desc='注册记账、审计税筹与资质代办', img='biz-finance.jpg',
         points=['公司注册、变更、注销与工商代办', '代理记账、审计与税收筹划', '各类许可证与资质办理'],
         detail='从企业设立到日常经营，提供公司注册、代理记账、税务事项办理辅导、审计、税收筹划与财税培训等连续服务，并配套各类许可证、资质办理，帮助企业把合规基础做扎实。'),
    dict(num='03', ico='知', name='知识产权与科技申报', desc='商标专利、著作权与项目申报', img='biz-consult.jpg',
         points=['商标查询、注册、续展与转让', '专利申请、软件著作权与版权登记', '高新技术企业认定与科技项目申报'],
         detail='由国家商标局和国家知识产权局备案的代理机构提供商标、专利、著作权等知识产权服务，并延伸至高企认定、双软认定、项目及科技申报，保护创新成果、对接政策资源。'),
    dict(num='04', ico='数', name='数字科技与大数据服务', desc='数据服务、软件开发与系统集成', img='biz-digital.jpg',
         points=['大数据服务与互联网数据服务', '电子商务平台与软件开发', '信息系统集成与云计算服务'],
         detail='围绕企业经营数据的采集、治理与应用，提供大数据服务、互联网数据服务、电子商务平台技术、软件开发销售、信息系统集成与云计算等服务，支持企业数字化升级。'),
    dict(num='05', ico='投', name='产业投资与园区运营', desc='产业投资、园区管理与新能源', img='biz-energy.jpg',
         points=['产业园区管理与载体运营', '优秀智造企业投资与投后协同', '光伏发电及储能电站投资建设'],
         detail='以产业投资连接资本与实体，关注智能制造、新能源等方向的优质企业；同时开展产业园区管理、酒店管理，并通过新能源板块参与光伏发电及储能电站的投资、建设与总承包服务。'),
    dict(num='06', ico='教', name='教育与文旅发展', desc='教育投资、文旅运营与传媒', img='biz-edu.jpg',
         points=['教育投资与办学服务协同', '文旅项目开发与运营', '影视传媒与品牌内容服务'],
         detail='通过教育投资、文旅发展与影视传媒等成员企业，承接教育项目、文旅空间与品牌内容相关业务，形成面向人才、文化与城市生活的服务延伸。'),
]

# ---------------------------------------------------------------- 成员企业
COMPANY_GROUPS = [
    ('企', '企业服务与连锁管理', '集团总部及企业管理主体', [
        ('莞促集团有限公司', '集团总部 · 企业总部管理', '集团总部'),
        ('莞促（广东）连锁企业管理有限公司', '财税与企业管理连锁服务', '成员企业'),
        ('莞促企业管理有限公司', '企业管理与咨询服务', '成员企业'),
        ('莞促（海南）企业管理有限公司', '区域企业管理服务', '成员企业'),
    ]),
    ('财', '财税与商务代理', '财税、审计与商事登记服务链', [
        ('广东莞促会计师事务所（普通合伙）', '审计与会计服务', '成员企业'),
        ('东莞市促顺税务师事务所有限公司', '税务师事务所服务', '成员企业'),
        ('莞促（广东）企业事务代理有限公司', '企业事务代理服务', '成员企业'),
        ('爱一键印章刻制有限公司', '印章刻制与商事配套', '成员企业'),
    ]),
    ('知', '知识产权与数字科技', '创新保护与数字化能力', [
        ('莞促（广东）知识产权代理有限公司', '商标、专利与版权代理', '成员企业'),
        ('东莞市一键网络科技有限公司', '网络科技与软件开发', '成员企业'),
        ('莞促跨境贸易服务（广东）有限公司', '跨境贸易综合服务', '成员企业'),
    ]),
    ('教', '教育与文旅', '人才、文化与城市生活', [
        ('莞促教育投资有限公司', '教育项目投资', '成员企业'),
        ('促苗有限公司', '教育与企业服务延伸', '成员企业'),
        ('莞促文旅发展（东莞）有限公司', '文旅项目开发与运营', '成员企业'),
        ('莞促影视传媒（广东）有限公司', '影视与品牌内容服务', '成员企业'),
    ]),
    ('能', '新能源与产业投资', '绿色能源与智造企业投资', [
        ('莞促新能源（广东）有限公司', '光伏发电与储能电站投资建设', '成员企业'),
        ('促联新能源（清远）有限公司', '区域新能源项目运营', '成员企业'),
        ('东莞市昂图智能科技有限公司', '桌面级数字创意设备研发制造', '投资企业'),
    ]),
    ('建', '建筑工程与劳务', '工程建设配套服务', [
        ('四川莞促建筑劳务有限公司', '建筑劳务与工程配套', '成员企业'),
    ]),
]


# ---------------------------------------------------------------- 组件
def head_meta(title, desc, keywords, path, og_image, page_type='website', article=None):
    canonical = SITE + '/' + path if path else SITE + '/'
    ogi = SITE + '/assets/img/' + og_image
    tags = [
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
        f'<title>{title}</title>',
        *(['<meta name="google-site-verification" content="EHeXrOnv56_4JXQoKXmaHYtrQHywk7ax0I5pUc1IjZg">'] if path == 'index.html' else []),
        f'<meta name="description" content="{desc}">',
        f'<meta name="keywords" content="{keywords}">',
        '<meta name="author" content="莞促集团有限公司">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        f'<link rel="canonical" href="{canonical}">',
        '<meta property="og:locale" content="zh_CN">',
        '<meta property="og:site_name" content="莞促集团">',
        f'<meta property="og:type" content="{"article" if article else "website"}">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{canonical}">',
        f'<meta property="og:image" content="{ogi}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{ogi}">',
    ]
    if article:
        tags += [
            f'<meta property="article:published_time" content="{article.get("iso_date", article["date"])}">',
            '<meta property="article:author" content="莞促集团">',
        ]
    return '\n'.join(tags), canonical, ogi


def jsonld(page_type, title, desc, canonical, path, extra=None, article=None, breadcrumb=None):
    org = {
        '@type': 'Organization', '@id': SITE + '/#organization',
        'name': '莞促集团有限公司', 'alternateName': '莞促集团', 'url': SITE,
        'logo': SITE + '/assets/img/logo.png',
        'image': SITE + '/assets/img/biz-hq.jpg',
        'description': '莞促集团立足东莞，业务涵盖企业总部管理、财税与工商服务、知识产权、数字科技、产业投资、教育文旅与新能源。',
        'foundingDate': '2017-10-27',
        'telephone': '+86-769-88763333', 'email': '18926805827@139.com',
        'address': {'@type': 'PostalAddress', 'streetAddress': '厚街镇将军路2号悦山花园77号楼102室',
                    'addressLocality': '东莞市', 'addressRegion': '广东省', 'addressCountry': 'CN'},
        'contactPoint': {'@type': 'ContactPoint', 'telephone': '+86-769-88763333',
                         'email': '18926805827@139.com', 'contactType': 'customer service',
                         'availableLanguage': ['zh-CN'], 'areaServed': 'CN'},
    }
    website = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE, 'name': '莞促集团',
               'publisher': {'@id': SITE + '/#organization'}, 'inLanguage': 'zh-CN'}
    node = {'@type': page_type, '@id': canonical + '#webpage', 'url': canonical,
            'name': title, 'description': desc, 'inLanguage': 'zh-CN',
            'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#organization'}}
    if article:
        node = {'@type': 'NewsArticle', '@id': canonical + '#article', 'headline': title,
                'description': desc, 'image': SITE + '/assets/img/' + article['cover'],
                'datePublished': article.get('iso_date', article['date']), 'dateModified': TODAY,
                'keywords': article.get('keywords', ''),
                'author': {'@id': SITE + '/#organization'},
                'publisher': {'@id': SITE + '/#organization'},
                'mainEntityOfPage': {'@id': canonical + '#webpage'},
                'articleSection': article['cat'], 'inLanguage': 'zh-CN'}
    graph = [org, website, node]
    if article:
        graph.append({'@type': 'WebPage', '@id': canonical + '#webpage', 'url': canonical,
                      'name': title, 'isPartOf': {'@id': SITE + '/#website'}})
    if extra:
        graph.append(extra)
    if breadcrumb:
        graph.append({'@type': 'BreadcrumbList', '@id': canonical + '#breadcrumb',
                      'itemListElement': [
                          {'@type': 'ListItem', 'position': i + 1, 'name': n,
                           'item': SITE + '/' + u if u else SITE + '/'}
                          for i, (n, u) in enumerate(breadcrumb)]})
    return '<script type="application/ld+json">\n' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2) + '\n</script>'


def header(base, page):
    links = ''.join(f'<a href="{base}{f}" data-nav="{k}">{n}</a>' for n, f, k in NAV)
    return f'''<div class="topbar"><div class="container">
<span><i class="spark"></i><b>莞促集团</b>　企业服务 · 数字赋能 · 产业投资<span class="hide-sm">　|　扎根东莞，服务粤港澳大湾区</span></span>
</div></div>
<header class="nav"><div class="container">
<a class="brand" href="{base}index.html" aria-label="莞促集团首页">
<img src="{base}assets/img/logo.png" alt="莞促集团标识"><span class="brand-txt"><strong>莞促集团</strong></span></a>
<span class="brand-slogan">企业服务 · 数字赋能 · 产业投资</span>
<nav class="nav-menu" aria-label="主导航">{links}</nav>
<a class="btn btn-primary nav-cta" href="{base}contact.html">联系洽谈</a>
<button class="menu-btn" aria-label="展开导航菜单" aria-expanded="false"><i></i></button>
</div></header>'''


def footer(base):
    nav1 = [n for n, f, k in NAV if k not in ('index',)][:3]
    nav2 = [n for n, f, k in NAV if k not in ('index',)][3:]
    def col(names):
        out = []
        for n in names:
            f = next(x[1] for x in NAV if x[0] == n)
            out.append(f'<li><a href="{base}{f}">{n}</a></li>')
        return ''.join(out)
    friends = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in FRIENDS)
    return f'''<footer class="footer"><div class="container">
<div class="footer-top">
<div>
<a class="brand" href="{base}index.html"><img src="{base}assets/img/logo.png" alt="莞促集团标识"><span class="brand-txt"><strong>莞促集团</strong></span></a>
<p class="footer-about">立足东莞的综合性企业服务与产业投资集团，业务涵盖企业总部管理、财税工商、知识产权、数字科技、产业投资、教育文旅与新能源。</p>
<div class="pills"><span class="pill">企业服务</span><span class="pill">产业投资</span><span class="pill">数字赋能</span></div>
</div>
<div><h4>网站导航</h4><div class="f2col"><ul>{col(nav1)}</ul><ul>{col(nav2)}</ul></div></div>
<div><h4>联系方式</h4>
<img class="footer-qr" src="{base}assets/img/qrcode.png" alt="莞促集团官网二维码">
<p class="footer-contact"><b>0769-88763333</b><br>业务咨询 18926805827<br>邮箱 18926805827@139.com</p>
</div>
</div>
<div class="footer-links"><span class="fl-label">友情链接</span>{friends}<span class="fl-sep">·</span><a href="{base}sitemap.html">网站地图</a></div>
<div class="footer-address">集团地址：广东省东莞市厚街镇将军路2号悦山花园77号楼102室</div>
<div class="footer-bottom"><span>&copy; <span data-year>2026</span> 莞促集团有限公司 版权所有</span><a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">粤ICP备17159526号-1</a><span>官网 www.guancu.com</span><span>服务时间 工作日 09:00–18:00</span></div>
</div></footer>'''


def page(path, title, desc, keywords, body, page_type='WebPage', og='biz-hq.jpg',
         navkey='', extra=None, article=None, breadcrumb=None):
    base = '../' if '/' in path else ''
    meta, canonical, ogi = head_meta(title, desc, keywords, path, og, article=article)
    ld = jsonld(page_type, title, desc, canonical, path, extra=extra, article=article, breadcrumb=breadcrumb)
    doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
{meta}
<link rel="icon" href="{base}assets/img/favicon.ico" sizes="any">
<link rel="icon" href="{base}assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{base}assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="{base}assets/css/style.css">
{ld}
</head>
<body data-page="{navkey}">
{header(base, navkey)}
<main>
{body}
</main>
{footer(base)}
<script src="{base}assets/js/main.js" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(doc)
    return path


def sec_head(eyebrow, h2, lead=''):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<div class="sec-head reveal"><span class="eyebrow">{eyebrow}</span><h2 class="h2">{h2}</h2>{l}</div>'


def page_hero(eyebrow, h1, lead, crumb, base='', compact=False):
    cls = 'page-hero compact' if compact else 'page-hero'
    return f'''<section class="{cls}"><div class="container">
<span class="eyebrow">{eyebrow}</span><h1 class="h2" style="font-size:clamp(30px,3.6vw,48px)">{h1}</h1>
<p class="lead">{lead}</p>
<div class="breadcrumb"><a href="{base}index.html">首页</a><span>/</span>{crumb}</div>
</div></section>'''


def news_card(a, base=''):
    return f'''<a class="news-card reveal" href="{base}{a['file']}">
<div class="news-shot"><img src="{base}assets/img/{a['cover']}" alt="{a['title']}" loading="lazy"><span class="badge">{a['cat']}</span></div>
<div class="news-body"><div class="news-meta">{a['date']}</div>
<div class="news-title">{a['title']}</div>
<p class="news-excerpt">{a['excerpt']}</p>
<span class="news-more">阅读全文 &rarr;</span></div></a>'''


def cta_block(title, text, base=''):
    return f'''<section class="section tight"><div class="container">
<div class="cta-dark reveal"><div class="container"><h2>{title}</h2><p>{text}</p>
<div class="hero-actions"><a class="btn btn-white btn-lg" href="{base}contact.html">业务咨询</a>
<a class="btn btn-outline btn-lg" href="{base}companies.html">了解集团版图</a></div></div></div>
</div></section>'''


def render_body(blocks, base):
    out = []
    for b in blocks:
        if b[0] == 'h2':
            out.append(f'<h2>{b[1]}</h2>')
        elif b[0] == 'h3':
            out.append(f'<h3>{b[1]}</h3>')
        elif b[0] == 'p':
            out.append(f'<p>{b[1]}</p>')
        elif b[0] == 'ul':
            out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in b[1]) + '</ul>')
        elif b[0] == 'figure':
            img, cap = b[1]
            out.append(f'<figure><img src="{base}assets/img/{img}" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>')
        elif b[0] == 'quote':
            out.append(f'<blockquote>{b[1]}</blockquote>')
    return '\n'.join(out)


# ---------------------------------------------------------------- 首页
WHY = [
    ('01', '深耕东莞', '扎根本地产业生态多年'),
    ('02', '多主体协同', '成员企业分工清晰、彼此支撑'),
    ('03', '全周期服务', '覆盖设立、成长与规范化管理'),
    ('04', '专业团队', '财税、知产、申报人才齐备'),
    ('05', '产业视野', '连接资本、园区与智造企业'),
    ('06', '长期经营', '以持续服务陪伴企业成长'),
]
FAQ = [
    ('莞促集团主要从事哪些业务？', '集团业务涵盖企业总部管理与企业管理咨询、财税与工商服务、知识产权与科技项目申报、数字科技与大数据服务、产业投资与园区运营、教育与文旅六大板块，由多家成员企业分别承接。'),
    ('集团总部位于哪里？', '集团注册地址为广东省东莞市厚街镇将军路2号悦山花园77号楼102室，业务立足东莞、面向粤港澳大湾区。'),
    ('集团旗下的公司有哪些？', '集团成员企业覆盖企业服务与连锁管理、财税与商务代理、知识产权与数字科技、教育与文旅、新能源与产业投资、建筑工程等领域，「成员企业」栏目集中展示完整名单。'),
    ('企业服务如何开始对接？', '可通过官网「联系我们」栏目中的电话或邮箱说明需求，沟通业务类型、企业情况与期望时间，之后由相应业务团队跟进对接。'),
    ('集团是否开展产业投资？', '集团关注智能制造、新能源等方向的优质企业，已参与投资东莞市昂图智能科技有限公司等企业，并通过新能源板块参与光伏发电及储能电站项目投资建设。'),
    ('新闻资讯栏目更新哪些内容？', '栏目发布集团动态、产业投资进展、行业观察与通知公告，涵盖走访交流、项目启动、区域产业动态及假期安排等信息。'),
]

def build_index():
    why = ''.join(f'''<div class="card reveal"><span class="num">{n} / WHY GUANCU</span><div class="ico">{i+1:02d}</div>
<h3 class="h3">{t}</h3><p>{d}</p></div>''' for i, (n, t, d) in enumerate(WHY))
    biz = ''.join(f'''<a class="card reveal" href="services.html#s{int(s['num'])}"><span class="num">SERVICE {s['num']}</span>
<div class="ico">{s['ico']}</div><h3 class="h3">{s['name']}</h3><p>{s['desc']}</p></a>''' for s in SERVICES)
    groups = ''.join(f'''<a class="card reveal" href="companies.html#g{i+1}"><span class="num">SECTOR {i+1:02d}</span>
<div class="ico">{g[0]}</div><h3 class="h3">{g[1]}</h3><p>{len(g[3])} 家成员与投资企业</p></a>'''
                     for i, g in enumerate(COMPANY_GROUPS))
    steps = [('01', '需求沟通', '明确业务类型与目标'), ('02', '方案梳理', '匹配专业团队与服务范围'),
             ('03', '资料准备', '按业务要求归集材料'), ('04', '服务实施', '按节点推进并同步进度'),
             ('05', '持续跟进', '交付后保持长期联络')]
    flow = ''.join(f'''<div class="flow-step reveal"><div class="flow-dot">{n}</div><div class="h3">{t}</div><p>{d}</p></div>'''
                   for n, t, d in steps)
    news = ''.join(news_card(a) for a in ARTICLES[:3])
    faq = ''.join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    body = f'''<section class="hero"><div class="hero-bg"><div class="glow g1"></div><div class="glow g2"></div><div class="glow g3"></div>{CITY_SVG}</div>
<div class="container">
<span class="eyebrow">GUANCU GROUP · DONGGUAN</span>
<h1 class="h1">扎根东莞，<br>与<span class="h2 grad">产业共同成长</span></h1>
<p class="lead">莞促集团以企业服务为根基，延伸至数字科技、产业投资、教育文旅与新能源，形成多主体协同的产业服务版图，持续为湾区企业提供专业支持。</p>
<div class="hero-actions"><a class="btn btn-primary btn-lg" href="about.html">了解集团概览</a><a class="btn btn-ghost btn-lg" href="services.html">浏览业务板块</a></div>
<div class="hero-stats">
<div class="stat"><b>2017</b><span>集团成立年份</span></div>
<div class="stat"><b>1 亿元</b><span>注册资本</span></div>
<div class="stat"><b>9 家</b><span>控股子公司</span></div>
<div class="stat"><b>6 大</b><span>业务板块</span></div>
</div>
<div class="float-tag f1">企业服务 · 财税 · 知识产权</div>
<div class="float-tag f2">数字科技 · 产业投资</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('WHY GUANCU / 集团优势', '把专业做深，把<span class="blue">协同做实</span>', '从一家企业事务代理机构，到多主体协同的集团化布局，莞促集团始终围绕企业经营的真实需求组织能力。')}
<div class="grid-3">{why}</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('SERVICES / 六大业务板块', '一条服务链，<span class="grad">覆盖企业成长全程</span>', '六大板块分别由专业成员企业承接，彼此协同，覆盖企业从设立、合规、创新保护到数字化与资本运作的主要环节。')}
<div class="grid-3">{biz}</div>
<p class="note"><a class="pill" href="services.html">查看业务板块详情 &rarr;</a></p>
</div></section>

<section class="section tight"><div class="container">
<div class="numbers reveal"><div><b>2006</b><span>企业事务代理业务起步</span></div><div><b>2017</b><span>莞促集团有限公司成立</span></div>
<div><b>9 家</b><span>控股子公司</span></div><div><b>19 家</b><span>成员与投资企业展示</span></div></div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('GROUP MAP / 集团版图', '六大板块，<span class="pink">一支协同的队伍</span>', '从企业服务出发，向财税、知识产权、数字科技、教育文旅、新能源与工程配套延伸，形成分工清晰、相互支撑的企业集群。')}
<div class="grid-3">{groups}</div>
<p class="note"><a class="pill" href="companies.html">查看全部成员企业 &rarr;</a></p>
</div></section>

<section class="section tight"><div class="container">
{sec_head('PROCESS / 服务流程', '从一次沟通，到<span class="blue">长期同行</span>')}
<div class="flow">{flow}</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('NEWS / 新闻资讯', '集团动态与<span class="pink">产业观察</span>', '走访交流、项目进展、通知公告与区域经济动态，记录集团与产业共同前行的脚步。')}
<div class="news-grid">{news}</div>
<p class="note"><a class="pill" href="news.html">查看全部资讯 &rarr;</a></p>
</div></section>

{cta_block('与莞促集团同行', '无论是企业服务、知识产权、数字化升级，还是产业投资与园区合作，都欢迎与我们建立联系。')}

<section class="section tight"><div class="container">
{sec_head('FAQ / 常见问题', '关于莞促集团，<span class="blue">先了解这些</span>')}
<div class="faq">{faq}</div>
</div></section>'''
    itemlist = {'@type': 'ItemList', 'name': '莞促集团业务板块',
                'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': s['name'],
                                     'url': SITE + '/services.html#s' + str(int(s['num']))}
                                    for i, s in enumerate(SERVICES)]}
    return page('index.html', '莞促集团｜东莞企业服务与产业投资集团',
                '莞促集团有限公司立足东莞，业务涵盖企业总部管理、财税与工商服务、知识产权、数字科技、产业投资、教育文旅与新能源，旗下多家成员企业协同服务湾区企业。',
                '莞促集团,莞促集团有限公司,东莞企业服务,产业投资,财税服务,知识产权,数字科技,集团官网',
                body, 'WebPage', 'biz-hq.jpg', 'index', extra=itemlist,
                breadcrumb=[('首页', '')])


# ---------------------------------------------------------------- 集团概览
def build_about():
    tl = [
        ('2006', '企业事务代理起步', '莞促（广东）连锁企业管理有限公司成立，从工商注册、代理记账与财税服务切入企业服务市场。'),
        ('2017', '集团化组建', '莞促集团有限公司于10月27日成立，注册资本1亿元人民币，以企业总部管理统筹多主体业务。'),
        ('2019', '服务网络延伸', '广东东莞分公司设立，知识产权、创业导师等资质与专业服务持续完善。'),
        ('2023', '新能源板块落地', '中核汇能·莞促新能源广东户用光伏项目启动大会召开，三方携手开发广东户用光伏市场。'),
        ('2025', '总部地址迁驻厚街', '集团住所变更至东莞市厚街镇将军路2号悦山花园，办公与业务衔接进一步优化。'),
        ('2026', '投资智造企业', '集团一行走进投资企业东莞市昂图智能科技有限公司，围绕技术、产品与产业发展开展学习交流。'),
    ]
    timeline = ''.join(f'''<div class="tl-item reveal"><div class="y">{y}</div><div class="t">{t}</div><div class="d">{d}</div></div>'''
                       for y, t, d in tl)
    cards = ''.join(f'''<div class="card reveal"><span class="num">CAPABILITY {i+1:02d}</span><div class="ico">{s['ico']}</div>
<h3 class="h3">{s['name']}</h3><p>{s['desc']}</p></div>''' for i, s in enumerate(SERVICES[:4]))
    culture = [('务实', '以解决企业实际问题为出发点'), ('专业', '由持证与备案机构承接专业服务'),
               ('协同', '成员企业分工协作、资源共享'), ('长期', '以持续服务陪伴企业成长')]
    cult = ''.join(f'''<div class="card reveal"><span class="num">VALUE {i+1:02d}</span><h3 class="h3">{t}</h3><p>{d}</p></div>'''
                   for i, (t, d) in enumerate(culture))
    facts = [('成立时间', '2017年10月27日'), ('注册资本', '10000万元人民币'),
             ('法定代表人 / 董事长', '谭喜'), ('统一社会信用代码', '91441900MA4X9CTL2B'),
             ('登记机关', '东莞市市场监督管理局'), ('注册地址', '广东省东莞市厚街镇将军路2号悦山花园77号楼102室')]
    rows = ''.join(f'<tr><th>{a}</th><td>{b}</td></tr>' for a, b in facts)
    body = f'''{page_hero('ABOUT US / 集团概览', '立足东莞，服务湾区', '从企业事务代理到多主体协同的产业服务集团，莞促集团把专业能力沉淀在每一家企业、每一个项目里。', '集团概览')}

<section class="section tight"><div class="container">
{sec_head('COMPANY PROFILE / 集团简介', '一家与<span class="blue">产业共同生长</span>的企业集团')}
<div class="prose">
<p>莞促集团有限公司成立于2017年10月27日，注册资本10000万元人民币，法定代表人为谭喜，登记机关为东莞市市场监督管理局，注册地址位于广东省东莞市厚街镇将军路2号悦山花园77号楼102室。集团所属行业为商务服务业，经营范围包括企业总部管理、企业管理、信息咨询服务、企业管理咨询、酒店管理、大数据服务与互联网数据服务。</p>
<p>集团的业务根基可追溯至2006年成立的企业事务代理机构。近二十年间，从公司注册、代理记账、财税咨询起步，逐步延伸至审计与税收筹划、知识产权与科技项目申报、数字科技与大数据服务、产业投资与园区运营、教育与文旅、新能源投资建设等领域，形成由多家成员企业分工承接、彼此支撑的业务格局。</p>
<p>公开工商信息显示，集团拥有9家控股子公司，业务主体覆盖企业服务、财税、知识产权、网络科技、教育投资、文旅发展、建筑劳务与新能源等方向；同时通过产业投资，与东莞市昂图智能科技有限公司等优秀智造企业建立连接。集团还持有代理记账许可证，并积累了多项作品著作权。</p>
<figure><img src="assets/img/about-visit.jpg" alt="集团学习交流活动现场" loading="lazy"><figcaption>集团赴投资企业开展学习交流</figcaption></figure>
</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('FACTS / 基本信息', '公开、清晰的<span class="pink">集团档案</span>')}
<div class="data-table reveal"><table><tbody>{rows}</tbody></table></div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('MILESTONES / 发展脉络', '一步一个脚印的<span class="blue">成长轨迹</span>')}
<div class="timeline">{timeline}</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('STRENGTH / 核心能力', '四大能力，<span class="grad">支撑长期服务</span>')}
<div class="grid-4">{cards}</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('CULTURE / 发展理念', '把事情做实，把<span class="pink">服务做长</span>')}
<div class="grid-4">{cult}</div>
</div></section>

{cta_block('进一步了解莞促集团', '业务板块、成员企业、新闻资讯与联系方式，都可以在这里继续查阅。')}'''
    return page('about.html', '集团概览｜莞促集团有限公司简介、发展历程与核心能力',
                '莞促集团有限公司成立于2017年，注册资本1亿元，总部位于东莞市厚街镇。了解集团简介、发展脉络、基本信息、核心能力与发展理念。',
                '莞促集团简介,莞促集团有限公司,谭喜,发展历程,集团档案,东莞企业集团',
                body, 'AboutPage', 'about-visit.jpg', 'about',
                breadcrumb=[('首页', ''), ('集团概览', 'about.html')])


# ---------------------------------------------------------------- 业务板块
def build_services():
    blocks = ''.join(f'''<a class="biz-card reveal" id="s{int(s['num'])}" href="contact.html">
<div class="biz-photo"><img src="assets/img/{s['img']}" alt="{s['name']}" loading="lazy"></div>
<span class="num">SERVICE {s['num']}</span><h3 class="h3">{s['name']}</h3>
<p>{s['detail']}</p>
<ul>{''.join(f'<li>{x}</li>' for x in s['points'])}</ul>
<div class="tag-list"><span>{s['desc']}</span></div></a>''' for s in SERVICES)
    rows = ''.join(f'<tr><th>{s["name"]}</th><td>{s["desc"]}</td><td>{"、".join(s["points"][:2])}</td></tr>' for s in SERVICES)
    steps = [('01', '需求沟通', '明确业务类型与时间要求'), ('02', '专业诊断', '梳理现状与所需材料'),
             ('03', '方案确认', '确定范围与责任团队'), ('04', '服务实施', '按节点推进并同步进度'),
             ('05', '交付跟进', '成果交付与后续支持')]
    flow = ''.join(f'''<div class="flow-step reveal"><div class="flow-dot">{n}</div><div class="h3">{t}</div><p>{d}</p></div>'''
                   for n, t, d in steps)
    promise = [('专业承接', '由对应成员企业与专业团队对接'), ('流程清晰', '服务节点与交付内容明确'),
               ('信息保密', '客户资料在授权范围内使用'), ('长期响应', '交付后保持沟通与跟进')]
    pcards = ''.join(f'''<div class="card reveal"><span class="num">PROMISE {i+1:02d}</span><div class="ico">{i+1:02d}</div>
<h3 class="h3">{t}</h3><p>{d}</p></div>''' for i, (t, d) in enumerate(promise))
    itemlist = {'@type': 'ItemList', 'name': '莞促集团六大业务板块',
                'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': s['name'],
                                     'description': s['desc'], 'url': SITE + '/services.html#s' + str(int(s['num']))}
                                    for i, s in enumerate(SERVICES)]}
    body = f'''{page_hero('SERVICES / 业务板块', '六大板块，覆盖企业成长全程', '企业服务、财税工商、知识产权、数字科技、产业投资与教育文旅，由专业成员企业分别承接、协同推进。', '业务板块')}

<section class="section tight"><div class="container">
{sec_head('WHAT WE DO / 服务总览', '一条清晰、<span class="blue">可衔接的服务链</span>', '从企业设立到合规经营，从创新保护到数字化升级，再到资本与产业资源的连接，集团围绕企业成长的真实需求组织能力。')}
<div class="grid-2" style="text-align:center">{blocks}</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('SERVICE LIST / 服务清单', '按板块<span class="pink">快速定位</span>')}
<div class="data-table reveal"><table><thead><tr><th>业务板块</th><th>服务定位</th><th>代表性服务</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('PROCESS / 服务流程', '五个节点，<span class="blue">过程可预期</span>')}
<div class="flow">{flow}</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('COMMITMENT / 服务承诺', '把每一次合作<span class="grad">做扎实</span>')}
<div class="grid-4">{pcards}</div>
</div></section>

{cta_block('说说您的需求', '告诉我们需要对接的业务方向，相关团队将与您进一步沟通。')}'''
    return page('services.html', '业务板块｜企业服务、财税工商、知识产权、数字科技与产业投资',
                '莞促集团六大业务板块：企业总部管理与咨询、财税与工商服务、知识产权与科技申报、数字科技与大数据服务、产业投资与园区运营、教育与文旅。',
                '莞促集团业务,企业服务,代理记账,商标注册,专利申请,大数据服务,产业投资,园区运营',
                body, 'CollectionPage', 'biz-digital.jpg', 'services', extra=itemlist,
                breadcrumb=[('首页', ''), ('业务板块', 'services.html')])


# ---------------------------------------------------------------- 成员企业
def build_companies():
    n = 0
    groups_html = []
    for i, (ico, name, desc, comps) in enumerate(COMPANY_GROUPS):
        items = []
        for cname, cdesc, ctag in comps:
            n += 1
            items.append(f'''<div class="company-card reveal"><span class="cnum">{n:02d}</span>
<div class="cname">{cname}</div><div class="cdesc">{cdesc}</div><span class="ctag">{ctag}</span></div>''')
        groups_html.append(f'''<div class="company-group" id="g{i+1}">
<div class="gh"><span class="gi">{ico}</span><span class="gt">{name}</span><span class="gd">{desc}</span></div>
<div class="company-list">{''.join(items)}</div></div>''')
    feats = [('专业分工', '各板块由专门主体承接'), ('区域协同', '东莞、海南、清远、四川多点布局'),
             ('产业联动', '服务、投资与实体企业相互支撑'), ('长期经营', '核心主体经营多年、持续服务')]
    fc = ''.join(f'''<div class="card reveal"><span class="num">FEATURE {i+1:02d}</span><div class="ico">{i+1:02d}</div>
<h3 class="h3">{t}</h3><p>{d}</p></div>''' for i, (t, d) in enumerate(feats))
    itemlist = {'@type': 'ItemList', 'name': '莞促集团成员与投资企业',
                'itemListElement': [{'@type': 'ListItem', 'position': j + 1, 'name': c[0],
                                     'description': c[1]} for j, c in enumerate(
                                         [x for g in COMPANY_GROUPS for x in g[3]])]}
    body = f'''{page_hero('GROUP COMPANIES / 成员企业', '一支分工清晰的企业集群', '集团成员与投资企业按六大板块协同布局，覆盖企业服务、财税、知识产权、数字科技、教育文旅、新能源与工程配套。', '成员企业')}

<section class="section tight"><div class="container">
{sec_head('GROUP MAP / 集团版图', '以集团总部为<span class="blue">核心的产业矩阵</span>', '专业化分工、跨区域布局、产业与资本联动，构成集团持续服务客户与合作伙伴的组织基础。')}
<div class="map-head reveal"><div class="map-core"><b>莞促集团有限公司</b><span>集团总部 · 企业总部管理 · 产业协同</span></div></div>
<div class="numbers reveal"><div><b>6 大</b><span>业务板块</span></div><div><b>{n} 家</b><span>成员与投资企业</span></div><div><b>9 家</b><span>控股子公司</span></div><div><b>4 省</b><span>业务布局区域</span></div></div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('DIRECTORY / 企业名录', '按板块<span class="pink">了解每一家企业</span>')}
{''.join(groups_html)}
</div></section>

<section class="section tight"><div class="container">
{sec_head('FEATURES / 版图特点', '有分工，更有<span class="blue">协同</span>')}
<div class="grid-4">{fc}</div>
</div></section>

{cta_block('与集团建立连接', '业务合作、产业协同与资源对接，欢迎与我们联系。')}'''
    return page('companies.html', '成员企业｜莞促集团旗下公司与投资企业名录',
                '莞促集团成员与投资企业完整名录，按企业服务与连锁管理、财税与商务代理、知识产权与数字科技、教育与文旅、新能源与产业投资、建筑工程六大板块展示。',
                '莞促集团旗下公司,莞促集团子公司,成员企业,集团版图,莞促新能源,昂图智能',
                body, 'CollectionPage', 'biz-arch.jpg', 'companies', extra=itemlist,
                breadcrumb=[('首页', ''), ('成员企业', 'companies.html')])


# ---------------------------------------------------------------- 新闻列表
def build_news_list(idx):
    total = NEWS_PAGES
    start = (idx - 1) * PER_PAGE
    arts = ARTICLES[start:start + PER_PAGE]
    f = news_filename(idx)
    cards = ''.join(news_card(a) for a in arts)
    prev = ('<span class="disabled">上一页</span>' if idx == 1
            else f'<a href="{news_filename(idx - 1)}">上一页</a>')
    nxt = ('<a href="' + news_filename(idx + 1) + '">下一页</a>' if idx < total
           else '<span class="disabled">下一页</span>')
    nums = ''.join(
        (f'<span class="current">{n}</span>' if n == idx else f'<a href="{news_filename(n)}">{n}</a>')
        for n in range(1, total + 1))
    cats = category_tags()
    itemlist = {'@type': 'ItemList', 'name': '莞促集团新闻资讯',
                'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': a['title'],
                                     'url': SITE + '/' + a['file']} for i, a in enumerate(arts)]}
    title = ('新闻资讯｜莞促集团动态、产业观察与通知公告' if idx == 1
             else f'新闻资讯 第{idx}页｜莞促集团动态、产业观察与通知公告')
    desc = (f'莞促集团新闻资讯栏目，发布集团动态、成员企业进展、产业观察、交流合作与通知公告，共{len(ARTICLES)}篇文章，当前第{idx}页。')
    crumb = '新闻资讯' + ('' if idx == 1 else f' · 第 {idx} 页')
    body = f'''{page_hero('NEWS / 新闻资讯', '集团动态与产业观察', '走访交流、项目进展、区域产业动态与通知公告，记录集团与产业共同前行的脚步。', crumb, compact=True)}

<section class="section tight news-list-section"><div class="container">
<div class="tag-list" style="margin:0 0 22px">{cats}</div>
<div class="news-grid">{cards}</div>
<div class="pager">{prev}{nums}{nxt}</div>
<p class="note">共 {len(ARTICLES)} 篇资讯 · 每页 {PER_PAGE} 篇 · 当前第 {idx} / {total} 页</p>
</div></section>

{cta_block('保持联络', '希望进一步了解集团动态或业务进展，欢迎与我们联系。')}'''
    return page(f, title, desc, '莞促集团新闻,集团动态,产业观察,通知公告,项目进展,走访交流',
                body, 'CollectionPage', arts[0]['cover'], 'news', extra=itemlist,
                breadcrumb=[('首页', ''), ('新闻资讯', 'news.html')])


# ---------------------------------------------------------------- 文章分类页
def build_category(name, slug, desc):
    base = '../'
    arts = [a for a in ARTICLES if a['cat'] == name]
    cards = ''.join(news_card(a, base) for a in arts)
    tags = category_tags(active=name, base=base)
    itemlist = {'@type': 'ItemList', 'name': f'莞促集团新闻资讯 · {name}',
                'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': a['title'],
                                     'url': SITE + '/' + a['file']} for i, a in enumerate(arts)]}
    crumb = f'<a href="../news.html">新闻资讯</a><span>/</span>{name}'
    body = f'''{page_hero('NEWS CATEGORY / 文章分类', name, desc, crumb, base=base, compact=True)}

<section class="section tight news-list-section"><div class="container">
<div class="tag-list" style="margin:0 0 22px">{tags}</div>
<div class="news-grid">{cards}</div>
<p class="note">本分类共 {len(arts)} 篇文章 · 全部资讯共 {len(ARTICLES)} 篇</p>
<div class="article-nav"><a class="btn btn-ghost" href="../news.html">返回全部资讯</a><a class="btn btn-primary" href="../sitemap.html">查看网站地图</a></div>
</div></section>

{cta_block('与莞促集团同行', '业务咨询、产业合作与资源对接，欢迎随时联络。', base)}'''
    title = f'{name}｜莞促集团新闻资讯分类'
    meta_desc = f'莞促集团新闻资讯「{name}」分类，共{len(arts)}篇文章。{desc}。'
    keywords = f'莞促集团,{name},新闻分类,集团资讯,文章归档'
    return page(cat_file(slug), title, meta_desc, keywords, body,
                'CollectionPage', arts[0]['cover'], 'news', extra=itemlist,
                breadcrumb=[('首页', ''), ('新闻资讯', 'news.html'), (name, cat_file(slug))])


# ---------------------------------------------------------------- 新闻详情
def build_article(a):
    base = '../'
    content = render_body(a['body'], base)
    rel = [x for x in ARTICLES if x['slug'] != a['slug']][:3]
    rel_html = ''.join(f'<a class="chip" href="{x["slug"]}.html">{x["title"][:22]}…</a>' for x in rel)
    cat_url = f'../{cat_file(CAT_SLUG[a["cat"]])}'
    body = f'''<section class="page-hero compact"><div class="container">
<span class="eyebrow">NEWS / <a href="{cat_url}">{a['cat']}</a></span>
<div class="breadcrumb"><a href="../index.html">首页</a><span>/</span><a href="../news.html">新闻资讯</a><span>/</span><a href="{cat_url}">{a['cat']}</a><span>/</span>正文</div>
</div></section>

<section class="section tight news-list-section"><div class="container">
<div class="article-head"><h1 class="h2">{a['title']}</h1>
<div class="article-meta"><span>发布日期：{a['date']}</span><span>栏目：<a href="{cat_url}">{a['cat']}</a></span><span>莞促集团</span></div></div>
<div class="article-cover"><img src="../assets/img/{a['cover']}" alt="{a['title']}"></div>
<div class="prose">{content}</div>
<div class="article-nav"><a class="btn btn-ghost" href="../news.html">返回资讯列表</a><a class="btn btn-ghost" href="{cat_url}">查看{a['cat']}分类</a><a class="btn btn-primary" href="../contact.html">业务咨询</a></div>
<div class="tag-list" style="margin:30px 0 0"><span class="pill">相关资讯</span>{rel_html}</div>
</div></section>

{cta_block('与莞促集团同行', '业务咨询、产业合作与资源对接，欢迎随时联络。', base)}'''
    ld_extra = None
    return page(a['file'], a['title'] + '｜莞促集团新闻资讯', a['desc'], a['keywords'],
                body, 'WebPage', a['cover'], 'news', extra=ld_extra, article=a,
                breadcrumb=[('首页', ''), ('新闻资讯', 'news.html'), (a['cat'], cat_file(CAT_SLUG[a['cat']]))])


# ---------------------------------------------------------------- 联系我们
def build_contact():
    items = [('电话', '0769-88763333', '集团联系电话'), ('业务咨询', '18926805827', '业务对接与咨询'),
             ('邮箱', '18926805827@139.com', '集团联系邮箱'), ('官网', 'www.guancu.com', '集团官方网站'),
             ('地址', '广东省东莞市厚街镇将军路2号悦山花园77号楼102室', '集团注册地址'),
             ('服务时间', '工作日 09:00–18:00', '咨询接待时间')]
    grid = ''.join(f'''<div class="contact-item reveal"><div class="ci">{i+1:02d}</div><h3>{t}</h3><p>{v}</p>
<p style="font-size:12px;color:var(--muted);font-weight:600;margin-top:6px">{d}</p></div>''' for i, (t, v, d) in enumerate(items))
    routes = [('企业服务与财税工商', '公司注册、代理记账、审计税筹、资质办理'),
              ('知识产权与科技申报', '商标、专利、著作权、高企认定与项目申报'),
              ('数字科技与大数据', '数据服务、平台开发、系统集成与数字化升级'),
              ('产业投资与园区合作', '产业投资、园区运营、新能源项目对接'),
              ('教育与文旅', '教育投资、文旅项目与品牌内容合作')]
    rhtml = ''.join(f'<div class="contact-item reveal"><h3>{t}</h3><p style="font-size:13.5px;line-height:1.8">{d}</p></div>' for t, d in routes)
    faq = [('如何对接具体业务？', '建议先通过电话或邮箱说明企业情况、业务类型与期望时间，由相应业务团队跟进沟通。'),
           ('需要提前准备哪些资料？', '不同业务所需材料不同，通常在明确服务范围后由对接团队提供清单；企业基础证照与经营资料可先行整理。'),
           ('是否支持线上沟通？', '标准化咨询环节支持线上沟通，涉及现场尽调、面签或资料核验的环节按业务要求线下办理。'),
           ('客户信息如何保密？', '客户资料仅在授权范围内用于业务办理，实行专人管理，未经同意不向无关第三方披露。')]
    fhtml = ''.join(f'<details class="reveal"><summary>{q}</summary><p>{x}</p></details>' for q, x in faq)
    body = f'''{page_hero('CONTACT / 联系我们', '期待与您建立连接', '业务咨询、产业合作与资源对接，欢迎通过以下方式与莞促集团联系。', '联系我们')}

<section class="section tight"><div class="container">
{sec_head('CONTACT INFO / 联系方式', '一个入口，<span class="blue">对接集团各类业务</span>')}
<div class="contact-grid">{grid}</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('CONSULT / 业务咨询', '把需求告诉我们')}
<form class="form-box reveal" id="consult-form">
<div class="form-row">
<div><label for="c-name">姓名</label><input id="c-name" name="name" type="text" placeholder="请输入姓名" required></div>
<div><label for="c-company">单位名称</label><input id="c-company" name="company" type="text" placeholder="请输入单位名称"></div>
<div><label for="c-phone">联系电话</label><input id="c-phone" name="phone" type="tel" placeholder="请输入联系电话" required></div>
<div><label for="c-topic">关注业务</label><select id="c-topic" name="topic">
<option value="企业服务与财税工商">企业服务与财税工商</option><option value="知识产权与科技申报">知识产权与科技申报</option>
<option value="数字科技与大数据">数字科技与大数据</option><option value="产业投资与园区合作">产业投资与园区合作</option>
<option value="教育与文旅">教育与文旅</option><option value="其他合作">其他合作</option></select></div>
<div class="full"><label for="c-msg">需求说明</label><textarea id="c-msg" name="message" placeholder="请简要描述您的需求"></textarea></div>
</div>
<button class="btn btn-primary btn-lg" type="submit">提交咨询</button>
<p class="note" id="form-tip">提交后将唤起邮件客户端，由专人跟进回复。</p>
</form>
</div></section>

<section class="section tight"><div class="container">
{sec_head('ROUTES / 业务对接方向', '按业务方向<span class="pink">快速找到团队</span>')}
<div class="contact-grid">{rhtml}</div>
</div></section>

<section class="section tight"><div class="container">
{sec_head('FAQ / 咨询常见问题', '沟通之前，<span class="blue">先了解这些</span>')}
<div class="faq">{fhtml}</div>
</div></section>'''
    return page('contact.html', '联系我们｜莞促集团电话、邮箱、地址与业务咨询',
                '联系莞促集团：电话0769-88763333，业务咨询18926805827，邮箱18926805827@139.com，地址广东省东莞市厚街镇将军路2号悦山花园77号楼102室。',
                '莞促集团联系方式,莞促集团电话,莞促集团地址,业务咨询,东莞企业服务',
                body, 'ContactPage', 'biz-service.jpg', 'contact',
                breadcrumb=[('首页', ''), ('联系我们', 'contact.html')])


# ---------------------------------------------------------------- 网站地图
def build_sitemap_page():
    main = ''.join(f'<a href="{f}">{n}</a>' for n, f, k in NAV if k != 'index')
    pages = ''.join(f'<a href="{news_filename(i)}">新闻资讯 第 {i} 页</a>' for i in range(2, NEWS_PAGES + 1))
    svc = ''.join(f'<a href="services.html#s{int(s["num"])}">{s["name"]}</a>' for s in SERVICES)
    grp = ''.join(f'<a href="companies.html#g{i+1}">{g[1]}</a>' for i, g in enumerate(COMPANY_GROUPS))
    half = (len(ARTICLES) + 1) // 2
    news_a = ''.join(f'<a href="{a["file"]}">{a["title"]}</a>' for a in ARTICLES[:half])
    news_b = ''.join(f'<a href="{a["file"]}">{a["title"]}</a>' for a in ARTICLES[half:])
    cats = ''.join(f'<a href="{cat_file(slug)}">{name}（{cat_count(name)}）</a>'
                   for name, slug, _ in CATEGORIES)
    total_pages = 7 + (NEWS_PAGES - 1) + len(ARTICLES) + len(CATEGORIES)
    body = f'''{page_hero('SITEMAP / 网站地图', '全站内容，一页可达', '按栏目整理的全部页面与文章入口，方便快速定位所需信息。', '网站地图')}

<section class="section tight"><div class="container">
<div class="sitemap-grid">
<div class="sitemap-box reveal"><h3>主导航栏目</h3><a href="index.html">首页</a>{main}{pages}</div>
<div class="sitemap-box reveal"><h3>业务板块</h3>{svc}</div>
<div class="sitemap-box reveal"><h3>集团版图</h3>{grp}</div>
</div>
<div class="sitemap-box reveal" style="margin-top:20px"><h3>新闻资讯分类</h3><div class="cat-links">{cats}</div></div>
<div class="grid-2" style="margin-top:20px">
<div class="sitemap-box reveal"><h3>新闻资讯文章（1—{half}）</h3>{news_a}</div>
<div class="sitemap-box reveal"><h3>新闻资讯文章（{half+1}—{len(ARTICLES)}）</h3>{news_b}</div>
</div>
<p class="note" style="margin-top:22px">全站共 {total_pages} 个内容页面 · 共 {len(ARTICLES)} 篇资讯 · {len(CATEGORIES)} 个文章分类 · 最近更新 {TODAY}</p>
</div></section>

{cta_block('需要帮助？', '如果一时没有找到想要的内容，欢迎直接与集团联系。')}'''
    return page('sitemap.html', '网站地图｜莞促集团全站页面与文章入口',
                '莞促集团官网网站地图，汇总主导航栏目、六大业务板块、集团成员企业分组与9篇新闻资讯文章的全部入口。',
                '莞促集团网站地图,sitemap,全站导航,栏目索引',
                body, 'WebPage', 'biz-arch.jpg', 'sitemap',
                breadcrumb=[('首页', ''), ('网站地图', 'sitemap.html')])


# ---------------------------------------------------------------- 404
def build_404():
    """独立生成 404：noindex,follow、无 canonical/OG/结构化数据、无自动跳转，仅普通链接入口。"""
    base = ''
    links = ''.join(
        f'<a class="card" href="{f}"><span class="num">LINK {i+1:02d}</span><h3 class="h3">{n}</h3></a>'
        for i, (n, f, k) in enumerate(NAV))
    body = f'''<section class="page-hero"><div class="container">
<span class="eyebrow">404 / PAGE NOT FOUND</span>
<h1 class="h2" style="font-size:clamp(30px,3.6vw,48px)">页面暂时无法访问</h1>
<p class="lead">您访问的页面不存在或已调整位置，请从首页、网站地图或下方栏目入口继续浏览。</p>
<div class="article-nav"><a class="btn btn-primary" href="index.html">返回首页</a><a class="btn btn-ghost" href="sitemap.html">查看网站地图</a></div>
</div></section>

<section class="section tight"><div class="container">
<div class="sec-head"><span class="eyebrow">QUICK LINKS / 常用入口</span><h2 class="h2">从这些<span class="blue">页面继续</span></h2></div>
<div class="grid-4">{links}</div>
</div></section>'''
    doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>页面未找到｜莞促集团</title>
<meta name="description" content="您访问的页面不存在或已调整，请从莞促集团官网首页或网站地图继续浏览。">
<meta name="robots" content="noindex,follow">
<link rel="icon" href="{base}assets/img/favicon.ico" sizes="any">
<link rel="icon" href="{base}assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{base}assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="{base}assets/css/style.css">
</head>
<body data-page="">
{header(base, '')}
<main>
{body}
</main>
{footer(base)}
<script src="{base}assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8') as fh:
        fh.write(doc)
    return '404.html'


# ---------------------------------------------------------------- SEO 文件
def build_seo_files(paths):
    urls = []
    for p in paths:
        if p == '404.html':
            continue
        loc = SITE + '/' + p
        if p == 'index.html':
            pri, freq = '1.0', 'weekly'
        elif p in ('news.html', 'sitemap.html'):
            pri, freq = '0.8', 'weekly'
        elif p.startswith('news-'):
            pri, freq = '0.5', 'weekly'
        elif p.startswith('category/'):
            pri, freq = '0.7', 'weekly'
        elif p.startswith('news/'):
            pri, freq = '0.6', 'monthly'
        else:
            pri, freq = '0.8', 'monthly'
        urls.append(f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>''')
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(urls) + '\n</urlset>\n'
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(xml)
    robots = f'''# 莞促集团官网 · 搜索引擎抓取规则
# 404.html 由服务器返回 404 状态并标记 noindex,follow，不在此禁止抓取
User-agent: *
Allow: /
Allow: /assets/

User-agent: Baiduspider
Allow: /
Allow: /assets/

User-agent: Googlebot
Allow: /
Allow: /assets/

Host: www.guancu.com
Sitemap: {SITE}/sitemap.xml
'''
    with open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots)
    with open(os.path.join(ROOT, 'CNAME'), 'w', encoding='utf-8') as f:
        f.write('www.guancu.com\n')
    with open(os.path.join(ROOT, '.nojekyll'), 'w', encoding='utf-8') as f:
        f.write('')
    # 便于提交到百度资源搜索平台 / Google Search Console 的 URL 清单
    all_urls = [SITE + '/' + p for p in paths if p != '404.html']
    with open(os.path.join(ROOT, 'urls.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_urls) + '\n')
    news_urls = ([SITE + '/' + a['file'] for a in ARTICLES]
                 + [SITE + '/' + cat_file(slug) for _, slug, _ in CATEGORIES])
    with open(os.path.join(ROOT, 'news-urls.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(news_urls) + '\n')
    return len(urls)


def main():
    paths = []
    paths.append(build_index())
    paths.append(build_about())
    paths.append(build_services())
    paths.append(build_companies())
    for i in range(1, NEWS_PAGES + 1):
        paths.append(build_news_list(i))
    paths.append(build_contact())
    paths.append(build_sitemap_page())
    for a in ARTICLES:
        paths.append(build_article(a))
    for name, slug, desc in CATEGORIES:
        paths.append(build_category(name, slug, desc))
    paths.append(build_404())
    n = build_seo_files(paths)
    print('生成页面：', len(paths), '个 HTML；sitemap.xml 收录：', n, '个 URL')
    print('新闻文章：', len(ARTICLES), '篇；列表分页：', NEWS_PAGES, '页；文章分类：', len(CATEGORIES), '个')
    for p in paths:
        print('  ', p)


if __name__ == '__main__':
    main()
