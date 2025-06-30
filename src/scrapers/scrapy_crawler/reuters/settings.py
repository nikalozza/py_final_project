USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
BOT_NAME = "aljazeera"
SPIDER_MODULES = ["reuters.spiders"]  # name may change to aljazeera.spiders
NEWSPIDER_MODULE = "reuters.spiders"  # adjust if renaming directories
ITEM_PIPELINES = {
    'reuters.pipelines.AlJazeeraPipeline': 300,  # ✅ exact class name match
}
