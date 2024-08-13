class Solution {
    public int solution(String[] strArr) {
        int[] arr = new int[31];
        for(int i=0; i<strArr.length; i++){
            arr[strArr[i].length()]++;
        }
        int answer = 0;
        for(int i=1; i<31; i++){
            if(arr[i] > answer){
                answer = arr[i];
            }
        }
        return answer;
    }
}