import java.util.HashMap;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Boolean> hashMap = new HashMap<>();
        for(String phone : phone_book){
            hashMap.put(phone, true);      
        }
        for(String phone : phone_book){
            for(int i=1; i<phone.length(); i++){
                if(hashMap.containsKey(phone.substring(0,i))){
                    return false;
                }
            }
        }
        return true;
    }
}