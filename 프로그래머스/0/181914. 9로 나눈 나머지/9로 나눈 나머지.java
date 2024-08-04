class Solution {
    public int solution(String number) {
        int answer = 0;
        int sm = 0;
        for(int i=0; i<number.length(); i++){
            sm += Integer.parseInt(number.charAt(i)+"");
        }
        answer = sm%9;
        return answer;
    }
}