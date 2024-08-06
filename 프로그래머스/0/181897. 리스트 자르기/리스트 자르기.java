import java.util.ArrayList;
class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        ArrayList<Integer> answer = new ArrayList<>();
        switch(n){
            case 1:
                for(int i=0; i<=slicer[1]; i++){
                    answer.add(num_list[i]);
                }
                break;
            case 2:
                for(int i=slicer[0]; i<num_list.length; i++){
                    answer.add(num_list[i]);
                }
                break;
            case 3:
                for(int i=slicer[0]; i<=slicer[1]; i++){
                    answer.add(num_list[i]);
                }
                break;
            case 4:
                for(int i=slicer[0]; i<=slicer[1]; i+=slicer[2]){
                    answer.add(num_list[i]);
                }
                break;
            default:
                break;
        }
        int[] lst = new int[answer.size()];
        for (int i=0; i< lst.length; i++){
            lst[i] = answer.get(i);
        }
        return lst;
        
        
        
        
        
        // switch(n){
        //     case 1: 
        //         int[] answer1 = new int[slicer[1]+1];
        //         for(int i=0; i<=slicer[1]; i++){
        //             answer1[i] = num_list[i];
        //         }
        //         return answer1;
        //     case 2: 
        //         int[] answer2 = new int[num_list.length - slicer[0] + 1];
        //         for(int i=slicer[0]; i<=num_list.length; i++){
        //             answer2[i] = num_list[i];
        //         }
        //         return answer2;
        //     case 3: 
        //         int[] answer3 = new int[slicer[1] - slicer[0] + 1];               
        //         for(int i=0; i<slicer[1] - slicer[0] + 1; i++){
        //             answer3[i] = num_list[i+slicer[0]];
        //         }
        //         return answer3;
        //     case 4: 
        //         int k = (slicer[1] - slicer[0]) / slicer[2] + 1;
        //         int[] answer4 = new int[k];
        //         for(int i=0; i<k; i++){
        //             answer4[i] = num_list[slicer[0]+i*slicer[2]];
        //         }
        //         return answer4;
        //     default: break;
        // }
        // int[] a = new int[0];
        // return a;
    }
}