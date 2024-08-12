import java.util.*;
class Solution {
    public String[] solution(String myString) {
        ArrayList<String> arr = new ArrayList<>();
        String s = "";
        for(int i=0; i<myString.length(); i++){
            if(myString.charAt(i)=='x'){
                if(!s.equals("")){
                    arr.add(s);
                }
                s = "";
            }else{
                s+=myString.charAt(i);
            }
        }
        if(!s.equals("")){
            arr.add(s);
        }
        String[] answer = new String[arr.size()];
        for(int i=0; i<answer.length; i++){
            answer[i] = arr.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}