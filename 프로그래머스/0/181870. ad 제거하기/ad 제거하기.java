import java.util.*;
class Solution {
    public String[] solution(String[] strArr) {
        ArrayList<String> lst = new ArrayList<>();
        for(int i=0; i<strArr.length; i++){
            if(strArr[i].indexOf("ad") == -1){
                lst.add(strArr[i]);
            }
        }
        String[] answer = new String[lst.size()];
        for(int i=0; i<answer.length; i++){
            answer[i] = lst.get(i);
        }
        return answer;
    }
}