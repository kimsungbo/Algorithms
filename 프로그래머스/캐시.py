def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cache = []
    
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
            elif city not in cache:
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
               

    return answer