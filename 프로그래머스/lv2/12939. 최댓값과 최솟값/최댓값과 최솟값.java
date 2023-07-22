class Solution {
    public String solution(String a) {
        String[] s = a.split(" ");
        int mx,mn,n;
        mx = mn= Integer.parseInt(s[0]);
        for(int i=1; i<s.length;i++){
            n = Integer.parseInt(s[i]);
            if (mx<n){
                mx = n;
            }
            if (mn>n){
                mn = n;
            }
        }
        return mn + " " + mx;
    }
}