import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        ArrayList<Integer> lst = new ArrayList();
        boolean complete = true;
        for(int i=0; i<arr.length; i++){
            complete = true;
            for(int j=0; j<delete_list.length; j++){
                if(arr[i] == delete_list[j]){
                    complete = false;
                    break;
                }   
            }
            if(complete){
                lst.add(arr[i]);
            }
        }
        int[] answer = new int[lst.size()];
        for(int i=0; i<answer.length; i++){
            answer[i] = lst.get(i);
        }
        return answer;
    }
}