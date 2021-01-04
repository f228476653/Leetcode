import java.util.*;

public class Find_the_Duplicate_Number_287 {
    public static int findDuplicate(int[] nums) {
        // sort
        //and find duplicate

        Arrays.sort(nums);
        Map<Integer,Integer> a = new HashMap<>();
        for(int i =0; i<nums.length; i++){
            if(a.containsKey(nums[i])){
                return nums[i];
            }
            a.put(nums[i],1);
        }
        return 0;
    }
    public static void main(String[] args){
        int b =findDuplicate(new int[]{1,4,2,2,3});
        System.out.println(b);
    }
}
