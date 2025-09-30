import json
import pandas as pd
from itemadapter import ItemAdapter

class NewsscrapingPipeline:
    def open_spider(self, spider):
        self.file = open("news_vnexpress.jsonl", "w", encoding="utf-8")
        self.items = []  # keep items in memory for Excel

    def close_spider(self, spider):
        self.file.close()
        # write all items to Excel
        if self.items:
            df = pd.DataFrame(self.items)
            df.to_excel("news_vnexpress.xlsx", index=False)

    def process_item(self, item, spider):
        data = ItemAdapter(item).asdict()
        line = json.dumps(data, ensure_ascii=False) + "\n"
        self.file.write(line)
        self.items.append(data)
        return item