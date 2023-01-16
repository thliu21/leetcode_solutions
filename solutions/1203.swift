class Graph {
    var nodes = Set<Int>()
    var edges = [Int: Set<Int>]()
    private var inDegree = [Int: Int]()

    func addNode(_ node: Int) {
        nodes.insert(node)
    }

    func addEdge(_ n: Int, _ m: Int) {
        addNode(n)
        addNode(m)
        if inDegree[m] == nil {
            inDegree[m] = 0
        }
        if edges[n] == nil {
            edges[n] = Set<Int>()
        }
        if let edge = edges[n],
           !edge.contains(m) {
            edges[n]!.insert(m)
            inDegree[m]! += 1
        }
    }
    
    func topoSort() -> [Int]? {
        var ret = [Int]()
        var zeroInd = [Int]()
        var indCopy = [Int: Int]()
        inDegree.forEach { node, ind in
            indCopy[node] = ind
        }
        
        nodes.forEach { node in
            let ind = indCopy[node] ?? 0
            if ind == 0 {
                zeroInd.append(node)
            }
        }
        
        while zeroInd.count > 0 {
            let node = zeroInd.last!
            zeroInd.removeLast()
            ret.append(node)
            edges[node]?.forEach { edge in
                guard indCopy[edge] != nil else { return }
                indCopy[edge]! -= 1
                if indCopy[edge] == 0 {
                    zeroInd.append(edge)
                }
            }
        }
        if ret.count == nodes.count {
            return ret
        }
        return nil
    }
}

class Solution {
    func sortItems(_ n: Int, _ m: Int, _ group: [Int], _ beforeItems: [[Int]]) -> [Int] {
        var groupItems = [Int: Set<Int>]()
        let groupGraph = Graph()
        var indvGroupGraph = [Int: Graph]()
        let newGroup = group.enumerated().map { $1 == -1 ? $0 + m : $1 }
        newGroup.enumerated().forEach { item, group in
            if !groupItems.keys.contains(group) {
                groupGraph.addNode(group)
                groupItems[group] = Set<Int>()
            }
            groupItems[group]?.insert(item)
            if !indvGroupGraph.keys.contains(group) {
                indvGroupGraph[group] = Graph()
            }
            indvGroupGraph[group]?.addNode(item)
        }
        
        beforeItems.enumerated().forEach { idx, beforeItem in
            beforeItem.forEach { item in
                let beforeGroup = newGroup[item]
                let afterGroup = newGroup[idx]
                if beforeGroup != afterGroup {
                    groupGraph.addEdge(beforeGroup, afterGroup)
                } else {
                    indvGroupGraph[beforeGroup]?.addEdge(item, idx)
                }
            }
        }
        
        guard let groupOrder = groupGraph.topoSort()
        else { return [] }
        
        var ret = [Int]()
        for group in groupOrder {
            if !indvGroupGraph.keys.contains(group) {
                ret.append(contentsOf: groupItems[group] ?? [])
            } else {
                if let topo = indvGroupGraph[group]?.topoSort() {
                    ret.append(contentsOf: topo)
                } else {
                    return []
                }
            }
        }
        return ret
    }
}

let s = Solution()
let sol = s.sortItems(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]])
print(sol)
