class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int num = 0;
        if(a%2 == 1 && b%2==1){
            num = 1;
        }else if(a%2 == 0 && b%2==0){
            num = 2;
        }
        switch(num){
            case 0: 
                answer = 2*(a+b);
                break;    
            case 1: 
                answer = a*a + b*b;
                break; 
            case 2:
                answer = a-b;
                if(answer<0){
                    answer *= -1;
                }
                break;
        }
    
        return answer;
    }
}