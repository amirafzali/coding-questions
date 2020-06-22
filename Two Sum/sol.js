var twoSum = function(nums, target) {
    const lookup = {};
    nums.forEach((elm, i) => {
        let hit = target-elm;
        if(hit in lookup) return [lookup[hit],i]
        lookup[elm] = i
    })
    return [-1,-1]
};