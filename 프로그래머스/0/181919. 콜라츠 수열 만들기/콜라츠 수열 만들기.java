import java.util.ArrayList;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(n);
        while(n!=1){
            if(n%2==0){
                n /= 2;
            }else{
                n = n*3 + 1;
            }
            answer.add(n);
        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}