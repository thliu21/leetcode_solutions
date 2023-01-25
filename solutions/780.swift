/*
向前倒推即可
https://www.youtube.com/watch?v=1E39PiQAGvE

python exec栈不够大会爆。。swift能过
*/

class Solution {
    func reachingPoints(_ sx: Int, _ sy: Int, _ tx: Int, _ ty: Int) -> Bool {
        if (sx > tx || sy > ty) {
            return false
        }
        if (sx == tx) {
            return (ty-sy) % sx == 0
        }
        if (sy == ty) {
            return (tx-sx) % sy == 0
        }
        
        if tx > ty {
            return self.reachingPoints(sx, sy, tx-ty, ty)
        }
        else if ty > tx {
            return self.reachingPoints(sx, sy, tx, ty-tx)
        }
        return false
    }
}