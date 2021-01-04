/// attempt 1
var twoSum = function(nums, target) {
    for(var i=0;i<nums.length;i++){
        var temp = target-nums[i]
        for (var x= 0; x<nums.length; x++ ){
            if(temp == nums[x] && x != i){
                return[i,x]
               }
        }
    }
};


// attempt 2
var twoSum = function(nums, target) {
    let obj = {};
    for(var i=0;i< nums.length;i++){
        let attamptNumber = target - nums[i];
        if (attamptNumber in obj){
            return [obj[attamptNumber] ,i]
        }
        obj[nums[i]] = i;
    }
};
