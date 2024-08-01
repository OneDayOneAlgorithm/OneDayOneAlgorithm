class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        int n = num_list.length;
        for(int i=0; i<n; i++){
            answer[i] = num_list[i];
        }
        if(num_list[n-1] > num_list[n-2]){
            answer[n] = num_list[n-1] - num_list[n-2];
        }else{
            answer[n] = num_list[n-1]*2;
        }
        return answer;
    }
}