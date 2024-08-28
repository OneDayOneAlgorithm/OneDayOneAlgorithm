import java.util.HashMap;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hashMap = new HashMap<>();
        for(String part : participant){
            if(hashMap.get(part) != null){
                hashMap.put(part, hashMap.get(part)+1);
            }else{
                hashMap.put(part,1);
            }
        }
        for(String com : completion){
            hashMap.put(com, hashMap.get(com) - 1);
        }       
        for(String key : hashMap.keySet()){
            if(hashMap.get(key) != 0){
                return key;
            }
        }
        return answer;
    }
}