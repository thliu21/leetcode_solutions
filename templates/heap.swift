class MinHeap {
    private var heap = [(Int, Int)]()
    
    func top() -> (Int, Int)? {
        heap[0]
    }
    
    var size: Int {
        heap.count
    }
    
    func pop() -> (Int, Int)? {
        if heap.count == 0 {
            return nil
        }
        let ret0 = heap[0].0
        let ret1 = heap[0].1
        if size > 0,
           let temp = heap.popLast() {
            heap[0] = temp
            self.pushDown(cur: 0)
        }
        return (ret0, ret1)
    }
    
    func add(_ value: Int, _ idx: Int) {
        heap.append((value, idx))
        pushUp(cur: size-1)
    }
    
    private func pushDown(cur: Int) {
        if cur > size {
            return
        }
        if cur*2 < size && heap[cur*2] < heap[cur] {
            let temp = heap[cur]
            heap[cur] = heap[cur*2]
            heap[cur*2] = temp
            self.pushDown(cur: cur*2)
        }
        if cur*2+1 < size && heap[cur*2+1] < heap[cur] {
            let temp = heap[cur]
            heap[cur] = heap[cur*2+1]
            heap[cur*2+1] = temp
            self.pushDown(cur: cur*2+1)
        }
    }
    
    private func pushUp(cur: Int) {
        if cur == 0 {
            return
        }
        let parent = (cur-1) / 2
        if heap[parent] > heap[cur] {
            let temp = heap[cur]
            heap[cur] = heap[parent]
            heap[parent] = temp
            self.pushUp(cur: parent)
        }
    }
}