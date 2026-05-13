//import "container/list"

type pair struct {
	key, value int
}

type LRUCache struct {
	cache    map[int]*list.Element
	queue    *list.List
	capacity int
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		cache:    make(map[int]*list.Element),
		queue:    list.New(),
	}
}

func (this *LRUCache) Get(key int) int {
	element, ok := this.cache[key]
	if !ok {
		return -1
	}
	this.queue.MoveToFront(element)
	return element.Value.(*pair).value
}

func (this *LRUCache) Put(key int, value int) {
	// If key exists: update value and move node to front
	if element, ok := this.cache[key]; ok {
		element.Value.(*pair).value = value
		this.queue.MoveToFront(element)
		return
	}

	// If at capacity: evict least recently used (back)
	if this.queue.Len() >= this.capacity {
		lru := this.queue.Back()
		if lru != nil {
			kv := lru.Value.(*pair)
			delete(this.cache, kv.key)
			this.queue.Remove(lru)
		}
	}

	// Insert new node at front and record it in the map
	element := this.queue.PushFront(&pair{key: key, value: value})
	this.cache[key] = element
}
