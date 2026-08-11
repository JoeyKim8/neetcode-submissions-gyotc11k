class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        int count = 0; // initialize the count
        int max = 0; // initialize the max count

        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 1){
                count++; // this adds the count of ones
            }
            else {
                count = 0; // resets the count back to 0 if theres a 0
            }

            if (count > max){ // everytime we get a new max, add to the 'max' count
                max = count;
            }

        }
        return max;
    }
}