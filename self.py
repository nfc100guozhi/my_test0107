class CacheManager:
    def __init__(self):
        self.cache = {}

    def add_item(self, key, value):
        self.cache[key] = value

    def remove_item(self, key):
        if key in self.cache:
            del self.cache[key]

    def check_unused_cache(self, condition_func):
        unused_keys = []
        for key, value in self.cache.items():
            if condition_func(value):
                unused_keys.append(key)
        
        return unused_keys

# 示例条件函数：检查缓存项是否过期
def is_expired(value):
    # 在这里根据您的需求判断缓存项是否过期，返回True表示过期
    return value['expiration_time'] < time.time()

# 创建缓存管理器
cache_manager = CacheManager()

# 示例：添加缓存项
cache_manager.add_item('key1', {'data': 'value1', 'expiration_time': some_timestamp})
cache_manager.add_item('key2', {'data': 'value2', 'expiration_time': some_timestamp})

# 检查无用缓存
unused_cache_keys = cache_manager.check_unused_cache(is_expired)

# 移除无用缓存项
for key in unused_cache_keys:
    cache_manager.remove_item(key)
