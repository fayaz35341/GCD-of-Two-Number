class Solution {
    gcd(a, b) {
        // code here
        let c1=[]
        for (let i=1;i<=Math.min(a,b);i++){
            if (a%i===0 && b%i===0){
                c1.push(i)
            }
        }
        return Math.max(...c1)
    }
}
console.log(new Solution().gcd(4,6))

// another
