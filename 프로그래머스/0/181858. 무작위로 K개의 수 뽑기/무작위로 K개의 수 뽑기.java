import java.util.*;
class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        for(int i=0; i<k; i++){
            answer[i] = -1;
        }
        boolean complete = true;
        int idx = 0;
        for(int i=0; i<arr.length; i++){
            complete = true;
            for(int j=0; j<answer.length; j++){
                if(arr[i] == answer[j]){
                    complete = false;
                    break;
                }
            }
            if(complete){
                answer[idx++] = arr[i];
                if(idx==k){
                    break;
                }
            }
        }
        return answer;
    }
}