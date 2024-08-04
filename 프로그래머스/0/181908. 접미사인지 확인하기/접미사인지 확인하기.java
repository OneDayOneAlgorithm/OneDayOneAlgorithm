class Solution {
    public int solution(String my_string, String is_suffix) {
        for(int i=0; i<my_string.length(); i++){
            if(is_suffix.equals(my_string.substring(my_string.length()-1-i))){
                return 1;
            }
        }
        return 0;
    }
}