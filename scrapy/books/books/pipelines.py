# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


def create_json_file():
    with open("books.json", "w") as f:
        f.write("[")


def append_to_json_file(item):
    
    for key, value in item.items():
        if isinstance(value, str):
            item[key] = value.replace('"', '\\"')  
        
        if key == "img_url":
            item[key] = value.replace("../", "https://books.toscrape.com/")
    
    with open("books.json", "a") as f:
        f.write(f"{item},\n")


def close_json_file():
    with open("books.json", "a") as f:
        f.write("]")


class BooksPipeline:
    def open_spider(self, spider):
        create_json_file()
    
    def close_spider(self, spider):
        close_json_file()
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter["url"] = adapter.get("url")
        adapter["title"] = adapter.get("title")
        adapter["price"] = adapter.get("price")
        adapter["img_url"] = adapter.get("img_url")
        
        append_to_json_file(adapter.asdict())
        return item
