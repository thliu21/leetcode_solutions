extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}

public extension String {
    
    /**
     Enables passing in negative indices to access characters
     starting from the end and going backwards.
     if num is negative, then it is added to the
     length of the string to retrieve the true index.
     */
    func negativeIndex(_ num: Int) -> Int {
        return num < 0 ? num + self.count : num
    }
    
    func strOpenRange(index i: Int) -> Range<String.Index> {
        let j = negativeIndex(i)
        return strOpenRange(j..<(j + 1), checkNegative: false)
    }
    
    func strOpenRange(
        _ range: Range<Int>, checkNegative: Bool = true
    ) -> Range<String.Index> {

        var lower = range.lowerBound
        var upper = range.upperBound

        if checkNegative {
            lower = negativeIndex(lower)
            upper = negativeIndex(upper)
        }
        
        let idx1 = index(self.startIndex, offsetBy: lower)
        let idx2 = index(self.startIndex, offsetBy: upper)
        
        return idx1..<idx2
    }
    
    func strClosedRange(
        _ range: CountableClosedRange<Int>, checkNegative: Bool = true
    ) -> ClosedRange<String.Index> {
        
        var lower = range.lowerBound
        var upper = range.upperBound

        if checkNegative {
            lower = negativeIndex(lower)
            upper = negativeIndex(upper)
        }
        
        let start = self.index(self.startIndex, offsetBy: lower)
        let end = self.index(start, offsetBy: upper - lower)
        
        return start...end
    }
    
    // MARK: - Subscripts
    
    /**
     Gets and sets a character at a given index.
     Negative indices are added to the length so that
     characters can be accessed from the end backwards
     
     Usage: `string[n]`
     */
    subscript(_ i: Int) -> String {
        get {
            return String(self[strOpenRange(index: i)])
        }
        set {
            let range = strOpenRange(index: i)
            replaceSubrange(range, with: newValue)
        }
    }
    
    
    /**
     Gets and sets characters in an open range.
     Supports negative indexing.
     
     Usage: `string[n..<n]`
     */
    subscript(_ r: Range<Int>) -> String {
        get {
            return String(self[strOpenRange(r)])
        }
        set {
            replaceSubrange(strOpenRange(r), with: newValue)
        }
    }

    /**
     Gets and sets characters in a closed range.
     Supports negative indexing
     
     Usage: `string[n...n]`
     */
    subscript(_ r: CountableClosedRange<Int>) -> String {
        get {
            return String(self[strClosedRange(r)])
        }
        set {
            replaceSubrange(strClosedRange(r), with: newValue)
        }
    }
    
    /// `string[n...]`. See PartialRangeFrom
    subscript(r: PartialRangeFrom<Int>) -> String {
        
        get {
            return String(self[strOpenRange(r.lowerBound..<self.count)])
        }
        set {
            replaceSubrange(strOpenRange(r.lowerBound..<self.count), with: newValue)
        }
    }
    
    /// `string[...n]`. See PartialRangeThrough
    subscript(r: PartialRangeThrough<Int>) -> String {
        
        get {
            let upper = negativeIndex(r.upperBound)
            return String(self[strClosedRange(0...upper, checkNegative: false)])
        }
        set {
            let upper = negativeIndex(r.upperBound)
            replaceSubrange(
                strClosedRange(0...upper, checkNegative: false), with: newValue
            )
        }
    }
    
    /// `string[...<n]`. See PartialRangeUpTo
    subscript(r: PartialRangeUpTo<Int>) -> String {
        
        get {
            let upper = negativeIndex(r.upperBound)
            return String(self[strOpenRange(0..<upper, checkNegative: false)])
        }
        set {
            let upper = negativeIndex(r.upperBound)
            replaceSubrange(
                strOpenRange(0..<upper, checkNegative: false), with: newValue
            )
        }
    }
}

struct Node: Hashable {
    let x: Int
    let y: Int
}

class Solution {
    func dfs(_ i: Int, _ j: Int, _ row: Int, _ col: Int, _ board: [[Character]], _ word: String, _ visited: inout Set<Node>) -> Bool {
        if word.count == 0 {
            return true
        }
        if i < 0 || j < 0 || i >= row || j >= col {
            return false
        }
        if visited.contains(Node(x: i, y: j)) {
            return false
        }
        visited.insert(Node(x: i, y: j))
        if board[i][j] != word[0] {
            return false
        }
        let m_x = [0, 0, 1, -1]
        let m_y = [1, -1, 0, 0]
        for p in 0...3 {
            let n_i = i + m_x[p]
            let n_j = j + m_y[p]
            if self.dfs(n_i, n_j, row, col, board, word[1...], &visited) {
                return true
            }
        }
        visited.remove(Node(x: i, y: j))
        return false
    }

    func exist(_ board: [[Character]], _ word: String) -> Bool {
        let row = board.count
        let col = board[0].count
        for i in (0..<row) {
            var visited = Set<Node>()
            for j in (0..<col) {
                if dfs(i, j, row, col, board, word, &visited) {
                    return true
                }
            }
        }
        return false
    }
}

let s = Solution()
let sol = s.exist([["a","b"]], "ba")
print(sol)