class Solution {
    public int solution(int[] num_list) {
        int n = num_list.length;
        if(n>=11){
            int sm = 0;
            for(int i:num_list){
                sm+=i;
            }
            return sm;
        }else{
            int mul = 1;
            for(int i:num_list){
                mul*=i;
            }
            return mul;
        }
    }
}