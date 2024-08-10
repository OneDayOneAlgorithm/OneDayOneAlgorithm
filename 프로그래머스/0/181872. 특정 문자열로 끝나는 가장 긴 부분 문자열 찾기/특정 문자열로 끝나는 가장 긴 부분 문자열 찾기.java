class Solution {
    public String solution(String myString, String pat) {
        String answer = "";
        int idx = myString.lastIndexOf(pat);
        for(int i=0; i<idx+pat.length(); i++){
            answer+=myString.charAt(i);
        }
        return answer;
    }
}