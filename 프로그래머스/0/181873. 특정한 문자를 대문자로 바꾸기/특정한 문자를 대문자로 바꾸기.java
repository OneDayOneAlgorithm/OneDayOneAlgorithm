class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
        for(int i=0; i<my_string.length(); i++){
            if((my_string.charAt(i)+"").equals(alp)){
                answer += (my_string.charAt(i)+"").toUpperCase();
            }else{
                answer += (my_string.charAt(i)+"");
            }
        }
        return answer;
    }
}