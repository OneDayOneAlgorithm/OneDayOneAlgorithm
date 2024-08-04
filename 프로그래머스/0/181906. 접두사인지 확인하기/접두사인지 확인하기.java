class Solution {
    public int solution(String my_string, String is_prefix) {
        int n = my_string.length();
        for(int i=1; i<=n; i++){
            if(is_prefix.equals(my_string.substring(0,i))){
                return 1;
            }
        }
        return 0;
    }
}