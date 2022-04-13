from django.core.cache.backends.redis import RedisCache
from typing import Optional


class TacticalRedisCache(RedisCache):
    def delete_many_pattern(self, pattern: str, version: Optional[int] = None) -> None:
        keys = self._cache.get_client().keys(f":{version if version else 1}:{pattern}")

        if keys:
            self._cache.delete_many(keys)