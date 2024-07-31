class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sm = 0;
        int mul = 1;
        for(int i=0; i<num_list.length; i++){
            int num = num_list[i];
            sm += num;
            mul *= num;
        }
        answer = sm*sm > mul ? 1 : 0;
        return answer;
    }
}