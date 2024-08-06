class Solution {
    public int[] solution(int start_num, int end_num) {
        int n = start_num-end_num;
        int[] answer = new int[n+1];
        for(int i = 0; i<n+1; i++){
            answer[i] = start_num - i; 
        }
        return answer;
    }
}