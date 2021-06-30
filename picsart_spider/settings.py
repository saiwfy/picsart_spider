# Scrapy settings for picsart_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
KEYWORDS = [
    # '格子',
    # 'lv',
    # 'gucci',
    # 'chanel',
    # '涂鸦',
    # '动漫',
    # '联名',
    # 'blackpink',
    # ------------
    # 'lisa',
    # '漫威',
    # '哈利波特',
    # 'hello kitty',
    # -------------以下只获取40页
    # '潮牌logo',
    # '中文',
    # '英文',
    # '日文',
    # -----------------
    # 'burberry',
    # 'prada',
    # 'balenciaga',
    # 'nike',
    # 'adidas',
    # 'vans',
    # --------------
    # 'puma',
    # 'converse',
    # 'superme',
    # 'champion',
    # 'dickies',
    # '川久保玲',
    # 'thrasher',
    # 'kenzo',
    # 'logo',
    # '复古',
    # '蕾丝',
    # -----------以下只爬30页
    # '蝴蝶',
    # '玫瑰',
    # '蒸汽波',
    # 'outline',
    # '翅膀',
    # '霓虹',
    # '头像',
    # '少女',
    # '古风',
    # '花朵',
    # '王俊凯',
    # '蔡徐坤',
    # '王一博',
    # 'tfboys',
    # '杂志',
    # '动漫少女',
    # '动漫人物',
    # '海贼王',
    # '火影忍者',
    # '银魂',
    # 'jojo',
    # '我的英雄学院',
    # '口袋妖怪',
    # '梦幻',
    # '童话',
    # '魔法',
    # 'dior',
    # 20201015----------------
    # '人物',
    # '头像',
    # '人像',
    # '潮酷',
    # '星黛露',
    # '卡通',
    # ----------
    # '童话',
    # '星空',
    # '宇宙',
    # '天空',
    # '皮卡丘',
    # '狐妖',
    # '动漫人物',
    # ---------------
    # '少女',
    # '雏菊',
    # '王者荣耀',
    # '渐变',
    # '桃子',
    # '草莓',
    # '扣子',
    # '桃子',
    # ----------------
    # '漫画',
    # '背景',
    # '美少女',
    # '星球',
    # '万圣',
    # '帅气',
    # '小马宝莉',
    # '芭比',
    # '糖果',
    # '美少女战士',
    # '易烊千玺',
    # '太阳',
    # '油画',
    # '男生',
    # '恶魔',
    # '花边',
    # '草',
    # '领带',
    # '领结',
    # '鸟',
    # 'ins',
    # '卡通人物',
    # '仙女',
    # '迪士尼公主',
    # '线条',
    # '网格',
    # '口袋',
    # '秋天',
    # '冬天'
    # 20201019-----------------
    # '南瓜',
    # '蝙蝠',
    # '女巫',
    # '棕色',
    # '蜘蛛网',
    # '幽灵'
    # 'dogbone',
    # '狗',
    # '小狗',
    # '感恩',
    # '圣诞',
    # '圣诞节',
    # '驯鹿',
    # '铃铛',
    # '礼物',
    # '花纹',
    # '肖战',
    # '泫雅',
    # 'BTS',
    # 'EXO',
    # 'NINE PERCENT',
    # '赖冠霖',
    # 'TFBOYS',
    # 'R1SE',
    # '吴亦凡',
    # '雪花',
    # '雪人',
    # '雪'
    # '条纹',
    # '纹理'
    # '元旦',
    # '新年'
    # '奶牛',
    # '牛',
    # '2021',
    # '格纹',
    # '中国风',
    # '油画',
    # '和风',
    # '中国风',
    # '线条',
    # '玫瑰',
    # '蝴蝶',
    # '蝴蝶结',
    # '樱花',
    # '烟花',
    # '日本',
    # '中国',
    # '花鸟',
    # '水墨',
    # '锦鲤',
    # '古典',
    # 'among us',

    # 'Marvel',
    # 'DC',
    # '美国队长',
    # '超人',
    # '蜘蛛侠',
    # '钢铁侠',
    # '绿巨人',
    # '蝙蝠侠',
    # '米奇',
    # '鬼灭',
    # '绿',
    # '白',
    # '熊猫',
    # '海绵宝宝',
    # '彩虹',
    # '星空',
    # '波点',
    # '像素',
    # 'minecraft'
    # '彩蛋',
    # '复活节'
    # 'pubg',
    # '迷彩',
    'pubg'
]

DOWNLOADER_MIDDLEWARES = {
    'picsart_spider.middlewares.ChromeDownloaderMiddleware': 543,
}

BOT_NAME = 'picsart_spider'

SPIDER_MODULES = ['picsart_spider.spiders']
NEWSPIDER_MODULE = 'picsart_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'picsart_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'picsart_spider.middlewares.PicsartSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'picsart_spider.middlewares.PicsartSpiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'picsart_spider.pipelines.PicsartSpiderPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
