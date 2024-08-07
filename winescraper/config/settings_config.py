
def get_tannico_settings():
    return {
        "FEEDS": {
            "tannico_data.json": {"format": "json", "indent": 4, "overwrite": True}
        },
        "ITEM_PIPELINES": {
            "winescraper.pipelines.TannicoPipeline": 300,
            # "winescraper.pipelines.WinescraperDataBasePipeline": 400
        },
        "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7",
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "FEED_EXPORT_ENCODING": "utf-8",
        "ROBOTSTXT_OBEY": False,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 15,
        "AUTOTHROTTLE_MAX_DELAY": 60,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 1.0,
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "HTTPCACHE_ENABLED": False

    }


def get_tannico_settings_without_vivino():
    return {
        "FEEDS": {
            # "tannico_data_without_vivino.json": {"format": "json",  "indent": 4, "overwrite": True}
            "tannico_data_without_vivino.json": {"format": "json",  "overwrite": True}
        },
        "ITEM_PIPELINES": {
            "winescraper.pipelines.TannicoPipeline": 300
        },
        "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7",
        "FEED_EXPORT_ENCODING": "utf-8",
        "ROBOTSTXT_OBEY": False,
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "HTTPCACHE_ENABLED": False

        # "PLAYWRIGHT_LAUNCH_OPTIONS": {
        #     "headless": False,
        # }
    }


def get_callmewine_settings_without_vivino():
    return {
        "FEEDS": {
            # "tannico_data_without_vivino.json": {"format": "json",  "indent": 4, "overwrite": True}
            "callmewine_data_without_vivino.json": {"format": "json",  "overwrite": True}
        },
        "ITEM_PIPELINES": {
            "winescraper.pipelines.CallMeWinePipeline": 300
        },
        "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7",
        "FEED_EXPORT_ENCODING": "utf-8",
        "ROBOTSTXT_OBEY": False,
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "HTTPCACHE_ENABLED": False

        # "PLAYWRIGHT_LAUNCH_OPTIONS": {
        #     "headless": False,
        # }
    }
