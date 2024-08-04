class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = my_string.substring(0,s);
        for(int i=s; i<e+1; i++){
            answer += my_string.charAt(e+s-i);
        }
        answer += my_string.substring(e+1);
        return answer;
    }
}