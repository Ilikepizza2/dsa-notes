1. Basics

    - Random

        1. Unordered_map → best = O(1), avg = O(1) and worst = O(n)

        1. Euclidean gcd: GCD(a, b) = GCD(a-b, b)

    
    - New BFS algorithm

        Goes level wise

        Every iteration, level increases

        ```jsx
        while(!q.empty())
                {
                    int sz=q.size();
                    while(sz--)
                    {
                        pair<int,int> p=q.front();
                        q.pop();
                        for(int i=0;i<4;i++)
                        {
                            int r=p.first+dir[i];
                            int c=p.second+dir[i+1];
                            if(r>=0 && r<m && c>=0 && c<n &&grid[r][c]==1)
                            {
                                grid[r][c]=2;
                                q.push({r,c});

                            }

                        }
                    }
                    levelw++; // level increases each iteration
                }
        ```

    

1. Specifics

    - Array

        - Rotate right by K steps

            ```cpp
            reverse(nums.begin(), nums.begin()+k);
            reverse(nums.begin()+k+1, nums.end());
            reverse(nums.begin(), nums.end());
            ```

        
        - Move zeroes

            ```cpp
            int ind=0,i=0;
                    while(i<nums.size()){
                        if(nums[i]!=0){
                            swap(nums[i], nums[ind]);
                            ind++;
                        }
                        i++;
                    }
            // 0 0 1 1 0 1 0
            // 0 0 1 1 0 1 0
            // 0 0 1 1 0 1 0
            // 1 0 0 1 0 1 0
            // 1 1 0 0 0 1 0
            // 1 1 0 0 0 1 0
            // 1 1 1 0 0 0 0
            ```

        
        - Move zeroes follow up (sort 0,1,2 array)

            ```cpp
            void sortColors(vector<int>& nums) {
                int ind0=0, n=nums.size(), ind2=n-1, i=0;
                while(i<=ind2){
                    if(nums[i]==0){
                        swap(nums[ind0], nums[i]);
                        i++;
                        ind0++;
                    }
                    else if(nums[i]==2){
                        swap(nums[ind2],nums[i]);
                        ind2--;
                    }
                    else i++;
                }
            }
            // 1 0 2 0 1 2 0
            // 1 0 2 0 1 2 0
            // 0 1 2 0 1 2 0
            // 0 1 0 0 1 2 2
            // 0 0 1 0 1 2 2
            // 0 0 0 1 1 2 2
            ```

        
        - Two sum in O(n)

            ```cpp
            vector<int> twoSum(vector<int> &numbers, int target)
            {
                //Key is the number and value is its index in the vector.
            	unordered_map<int, int> hash;
            	vector<int> result;
            	for (int i = 0; i < numbers.size(); i++) {
            		int numberToFind = target - numbers[i];

                        //if numberToFind is found in map, return them
            		if (hash.find(numberToFind) != hash.end()) {
                                //+1 because indices are NOT zero based
            			result.push_back(hash[numberToFind] + 1);
            			result.push_back(i + 1);			
            			return result;
            		}

                        //number was not found. Put it in the map.
            		hash[numbers[i]] = i;
            	}
            	return result;
            }
            ```

        
        - Find increasing triplet in O(n) time and O(1) space

            ```cpp
            bool increasingTriplet(vector<int>& nums) {
                int c1 = INT_MAX, c2 = INT_MAX;
                for (int x : nums) {
                    if (x <= c1) {
                        c1 = x;           // c1 is min seen so far (it's a candidate for 1st element)
                    } else if (x <= c2) { // here when x > c1, i.e. x might be either c2 or c3
                        c2 = x;           // x is better than the current c2, store it
                    } else {              // here when we have/had c1 < c2 already and x > c2
                        return true;      // the increasing subsequence of 3 elements exists
                    }
                }
                return false;
            }
            ```

        
        - Element occurring more than n/2 times

            1. Moore’s voting algorithm: O(n)

                ```cpp
                int n=nums.size(), c=nums[0], cnt=0;
                for(int i=0;i<n;i++){
                    if(cnt==0){
                        c=nums[i];
                        cnt=1;
                        continue;
                    }
                    if(nums[i]==c){
                        cnt++;
                    }
                    else{
                        cnt--;
                    }
                }
                // ek baar check krlena ki wo sahi element h ya nahi
                return c;
                ```

            
            1. The bits in the majority are just the majority bits of all numbers. (O(n))

            1. sort and pick n/2nd number (O(nlogn))

        
        - Element occurring more than n/3 times

            Same shit as n/2 times

            In moore’s voting algo:

            ```cpp
            vector<int> majorityElement(vector<int> v) {
                int n = v.size(); //size of the array

                int cnt1 = 0, cnt2 = 0; // counts
                int el1 = INT_MIN; // element 1
                int el2 = INT_MIN; // element 2

                // applying the Extended Boyer Moore's Voting Algorithm:
                for (int i = 0; i < n; i++) {
                    if (cnt1 == 0 && el2 != v[i]) {
                        cnt1 = 1;
                        el1 = v[i];
                    }
                    else if (cnt2 == 0 && el1 != v[i]) {
                        cnt2 = 1;
                        el2 = v[i];
                    }
                    else if (v[i] == el1) cnt1++;
                    else if (v[i] == el2) cnt2++;
                    else {
                        cnt1--, cnt2--;
                    }
                }
            		// ek baar dono elements ko check krlena ki sachme n/3 se zyada baar ho rhe h ya nahi
            }
            ```

        
        - Max sub-array sum

            - O(n3) generate all subarrays and sum on it linearly

                  

            
            - O(n2) generate all subarrays and sum while generating in the j loop

                ```cpp
                int maxSubarraySum(int arr[], int n) {
                    int maxi = INT_MIN; // maximum sum

                    for (int i = 0; i < n; i++) {
                        int sum = 0;
                        for (int j = i; j < n; j++) {
                            // current subarray = arr[i.....j]

                            //add the current element arr[j]
                            // to the sum i.e. sum of arr[i...j-1]
                            sum += arr[j];

                            maxi = max(maxi, sum); // getting the maximum
                        }
                    }

                    return maxi;
                }
                ```

            
            - O(n) kadane’s algo (keep adding until sum is positive. Make sum 0 once if is negative)

                ```cpp
                int sum=0, maxi=INT_MIN, rangestart=-1, rangeend=-1, tempstart=0;
                for(int i=0;i<nums.size();i++){
                    sum+=nums[i];
                		if(sum>maxi){
                			maxi=sum;
                			rangestart=tempstart;  // for printing
                			rangeend=i;            // for printing
                		}
                    if(sum<0){
                        sum=0;
                				tempstart=i+1;      // for printing
                    }
                }
                return maxi;
                ```

            

        - Max continuous sequence - (100 1 200 4 7 3 1 2) → (1, 2, 3, 4)

            1. Using unordered_set - Note that this is O(n) (O_O)

                ```cpp
                int longestConsecutive(vector<int>& nums) {
                    unordered_set<int> st;
                    for(int i=0;i<nums.size();i++){
                        st.insert(nums[i]);
                    }
                    int cur=0, maxi=0;
                    for(auto i: st){
                        if(st.find(i-1)!=st.end()) continue;
                        cur=0;
                        while(st.find(i+cur)!=st.end()){
                            cur++;
                        }
                        maxi=max(cur, maxi);
                    }
                    return maxi;
                }
                ```

            
            1. Using DSU

        
        - Make matrix zero

            ![[image.png]]

            ```cpp
            class Solution {
            public:
                void setZeroes(vector<vector<int>>& matrix) {
                    int col0=0, n=matrix.size(), m=matrix[0].size();
                    for(int i=0;i<n;i++){
                        if(matrix[i][0]==0) col0=1;
                        for(int j=1;j<m;j++){
                            if(matrix[i][j]==0){
                                matrix[0][j]=0;
                                matrix[i][0]=0;
                            }
                        }
                    }
                    for(int i=0;i<n;i++){
                        for(int j=1;j<n;j++){
                            if(matrix[i][j]==0||matrix[0][j]==0)
                            matrix[i][j]=0;
                        }
                        if(col0==1) matrix[i][0]=0;
                    }
                }
            };
            ```

        
        - Insert, delete, get random in O(1)

            Use vector and hashmap. Use hashmap to store the indices of the values. Main problem occurs while deleting. So, just swap the element of vector with the last element. Now you can easily popback. Remember to update the index of the previously last element in the hashmap beforehand.

        
        - Rotate matrix

            ```cpp
            /*
             * clockwise rotate
             * first swap the symmetry, then reverse left to right
             * 1 2 3     1 4 7     7 4 1 
             * 4 5 6  => 2 5 8  => 8 5 2 
             * 7 8 9     3 6 9     9 6 3 
            */
            void rotate(vector<vector<int> > &matrix) {
                for (int i = 0; i < matrix.size(); ++i) {
                    for (int j = i + 1; j < matrix[i].size(); ++j){
                        swap(matrix[i][j], matrix[j][i]);
            				}
            				reverse(matrix[i].begin(), matrix[i].end());
                }
            }

            /*
             * anticlockwise rotate
             * first swap the symmetry, then reverse up to down
             * 1 2 3     1 4 7    3 6 9 
             * 4 5 6  => 2 5 8 => 2 5 8 
             * 7 8 9     3 6 9    1 4 7 
            */
            void anti_rotate(vector<vector<int> > &matrix) {
                for (int i = 0; i < matrix.size(); ++i) {
                    for (int j = i + 1; j < matrix[i].size(); ++j)
                        swap(matrix[i][j], matrix[j][i]);
                }
            		reverse(matrix.begin(), matrix.end());
            }
            ```

        
        - Number of Subarray sum equals K

            ```cpp
            int subarraySum(vector<int>& nums, int k) {
                map<int, int> mp;
                int sum=0, ans=0;
                mp[0]=1;
                for(int i=0;i<nums.size();i++){
                    sum+=nums[i];
                    ans+=mp[sum-k];
                    mp[sum]++;
                }
                return ans;
            }
            ```

        
        - Number of Subarray xor equals K

            same as previous question (In both question note that `mp[xorr]++` after `total+=mp[xorr^B]`)

            ```cpp
            int Solution::solve(vector<int> &A, int B) {
                unordered_map<int, int> mp;
                int n=A.size(), xorr=0, total=0;
                mp[0]++;
                for(int i=0;i<n;i++){
                    xorr^=A[i];
                    if(mp.find(xorr^B)!=mp.end())
                    total+=mp[xorr^B];
                    mp[xorr]++;
                }
                return total;
            }
            ```

        
        - Next Permutation

            ![[prep/DSA Notes/Private & Shared/Untitled.png|Untitled.png]]

            ```cpp
            void nextPermutation(vector<int>& nums) 
            {
                int n=nums.size();
                int l,r;
                for(l=n-2;l>=0;l--)                           // find decreasing sequence
                {
                    if(nums[l]<nums[l+1]) break;
                }
                if(l<0) reverse(nums.begin(),nums.end());
                else
                {
                    for(r=n-1;r>l;r--)                       // find rightmost successor to pivot
                    {
                        if(nums[r]>nums[l]) break;
                    }
                    swap(nums[l],nums[r]);                  // swap l,r

                    reverse(nums.begin()+l+1,nums.end());   // reverse from l+1 to end
                }
            }
            ```

        
        - Wiggle sort

            Wiggle sort I: a1 ≤ a2 ≥ a3 ≤ a4 ≥ a5…

            O(nlogn): sort the array and just swap alternate indices.

            O(n): swap the adjacent elements if they are in wrong order

            Wiggle sort II: a1 < a2 > a3 < a4 > a5…

        
        - 3SUM

            We have to find three numbers whose sum is 0. A+B+C=0 → A=-(B+C). We use this.

            However, in `ThreeSum`, we have multiple duplicate  
            solutions that can be found. Most of the OLE errors happened here  
            because you could've ended up with a solution with so many duplicates.

            The naive solution for the duplicates will be using the STL methods like below :

            ```
            std::sort(res.begin(), res.end());
            res.erase(unique(res.begin(), res.end()), res.end());
            ```

            But according to my submissions, this way will cause you double your time consuming almost.

            A better approach is that, to jump over the number which has been scanned, no matter it is part of some solution or not.

            If the three numbers formed a solution, we can safely ignore all the duplicates of them.

            We can do this to all the three numbers such that we can remove the duplicates.

            **If it was sum of three numbers = k, then we use same reason A+B+C=k → A=k-(B+C)**

            ```cpp
            class Solution {
            public:
                vector<vector<int>> threeSum(vector<int>& nums) {
                    int n=nums.size(), prev=-1e6-10;
                    sort(nums.begin(), nums.end());
                    vector<vector<int>> ans;

                    for(int i=0;i<n;i++){
                        if(prev==nums[i]) continue;
                        int target=-nums[i];
                        int front = i+1;
                        int back = n-1;
                        while(front<back){
                            if(nums[front]+nums[back]<target){
                                front++;
                            }
                            else if(nums[front]+nums[back]>target){
                                back--;
                            }
                            else{
                                vector<int> triplet = {nums[i], nums[front], nums[back]};
                                ans.push_back(triplet);
                                while(front<back&&nums[front]==triplet[1])front++;
                                while(front<back&&nums[back]==triplet[2])back--;
                            }
                        }
                        prev=nums[i];
                    }

                    return ans;
                }
            };
            ```

        
        - 4SUM in 4 arrays find number of quadruplets.

            4 approaches.

            1. O($n^4$) : Brute force

            1. O($n^3$ log n): Sort the 4th array and brute force on first three array and use upperbound - lowerbound to count the number.

                - ```cpp
                    class Solution {
                    public:
                        int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
                            int n=nums1.size(), ans=0;
                            sort(nums4.begin(), nums4.end());
                            for(int i=0;i<n;i++){
                                for(int j=0;j<n;j++){
                                    for(int k=0;k<n;k++){
                                        int target=nums1[i]+nums2[j]+nums3[k];
                                        auto it=lower_bound(nums4.begin(), nums4.end(), -target);
                                        if(it==nums4.end()||*it!=-target) continue;
                                        auto it2=upper_bound(nums4.begin(), nums4.end(), -target);
                                        ans+=it2-it;
                                    }
                                }
                            }
                            return ans;
                        }
                    };
                    ```

                

            1. O($n^3$) time and O($n$) space: Use a hashmap to count the 4th array elements.

                - ```cpp
                    class Solution {
                    public:
                        int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
                            int n=nums1.size(), ans=0;
                            unordered_map<int, int> mp;
                            for(int i=0;i<n;i++){
                                mp[nums4[i]]++;
                            }
                            for(int i=0;i<n;i++){
                                for(int j=0;j<n;j++){
                                    for(int k=0;k<n;k++){
                                        int target=nums1[i]+nums2[j]+nums3[k];
                                        ans+=mp[-target];
                                    }
                                }
                            }
                            return ans;
                        }
                    };
                    ```

                

            1. O($n^2)$ time and O($n^2$) space: Use hashmap to count all sums of 3rd and 4th array

                - ```cpp
                    class Solution {
                    public:
                        int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
                            int n=nums1.size(), ans=0;
                            unordered_map<int, int> mp;
                            for(int i=0;i<n;i++){
                                for(int j=0;j<n;j++){
                                    mp[nums1[i]+nums2[j]]++;
                                }
                            }
                            for(int i=0;i<n;i++){
                                for(int j=0;j<n;j++){
                                    int target=nums3[i]+nums4[j];
                                    ans+=mp[-target];
                                }
                            }
                            return ans;
                        }
                    ```

                

        
        - Longest sub-array with sum=0.

            ### NOTE: If prefix sum repeats, that means sum of that sub-array is 0

            - **Ex-1:** 15,-2,2,-8,1,7,10,23

            - Prefix sum: 15,13,15,7,8,15,25,48

            - Possibility-1: 15,**13**,**15**,7,8,15,25,48

            - Possibility-2: 15,13,15,**7,8,15**,25,48

            - Possibility-3: 15,**13,15,7,8,15**,25,48

            ### Note: You have to put 0 sum at index -1

            ```cpp
            int maxLen(vector<int>&A, int n)
                {   
                    // Your code here
                    unordered_map<int, vector<int>> mp;
                    int sum=0;
                    mp[0].push_back(-1);
                    for(int i=0;i<n;i++){
                        sum+=A[i];
                        mp[sum].push_back(i);
                    }
                    int ans=0;
                    for(auto i: mp){
                        ans=max(ans, i.second.back()-i.second[0]);
                    }
                    return ans;
                }
            ```

        
        - Longest sub-array with sum k

            - Using hash-map is the best case for if there are 0s and negatives

                Record the first instance of a sum in the hash-map. Find current sum - K in the hash-map

                ```cpp
                int lenOfLongSubarr(int A[],  int N, int K) 
                    { 
                      // Complete the function
                      unordered_map<int, int> mp;
                      int sum=0, ans=0;
                      mp[0]=-1;
                      for(int i=0;i<N;i++){
                          sum+=A[i];
                          if(mp.find(sum-K)!=mp.end()){
                              ans=max(ans, i-mp[sum-K]);
                          }
                          if(mp.find(sum)==mp.end()){
                              mp[sum]=i;
                          }
                      }
                      return ans;
                  }
                ```

            
            - If only positives, then sliding window.

                ```cpp
                int left = 0, right = 0;
                    long long sum = a[0];
                    int maxLen = 0;
                    while (right < n) {
                        // if sum > k, reduce the subarray from left
                        // until sum becomes less or equal to k:
                        while (left <= right && sum > k) {
                            sum -= a[left];
                            left++;
                        }
                        if (sum == k) {
                            maxLen = max(maxLen, right - left + 1);
                        }
                        right++;
                        if (right < n) sum += a[right];
                    }

                    return maxLen;
                ```

            

        - Repeating and missing number in an array

            4 approaches

            1. Use map to count occurrences

            1. 2 for loops to check for each number

            1. Use math

                1. Make two equations

                    1st equation from Sum of n natural numbers

                    2nd equation from sum of squares of n natural numbers

                    Use these two equations two solve for x and y

                
                1. Use xor

                    - Easy shit (see here)

                        Assume the repeating number to be X and the missing number to be Y.

                        **Step 1: Find the XOR of the repeating number(X) and the missing number(Y)**

                        **i.e. (X^Y) = (a[0]^a[1]^…..^a[n-1]) ^ (1^2^……..^N)**

                        - In order to find the XOR of the repeating number and the missing number, we will first XOR all the array elements and with that value,  
                            we will again XOR all the numbers from 1 to N.(X^Y) = (a[0]^a[1]^…..^a[n-1]) ^ (1^2^3^……..^N)

                        **Step 2: Find the first different bit from right between the**  
                        **repeating and the missing number i.e. the first set bit from right in**  
                        **(X^Y)**

                        - By convention, the repeating and the missing number must be  
                            different and since they are different they must contain different bits. Now, our task is to find the first different bit from the right i.e.  
                            the end. We know, the XOR of two different bits always results in 1. The position of the first different bit from the end will be the first set  
                            bit(_from the right_) in (X^Y) that we have found in step 1.

                        **Step 3: Based on the position of the different bits we will**  
                        **group all the elements ( i.e. all array elements + all elements between 1**  
                        **to N) into 2 different groups**

                        - Assume an imaginary array containing all the array elements and  
                            all the elements between 1 to N. Now, we will check that particular  
                            position for each element of that imaginary array and then if the bit is 0, we will insert the element into the 1st group otherwise, we will  
                            insert it into the 2nd group.

                        - After performing this step, we  
                            will get two groups. Now, if we XOR all the elements of those 2 groups,  
                            we will get 2 numbers. One of them will be the repeating number and the  
                            other will be the missing number. But until now, we do not know which  
                            one is repeating and which one is missing.

                        **Last step: Figure out which one of the numbers is repeating and which one is missing**

                        - We will traverse the entire given array and check which one of  
                            them appears twice. And the number that appears twice is the repeating  
                            number and the other one is the missing number.

                        ### Approach:

                        The steps are as follows:

                        1. For the first step, we will run a loop and calculate the XOR of  
                            all the array elements and the numbers between 1 to N. Let’s call this  
                            value xr.

                        1. In order to find the position of the first set bit  
                            from the right, we can either use a loop or we can perform AND of the xr and negation of (xr-1) i.e. (xr & ~(xr-1)).

                        1. Now, we will  
                            take two variables i.e. zero and one. Now, we will check the bit of that position for every element (array elements as well as numbers between 1 to N).

                            1. **If the bit is 1:** We will XOR that element with variable one.

                            1. **If the bit is 0:** We will XOR that element with variable zero.

                        
                        1. Finally, we have two variables i.e. two numbers zero and one. Among them, one is repeating and the other is missing. It’s time to identify them.

                            1. We will traverse the entire array and check how many times variable zero appears.

                            1. If it appears twice, it will be the repeating number, otherwise, it will  
                                be the missing. Now, based on variable zero’s identity, we can easily  
                                identify in which category, variable one belongs.

                        
                        **Note:** _For a better understanding of intuition, please watch the video at the bottom of the page._

                        ```cpp
                        vector<int> findMissingRepeatingNumbers(vector<int> a) {
                            int n = a.size(); // size of the array

                            int xr = 0;

                            //Step 1: Find XOR of all elements:
                            for (int i = 0; i < n; i++) {
                                xr = xr ^ a[i];
                                xr = xr ^ (i + 1);
                            }

                            //Step 2: Find the differentiating bit number:
                            int number = (xr & ~(xr - 1));

                            //Step 3: Group the numbers:
                            int zero = 0;
                            int one = 0;
                            for (int i = 0; i < n; i++) {
                                //part of 1 group:
                                if ((a[i] & number) != 0) {
                                    one = one ^ a[i];
                                }
                                //part of 0 group:
                                else {
                                    zero = zero ^ a[i];
                                }
                            }

                            for (int i = 1; i <= n; i++) {
                                //part of 1 group:
                                if ((i & number) != 0) {
                                    one = one ^ i;
                                }
                                //part of 0 group:
                                else {
                                    zero = zero ^ i;
                                }
                            }

                            // Last step: Identify the numbers:
                            int cnt = 0;
                            for (int i = 0; i < n; i++) {
                                if (a[i] == zero) cnt++;
                            }

                            if (cnt == 2) return {zero, one};
                            return {one, zero};
                        }
                        ```

                    

            
            1. Use swap sort (O(n) time and O(1) space but modification to array)

                place every number into it’s place ( x-1 index) and then check each number. If a number doesn’t match it’s index+1, the index+1 is missing number and number is duplicate number

                ```cpp
                vector<int> findTwoElement(vector<int> arr, int n) {
                        // code here
                        int ind=0;
                        while(ind<n){
                            if(arr[ind]!=arr[arr[ind]-1])
                                swap(arr[ind], arr[arr[ind]-1]);
                            else ind++;
                        }
                        int dup=0, mis=0;
                        for(int i=0;i<n;i++){
                            if(arr[i]!=i+1){
                                mis=i+1;
                                dup=arr[i];
                            }
                        }
                        return {dup, mis};
                    }
                ```

            

        - maximum sum of smallest and second smallest elements chosen from all possible sub-arrays

            This is just max sum of two consecutive elements in the array

        
        - Print spiral matrix

            [https://www.youtube.com/watch?v=3Zv-s9UUrFM](https://www.youtube.com/watch?v=3Zv-s9UUrFM)

            ```cpp
            vector<int> spiralOrder(vector<vector<int>>& matrix) {
                vector<int> ans;
                int n=matrix.size(), m=matrix[0].size();
                int top=0, right=m-1, bottom=n-1, left=0;
                while(top<=bottom && left<=right){
                    for(int i=left;i<=right;i++){
                        ans.push_back(matrix[top][i]);
                    }
                    top++;
                    for(int i=top;i<=bottom;i++){
                        ans.push_back(matrix[i][right]);
                    }
                    right--;
                    if(top<=bottom){
                        for(int i=right;i>=left;i--){
                            ans.push_back(matrix[bottom][i]);
                        }
                        bottom--;
                    }
                    if(left<=right){
                        for(int i=bottom;i>=top;i--){
                            ans.push_back(matrix[i][left]);
                        }
                        left++;
                    }
                }
                return ans;
            }
            ```

        
        - Max sub-array product

            if 0 then divide the array into before the 0 and after 0. If even negatives, then no problem. If odd negatives, one negative either from first or last will be discarded. So basically you have to take max of prefix or suffix

            ```cpp
            class Solution {
            public:
                int maxProduct(vector<int>& nums) {
                    int pre=1, suf=1;
                    int ans=INT_MIN;
                    int n=nums.size();
                    for(int i=0;i<n;i++){
                        if(pre==0) pre=1;
                        if(suf==0) suf=1;
                        pre=pre*nums[i];
                        suf=suf*nums[n-i-1];
                        ans=max({ans, pre, suf});
                    }
                    return ans;
                }
            };
            ```

        
        - Find MEX

            Use swap sort. First out of place index is the answer. Note that this is O(n)

            ```cpp
            class Solution {
            public:
                int firstMissingPositive(vector<int>& nums) {
                    int n=nums.size();
                    for(int i=0;i<n;i++){
                        if(nums[i]<=0||nums[i]>n) continue;

                        while(nums[i]!=nums[nums[i]-1]){
                            swap(nums[i], nums[nums[i]-1]);
                            if(nums[i]<=0||nums[i]>n) break;
                        }
                    }
                    for(int i=0;i<nums.size();i++){
                        if(nums[i]!=i+1) return i+1;
                    }
                    return nums.size()+1;
                }
            };
            ```

        
        - Find product of all elements of array excluding the current one

            Without using division operator or prefix and suffix array in O(1) space and O(n) time

            You can use combine the prefix and suffix array into the answer array only.

            ```cpp
            class Solution {
            public:
                vector<int> productExceptSelf(vector<int>& nums) {
                    int n=nums.size();
                    vector<int> ans(n, 1);
                    for(int i=1;i<n;i++){
                        ans[i]*=nums[i-1]*ans[i-1];
                    }

                    for(int i=n-2;i>=0;i--){
                        ans[i]*=nums[i+1];
                    }

                    return ans;
                }
            };
            ```

        
        - Count inversions

            ![[prep/DSA Notes/Private & Shared/Untitled 1.png|Untitled 1.png]]

            ```cpp
            void merge(int l, int m, int r, vector<int>& a, int &cnt){
                int ind1=l;
                int ind2=m+1;
                vector<int> temp;
                while(ind1<=m&&ind2<=r){
                    if(a[ind1]<=a[ind2]){       // note that equals should be here
                        temp.push_back(a[ind1]);
                        ind1++;
                    }
                    else {
                        temp.push_back(a[ind2]);
                        cnt+=(m-ind1+1);       // this is the only change from mergesort
                        ind2++;
                    }
                }
                while(ind1<=m){
                    temp.push_back(a[ind1]);
                    ind1++;
                }
                while(ind2<=r){
                    temp.push_back(a[ind2]);
                    ind2++;
                }
                int ind=l;
                for(auto i: temp){
                    a[ind]=i;
                    ind++;
                }
            }
            void mergeSort(int l, int r, vector<int>& a, int &cnt){
                if(l>=r) return;
                int m=(l+r)/2;
                mergeSort(l, m, a, cnt);
                mergeSort(m+1, r, a, cnt);
                merge(l,m,r,a, cnt);
            }
            int numberOfInversions(vector<int>&a, int n) {
                // Write your code here.
                int cnt=0;
                mergeSort(0, n-1, a, cnt);
                return cnt;

            }
            ```

        
        - Reverse pairs

            Using merge sort, before the merge, go through a function which counts the pairs

            ```cpp
            class Solution {
            public:
                void mergeSort(vector<int>& nums, int l, int r, int& cnt){
                    if(l>=r) return;
                    int m=(l+r)/2;
                    mergeSort(nums,l,m, cnt);
                    mergeSort(nums, m+1, r, cnt);
                    cntpairs(nums, l, m, r, cnt);
                    merge(nums, l, m, r);
                }
                void cntpairs(vector<int>& nums, int l, int m, int r, int& cnt){
                    int ind2=m+1;
                    for(int i=l;i<=m;i++){
                        while(ind2<=r&&(long long)nums[i]>(long long)nums[ind2]*2) ind2++;
                        cnt+=ind2-(m+1);
                    }
                }

                void merge(vector<int>& nums, int l, int m, int r){
                    int ind1=l, ind2=m+1;
                    vector<int> temp;
                    while(ind1<=m&&ind2<=r){
                        if(nums[ind1]<=nums[ind2]){
                            temp.push_back(nums[ind1]);
                            ind1++;
                        }
                        else{
                            temp.push_back(nums[ind2]);
                            ind2++;
                        }
                    }
                    while(ind1<=m){
                        temp.push_back(nums[ind1]);
                        ind1++;
                    }
                    while(ind2<=r){
                        temp.push_back(nums[ind2]);
                        ind2++;
                    }
                    int ind=l;
                    for(auto i: temp){
                        nums[ind]=i;
                        ind++;
                    }
                }
                int reversePairs(vector<int>& nums) {
                    int cnt=0;
                    mergeSort(nums, 0, nums.size()-1, cnt);
                    return cnt;
                }
            };
            ```

        

    - Sorting

        - Selection sort

            In each iteration, select the current index and iterate through the next part of array to find index with min element. Now swap the current and minimum element index.

            ```cpp
            for(int i=0;i<n;i++){
                int minind=i;
                for(int j=i;j<n;j++){
                    if(arr[minind]>arr[j]){
                        minind=j;
                    }   
                }
                swap(arr[i], arr[minind]);
            }
            ```

        
        - Bubble sort

            Every iteration, the algo bubbles the largest element to the last of the unsorted array. That is why the unsorted array is only n-i-1 size(second loop). This is why first loop runs only n-1 times (because at that point the size of unsorted array becomes 1.

            ```cpp
            bool swapped;
            for (i = 0; i < n - 1; i++) {
                swapped = false;
                for (j = 0; j < n - i - 1; j++) {
                    if (arr[j] > arr[j + 1]) {
                        swap(&arr[j], &arr[j + 1]);
                        swapped = true;
                    }
                }

                // If no two elements were swapped by inner loop,
                // then break
                if (swapped == false)
                    break;
            }
            ```

        
        - Insertion sort

            Basically every iteration, shift every element left(or right if you start from end) until the correct place for the current arr[i] is found.

            ```cpp
            for (i = 1; i < n; i++) {
                key = arr[i];
                j = i - 1;
                while (j >= 0 && arr[j] > key) {
                    arr[j + 1] = arr[j];
                    j = j - 1;
                }
                arr[j + 1] = key;
            }
            ```

        

    - Linked List

        - Some theory

            ### Theory

            Binary search cannot be implemented efficiently in linked lists. (As random access is not possible- O(N) time complexity of BS in linked lists)

            However, using skip lists, searching can be performed in O(Log n) time but that will take a lot of extra space. (Multiple layers have to be formed.)

            Which sorting algorithm for linked lists and arrays?

            Arrays- randomized version of quicksort

            Randomized Quick Sort Algorithm- The algorithm exactly follows the standard algorithm except it randomizes the pivot selection

            Worst case complexity of quick sort occurs when the array is already sorted. O(n^2)

            Linked list- Merge Sort

            C++ STL

            The algorithm used by sort() is IntroSort. Introsort being a hybrid sorting algorithm uses three sorting algorithms to minimize the running time- Quicksort, Heapsort and Insertion Sort.

            Linked List contains a loop when the last node does not point to NULL but points to some other node in the linked list itself.

            [https://www.interviewbit.com/linked-list-interview-questions/](https://www.interviewbit.com/linked-list-interview-questions/)

            [https://leetcode.com/problems/odd-even-linked-list/](https://leetcode.com/problems/odd-even-linked-list/)

            A given linked list is sorted based on absolute values. Write a function to sort the list based on actual values in O(n) time.

            [Hint- whenever we find a negative value, we push it to to head of the linked list]

            [https://leetcode.com/problems/reverse-linked-list-ii/submissions/960213984/](https://leetcode.com/problems/reverse-linked-list-ii/submissions/960213984/)

            (make 2 cases- when left=1 and not left is not 1)

            [https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) [seems easy but tricky]

            [https://leetcode.com/problems/swap-nodes-in-pairs/](https://leetcode.com/problems/swap-nodes-in-pairs/)

            [https://leetcode.com/problems/intersection-of-two-linked-lists/description/](https://leetcode.com/problems/intersection-of-two-linked-lists/description/) [IMP wasn't able to do this]

            [https://leetcode.com/problems/reverse-nodes-in-k-group/description/](https://leetcode.com/problems/reverse-nodes-in-k-group/description/) (If we can use extra space use stack)

            [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/) [V. V. imp]

            [https://leetcode.com/problems/linked-list-components/description/](https://leetcode.com/problems/linked-list-components/description/)

            **Dummy Node[very imp concept]**

        
        - Silly mistake in cycle detection (hashing, tortoise hair)

            ```cpp
            if(head == NULL) return false;
                node* fast = head;
                node* slow = head;

                while(fast->next != NULL && fast->next->next != NULL) {
                    fast = fast->next->next;
                    slow = slow->next;
                    if(fast == slow) return true;
                }
                return false;
            ```

            vs

            ```cpp
            if(head == NULL) return false;
                node* fast = head;
                node* slow = head;

                while(fast->next != NULL && fast->next->next != NULL) {
                    if(fast == slow) return true; // silly mistake cz initially slow==fast
                    fast = fast->next->next;
                    slow = slow->next;
                }
                return false;
            ```

        
        - Length of cycle

            1. use hashmap for hash[node]++. hash[node]==1 → cycle. Use a counter and again start. hash[node]==2 return counter

            1. Use slow and fast. First time slow==fast → cycle. Use a counter and start slow. Second time slow == fast return counter.

        
        - Reversing a linked list

            ```cpp
            ListNode* reverseList(ListNode* head) {   // iterative
                    ListNode *newHead = NULL;
                    while (head != NULL) {
                        ListNode *next = head->next;
                        head->next = newHead;
                        newHead = head;
                        head = next;
                    }
                    return newHead;
                }

            ListNode* reverseList(ListNode* &head) {   // recursive

                    if (head == NULL||head->next==NULL)
                        return head;

                    ListNode* nnode = reverseList(head->next);
                    head->next->next = head;
                    head->next = NULL;
                    return nnode;
                }
            ```

        
        - Intersection point

            ```cpp
            class Solution {
            public:
                ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
                    auto c1=headA, c2=headB; int flag=0;
                    while(c1!=c2){
                        c1=c1==NULL?headB:c1->next;
                        c2=c2==NULL?headA:c2->next;
                    }

                    return c1;
                }
            };
            ```

            **Visualization of this solution:**

            **Case 1 (Have Intersection & Same Len):**

            ```
                   a
            A:     a1 → a2 → a3
                               ↘
                                 c1 → c2 → c3 → null
                               ↗
            B:     b1 → b2 → b3
                   b
            ```

            ```
                        a
            A:     a1 → a2 → a3
                               ↘
                                 c1 → c2 → c3 → null
                               ↗
            B:     b1 → b2 → b3
                        b
            ```

            ```
                             a
            A:     a1 → a2 → a3
                               ↘
                                 c1 → c2 → c3 → null
                               ↗
            B:     b1 → b2 → b3
                             b
            ```

            ```
            A:     a1 → a2 → a3
                               ↘ a
                                 c1 → c2 → c3 → null
                               ↗ b
            B:     b1 → b2 → b3
            ```

            Since `a == b` is true, end loop `while(a != b)`, return the intersection node `a = c1`.

            **Case 2 (Have Intersection & Different Len):**

            ```
                        a
            A:          a1 → a2
                               ↘
                                 c1 → c2 → c3 → null
                               ↗
            B:     b1 → b2 → b3
                   b
            ```

            ```
                             a
            A:          a1 → a2
                               ↘
                                 c1 → c2 → c3 → null
                               ↗
            B:     b1 → b2 → b3
                        b
            ```

            ```
            A:          a1 → a2
                               ↘ a
                                 c1 → c2 → c3 → null
                               ↗
            B:     b1 → b2 → b3
                             b
            ```

            ```
            A:          a1 → a2
                               ↘      a
                                 c1 → c2 → c3 → null
                               ↗ b
            B:     b1 → b2 → b3
            ```

            ```
            A:          a1 → a2
                               ↘           a
                                 c1 → c2 → c3 → null
                               ↗      b
            B:     b1 → b2 → b3
            ```

            ```
            A:          a1 → a2
                               ↘                a = null, then a = b1
                                 c1 → c2 → c3 → null
                               ↗           b
            B:     b1 → b2 → b3
            ```

            ```
            A:          a1 → a2
                               ↘
                                 c1 → c2 → c3 → null
                               ↗                b = null, then b = a1
            B:     b1 → b2 → b3
                   a
            ```

            ```
                        b
            A:          a1 → a2
                               ↘
                                 c1 → c2 → c3 → null
                               ↗
            B:     b1 → b2 → b3
                        a
            ```

            ```
                             b
            A:          a1 → a2
                               ↘
                                 c1 → c2 → c3 → null
                               ↗
            B:     b1 → b2 → b3
                             a
            ```

            ```
            A:          a1 → a2
                               ↘ b
                                 c1 → c2 → c3 → null
                               ↗ a
            B:     b1 → b2 → b3
            ```

            Since `a == b` is true, end loop `while(a != b)`, return the intersection node `a = c1`.

            **Case 3 (Have No Intersection & Same Len):**

            ```
                   a
            A:     a1 → a2 → a3 → null
            B:     b1 → b2 → b3 → null
                   b
            ```

            ```
                        a
            A:     a1 → a2 → a3 → null
            B:     b1 → b2 → b3 → null
                        b
            ```

            ```
                             a
            A:     a1 → a2 → a3 → null
            B:     b1 → b2 → b3 → null
                             b
            ```

            ```
                                  a = null
            A:     a1 → a2 → a3 → null
            B:     b1 → b2 → b3 → null
                                  b = null
            ```

            Since `a == b` is true (both refer to null), end loop `while(a != b)`, return `a = null`.

            **Case 4 (Have No Intersection & Different Len):**

            ```
                   a
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
                   b
            ```

            ```
                        a
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
                        b
            ```

            ```
                             a
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
                             b
            ```

            ```
                                  a
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
                                  b = null, then b = a1
            ```

            ```
                   b                   a = null, then a = b1
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
            ```

            ```
                        b
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
                   a
            ```

            ```
                             b
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
                        a
            ```

            ```
                                  b
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
                             a
            ```

            ```cpp

                                       b = null
            A:     a1 → a2 → a3 → a4 → null
            B:     b1 → b2 → b3 → null
                                  a = null
            ```

              

        
        - Find starting point of cycle

            1. First hit on hash table is the starting point

            1. Using slow and fast pointers

                - Steps:

                    - Initially take two pointers, fast and slow. The fast pointer  
                        takes two steps ahead while the slow pointer will take a single step  
                        ahead for each iteration.

                    - We know that if a cycle exists, fast and slow pointers will collide.

                    - If the cycle does not exist, the fast pointer will move to NULL

                    - Else, when both slow and fast pointer collides, it [detects a cycle](https://takeuforward.org/data-structure/detect-a-cycle-in-a-linked-list/) exists.

                    - Take another pointer, say entry. Point to the very first of the linked list.

                    - Move the slow and the entry pointer ahead by single steps until they collide.

                    - Once they collide we get the starting node of the linked list.

                

        
        - Check if palindrome

            ![[prep/DSA Notes/Private & Shared/Untitled 2.png|Untitled 2.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 3.png|Untitled 3.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 4.png|Untitled 4.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 5.png|Untitled 5.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 6.png|Untitled 6.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 7.png|Untitled 7.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 8.png|Untitled 8.png]]

        
        - Remove nth node from last

            A one pass solution can be done using pointers. Move one pointer **fast** --> **n+1**  
            places forward, to maintain a gap of n between the two pointers and  
            then move both at the same speed. Finally, when the fast pointer reaches  
            the end, the slow pointer will be **n+1** places behind - just the right spot for it to be able to skip the next node.

        
        - Add 1 to linked list

            Simple recursion to find out carry

            ```cpp
            int recur(Node* head){
                if(head->next==NULL){
                    head->data=head->data+1;
                    if(head->data==10){
                        head->data=0;
                        return 1;
                    }
                    else return 0;
                }
                int carry=recur(head->next);
                if(carry==1){
                    head->data=head->data+1;
                    if(head->data==10){
                        head->data=0;
                        return 1;
                    }
                    else return 0;
                }
                return 0;
            }
            Node *addOne(Node *head)
            {
                // Write Your Code Here.
                if(recur(head)==1){
                    Node* temp = new Node(1);
                    temp->next=head;
                    return temp;
                }
                return head;
            }
            ```

        
        - Sort 0,1,2 linked list

            1. Count the number of 0,1,2 and just change data

            1. divide the linked list into three linked lists of 0s, 1s and 2s. Finally merge them together

                ```cpp
                void add(Node* &node, Node* &tail){
                    if(tail==NULL){
                        tail = node;
                    }
                    else {
                        tail->next=node;
                        tail = node;
                    }
                }
                Node* sortList(Node *head){
                    // Write your code here.
                    Node* head0=NULL; Node* tail0=NULL;Node* head1=NULL;Node* tail1=NULL;Node* head2=NULL;Node* tail2=NULL;
                    Node* cur=head;
                    while(cur!=NULL){
                        Node* next = cur->next;
                        if(cur->data==0){
                            add(cur, tail0);
                            if(head0==NULL){
                                head0=tail0;
                            }
                            cur->next=NULL;
                        }
                        else if(cur->data==1){
                            add(cur, tail1);
                            if(head1==NULL){
                                head1=tail1;
                            }
                            cur->next=NULL;
                        }
                        else{
                            add(cur, tail2);
                            if(head2==NULL){
                                head2=tail2;
                            }
                            cur->next=NULL;
                        }
                        cur=next;
                    }
                    if(head0!=NULL){
                        head=head0;
                        if(head1!=NULL){
                            tail0->next=head1;
                        }
                        else if(head2!=NULL){
                            tail0->next=head2;
                        }
                    }
                    else if(head1!=NULL){
                        head=head1;
                    }
                    else {
                        head=head2;
                    }
                    if(head1!=NULL){
                        if(head2!=NULL){
                            tail1->next=head2;
                        }
                    }
                    return head;

                }
                ```

            

        - Removing duplicates from DLL

            ### Note: Remember to make next of prev to be NULL

            ```cpp
            Node * removeDuplicates(Node *head)
            {
                // Write your code here
                Node* prev=head;
                Node* cur=prev->next;
                if(cur==NULL) return head;
                while(cur!=NULL){
                    if(cur->data==prev->data){
                        Node* temp = cur->next;
                        prev->next=NULL;
                        delete cur;
                        cur=temp;
                        continue;
                    }
                    else {
                        prev->next=cur;
                        prev=cur;
                        cur=cur->next;
                    }
                }
                return head;
            }
            ```

        
        - Reverse a linked list in groups of k

            For k=3 and linked list 1→2→3→4→5→6→7

            insert a dummy head 0→1→2→3→4→5→6→7

            Take a prev at dummy head. Now in a loop while checking n≥k, cur=prev→next and next=cur→next.

            ![[prep/DSA Notes/Private & Shared/Untitled 9.png|Untitled 9.png]]

            Now for num = k-1 times,

            ```cpp
            cur->next=next->next;   // 1
            next->next=prev->next;  // 2
            prev->next=next;        // 3
            next=cur->next;         // 4
            ```

            ![[prep/DSA Notes/Private & Shared/Untitled 10.png|Untitled 10.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 11.png|Untitled 11.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 12.png|Untitled 12.png]]

            2nd iteration within the same loop:

            ![[prep/DSA Notes/Private & Shared/Untitled 13.png|Untitled 13.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 14.png|Untitled 14.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 15.png|Untitled 15.png]]

            Now num=0 so stop the inner loop.

            update prev to cur and n-=k;

            ![[prep/DSA Notes/Private & Shared/Untitled 16.png|Untitled 16.png]]

            repeat the outer loop which again sets the cur to prev→next and next to cur→next

            ![[prep/DSA Notes/Private & Shared/Untitled 17.png|Untitled 17.png]]

            ```cpp
            class Solution {
            public:
                int sizeLL(ListNode* head){
                    if(!head) return 0;
                    return 1+sizeLL(head->next);
                }
                ListNode* reverseKGroup(ListNode* head, int k) {
                    // first, we have to calculate the length of list because we have to stop at the last <k sized group
                    int n = sizeLL(head);
                    ListNode* dummy= new ListNode(-1);
                    dummy->next=head;
                    ListNode* prev=dummy;
                    ListNode* cur;
                    ListNode* next;
                    while(n>=k){
                        cur = prev->next;
                        next = cur->next;
                        int num=k-1;
                        while(num--){
                            cur->next=next->next;
                            next->next=prev->next;
                            prev->next=next;
                            next=cur->next;
                        }
                        prev=cur;
                        n-=k;
                    }
                    return dummy->next;
                }
            };
            ```

        
        - Rotate a Linked List

            ![[prep/DSA Notes/Private & Shared/Untitled 18.png|Untitled 18.png]]

            In first iteration, move a pointer to the last and simultaneously calculate length. Connect last to head so you have a circular linked list now.

            Now if you have to rotate by k, you have to move head n-k forward, then unlink the node and return the next node

            ![[prep/DSA Notes/Private & Shared/Untitled 19.png|Untitled 19.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 20.png|Untitled 20.png]]

            ```cpp
            class Solution {
            public:
                ListNode* rotateRight(ListNode* head, int k) {
                    ListNode* cur = head;
                    int n=1;
                    if(!cur||!cur->next) return head;
                    while(cur->next!=NULL){
                        cur=cur->next;
                        n++;
                    }
                    cur->next=head;
                    ListNode* prev=head;
                    cur=prev->next;
                    k%=n; // important
                    cout<<n<<' ';
                    int num=n-k-1;
                    while(num--){
                        cur=cur->next;
                        prev=prev->next;
                    }
                    prev->next=NULL;
                    return cur;
                }
            };
            ```

        
        - Flatten a linked list

            n sorted linked lists with child pointers connected with each other using next pointer at heads. Merge everything into a single sorted linked list.

            ![[prep/DSA Notes/Private & Shared/Untitled 21.png|Untitled 21.png]]

            Keep merging last two linked lists into one and return it as the second list for the prev one. Use a dummy pointer to start.

            ```cpp
            Node* recur(Node* cur1){
            	if(cur1->next==NULL) return cur1;
            	Node* cur2=recur(cur1->next);
            	Node* headkaPrev = new Node(0);
            	cur1->next=NULL;
            	// cur2->next=NULL;
            	Node* cur=headkaPrev;
            	while(cur1!=NULL&&cur2!=NULL){
            		if(cur1->data<=cur2->data){
            			cur->child=cur1;
            			cur=cur->child;
            			cur1=cur1->child;
            		}
            		else {
            			cur->child=cur2;
            			cur=cur->child;
            			cur2=cur2->child;
            		}
            	}
            	if(cur1) cur->child=cur1;
            	else cur->child=cur2;
            	return headkaPrev->child;
            }
            Node* flattenLinkedList(Node* head) 
            {
            	// Write your code here
            	return recur(head);
            }
            ```

        
        - Deep copy a linked list with a random pointer and a next pointer

            ![[prep/DSA Notes/Private & Shared/Untitled 22.png|Untitled 22.png]]

            ```cpp
            Node* copyRandomList(Node* head) {
                // handling the case where linked list is of 0 size at first so I don't forget
                if(!head) return head;
                // we start off by iterating over the linked list and creating duplicate nodes in between each node
                Node* cur=head;
                Node* dup = NULL;
                while(cur!=NULL){
                    dup = new Node(cur->val);
                    dup->next=cur->next;
                    cur->next=dup;
                    cur=dup->next;
                }
                // Now every node has it's duplicate node just after it.
                // So just point the random pointer of duplicate node to random pointer of real node's next node.
                cur=head;
                dup=head->next;
                while(dup!=NULL){
                    if(cur->random==NULL) {
                        dup->random=NULL;
                    }
                    else{
                        dup->random=cur->random->next;
                    }
                    if(dup->next==NULL) break;
                    dup=dup->next->next;
                    cur=cur->next->next;
                }
                // Now we have all the random pointers pointed correctly. 
                // Now we just have to seperate the two linked lists :)
                cur=head;dup=head->next;
                Node* dupHead=dup;
                while(dup!=NULL){
                    if(dup->next==NULL){
                        // pointing them NULL is important because we have to revert the original linked list to original state
                        cur->next=NULL;
                        dup->next=NULL;
                        break;
                    }
                    cur->next=cur->next->next;
                    dup->next=dup->next->next;
                    cur=cur->next;
                    dup=dup->next;
                }
                return dupHead;
            }
            ```

        
        - Reorder list

            Q: L0→L1→L2→…→Ln-1→Ln ⇒ L0→Ln→L1→Ln-1…

            First find the mid. And make two cases for odd and even length list.

            Use recursion which ends at the mid. While coming out of each recursion, use a temporary pointer to keep track of each next node.

            ```cpp
            pair<ListNode*, ListNode*> recur(ListNode* head, ListNode* slow, ListNode* slowKaNext){
                if(head==slow){
                    ListNode* temp=NULL;
                    if(slowKaNext==NULL){
                        temp=slow->next;
                        slow->next=NULL;
                    }
                    else {
                        temp=slowKaNext->next;
                        slowKaNext->next=NULL;
                    }
                    return {head, temp};
                }
                pair<ListNode*, ListNode*> pi= recur(head->next, slow, slowKaNext);
                ListNode* third=pi.first;
                ListNode* second=pi.second;
                ListNode* temp=second->next;
                head->next=second;
                second->next=third;
                return {head, temp};
            }
            ListNode* Solution::reorderList(ListNode* head) {
                int n=0;
                if(head->next==NULL) return head;
                ListNode* slow=head;
                ListNode* fast=head;
                while(fast->next!=NULL&&fast->next->next!=NULL){
                    slow=slow->next;
                    fast=fast->next->next;
                    n++;
                    if(fast->next==NULL){
                        n=n*2-1;
                    }
                    else{
                        n=n*2;
                    }
                }
                ListNode* temp=slow;
                if(n%2==0){
                    temp=slow->next;
                }
                // if(n%2==0)
                // cout<<slow->val<<' '<<temp->val<<'\n';
                // else cout<<slow->val<<'\n';
                return recur(head, slow, temp).first;
            }
            ```

        

    - BT

        - Iterative preorder traversal

            Here we first take the node, go RIGHT first and then left

            ```cpp
            class Solution {
                void recur(TreeNode* root, vector<int>& ans){
                    if(root==NULL) return;
                    ans.push_back(root->val);
                    if(root->left!=NULL) recur(root->left, ans);
                    if(root->right!=NULL) recur(root->right, ans);
                }
            public:
                vector<int> preorderTraversal(TreeNode* root) {
                    vector<int> ans;
                    // recur(root, ans); // for recursive
                    stack<TreeNode*> st;
                    if(!root) return {};
                    st.push(root);
                    while(!st.empty()){
                        TreeNode* v=st.top();
                        st.pop();
                        ans.push_back(v->val);
                        if(v->right!=NULL){
                            st.push(v->right);
                        }
                        if(v->left!=NULL){
                            st.push(v->left);
                        }
                    }
                    return ans;
                }
            };
            ```

        
        - Iterative postorder traversal

            Same as pre order but first go LEFT then go RIGHT and reverse the answer. If says use two stack, just reverse using the other stack.

            ```cpp
            class Solution {
                void recur(TreeNode* root, vector<int>& ans){
                    if(root==NULL) return;
                    if(root->left!=NULL) recur(root->left, ans);
                    if(root->right!=NULL) recur(root->right, ans);
                    ans.push_back(root->val);
                }
            public:
                vector<int> postorderTraversal(TreeNode* root) {
                    vector<int> ans;
                    // recur(root, ans); // for recursive
                    stack<TreeNode*> st;
                    if(!root) return {};
                    st.push(root);
                    while(!st.empty()){
                        TreeNode* v=st.top();
                        st.pop();
                        ans.push_back(v->val);
                        if(v->left!=NULL){
                            st.push(v->left);
                        }
                        if(v->right!=NULL){
                            st.push(v->right);
                        }
                    }
                    reverse(ans.begin(), ans.end());
                    return ans;
                }
            };
            ```

        
        - Iterative inorder traversal

            Go left left left left until NULL then print and go right then go left left left……

            ```cpp
            public:
                vector<int> inorderTraversal(TreeNode* root) {
                    vector<int> ans;
                    // recur(root, ans); // for recursion
                    stack<TreeNode*> st;
                    TreeNode* node = root;
                    while(true){
                        if(node!=NULL){
                            st.push(node);
                            node=node->left;
                        }
                        else{
                            if(st.empty()) break;
                            node=st.top();
                            st.pop();
                            if(node){
                                ans.push_back(node->val);
                                node=node->right;
                            }
                        }
                    }
                    return ans;
                }
            };
            ```

        
        - Preorder, inorder and postorder in a single traversal

            We use a stack of pair<TreeNode*, int>

            let second value be type:

            If type==1

            add to preorder, type++, add left

            If type==2

            add to inorder, type++, add right

            If type==3

            add to postorder

            ```cpp
            vector<vector<int>> getTreeTraversal(BinaryTreeNode<int> *root){
                // Write your code here.
            		 // note the weird struct of codestudio binary tree
                stack<pair<BinaryTreeNode<int>*, int>> st;   
                vector<int> preorder, inorder, postorder;
                if(root==NULL) return {inorder, preorder, postorder};
                st.push({root, 1});
                while(!st.empty()){
                    BinaryTreeNode<int>* v=st.top().first;
                    int type = st.top().second;
                    if(type==1){
                        preorder.push_back(v->data);
                        st.pop();
                        st.push({v, 2});
                        if(v->left!=NULL) st.push({v->left, 1});
                        continue;
                    }
                    else if(type==2){
                        inorder.push_back(v->data);
                        st.pop();
                        st.push({v, 3});
                        if(v->right!=NULL) st.push({v->right, 1});
                        continue;
                    }
                    else if(type==3){
                        postorder.push_back(v->data);
                        st.pop();
                    }
                }
                return {inorder, preorder, postorder};
            }
            ```

        
        - Populate next right pointer

            ```cpp
            Example Input

                     1
                   /  \
                  2    3
                 / \  / \
                4  5  6  7

            

            Example Output

                     1 -> NULL
                   /  \
                  2 -> 3 -> NULL
                 / \  / \
                4->5->6->7 -> NULL
            ```

            Now, Use level order traversal. Keep a prev node and make next of prev to cur.

            ```cpp
            void Solution::connect(TreeLinkNode* A) {
                queue<TreeLinkNode*> q;
                q.push(A);
                while(!q.empty()){
                    int sz=q.size();
                    int num=sz;
                    TreeLinkNode* prev=NULL;
                    while(sz--){
                        TreeLinkNode* cur=q.front();
                        q.pop();
                        TreeLinkNode* left=cur->left;
                        TreeLinkNode* right=cur->right;
                        if(prev!=NULL){
                            prev->next=cur;
                        }
                        if(left!=NULL) q.push(left);
                        if(right!=NULL) q.push(right);
                        prev=cur;
                    }
                }
            }
            ```

        
        - Basics

            - Height

                1. Using bfs

                1. Using dfs

                    ```cpp
                    int recur(TreeNode* root){
                    	  if(root==NULL) return 0;
                    	  return 1+max(recur(root->left), recur(root->right));
                    }
                    ```

                

            - Diameter (Hint: Use height)

                Largest **height** of left tree+right tree

            
            - Max path sum (Similar to Diameter)

                ```cpp
                class Solution {
                    int maxi=INT_MIN;
                    int recur(TreeNode* root){
                        if (root == NULL) return 0;

                        int leftMaxPath = max(0, recur(root -> left));
                        int rightMaxPath = max(0, recur(root -> right));
                        int val = root -> val;
                        maxi = max(maxi, (leftMaxPath + rightMaxPath) + val);
                        return max(leftMaxPath, rightMaxPath) + val;
                    }
                public:
                    int maxPathSum(TreeNode* root) {
                        recur(root);
                        return maxi;
                    }
                };
                ```

            
            - Is same tree?

                ```cpp
                bool recur(TreeNode* p, TreeNode* q){
                        if(p==NULL&&q==NULL) return true;
                        if(p==NULL) return false;
                        if(q==NULL) return false;
                        if(p->val!=q->val) return false;
                        bool left=true, right=true;
                        left=recur(p->left, q->left);
                        right=recur(p->right, q->right);
                        return left&&right;
                    }
                ```

            
            - Zigzag level-wise traversal (At each level, if flag, reverse the order and if !flag, don’t reverse)

                ![[prep/DSA Notes/Private & Shared/Untitled 23.png|Untitled 23.png]]

                Ans = `[[3],[20,9],[15,7]]`

                ```cpp
                vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
                        queue<TreeNode*> q1;
                        q1.push(root);
                        if(root==NULL) return {};
                        int flag=1;
                        vector<vector<int>> ans;
                        while(!q1.empty()){
                            int sz=q1.size();
                            queue<TreeNode*> q2;
                            vector<int> vs;
                            flag*=-1;
                            while(sz--){
                                TreeNode* v=q1.front();
                                q1.pop();
                                vs.push_back(v->val);
                                if(v->left!=NULL){
                                    q1.push(v->left);
                                }
                                if(v->right!=NULL){
                                    q1.push(v->right);
                                }
                            }
                            if(flag==1) reverse(vs.begin(), vs.end());
                            ans.push_back(vs);
                        }
                        return ans;
                    }
                ```

            

        - Boundary traversal

            Easy logic but implementation

            Step 1: Take the left boundary by going left. If can’t go anymore left then go right then again left. Repeat all this until you get to leaf node

            Step 2: Take all the leaf nodes. Do this using preorder traversal to get them in order.

            Step 3: Take all right boundary by doing opposite of left boundary.

            You have to reverse one of the left or right boundary or even leaf nodes depending on clockwise/anticlockwise boundary traversal.

            ```cpp
            bool isLeaf(node * root) {
              return !root -> left && !root -> right;
            }

            void addLeftBoundary(node * root, vector < int > & res) {
              node * cur = root -> left;
              while (cur) {
                if (!isLeaf(cur)) res.push_back(cur -> data);
                if (cur -> left) cur = cur -> left;
                else cur = cur -> right;
              }
            }
            void addRightBoundary(node * root, vector < int > & res) {
              node * cur = root -> right;
              vector < int > tmp;
              while (cur) {
                if (!isLeaf(cur)) tmp.push_back(cur -> data);
                if (cur -> right) cur = cur -> right;
                else cur = cur -> left;
              }
            	// just for reversing
              for (int i = tmp.size() - 1; i >= 0; --i) {
                res.push_back(tmp[i]);
              }
            }

            void addLeaves(node * root, vector < int > & res) {
              if (isLeaf(root)) {
                res.push_back(root -> data);
                return;
              }
              if (root -> left) addLeaves(root -> left, res);
              if (root -> right) addLeaves(root -> right, res);
            }

            vector < int > printBoundary(node * root) {
              vector < int > res;
              if (!root) return res;

              if (!isLeaf(root)) res.push_back(root -> data);

              addLeftBoundary(root, res);

              // add leaf nodes
              addLeaves(root, res);

              addRightBoundary(root, res);
              return res;
            }
            ```

        
        - Vertical order traversal

            This is genuinely easy. Just keep a map for the x-index of a vector. Multiset keeps the nodes sorted. You can modify the following code a bit for a unordered_map.

            Time: O(nlogn)

            Space: O(n)

            ```cpp
            class Solution {
                map<int, multiset<pair<int, int>>> vt;
                void preorder(TreeNode* root, int curr, int height){
                    if(!root) return;
                    vt[curr].insert({height, root->val});
                    if(root->left){
                        preorder(root->left, curr-1, height+1);
                    }
                    if(root->right){
                        preorder(root->right, curr+1, height+1);
                    }
                }
            public:
                vector<vector<int>> verticalTraversal(TreeNode* root) {
                    vector<vector<int>> ans;
                    preorder(root, 2000, 0);
                    for(auto i: vt){
                        vector<int> temp;
                        for(auto j: i.second){
                            temp.push_back(j.second);
                        }
                        ans.push_back(temp);
                    }
                    return ans;
                }
            };
            ```

        
        - Top/left/right/bottom view

            - Top view

                Basic BFS starting from node so that we get the node closest to top first. Queue holding the node and x index. Map holding the value of first node spotted at that x index.

                ```cpp
                map<int, int> mp;
                queue<pair<Node*, int>> q;
                q.push({root, 0});
                while(!q.empty()){
                    int sz=q.size();
                    while(sz--){
                        Node* v=q.front().first;
                        int ind = q.front().second;
                        q.pop();
                        if(mp.find(ind)==mp.end()){
                            mp[ind]=v->data;
                        }
                        if(v->right!=NULL){
                            q.push({v->right, ind+1});
                        }
                        if(v->left!=NULL){
                            q.push({v->left, ind-1});
                        }
                    }
                }
                vector<int> ans;
                for(auto i: mp){
                    ans.push_back(i.second);
                }
                return ans;
                ```

            
            - Bottom view

                Just store the last node spotted at that index in map. Just comment out the line that stops further nodes from being stored for an index

                ```cpp
                class Solution {
                  public:
                    vector <int> bottomView(Node *root) {
                        // Your Code Here
                        map<int, int> mp;
                        queue<pair<Node*, int>> q;
                        q.push({root, 0});
                        while(!q.empty()){
                                int sz=q.size();
                            while(sz--){
                                Node* v=q.front().first;
                                int ind = q.front().second;
                                q.pop();
                                // if(mp.find(ind)==mp.end()){
                                    mp[ind]=v->data;
                                // }
                                if(v->left!=NULL){
                                    q.push({v->left, ind-1});
                                }
                                if(v->right!=NULL){
                                    q.push({v->right, ind+1});
                                }
                            }
                        }
                        vector<int> ans;
                        for(auto i: mp){
                            ans.push_back(i.second);
                        }
                        return ans;
                    }
                ```

            
            - Right/left view

                Same thing but here use y index (level). BFS would be easy. The following code is for right view. If for left view, just use the first node spotted each level. (Commenting in the 2 lines would work)

                ```cpp
                class Solution {
                public:
                    vector<int> rightSideView(TreeNode* root) {
                        queue<TreeNode*> q;
                        q.push(root);
                        vector<int> ans;
                        int ind=-1;
                        if(!root) return ans;
                        while(!q.empty()){
                                int sz=q.size();
                                ind++;
                                ans.push_back(-1);
                            while(sz--){
                                TreeNode* v=q.front();
                                q.pop();
                                // if(mp.find(ind)==mp.end()){
                                ans[ind]=v->val;
                                // }
                                if(v->left!=NULL){
                                    q.push(v->left);
                                }
                                if(v->right!=NULL){
                                    q.push(v->right);
                                }
                            }
                        }
                        return ans;
                    }
                };
                ```

            

        - Symmetric tree

            ```cpp
            bool checkLeftRight(TreeNode* one, TreeNode* two){
                if(one!=NULL&&two==NULL) return false;
                if(two!=NULL&&one==NULL) return false;
                if(one==NULL&&two==NULL) return true;
                if(one->val!=two->val) return false;
                if(!one->left&&!two->right&&!one->right&&!two->left) return true;
                bool checkleft=checkLeftRight(one->left, two->right);
                bool checkRight=checkLeftRight(one->right, two->left);
                return checkleft&&checkRight;
            }
            ```

        
        - LCA

            If the current (sub)tree contains both p and q, then the function result is their LCA. If only one of them is in that subtree, then the result is that one of them. If neither are in that subtree, the result is null

            ```cpp
            class Solution {    
            public:
                TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
                    if(root==NULL) return NULL;
                    if(root==p) return p;
                    if(root==q) return q;
                    TreeNode* right=lowestCommonAncestor(root->right, p, q);
                    TreeNode* left=lowestCommonAncestor(root->left, p, q);
                    if(right==NULL) return left;
                    else if(left==NULL) return right;
                    else return root;
                }
            };
            ```

        
        - Max width of tree

            We can’t do this normally because the height maybe different on left and right

            ![[prep/DSA Notes/Private & Shared/Untitled 24.png|Untitled 24.png]]

            ```cpp
            int widthOfBinaryTree(TreeNode* root) {
                    queue<pair<TreeNode*, long long>> q;
                    q.push({root, 1});
                    long long maxw=0;
                    int height=1;
                    long long prevMax=0;
                    while(!q.empty()){
                        int sz=q.size();
                        long long mini=LONG_LONG_MAX, maxi=LONG_LONG_MIN;
                        while(sz--){
                            TreeNode* v=q.front().first;
                            long long ind=q.front().second;
                            q.pop();
                            // cout<<ind<<'-'<<v->val<<' ';
                            maxi=max(maxi, ind);
                            mini=min(mini, ind);
                            if(v->right) q.push({v->right, 2*ind+1-prevMax});
                            if(v->left) q.push({v->left, 2*ind-prevMax});
                        }
                        cout<<"\n";
                        maxw=max(abs(maxi-mini+1), maxw);
                        prevMax=maxi;
                        height++;
                    }
                    return maxw;
                }
            ```

        
        - Minimum time to burn tree

            basic BFS. Main problem with BFS was that you weren’t able to go up the tree (parent). So keep a parent array for that using level order traversal.

            ```cpp
            // This function for both level order and finding out the start node(virus)
            void levelOrder(TreeNode* root, unordered_map<TreeNode*, TreeNode*> &pars, TreeNode* &virus, int target){
                    if(root->val==target) virus=root;
                    if(root->left!=NULL){
                        pars[root->left]=root;
                        levelOrder(root->left, pars, virus, target);
                    }
                    if(root->right!=NULL){
                        pars[root->right]=root;
                        levelOrder(root->right, pars, virus, target);
                    }
                }
            public:
                int amountOfTime(TreeNode* root, int start) {
                    unordered_map<TreeNode*, TreeNode*> pars;
                    unordered_set<TreeNode*> vis;
                    TreeNode* virus=NULL;
                    levelOrder(root, pars, virus, start);
                    int level=-1;
                    vis.insert(virus);
                    queue<TreeNode*> q;
                    q.push(virus);
                    while(!q.empty()){
                        int sz=q.size();
                        while(sz--){
                            TreeNode* v=q.front();
                            q.pop();
                            if(v->left!=NULL){
                                if(vis.find(v->left)==vis.end())
                                q.push(v->left);
                                vis.insert(v->left);
                            }
                            if(v->right!=NULL){
                                if(vis.find(v->right)==vis.end())
                                q.push(v->right);
                                vis.insert(v->right);
                            }
                            if(pars.find(v)!=pars.end()){
                                if(vis.find(pars[v])==vis.end())
                                q.push(pars[v]);
                                vis.insert(pars[v]);
                            }
                        }
                        level++;
                    }
                    return level;
                }
            ```

        
        - Total number of nodes in a complete binary tree in O(log n)

            For complete tree if you go left everytime, then the height would be same as if you go right everytime. If both are equal then total number of nodes = 2^(height)-1

            If they aren’t equal, you recursively call this for left and right nodes until they are complete.

            ```cpp
            class Solution {
            public:
                int Lefthelper(TreeNode* node){
                    if(node->left==NULL){
                        return 1;
                    }
                    else return 1+Lefthelper(node->left);
                }
                int Righthelper(TreeNode* node){
                    if(node->right==NULL){
                        return 1;
                    }
                    else return 1+Righthelper(node->right);
                }
                int levelTraversal(TreeNode* node){
                    if(node==NULL) return 0;
                    int leftNodes=Lefthelper(node);
                    int rightNodes=Righthelper(node);
                    if(leftNodes==rightNodes) return (1<<leftNodes)-1;
                    else return 1+levelTraversal(node->left)+levelTraversal(node->right);
                }
                int countNodes(TreeNode* root) {
                    return levelTraversal(root);
                }
            };
            ```

              

        
        - You need at least an in-order and any other order(except in-order) for a unique binary tree construction

        - Construct binary tree from inorder and preorder

            Take a range for inorder. Take only index from first in preorder bcz in preorder, the root is first. In inorder, everything to the left of root is on the left and everything on the right of root is right. Use recursion to find left first and then right.

            ```cpp
            class Solution {
            public:
                TreeNode* recur(vector<int>& preorder, vector<int>& inorder, int li, int ri, int &indp){
                    if(li==ri){
                        TreeNode* node = new TreeNode(inorder[li]);
                        indp++;
                        return node;
                    }
                    int n=preorder.size();
                    for(int i=li;i<=ri;i++){
                        if(inorder[i]==preorder[indp]){
                            TreeNode* node=new TreeNode(inorder[i]);
                            indp++;
                            TreeNode* left=recur(preorder, inorder, li, i-1, indp);
                            TreeNode* right=recur(preorder, inorder, i+1, ri, indp);
                            node->right=right;
                            node->left=left;
                            return node;
                        }
                    }
                    return NULL;
                }
                TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
                    int indp=0;
                    return recur(preorder, inorder, 0, preorder.size()-1, indp);
                }
            };
            ```

        
        - Construct binary tree from inorder and postorder

            Take a range for inorder. Take only index from last in postroder bcz in postorder, the root is first. In inorder, everything to the left of root is on the left and everything on the right of root is right. Use recursion to find right first and then left.

            ```cpp
            class Solution {
            public:
                TreeNode* recur(vector<int>& inorder, vector<int>& postorder, int li, int ri, int &indpost){
                    if(li==ri){
                        TreeNode* node = new TreeNode(inorder[li]);
                        indpost--; // index of postorder decreased
                        return node;
                    }
                    for(int i=li;i<=ri;i++){
                        if(inorder[i]==postorder[indpost]){
                            TreeNode* node = new TreeNode(inorder[i]);
                            indpost--; // index of postorder decreased
            								// right calculated first
                            TreeNode* right = recur(inorder, postorder, i+1, ri, indpost);
                            TreeNode* left = recur(inorder, postorder, li, i-1, indpost);
                            node->left = left;
                            node->right = right;
                            return node;
                        }
                    }
                    return NULL;
                }
                TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
                    int indpost=postorder.size()-1;
                    return recur(inorder, postorder, 0, inorder.size()-1, indpost);
                }
            };
            ```

        
        - Serialize/de-serialize a binary tree

            ```cpp
            class Codec {
            public:

                // Encodes a tree to a single string.
                void recurser(TreeNode* root, string &s){
                    if(root==NULL){
                        s+="N";
                        s.push_back(',');
                        return;
                    }
                    string a=to_string(root->val);
                    s+=a;
                    s.push_back(',');
                    recurser(root->left, s);
                    recurser(root->right, s);

                }
                string serialize(TreeNode* root) {
                    string s="";
                    recurser(root,s);
                    return s;
                }

                // Decodes your encoded data to tree.
                TreeNode* recurdeser(vector<int>& v, int &ind){
                    if(v[ind]==-1001) return NULL;
                    TreeNode* node = new TreeNode(v[ind]);

                    TreeNode* left = NULL;
                    ind++;
                    if(ind<v.size()) left = recurdeser(v, ind);
                    TreeNode* right = NULL;
                    ind++;
                    if(ind<v.size()) right = recurdeser(v, ind);
                    node->left=left;
                    node->right = right;
                    return node;
                }
                TreeNode* deserialize(string data) {
                    vector<int> v;
                    cout<<data;
                    string s="";
                    for(int i=0;i<data.size();i++){
                        if(data[i]!=','){
                            s.push_back(data[i]);
                        }
                        else{
                            if(s=="N")
                            v.push_back(-1001);
                            else
                            v.push_back(stoi(s));
                            s="";
                        }
                    }

                    TreeNode* root = NULL;
                    int ind=0;
                    root = recurdeser(v, ind);
                    return root;
                }
            }; 
            ```

        
        - Morris Traversal

            - Morris Traversal inorder

                Works by creating a way to get back to root after going left. Inorder → LEFT, ROOT, RIGHT

                ```cpp
                vector<int> inorderTraversal(TreeNode* root){
                        // Morris traversal
                        // Here we make a thread to the rightmost child of the left subtree back to the root. 
                        // This is done through the right pointer of the last child.
                        TreeNode* cur=root;
                        vector<int> inorder;
                        while(cur!=NULL){
                            if(cur->left==NULL){
                                inorder.push_back(cur->val);
                                cur=cur->right;
                            }
                            else{
                                TreeNode* lastChild = cur->left;
                                while(lastChild->right!=NULL&&lastChild->right!=cur){   // second condition so that we don't go in a loop in the second iteration when right of lastChild is connected to the root where we began
                                    lastChild=lastChild->right;
                                }

                                if(lastChild->right==NULL){
                                    // make the thread
                                    lastChild->right=cur;
                                    cur=cur->left;
                                }
                                else if(lastChild->right==cur){
                                    // break the thread
                                    lastChild->right=NULL;
                                    inorder.push_back(cur->val);
                                    cur=cur->right;
                                }
                            }
                        }
                        return inorder;
                    }
                ```

            
            - Morris Traversal preorder

                ONLY change from inorder is that we don’t add the root while breaking the thread but while making the thread apart from when there’s no left

                ```cpp
                vector<int> preorderTraversal(TreeNode* root){
                        // Morris traversal
                        // Here we make a thread to the rightmost child of the left subtree back to the root. 
                        // This is done through the right pointer of the last child.
                        TreeNode* cur=root;
                        vector<int> preorder;
                        while(cur!=NULL){
                            if(cur->left==NULL){
                                preorder.push_back(cur->val);
                                cur=cur->right;
                            }
                            else{
                                TreeNode* lastChild = cur->left;
                                while(lastChild->right!=NULL&&lastChild->right!=cur){   // second condition so that we don't go in a loop in the second iteration when right of lastChild is connected to the root where we began
                                    lastChild=lastChild->right;
                                }

                                if(lastChild->right==NULL){
                                    // make the thread
                                    lastChild->right=cur;
                                    preorder.push_back(cur->val);    // only change from inorder
                                    cur=cur->left;
                                }
                                else if(lastChild->right==cur){
                                    // break the thread
                                    lastChild->right=NULL;
                                    // preorder.push_back(cur->val);  // only change from inorder
                                    cur=cur->right;
                                }
                            }
                        }
                        return preorder;
                    }
                ```

            

        - Flatten tree

            Did this one easily :) . Just use recursion for both the sides

            ```cpp
            TreeNode* recur(TreeNode* cur){
                    TreeNode* root = cur;
                    if(!cur) return cur;
                    if(cur->left!=NULL){
            						// keep the right in a temporary variable
                        TreeNode* temp=cur->right;
            						// convert the left subtree into a linked list and attach to right
                        cur->right=recur(cur->left);
                        cur->left=NULL;
            						// go the last of the linked list and attach the original right stored in temp
                        while(cur->right!=NULL){
                            cur=cur->right;
                        }
                        cur->right=temp;
                    }
            				// if no left then easy, just attach the right
                    cur->right=recur(cur->right);
                    return root;
                }
                void flatten(TreeNode* root) {
                    recur(root);
                }
            ```

        

    - BST

        - Deleting a node from BST

            When we delete a node from a binary search tree (BST), there are three cases to consider:

            1. The node is a leaf node (no children): In this case, we can simply remove the node from the tree.

            1. The node has one child: In this case, we can replace the node with its child.

            1. The node has two children: In this case, we need to find the node's successor (the smallest node in the right subtree) and replace the node with its successor. Then, we need to delete the successor node from the right subtree.

            The steps for deleting a node from a BST are as follows:

            1. Find the node we want to delete.

            1. If the node is a leaf node or has one child, remove it from the tree.

            1. If the node has two children, find its successor and replace it with the node to be deleted.

            1. Delete the successor from the right subtree.

            ```jsx
            class Solution {
                TreeNode* searchminright(TreeNode* root){
                    while(root->left){
                        root=root->left;
                    }
                    return root;
                }
            public:
                TreeNode* deleteNode(TreeNode* root, int key) {
                    if(!root) return NULL;
                    if(root->val==key){
                        if(root->left==NULL&&root->right==NULL){
                            delete root;
                            return NULL;
                        }   
                        else if(root->left!=NULL&&root->right==NULL){
                            TreeNode* temp=root->left;
                            delete root;
                            return temp;
                        }
                        else if(root->right!=NULL&&root->left==NULL){
                            TreeNode* temp=root->right;
                            delete root;
                            return temp;
                        }
                        else{
                            int mini=searchminright(root->right)->val;
                            root->val=mini;
                            root->right=deleteNode(root->right, mini);
                            return root;
                        }
                    }
                    else if(root->val>key){
                        root->left=deleteNode(root->left, key);
                        return root;
                    }
                    else if(root->val<key){
                        root->right=deleteNode(root->right, key);
                        return root;
                    }
                    return root;
                }
            };
            ```

              

        
        - Balance a BST

            O(n) extra space → get the inorder in a separate vector. Then in each recursion call, mid will be the root node. left child would be recur(left, mid-1) and right child would be recur(mid+1, right)

            ```cpp
            void recur(TreeNode* root, vector<TreeNode*>& inorder){
                if(!root) return;
                recur(root->left, inorder);
                inorder.push_back(root);
                recur(root->right, inorder);
            }
            TreeNode* build(vector<TreeNode*>& inorder, int left, int right){
                if(left>right) return NULL;
                int mid = (left+right)/2;
                inorder[mid]->left= build(inorder, left, mid-1);
                inorder[mid]->right=build(inorder, mid+1,right);
                return inorder[mid];
            }
            TreeNode* balanceBST(TreeNode* root) {
                vector<TreeNode*> inorder;
                recur(root, inorder);
                return build(inorder, 0, inorder.size()-1);
            }
            ```

        
        - Inorder of BST is sorted

            ```
            void inorder(TreeNode* root, int &k, int& ans){
                    if(!root) return;
                    inorder(root->left, k, ans);
                    k--;
                    if(k==0){
                        ans=root->val;
                        return;
                    }
                    inorder(root->right, k, ans);
                }
            ```

            Kth smallest element. Note the &k.

        
        - Validate a BST

            Keep a range from mini to maxi. The root should lie between that. While going left, the all nodes should be less than root and while going right, all the nodes should be greater than the root.

            ```cpp
            bool recur(TreeNode* root, TreeNode* mini, TreeNode* maxi){
                    if(!root) return true;
                    if(mini!=NULL&&mini->val>=root->val) return false;
                    if(maxi!=NULL&&maxi->val<=root->val) return false;
                    return recur(root->left, mini, root)&&recur(root->right, root, maxi);
                }
            public:
                bool isValidBST(TreeNode* root) {
                    return recur(root, NULL, NULL);
                }
            ```

        
        - Note the difference in finding LCA in BST and BT

            - BST

                If both nodes lie on left of node then check left

                If both nodes lie on right of node then check right

                otherwise the node is the LCA

                ```cpp
                int curr=root->val;
                if(curr>q->val&&curr>p->val) return lowestCommonAncestor(root->left, p, q);
                if(curr<q->val&&curr<p->val) return lowestCommonAncestor(root->right, p, q);
                return root;
                ```

                  

            
            - BT

                If left or right = the nodes then return nodes

                postorder and if right is null → return left, if left is null then return right, else return root

                ```cpp
                if(root==NULL||root==p||root==q) return root;
                TreeNode* right=lowestCommonAncestor(root->right, p, q);
                TreeNode* left=lowestCommonAncestor(root->left, p, q);
                if(right==NULL) return left;
                else if(left==NULL) return right;
                else return root;
                ```

            

            

        - Inorder successor:

            1. Store inorder and print next value

            1. Do inorder and use a global variable which stores the min value greater than target

            1. If cur≤target, go right. If cur>target, store ans and go left

                ```cpp
                Node * inOrderSuccessor(Node *root, Node *x)
                    {
                        //Your code here
                        Node* cur=root;
                        Node* ans=NULL;
                        while(cur!=NULL){
                            if(cur->data<=x->data){
                                cur=cur->right;
                            }
                            else{
                                ans=cur;
                                cur=cur->left;
                            }
                        }
                        return ans;
                    }
                ```

            

        - Making a BST from preorder

            We can keep a upperbound. While going left, we update the upperbound to node’s value. While going right, we don’t update the upperbound.

            ```cpp
            class Solution {
                TreeNode* recur(vector<int>& preorder, int &ind, int upperbound){
                    if(ind==preorder.size()) return NULL;
                    if(preorder[ind]>=upperbound) return NULL;
                    TreeNode* root = new TreeNode(preorder[ind]);
                    ind++;
                    root->left = recur(preorder, ind, root->val);
                    root->right = recur(preorder, ind, upperbound);
                    return root;
                }
            public:
                TreeNode* bstFromPreorder(vector<int>& preorder) {
                    int ind=0;
                    return recur(preorder, ind, INT_MAX);
                }
            };
            ```

        
        - make bst from bt

            We find inorder of bt as vector<nodes>. We sort inorder by value. Now, again inorder on bt and replace the nodes while while going through the inorder of bt by that of bst

        
        - 2 sum in BST

            just apply binary search for each element in inorder.

            ```cpp
            class Solution {
                bool find(TreeNode* root, int target){
                    if(!root) return false;
                    if(root->val==target) return true;
                    if(root->val<target) return find(root->right, target);
                    if(root->val>target) return find(root->left, target);
                    return false;
                }
                bool inorder(TreeNode* root, TreeNode* node, int k){
                    if(!node) return false;
                    bool left = inorder(root, node->left, k);
                    bool check = find(root, k-node->val);
                    if(k-node->val == node->val) check = false;
                    bool right = inorder(root, node->right, k);
                    return left||check||right;
                }
            public:
                bool findTarget(TreeNode* root, int k) {
                    return inorder(root, root, k);
                }
            };
            ```

        
        - Recovering a BST if two nodes are swapped

            Here are the steps to recover a BST if two nodes are swapped using no extra space:

            1. Traverse the tree in inorder and keep track of the last visited node.

            1. If the current node is smaller than the last visited node, mark the previous as first and current as second node

            1. If another node is found that is smaller than the last visited node, mark this node as the last swapped node.

            1. After the traversal is complete, if we found the second violation (last ≠ NULL), we swap the first and last. Otherwise we swap first and second.

            ```cpp
            class Solution {
                void inorder(TreeNode* root, TreeNode* &prev, TreeNode* &first, TreeNode* &second, TreeNode* &last){
                    if(!root) return;
                    inorder(root->left, prev, first, second, last);
                    if(prev->val>root->val){
                        if(first == NULL){
                            first = prev;
                            second = root;
                        }
                        else{
                            last = root;
                        }
                    }
                    cout<<prev->val<<' '<<root->val<<'\n';
                    prev = root;
                    inorder(root->right, prev, first, second, last);
                }
            public:
                void recoverTree(TreeNode* root) {
                    TreeNode* first = NULL;
                    TreeNode* second = NULL;
                    TreeNode* last = NULL;
                    TreeNode* prev = new TreeNode(INT_MIN);
                    inorder(root, prev, first, second, last);
                    if(first&&last) swap(first->val, last->val);
                    else if(first&&second) swap(first->val, second->val);
                }
            };
            ```

        
        - Generate all unique BST

            Given a number n, generate all structurally unique binary search trees with nodes from 1 to n.

            ```cpp
            class Solution {
            public:
                vector<TreeNode*> recur(int l, int r){
                    vector<TreeNode*> res;
                    if(l>r) return {NULL};
                    for(int i=l;i<=r;i++){
            						vector<TreeNode*> leftVec=recur(l, i-1);
            						vector<TreeNode*> rightVec=recur(i+1, r)
                        for(auto left: leftVec){
                            for(auto right: rightVec){
                                TreeNode* root = new TreeNode(i);
                                root->left=left;
                                root->right=right;
                                res.push_back(root);
                            }
                        }
                    }
                    return res;
                }
                vector<TreeNode*> generateTrees(int n) {
                    return recur(1, n);
                }
            };
            ```

        

    - Heaps

        - basics:

            Node: ith index

            Left child: 2*i index

            Right child: 2*i+1 index

            Parent: i/2 index

            > Identify this question is of heap?  
            > Keywords: Kth, Smallest/Largest  
            > Kth + smallest → Max-heap  
            > Kth + largest → Min-heap

            priority_queue<int, vector<int>, greater<int>> min_heap;

            priority_queue<int> max_heap;

            heap.pop(), heap.push(), heap.size(), heap.top()

        
        - Heapify

        - Kth largest/smallest

            ```cpp
            int findKthLargest(vector<int>& nums, int k) {
                    priority_queue<int, vector<int>, greater<int>> heap;
                    for(int i = 0;i<nums.size();i++){
                        heap.push(nums[i]);
                        if(heap.size()>k)
                            heap.pop();
                    }
                    return heap.top();
                }
            ```

        
        - Nearly sorted array/k sorted array

            Given unsorted array with elements at at max k distance from their original position in sorted array.

            ```cpp
            vector<int> arr = {6,5,3,2,8,10,9}
            int k = 3;

            priority_queue<int, vector<int>, greater<int>> heap;
            int num = k, ind = 0;
            while(num--){
            	heap.push(arr[ind]);
            	ind++;
            }
            for(int i = ind;i<arr.size();i++){
            	heap.push(arr[i]);
            	arr[i-ind]=heap.top();
            	heap.pop();
            }
            ind++;
            while(!heap.empty()){
            	arr[ind]=heap.top();
            	heap.pop();
            	ind++;
            }
            ```

        
        - Merge k sorted arrays

            - Create a min heap of size k containing the first element from each array

            - Pop the smallest element from the heap and add it to the output array

            - Replace the popped element in the heap with the next element from the same array

            - Repeat steps 2-3 until all elements have been added to the output array

            ```cpp
            typedef pair<pair<int, int>, int> ppi;
            class Solution
            {
                public:
                //Function to merge k sorted arrays.
                vector<int> mergeKArrays(vector<vector<int>> arr, int K)
                {
                    //code here
                    priority_queue<ppi, vector<ppi>, greater<ppi>> min_heap;
                    vector<int> ans;
                    for(int i=0;i<arr.size();i++){
                        min_heap.push({{arr[i][0], i}, 0});
                    }
                    while(!min_heap.empty()){
                        int num = min_heap.top().first.first;
                        int i = min_heap.top().first.second;
                        int j = min_heap.top().second;
                        min_heap.pop();
                        ans.push_back(num);
                        if(j<K-1){
                            min_heap.push({{arr[i][j+1], i}, j+1});
                        }
                    }
                    return ans;
                }
            };
            ```

        
        - Merge K sorted Lists

            Similar approach. What’s different?

            Ans → use a comparator function (has to be wrapped in a struct). And the priority queue would be of ListNode*

            To merge k sorted lists, we can use a min heap of size k containing the first node from each list. We can then pop the smallest element from the heap and add it to the output list. We then replace the popped element in the heap with the next element from the same list, and repeat the process until all elements have been added to the output list.

            To implement this approach, we need to create a struct and comparator function, as the priority queue needs to be of ListNode* type. The struct should contain the list node and the index of the list it belongs to. The comparator function should compare the values of the list nodes.

            ```cpp
            typedef ListNode* li;
            class Solution {
            struct compare {                               // custom comparator struct
                bool operator()(ListNode* l, ListNode* r) {
                    return l->val > r->val;
                }
            };
            public:
                ListNode* mergeKLists(vector<ListNode*>& lists) {
                    priority_queue<li, vector<li>, compare> min_heap;  // no need of template variables in comparator
                    for(auto i: lists){
                        if(i!=NULL)                // look out for nulls
                        min_heap.push(i);
                    }
                    if(min_heap.empty()) return NULL;
                    ListNode* node = min_heap.top();
                    ListNode* curr = node;
                    min_heap.pop();
                    if(node->next)
                    min_heap.push(node->next);
                    while(!min_heap.empty()){
                        ListNode* temp = min_heap.top();
                        min_heap.pop();
                        if(temp->next)
            	            min_heap.push(temp->next);
                        curr->next = temp;
                        curr = temp;
                    }

                    return node;
                }
            };
            ```

        
        - Hands of straights

            **Approach 1 (my approach):**

            Problem statement: [https://leetcode.com/problems/hand-of-straights/](https://leetcode.com/problems/hand-of-straights/)

            - We maintain a map of all the cards in the hand and their frequency.

            - We traverse the map from the smallest card to the greatest.

            - For each card, we check if there are enough cards in the hand to form a valid straight of length w.

            - We decrement the frequency of each card that we use to form the straight from the map.

            - If we successfully form all straights from the hand, we return true. If we run out of cards to form a straight, we return false.

            ```cpp
            bool isNStraightHand(vector<int>& hand, int W) {
                    if(hand.size()%W!=0) return false;
                    map<int, int> mp;
                    for(int i = 0;i<hand.size();i++) mp[hand[i]]++;
                    while(mp.size()>0){
                        int curr = mp.begin()->first, i = 0;
                        while(i<W){
                            if(mp.find(curr+i)==mp.end()) return false;
                            mp[curr+i]--;
                            if(mp[curr+i]==0) mp.erase(curr+i);
                            i++;
                        }
                    }
                    return true;
                }
            ```

            **Approach 2 (using priority_queue and unordered_map):**

            Problem statement: [https://leetcode.com/problems/hand-of-straights/](https://leetcode.com/problems/hand-of-straights/)

            - We can maintain a map of all the cards in the hand and their frequency.

            - We can traverse the map from the smallest card to the greatest.

            - For each card, we can check if there are enough cards in the hand to form a valid straight of length w.

            - We can decrement the frequency of each card that we use to form the straight from the map.

            - If we successfully form all straights from the hand, we return true. If we run out of cards to form a straight, we return false.

            We can implement this using a priority queue, which will store pairs of the card value and the frequency. We can then sort the cards in the queue by their value and pop the smallest card each time. We can then check whether there are enough cards in the hand to form a straight of length w, and repeat the process until all cards have been used or we cannot form any more straights.

        
        - Task Scheduler

            # Task Scheduler

            Problem statement: [https://leetcode.com/problems/task-scheduler/](https://leetcode.com/problems/task-scheduler/)

            In cycles of n, do the most frequent job and take it out of the queue into a temp vector. If the tasks are left, the tasks are added back into the queue.

              

            ```cpp
            class Solution {
            public:
                int leastInterval(vector<char>& tasks, int n) {
                    vector<int> hash(26, 0);
                    for(auto i: tasks){
                        hash[i-'A']++;
                    }
                    priority_queue<pair<int, int>> pq;
                    for(int i=0;i<26;i++){
                        if(hash[i]>0)
                        pq.push({hash[i], i});
                    }
                    int ans = 0;
                    while(!pq.empty()){
                        vector<pair<int,int>> temp;
                        for(int i=0;i<=n;i++){
                            ans++;
                            if(pq.empty()) continue;
                            auto [freq, ch] = pq.top();
                            pq.pop();
                            hash[ch]--;
                            if(hash[ch]>0){
                                temp.push_back({hash[ch], ch});
                            }
                            if(pq.empty()&&temp.empty()) break;
                        }
                        for(auto i: temp){
                            pq.push(i);
                        }
                    }
                    return ans;
                }
            };
            ```

            ```cpp
            bool isNStraightHand(vector<int>& hand, int W) {
                if(hand.size()%W!=0) return false;
                map<int, int> mp;
                for(int i = 0;i<hand.size();i++) mp[hand[i]]++;
                priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap;
                for(auto i: mp){
                    min_heap.push({i.first, i.second});
                }
                while(!min_heap.empty()){
                    int curr = min_heap.top().first, i = 0;
                    while(i<W){
                        if(min_heap.empty()||min_heap.top().first!=curr+i) return false;
                        int freq = min_heap.top().second;
                        if(freq == 1) min_heap.pop();
                        else min_heap.top().second--;
                        i++;
                    }
                }
                return true;
            }
            ```

        
        - Find median in a stream

            First check out similar problem called [Kth largest number in stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/#:~:text=Implement%20KthLargest%20class%3A,largest%20element%20in%20the%20stream). Easy shit.

            ![[Screenshot_20230601_215221.png]]

            ```cpp
            class KthLargest {
                priority_queue<int, vector<int>, greater<int>> pq;
                int kth=0;
            public:
                KthLargest(int k, vector<int>& nums) {
                    kth=k;
                    for(int i=0;i<nums.size();i++){
                        pq.push(nums[i]);
                        if(pq.size()==k+1){
                            pq.pop();
                        }
                    }
                }

                int add(int val) {
                    pq.push(val);
                    if(pq.size()==kth+1) pq.pop();
                    return pq.top();
                }
            };
            ```

              

            ## Now, we move to real problem

            ![[Screenshot_20230601_215306.png]]

            ### Solution:

            We can use two priority queues to solve this problem: a max heap to store the smaller half of the elements and a min heap to store the larger half of the elements. The max heap will contain the smallest half of the elements, while the min heap will contain the largest half of the elements. We can then find the median by taking the top element of the max heap if the total number of elements is odd, or by taking the average of the top elements of the max and min heaps otherwise.

            - We need to balance the size between `maxHeap` and `minHeap` while processing. Hence after adding `k` elements,

                - If `k = 2 * i` then `maxHeap.size = minHeap.size = i`

                - If `k = 2 * i + 1`, let `maxHeap` store 1 element more than `minHeap`, then `maxHeap.size = minHeap.size + 1`.

            
            - When adding a new number `num` into our `MedianFinder`:

                - Firstly, add `num` to the `maxHeap`, now `maxHeap` may contain the big element (which should belong to `minHeap`). So we need to balance, by removing the highest element from `maxHeap`, and offer it to `minHeap`.

                - Now, the `minHeap` might hold more elements than `maxHeap`, in that case, we need to balance the size, by removing the lowest element from `minHeap` and offer it back to `maxHeap`.

            
            ```cpp
            class MedianFinder {
                priority_queue<int> max_heap;
                priority_queue<int, vector<int>, greater<int>> min_heap;
            public:
                /** initialize your data structure here. */
                MedianFinder() {

                }

                void addNum(int num) {
                    max_heap.push(num);
                    min_heap.push(max_heap.top());
                    max_heap.pop();
                    if(max_heap.size()<min_heap.size()){
                        max_heap.push(min_heap.top());
                        min_heap.pop();
                    }
                }

                double findMedian() {
                    if(max_heap.size()==min_heap.size()){
                        return (double)(max_heap.top()+min_heap.top())/2;
                    }
                    else{
                        return max_heap.top();
                    }
                }
            };
            ```

        
        - Maximum sum combinations

            Sort the arrays and put the max into the heap along with their indices. We have to avoid taking same indices twice, so use a visited set. Take the top sum, put in answer. From the top index, once move the first index back and put into pq and then move another index back and put into pq. Do this until Array is of C size.

            ```cpp
            vector<int> Solution::solve(vector<int> &A, vector<int> &B, int C) {
                vector<int> res;
                priority_queue<pair<int, pair<int,int>>> pq;
                set<pair<int, int>> vis;
                sort(A.begin(), A.end());
                sort(B.begin(), B.end());
                int n=A.size();
                pq.push({A[n-1]+B[n-1], {n-1, n-1}});
                vis.insert({n-1, n-1});
                while(res.size()<C){
                    res.push_back(pq.top().first);
                    int x=pq.top().second.first;
                    int y=pq.top().second.second;
                    pq.pop();
                    if(x>0&&vis.find({x-1, y})==vis.end()){
                        pq.push({A[x-1]+B[y], {x-1, y}});
                        vis.insert({x-1, y});
                    }
                    if(y>0&&vis.find({x, y-1})==vis.end()){
                        pq.push({A[x]+B[y-1], {x, y-1}});
                        vis.insert({x, y-1});
                    }
                }
                return res;
            }
            ```

        
        - The skyline problem

            Make a set for each point with it’s height in sorted order. Insert the start of building with negative height to indicate that it is the start. Now initialize a set of heights with 0. keep track of prev height. Iterate over the points and if it is the start, then put the height into the heights set. If it is the end, then get it out. Now, if the biggest height available in the set is not equal to the prev height, that means we have to put it in the ans vector. Update prev to biggest height.

            ```cpp
            class Solution {
            public:
                vector<vector<int>> getSkyline(vector<vector<int>>& a) {
                    multiset<pair<int, int>> mp;
                    for(auto i: a){
                        mp.insert({i[0], -i[2]});
                        mp.insert({i[1], i[2]});
                    }

                    vector<vector<int>> ans;
                    multiset<int, greater<int>> st;

                    st.insert(0);
                    int prevh = 0;

                    for(auto i: mp){
                        int curp = i.first;
                        int curh = i.second;

                        if(curh < 0)
                            st.insert(-curh);
                        else
                            st.erase(st.find(curh));

                        int bigh = *st.begin();

                        if(prevh != bigh){
                            ans.push_back({curp, bigh});
                        }
                        prevh = bigh;
                    }
                    return ans;
                }
            };
            ```

        

    - Stacks and Queues

        Note: If interviewer asks not to use stl stack, just use vector with push_back, pop_back and back() for push, pop and top. Same as stack.

        - Basic implementations

            - Implement a stack using queue

                - Using two queues

                    Push: Add x to Q2, put each element of Q1 into Q2, swap Q1 and Q2

                    pop: pop from Q1

                
                - Using one queue

                    As a wise person once said, implementing a stack using queue is a dumb idea.

                    You have to rotate the whole queue after pushing an element. Other operations remain same

                      

                    ```cpp
                    class MyStack {
                    public:
                        queue<int> q;
                        MyStack() {

                        }

                        void push(int x) {
                            q.push(x);
                            int n=q.size();
                            for(int i=0;i<n-1;i++){
                                q.push(q.front());
                                q.pop();
                            }
                        }

                        int pop() {
                            int x = q.front();
                            q.pop();
                            return x;
                        }

                        int top() {
                            return q.front();
                        }

                        bool empty() {
                            return q.empty();
                        }
                    };
                    ```

                      

                

            - Implement a queue using stack

                Two stacks → primary and secondary. While pushing, first pour everything of primary into secondary, then push the element into secondary then pour the whole secondary into primary back. Use primary for top, pop and empty operations

                ```cpp
                class MyQueue {
                public:
                    stack<int> primary, temp;
                    MyQueue() {

                    }

                    void push(int x) {
                        while(!primary.empty()){
                            temp.push(primary.top());
                            primary.pop();
                        }
                        primary.push(x);
                        while(!temp.empty()){
                            primary.push(temp.top());
                            temp.pop();
                        }
                    }

                    int pop() {
                        int x=primary.top();
                        primary.pop();
                        return x;
                    }

                    int peek() {
                        return primary.top();
                    }

                    bool empty() {
                        return primary.empty();
                    }
                };
                ```

            
            - Implement a queue using linked list

                In push operation, remember that you have to check using front and not rear otherwise you’ll get wrong answer

                Push:

                ![[prep/DSA Notes/Private & Shared/Untitled 25.png|Untitled 25.png]]

                Pop:

                ![[prep/DSA Notes/Private & Shared/Untitled 26.png|Untitled 26.png]]

                ```cpp
                void MyQueue:: push(int x)
                {
                    // Your Code
                    QueueNode* temp=new QueueNode(x);
                    if(front!=NULL){
                        rear->next=temp;
                        rear=temp;
                    }
                    else{
                        front=temp;
                        rear=temp;
                    } 
                }

                //Function to pop front element from the queue.
                int MyQueue :: pop()
                {
                    // Your Code   
                    if(front==NULL) return -1;
                    int x=front->data;
                    QueueNode* temp=front;
                    front=front->next;
                    delete temp;
                    return x;
                }
                ```

            
            - Implement a stack using linked list

                push at front and pop at front.

                ```cpp
                Node* front=NULL;
                void push(int data)
                    {
                        //Write your code here
                        Node* temp = new Node(data);
                        temp->next=front;
                        front=temp;
                        sz++;

                    }
                void pop()
                    {
                        //Write your code here
                        if(front==NULL) return;
                        sz--;
                        Node* temp=front->next;
                        delete front;
                        front=temp;
                    }

                int getTop()
                    {
                        //Write your code here
                        if(front==NULL) return -1;
                        return front->data;
                    }
                ```

            

        - Implement a min-stack

            ### O(2*n) space and O(1) time:

            Use a stack of pair of int. First is the pushed item and second is min until now.

            ```cpp
            stack<pair<int, int>> st;
                MinStack() {

                }

                void push(int val) {
                    if(st.empty()) st.push({val, val});
                    else st.push({val, min(val, st.top().second)});
                }

                void pop() {
                    st.pop();
                }

                int top() {
                    return st.top().first;
                }

                int getMin() {
                    return st.top().second;
                }
            ```

            ### O(n) space and O(1) time:

            IDK dude samjha nahi

            ```cpp
            class MinStack {
              stack < long long > st;
              long long mini;
              public:
                /** initialize your data structure here. */
                MinStack() {
                  while (st.empty() == false) st.pop();
                  mini = INT_MAX;
                }

              void push(int value) {
                long long val = Long.valuevalue;
                if (st.empty()) {
                  mini = val;
                  st.push(val);
                } else {
                  if (val < mini) {
                    st.push(2 *val*1LL - mini);
                    mini = val;
                  } else {
                    st.push(val);
                  }
                }
              }

              void pop() {
                if (st.empty()) return;
                long long el = st.top();
                st.pop();

                if (el < mini) {
                  mini = 2 * mini - el;
                }
              }

              int top() {
                if (st.empty()) return -1;

                long long el = st.top();
                if (el < mini) return mini;
                return el;
              }

              int getMin() {
                return mini;
              }
            };
            ```

            This code implements a class called MinStack that allows the user to perform stack operations like push, pop, top, and also provides an additional feature of finding the minimum element in the stack in constant time (O(1)). This feature is particularly useful when working with large datasets where finding the minimum element in the stack can be time-consuming.

            The MinStack class is implemented using a stack data structure to store the elements. Additionally, it maintains a variable called mini that keeps track of the current minimum element in the stack. The push method of the class is designed to check if the new element being added is smaller than the current minimum element. If it is, the value of the new element is adjusted before being pushed onto the stack. Specifically, the adjusted value is calculated as 2 * val - mini, where val is the original value of the new element and mini is the current minimum value in the stack.

            The pop method of the class is designed to remove the top element from the stack and update the value of the minimum element if necessary. Specifically, if the popped element is smaller than the current minimum element, the value of the minimum element is updated as 2 * mini - el, where el is the value of the popped element.

            The top method of the class is designed to return the top element of the stack, while the getMin method is designed to return the current minimum element in the stack. These methods can be used to retrieve the required information about the stack in constant time (O(1)).

            Overall, the MinStack class is a useful data structure that provides an efficient way to perform stack operations while also keeping track of the minimum element in the stack. It is a good example of how a simple modification to a basic data structure can lead to significant improvements in performance and functionality.

        
        - infix postfix prefix

            **isalpha:** Checks if it is alphabet

            - Infix to postfix

                1. Scan the string from left to right.

                2. If scanned charecter(sc) is a alphabet then add it to the answer.

                3. If sc is a opening parenthesis '(' then push it to the stack

                4. If sc is a closing parenthesis ')' then till we find this  
                '(' in the stack we need to pop the element from the stack and add it to  
                the answer.(Associativity)

                5.  If sc is a operator then while the operators present in  
                the stack has higher precedence we need to pop from the stack and add it  
                to the answer. Then add the scanned operator to the stack.

                6. Add remaining elements from the stack to the answer

            
            - Prefix to infix

                ```cpp
                class Solution {
                  public:
                    string preToInfix(string pre_exp) {
                        stack<string>st;
                        int n=pre_exp.size()-1;
                        for(int i=n;i>-1;i--)
                        {
                            char ch = pre_exp[i];
                            if(ch=='^' || ch=='/' || ch=='*' || ch=='+' || ch=='-')
                            {
                                string exp = "(" + st.top() + ch;
                                st.pop();
                                exp += st.top() + ")";
                                st.pop();
                                st.push(exp);
                            }
                            else
                            {
                                string temp="";
                                temp += ch;
                                st.push(temp);
                            }
                        }
                        return st.top();
                    }
                };
                ```

            
            - Prefix to Postfix

                ```cpp
                string preToPost(string str) {
                        stack<string> st;
                        for (int i = str.length()-1; i>=0; i--) {
                              char c=str[i];
                              if((c>='a' && c<='z') || (c>='A' && c<='Z')){
                                    st.push(string(1,str[i]));
                                }
                              else {
                                  string topfirst=st.top();st.pop();
                                  string topsecond=st.top();st.pop();
                                  st.push(a+b+c);
                              }
                        }
                        return st.top();
                    }
                ```

            
            - Postfix to Prefix

                ```cpp
                string postToPre(string s) {
                        // Write your code here
                        stack<string> st;
                        string str;
                        for(int i=0;i<s.size();i++){
                            if(isalpha(s[i])){
                                string temp = "";
                                temp += s[i];
                                st.push(temp);
                            }

                            else{

                                string s1 = st.top();

                                st.pop();

                                string s2 = st.top();

                                st.pop();

                                string temp = "";

                                temp += s[i]+s2+s1;

                                st.push(temp);

                            }

                        }

                        return st.top();

                    }
                ```

            
            - Postfix to infix

                ```cpp
                bool isopd(char ch)
                  {
                        return (ch>='a' and ch <='z') || (ch >= 'A' and ch <= 'Z') || (ch >= '0' and ch <= '9');
                  }
                string postToInfix(string exp) {
                    // Write your code here
                    stack<string>stk;
                    for(int i=0;i<exp.length();i++)
                    {
                         if(isopd(exp[i]))
                         {   
                               string temp(1 , exp[i]);
                               stk.push(temp);
                         }
                         else
                         {
                              string x = stk.top(); stk.pop();
                              string y = stk.top(); stk.pop();
                               stk.push('('+y+exp[i]+x+')');
                         }
                    }
                    return stk.top();
                }
                ```

            
            - Infix to prefix

                - **Step 1:** Reverse the infix expression. Note while reversing each ‘(‘ will become ‘)’ and each ‘)’ becomes ‘(‘.

                - **Step 2:** Convert the reversed **[infix expression to “nearly” postfix expression](https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/)**.

                    - While converting to postfix expression, instead of using pop operation to pop operators with greater than or equal precedence, here we will only pop  
                        the operators from stack that have greater precedence.

                
                - **Step 3:** Reverse the postfix expression.

            

        ### Monotonic stack:

        Stack with it’s elements in only one order → increasing or decreasing

        - Balanced parenthesis without using stack

            If only one type of parenthesis, we can use a counter. `) → - and (→ +`. if at any point it goes negative, invalid.

        
        - Next Greater Element

            ## Next Greater Element

            ### Problem statement

            Given an array of integers, find the next greater element for each element in the array.

            The "next greater element" of an element in the array is the first element to its right that is greater than it. If no such element exists, output -1.

            ### Approach

            We can use a stack to solve this problem. We can initialize an empty stack and iterate through the array from right to left. For each element, we can pop all elements from the stack that are smaller than the current element and update their next greater element to be the current element. We can then push the current element onto the stack.

            After the iteration is complete, any elements remaining in the stack do not have a next greater element. We can update their next greater element to be -1.

            ### Complexity Analysis

            - Time complexity: O(n), where n is the length of the array. This is because each element is pushed onto and popped off the stack at most once.

            - Space complexity: O(n), where n is the length of the array. This is because we use a stack to store at most n elements.

            ### Code

            ```cpp
            vector<int> nextGreaterElements(vector<int>& nums) {
                int n = nums.size();
                vector<int> res(n, -1);
                stack<int> st;
                for(int i = n-1; i>=0; i--){
                    while(!st.empty() && nums[st.top()]<=nums[i]){
                        st.pop();
                    }
                    if(!st.empty()){
                        res[i] = nums[st.top()];
                    }
                    st.push(i);
                }
                return res;
            }
            ```

            ### Example

            Input: [1,2,1]

            Output: [2,-1,2]

            Explanation: The next greater element for 1 is 2. The next greater element for 2 is -1 since there is no element to its right that is greater than it. The next greater element for the last 1 is 2.

        
        - Next Greater Element in circular array

            ```cpp
            vector<int> nextGreaterElements(vector<int>& nums) {
                    int n = nums.size();
                    stack<int> st;
                    vector<int> res(n, -1);
                    for(int i=2*n-1;i>=0;i--){
                        while(!st.empty()&&nums[st.top()]<=nums[i%n]){
                            st.pop();
                        }
                        if(st.empty()){
                            res[i%n]=-1;
                        }
                        else{
                            res[i%n]=nums[st.top()];
                        }
                        st.push(i%n);
                    }
                    return res;
                }
            ```

        
        - Largest Rectangular Area in histogram

            Har index pe uske left me nearest smaller and right me nearest smaller ke beech me hi rectangle ban payega

            ![[prep/DSA Notes/Private & Shared/Untitled 27.png|Untitled 27.png]]

            - big but intuitive code

                ```cpp
                class Solution {
                public:
                    int largestRectangleArea(vector<int>& heights) {
                        int n = heights.size();
                        stack<int> nse, pse;
                        vector<int> ns(n, -1), ps(n, -1);
                        for(int i=0;i<n;i++){
                            while(!pse.empty()&&heights[pse.top()]>=heights[i]){
                                pse.pop();
                            }
                            if(!pse.empty()){
                                ps[i]=pse.top();
                            }
                            pse.push(i);
                        }
                        for(int i=n-1;i>=0;i--){
                            while(!nse.empty()&&heights[nse.top()]>=heights[i]){
                                nse.pop();
                            }
                            if(!nse.empty()){
                                ns[i]=nse.top();
                            }
                            nse.push(i);
                        }

                        int maxi = 0, nexti, previ;
                        for(int i=0;i<n;i++){
                            if(ns[i]!=-1)
                            nexti = heights[i]*abs(i-ns[i]);
                            else 
                            nexti = heights[i]*(n-i);
                            if(ps[i]!=-1)
                            previ = heights[i]*abs(i-ps[i]);
                            else 
                            previ = heights[i]*(i+1);
                            int sum = nexti+previ-heights[i];
                            maxi=max(maxi, sum);
                        }
                        return maxi;
                    }
                };
                ```

            
            - small but kisi aur ka code

                # Largest Rectangle in Histogram

                ## Problem Statement

                Given an array of non-negative integers representing the heights of bars in a histogram, find the largest rectangular area that can be formed in the histogram.

                ## Example

                Input: `[2,1,5,6,2,3]`

                Output: `10`

                ## Solution

                We can use a stack to solve this problem. We can iterate through the array from left to right and maintain a stack of indices representing the bars that are currently in consideration for forming a rectangle. For each bar, we can add it to the stack if it is taller than the previous bar, or keep popping bars off the stack until we find a bar that is shorter than the current bar. For each bar that is popped off the stack, we can calculate the area of the rectangle that it forms using the following formula:

                ```
                area = heights[top] * (i - stack.top() - 1)
                ```

                where `heights[top]` is the height of the popped bar, `i` is the current index, and `stack.top()` is the index of the previous bar that is still in the stack.

                We can keep track of the maximum area that we encounter during this process and return it as the answer.

                ## Complexity Analysis

                - Time complexity: O(n), where n is the length of the input array. This is because each bar is pushed onto and popped off the stack at most once.

                - Space complexity: O(n), where n is the length of the input array. This is because we use a stack to store at most n elements.

                ## Code

                ```cpp
                class Solution {
                public:
                    int largestRectangleArea(vector<int>& heights) {
                        int n = heights.size();
                        stack<int> st;
                        int maxi = 0;
                        for(int i=0;i<=n;i++){
                            while(!st.empty()&&(i==n||heights[st.top()]>heights[i])){
                                int top = st.top();
                                st.pop();
                                int area = heights[top]*(st.empty()?i:(i-st.top()-1));
                                maxi=max(maxi, area);
                            }
                            st.push(i);
                        }
                        return maxi;
                    }
                };
                ```

            

        - Maximal Rectangle

            Binary matrix. Biggest rectangle of only ones

            Similar to largest rectangular area histogram. Break the current height of building if in that column, we encounter a zero.

            ![[prep/DSA Notes/Private & Shared/Untitled 28.png|Untitled 28.png]]

            ```cpp
            class Solution {
                int largestRectangleArea(vector<int>& heights) {
                    int n = heights.size();
                    stack<int> st;
                    int maxi = 0;
                    for(int i=0;i<=n;i++){
                        while(!st.empty()&&(i==n||heights[st.top()]>heights[i])){
                            int top = st.top();
                            st.pop();
                            int area = heights[top]*(st.empty()?i:(i-st.top()-1));
                            maxi=max(maxi, area);
                        }
                        st.push(i);
                    }
                    return maxi;
                }
            public:
                int maximalRectangle(vector<vector<char>>& matrix) {
                    vector<int> curHeights(matrix[0].size(), 0);
                    int maxi = 0;
                    for(int i=0;i<matrix.size();i++){
                        for(int j=0;j<matrix[0].size();j++){
                            if(matrix[i][j]=='1') curHeights[j]+=1;
                            if(matrix[i][j]=='0') curHeights[j]=0;
                        }
                        maxi=max(maxi, largestRectangleArea(curHeights));
                    }
                    return maxi;
                }
            };
            ```

        
        - Rainwater Trapping

            - My way:

                Only keep track of max to the left until now and max to the right until now

                ```cpp
                int trap(vector<int>& height) {
                        int n = height.size();
                        vector<int> highestr(n, height[n-1]), highestl(n, height[0]);
                        for(int i=0;i<n;i++){
                            if(i!=0)
                            highestl[i]=max(height[i], highestl[i-1]);
                            if(i!=0)
                            highestr[n-1-i]=max(height[n-1-i], highestr[n-1-i+1]);
                        }
                        int sum=0;
                        for(int i=0;i<n;i++){
                            int curHeight = min(highestl[i], highestr[i]);
                            if(curHeight>height[i]){
                                sum+=curHeight-height[i];
                            }
                        }
                        return sum;
                    }
                ```

            
            - O(1) space way:

                **Problem Statement:**

                Given an array `height` representing the height of buildings, where the width of each building is 1, compute the amount of rainwater that can be trapped between the buildings.

                **Example:**

                Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

                Output: 6

                **Solution:**

                In the rainwater trapping problem, for each cell, the container has two walls, left wall and right wall. The amount of water a cell can trap depends on the minimum height of the left wall and right wall, and also, of course, the current cell height.

                To find the O(1) space solution, we can realize that the values we need at each step can be computed on the fly using two-pointer technique.

                1. Initialize two pointers, left and right, where left = 0 and right = n-1, where n is the number of buildings.

                1. Initialize left_max = 0 and right_max = 0 for storing the maximum left wall and right wall height.

                1. While `left <= right`, perform the following operations:  
                    a. If height[left] is smaller than or equal to height[right]:  
                    i. Update left_max = max(left_max, height[left]).  
                    ii. Increase trapped water by left_max - height[left].  
                    iii. Increment left pointer.  
                    b. Else if height[left] is greater than height[right]:  
                    i. Update right_max = max(right_max, height[right]).  
                    ii. Increase trapped water by right_max - height[right].  
                    iii. Decrement right pointer.

                **Complexity Analysis:**

                1. Time Complexity: Since we are iterating through the array once using the two pointers, the time complexity is O(n), where n is the number of buildings.

                1. Space Complexity: We only use constant extra space for storing the pointers and max variables, hence the space complexity is O(1).

                **C++ Code:**

                ```cpp
                int trap(vector<int>& height) {
                    int left = 0, right = height.size() - 1;
                    int left_max = 0, right_max = 0;
                    int trapped_water = 0;

                    while (left <= right) {
                        if (height[left] <= height[right]) {
                            left_max = max(left_max, height[left]);
                            trapped_water += left_max - height[left];
                            left++;
                        } else {
                            right_max = max(right_max, height[right]);
                            trapped_water += right_max - height[right];
                            right--;
                        }
                    }
                    return trapped_water;
                }
                ```

                **Common Silly Mistakes:**

                1. Using the wrong pointer in the loop condition or when updating `trapped_water`, for example, using right instead of left, or vice versa.

                1. Initializing the left and right pointers to the wrong position.

                1. Forgetting to update the left_max or right_max values while looping the height array.

                **Related Problems:**

                1. Container With Most Water (LeetCode 11): In this problem, we have to find two lines that together with the x-axis forms a container that can contain the most water.

                1. Largest Rectangle in Histogram (LeetCode 84): In this problem, we have to find the largest rectangular area in the histogram, where the width is equal to 1 for each bar.

            

        - Sum of Subarray Minimums

            ## **Problem Statement:**

            Given an array `arr` of positive integers, find the sum of all minimum values of subarrays in the input array. The answer might be large, so return the answer modulo 10^9 + 7.

            ## **Example:**

            Input: arr = [3,1,2,4]

            Output: 17

            ## **Solution:**

            1. Inside the function, define two monotonic stacks "nse" and "pse" to store the indices of next smaller elements and previous smaller elements, respectively.

            1. Define two vectors "ns" and "ps" to store the index of the next smaller element and the previous smaller element for every element in "arr".

            1. The first loop iterates through "arr" to fill the "ps" vector:

                a. For each element "arr[i]", we iterate through all the elements to the left of it by popping any element from the stack "pse" that is greater than or equal to the current element.

                b. Once we exit the inner loop, if the "pse" stack is not empty, the top element will be the index of the previous smaller element for "arr[i]". Assign this value to "ps[i]".

                c. Push the current index "i" to the "pse" stack.

            
            1. The second loop iterates through "arr" in reverse to fill the "ns" vector:

                a. For each element "arr[i]", the inner loop pops any element from the stack "nse" that is not smaller than the current element.

                b. Once we exit the inner loop, if the "nse" stack is not empty, the top element will be the index of the next smaller element for "arr[i]". Assign this value to "ns[i]".

                c. Push the current index "i" to the "nse" stack.

            
            1. Initialize a variable "sum" to store the result and a constant "mod" with a value of 10^9 + 7.

            1. The final loop iterates through "arr" to calculate the sum of subarray minimums:

                a. With the help of "ns" and "ps" vectors, calculate the number of subarrays contributed by each element by multiplying the distances of the next smaller element and the previous smaller element from the current index.

                **b. Update the "sum" by adding the product of the subarray count and the current element, taking the modulo with "mod" to avoid overflow.**

            
            1. Return the final "sum" as the result.

            ## **Complexity Analysis:**

            1. Time Complexity: Since we push each element onto the stack exactly once and pop elements that are no longer valid only once, the time complexity is O(n), where n is the length of the input array.

            1. Space Complexity: In the worst case, we might need to store all elements on the stack, so the space complexity is also O(n).

            ## **C++ Code:**

            ```cpp
            class Solution {
            public:
                int sumSubarrayMins(vector<int>& arr) {
                    stack<int> nse, pse;
                    int n = arr.size();
                    vector<int> ns(n, n), ps(n, -1);

                    for(int i = 0; i < n; i++){
                        while(!pse.empty() && arr[i] <= arr[pse.top()])
                            pse.pop();
                        if(!pse.empty()){
                            ps[i] = pse.top();
                        }
                        pse.push(i);
                    }

                    for(int i = n - 1; i >= 0; i--){
                        while(!nse.empty() && arr[i] < arr[nse.top()])
                            nse.pop();
                        if(!nse.empty()){
                            ns[i] = nse.top();
                        }
                        nse.push(i);
                    }

                    long long sum = 0;
                    int mod = 1e9 + 7;
                    for(int i = 0; i < n; i++){
                        long long numSubarrays = (i - ps[i]) * (ns[i] - i);
                        sum = (sum + numSubarrays * arr[i] % mod) % mod;
                    }
                    return sum;
                }
            };
            ```

              

            **Note: You can merge the two loops for calculating nse and pse**

            ## **Common Silly Mistakes:**

            1. **For handling duplicate elements, you keep duplicate elements in one stack and not in the other stack. Otherwise you’ll incorrectly handle them.**

            1. Previous * Next = number of subarrays including that index

            1. Forgetting to calculate the modulo at each step, which might lead to integer overflow.

            ## **Related Problems:**

            1. Largest Rectangle in Histogram (LeetCode 84): In this problem, we have to find the largest rectangular area possible in a histogram.

            1. Longest Valid Parentheses (LeetCode 32): In this problem, we need to find the length of the longest valid (well-formed) parentheses substring, which can also be solved using a stack data structure.

        
        - Sum of Subarray Ranges

            Follow up question of previous. Just find all nse, pse, nge, pge and find greatest in subarray - min in subarray

            ```cpp
            class Solution {
            public:
                long long subArrayRanges(vector<int>& nums) {
                    int n = nums.size();
                    stack<int> nse, pse, nge, pge;
                    vector<int> ng(n, n), pg(n, -1), ns(n, n), ps(n, -1);
                    for(int i = 0; i < n; i++){
                        while(!pse.empty() && nums[i] <= nums[pse.top()])
                            pse.pop();
                        if(!pse.empty()){
                            ps[i] = pse.top();
                        }
                        pse.push(i);
                        while(!pge.empty() && nums[i] >= nums[pge.top()])
                            pge.pop();
                        if(!pge.empty()){
                            pg[i] = pge.top();
                        }
                        pge.push(i);
                    }

                    for(int i = n - 1; i >= 0; i--){
                        while(!nse.empty() && nums[i] < nums[nse.top()])
                            nse.pop();
                        if(!nse.empty()){
                            ns[i] = nse.top();
                        }
                        nse.push(i);
                        while(!nge.empty() && nums[i] > nums[nge.top()])
                            nge.pop();
                        if(!nge.empty()){
                            ng[i] = nge.top();
                        }
                        nge.push(i);
                    }

                    long long sum = 0;
                    for(int i=0;i<n;i++){
                        sum+=(long long)(i-pg[i])*(ng[i]-i)*(long long)nums[i]-(long long)(i-ps[i])*(long long)(ns[i]-i)*(long long)nums[i];
                    }
                    return sum;
                }
            };
            ```

        
        - Asteroid Collision

            Easy shit. Push positive and pop when encounter bigger negative. Beware of equals.

            ```cpp
            class Solution {
            public:
                vector<int> asteroidCollision(vector<int>& asteroids) {
                    stack<int> st;
                    vector<int> ans;
                    int n = asteroids.size();
                    for(int i=0;i<n;i++){
                        if(asteroids[i]>0){
                            st.push(asteroids[i]);
                        }
                        if(asteroids[i]<0){
                            while(!st.empty()&&abs(st.top())<abs(asteroids[i])){
                                st.pop();
                            }
                            if(!st.empty()&&st.top()==-asteroids[i]){
                                st.pop();
                                continue;
                            }
                            if(st.empty()){
                                ans.push_back(asteroids[i]);
                            }
                        }
                    }
                    int ind = ans.size();
                    while(!st.empty()){
                        ans.push_back(st.top());
                        st.pop();
                    }
                    reverse(ans.begin()+ind, ans.end());
                    return ans;
                }
            };
            ```

        
        - Remove k digits

            - Use a Stack: To efficiently keep track of the digits while removing k elements, we can use a stack data structure. The stack will store the digits in increasing order from the left. When encountering a digit smaller than the top of the stack, we can pop the top element from the stack and decrement k. This process continues until eith er k becomes 0 or the stack is empty.

            - Handle Edge Cases: Be sure to consider edge cases, such as when the number is already in its smallest form, or when k is equal to the length of the number. Additionally, make sure to handle leading zeros in the resulting number.

            ```cpp
            class Solution {
            public:
                string removeKdigits(string num, int k) {
                    stack<char> st;
                    string ans = "";
                    for(auto i: num){
                        while(!st.empty()&&st.top()>i&&k>0){
                            k--;
                            st.pop();
                        }
                        st.push(i);
                    }
                    bool flag=false;
                    while(k>0&&!st.empty()){
                        if(st.top()=='0') {st.pop();continue;}
                        st.pop();
                        k--;
                    }
                    while(!st.empty()) {ans.push_back(st.top()); st.pop();}
                    while(!ans.empty()&&ans.back()=='0') ans.pop_back();
                    if(ans.empty()) ans='0';
                    reverse(ans.begin(), ans.end());
                    return ans;
                }
            };
            ```

        
        - Sliding window maximum

            **Easy shit. Just use deque and keep it in decreasing order. So, element at front is the max. Pop front any index that lies out of window.**

            ```cpp
            class Solution {
            public:
                vector<int> maxSlidingWindow(vector<int>& nums, int k) {
                    deque<int> q;
                    int n = nums.size();
                    for(int i=0;i<k;i++){
                        while(!q.empty()&&nums[q.back()]<nums[i]){
                            q.pop_back();
                        }
                        q.push_back(i);
                    }
                    vector<int> ans;
                    ans.push_back(nums[q.front()]);
                    for(int i=k;i<n;i++){
                        if(q.front()<=i-k) q.pop_front();
                        while(!q.empty()&&nums[q.back()]<nums[i]){
                            q.pop_back();
                        }
                        q.push_back(i);
                        ans.push_back(nums[q.front()]);
                    }
                    return ans;
                }
            };
            ```

            This code aims to solve the famous problem called "Sliding Window Maximums". Given an array of integers and a sliding window size k, we need to find the maximum value in each window of size k, while the window moves over the array from left to right.

            We will now discuss the logic and functionality of the code along with the common mistakes and how to recognize that this problem uses a deque.

            1. Approach and Intuition:

            The most optimal approach to solve this problem is using a deque (double-ended queue). A deque is preferred because it allows us to perform insertions and deletions at both the beginning and the end in O(1) time complexity. Our goal is to maintain a decreasing order of the elements in the deque so that the front of the deque always contains an index of the maximum element in the window.

            1. Code Explanation:  
                JUST KEEP THE DEQUE IN DECREASING ORDER

            - Firstly, we initialize an empty deque `q`.

            - We iterate through the numbers in `nums` from the 0-th index to the (k-1)-th index, and for each number:

                - We remove all elements from the deque's back that are smaller than the current number at index `i` (nums[i]).

                - We push the index `i` to the back of the deque.

            
            - After the first k iterations, we have the first maximum number in the front of the deque. So, we push the first maximum number into the `ans` vector.

            - Next, we need to slide the window over the `nums` vector. We iterate through the numbers in `nums` from the k-th index to the `n-1` index, and for each number:

                - If the front of the deque (i.e., maximum of the last window) is out of range of the current window (i.e., less or equal to i - k), we pop it from the front.

                - We remove all elements from the deque's back that are smaller than the current number at index `i` (nums[i]).

                - We push the index `i` to the back of the deque.

                - We add the maximum of the current window (nums[q.front()]) to our `ans` vector.

            
            Finally, we return the `ans` vector as output.

            1. Identifying the problem uses a deque:

            The first clue to recognize that the "Sliding Window Maximums" problem might use a deque is the constraint of finding the maximum number in an interval or subarray. Additionally, deque allows O(1) insertion and deletion at the beginning and end, making it optimal for handling problems with sliding intervals. So if there is a problem where we need to maintain a certain ordering of elements within a sliding interval, think of a deque.

              

        
        - The celebrity problem

            Take out two candidates. If a knows b, push b, else push a. The last one remaining is the potential celebrity. Last me validate krlo ek baar.

            ```cpp
            class Solution 
            {
                public:
                //Function to find if there is a celebrity in the party or not.
                bool knows(int a, int b, vector<vector<int>>& M){
                    if(M[a][b]==1) return true;
                    return false;
                }
                int celebrity(vector<vector<int> >& M, int n) 
                {
                    // code here 
                    stack<int> st;
                    for(int i=0;i<n;i++){
                        st.push(i);
                    }
                    while(st.size()!=1){
                        int x=st.top();
                        st.pop();
                        int y=st.top();
                        st.pop();
                        if(knows(x, y, M)){
                            st.push(y);
                        }
                        else st.push(x);
                    }
                    int potential=st.top();
                    // just validating
                    for(int i=0;i<n;i++){
                        if(M[potential][i]==1) return -1;
                        if(i!=potential&&M[i][potential]==0) return -1;
                    }
                    return potential;
                }
            };
            ```

        
        - LRU cache

            Take a doubly linked list. Take a hashmap. Store the reference of the node in hashmap. The least recently used is on the beginning of linked list. The most recently used is on the tail of linked list. On getting a value, delete previous node, create new node on tail and update the hashmap for the key to the new node at tail.

        
        - LFU cache

            two maps → one containing the key, ref pairs. one containing the head and tail of linked list with the particular frequency.

            DLL for each frequency.

            Get → if present, delete prev frequency and add to freq+1.

            Put → if present, change value of key node and get. If not present, if capacity full, delete the lowest freq linked list head. Add new node to tail of freq=1.

        

    - Two pointers/Sliding window

        - Important note for sliding window:

            First learn this important concept of `at most` . This can be used for questions where you have to find `exactly` . For example, Number of subarrays with sum `exactly k`.

            Note that for number of subarrays/sub-strings, you can keep one end of the window at the current index for each index. Now the size of window becomes the number of subarrays with last element as the current index.

            - Note that for max size of sub-array/sub-strings and exactly equal, just replace ans = max(ans, r-l+1) and if(goal≥0) to if(goal==0). `Idk why this doesn't work in exactly k always. Why do we have to take atmost k - atmost k-1` → This is because here we need max size, we can make the window to be maximum. However, when we need number of subarrays, the two pointers don’t end up at each end of all subarrays. That is why we need “at most” shit.

                > [!info] Longest K unique characters substring | Practice | GeeksforGeeks  
                > Given a string you need to print the size of the longest possible substring that has exactly K&nbsp;unique characters.  
                > [https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-k-unique-characters-substring](https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-k-unique-characters-substring)  

                ```cpp
                class Solution{
                  public:
                    int longestKSubstr(string s, int k) {
                    // your code here
                    long long int l=0, n=s.length(), ans=0;
                        vector<int> hash(26, 0);
                        if(k<0) return -1;
                        for(int r=0;r<n;r++){
                            if(hash[s[r]-'a']==0)
                                k--;
                            hash[s[r]-'a']++;
                            while(k<0){
                                hash[s[l]-'a']--;
                                if(hash[s[l]-'a']==0) k++;
                                l++;
                            }
                            if(k==0)
                            ans=max(ans, r-l+1);
                        }
                        if(ans==0) return -1;
                        return ans;
                    }
                };
                ```

            
            ## NOTE: ALL THIS DOESN’T WORK WHEN WE INCLUDE NEGATIVE AND ZEROES.

            ```cpp
            class Solution {
                int atMost(vector<int>& nums, int goal){
                    int ans=0,l=0,n=nums.size();
                    if(goal<0) return 0;
                    for(int r=0;r<n;r++){
                        goal-=nums[r];
                        while(goal<0){
                            goal+=nums[l];
                            l++;
                        }
            						if(goal>=0)
                        ans+=r-l+1;
                    }
                    return ans;
                }
            public:
                int numSubarraysWithSum(vector<int>& nums, int goal) {
                    return atMost(nums, goal)-atMost(nums, goal-1);
                }
            };
            ```

        
        - Another question like in the note:

            count all possible sub-strings that have exactly k distinct characters.

            ```cpp
            class Solution
            {
                long long int AtMost(string &s, int k){
                    long long int l=0, n=s.length(), ans=0;
                    vector<int> hash(26, 0);
                    if(k<0) return 0;
                    for(int r=0;r<n;r++){
                        if(hash[s[r]-'a']==0)
                            k--;
                        hash[s[r]-'a']++;
                        while(k<0){
                            hash[s[l]-'a']--;
                            if(hash[s[l]-'a']==0) k++;
                            l++;
                        }
                        if(k>=0)
                        ans+=r-l+1;
                    }
                    return ans;
                }
              public:
                long long int substrCount (string s, int k) {
                	//code here.
                	return AtMost(s, k)-AtMost(s, k-1);
                }
            };
            ```

        
        - Longest Sub-string Without Repeating Characters

            1. Approach 1 O(2n) time:

                ```cpp
                class Solution {
                public:
                    int lengthOfLongestSubstring(string s) {
                        vector<int> vec(255, 0);   
                        int maxi = 0;
                        int l=0, r=0;
                        if(s=="") return 0;
                        while(r<s.length()){
                            int num = s[r];
                            if(vec[num]==0){
                                vec[num]++;
                            }
                            else if(vec[num]==1){     // when the char is already marked 1
                                maxi = max(maxi, r-l); 
                                while(s[l]!=num){     // mark all the chars from first occurence to second occurence as 0 and update the second occurence to 1
                                    vec[s[l]]=0;
                                    l++;
                                }
                                l++;
                            }
                            r++;
                        }
                        maxi = max(maxi, r-l);
                        return maxi;
                    }
                };
                ```

            
            1. Approach 2 O(n) time:

                ```cpp
                class Solution {
                public:
                    int lengthOfLongestSubstring(string s) {
                        vector<int> vec(255, -1);   // store the index at which the char was last encountered
                        int maxi = 0;
                        int l=0, r=0;
                        if(s=="") return 0;
                        while(r<s.length()){
                            int num = (int)(s[r]);
                            if(vec[num]<l){          // if the encountered char was last encountered at someplace before our window
                                vec[num]=r;          // update the vector to current index
                            }
                            else if(vec[num]>=l){
                                maxi = max(maxi, r-l);
                                l=vec[num]+1;        // just update the l to after the first encounter
                                vec[num]=r;          // don't forget to mark the current index in the vector
                            }
                            r++;
                        }
                        maxi = max(maxi, r-l);
                        return maxi;
                    }
                };
                ```

            

        - Minimum Window Substring

            Use two hashmaps. One is for target and one is for current. Run the loop until r becomes equal to s length. Every iteration, add s[r] to current and check the whole cur with target O(52) ~ O(1). If it is ≥ target, then it might be an answer. Increase L until any cur becomes smaller than r and then repeat the whole loop. O(n+m)

            ```jsx
            class Solution {
            public:
                string minWindow(string s, string t) {
                    unordered_map<char, int> target;
                    unordered_map<char, int> cur;
                    for(auto i:  t){
                        target[i]++;
                    }

                    int l=0, r=0, la=-1, ra=1e7;
                    while(r<s.length()){
                        int flag=true;
                        cur[s[r]]++;
                        r++;
                        for(auto i: target){
                            if(cur.find(i.first)==cur.end()||cur[i.first]<target[i.first]){
                                flag=false;
                                break;
                            }
                        }
                        if(flag){
                            if(r-l<ra-la){
                                ra=r;
                                la=l;
                            }
                            while(flag&&l<=r){
                                cur[s[l]]--;
                                if(cur[s[l]]<target[s[l]]){
                                    flag=false;
                                    l++;
                                    break;
                                }
                                l++;
                                if(r-l<ra-la){
                                    ra=r;
                                    la=l;
                                }
                            }
                        }
                    }
                    string ans="";
                    if(la==-1) return ans;
                    for(int i=la;i<ra;i++){
                        ans.push_back(s[i]);
                    }
                    return ans;
                }
            };
            ```

        
        - Minimum Window Subsequence

            Every window, if subsequence, decrease window by increasing L and if not subsequence, R increase. O(n^2)

            ```cpp
            bool isSubsequence(string &s, string& t, int l, int r){
            	int inds=l, n=r, indt=0, m=t.length();
            	while(inds<n){
            		if(s[inds]==t[indt]){
            			indt++;
            		}
            		if(indt>=m) return true;
            		inds++;
            	}
            	return false;
            }
            string minWindow(string s, string t)
            {
            	// Write your Code here

            	int l=0, r=0, la=-1, ra=1e7;
            	while(r<s.length()){
            		int flag=true;
            		r++;
            		if(!isSubsequence(s,t, l, r)) flag=false;
            		if(flag){
            			if(r-l<ra-la){
            				ra=r;
            				la=l;
            			}
            			while(flag&&l<=r){
            				l++;
            				if(!isSubsequence(s,t, l, r)){
            					flag=false;
            					break;
            				}
            				if(r-l<ra-la){
            					ra=r;
            					la=l;
            				}
            			}
            		}
            	}
            	string ans="";
            	if(la==-1) return ans;
            	for(int i=la;i<ra;i++){
            		ans.push_back(s[i]);
            	}
            	return ans;
            }
            ```

        

    - Bit Manipulation

        Finding the rightmost set bit

        x=n & ~(n-1)

        Note this is not the number of bit but the whole 2^number of bits.

        - **Set the rightmost unset bit**

            My unoptimized code:

            ```cpp
            int cnt = 0, num=N;
                    while(num>0){
                        if((num&1)==0){
                            break;
                        }
                        num=num>>1;
                        cnt++;
                    }
                    if((1<<cnt)>N) return N;
                    return N|(1<<cnt);
            ```

            Optimized code:

            ```cpp
            int setBit(int N)
                {
                    if(N & N+1){      //checks if N is not 1/3/7/15/31...
                        return N|N+1; // important note
                    }else{
                       return  N;
                    }
                }
            ```

        
        - **Number of bits to flip to convert from 1 number to another**

            Mine:

            ```cpp
            class Solution {
            public:
                int minBitFlips(int start, int goal) {
                    if(start>goal) swap(start, goal);
                    int cnt=0;
                    while(goal>0){
                        if((goal&1)!=(start&1)) cnt++;
                        goal=goal>>1;
                        start=start>>1;
                    }
                    return cnt;
                }
            };
            ```

            Optimized:

            ```cpp
            class Solution {
            public:
                int minBitFlips(int start, int goal) {
                    return __builtin_popcount(start^goal);
                }
            };
            ```

        
        - **Check out power set Iterative/recursive**

        - **XOR up to some x**

            0, 1, 2, 3 xor = 0

            4, 5, 6, 7 xor = 0

            and goes on

            Therefore xor of numbers up to n

            ```cpp
            if(x%4==0){
                  return x;  // xor upto x
              }
              if(x%4==1){
                  return 1;  // xor upto x
              }
              if(x%4==2){
                  return x+1;  // xor upto x
              }
              if(x%4==3){
                  return 0;  // xor upto x
              }
            ```

        
        - Divide two numbers without using mod, multiplication or division operators

            Since we don’t know the quotient and remainder the equation we know is:

            `58 = (q) * 5 + rem`

            We get a hint at what we would like to do here. We will first  
            multiply 5 with maximum power of 2 such that the resulting number is  
            still smaller than the dividend (read further if you don't understand  
            why). Since multiplication operator is not allowed, we would use bit-wise  
            left shift to achieve this multiplication: each time we shift 5 by 1,  
            we multiply it by 2:

            ```
            	5 << 0 = 5               // less than dividend
            	5 << 1 = 5*2 = 10        // less than dividend
            	5 << 2 = 5*2*2 = 20      // less than dividend
            	5 << 3 = 5*2*2*2 = 40    // less than dividend
            	5 << 4 = 5*2*2*2*2 = 80  // (stop and consider the previous value as the result is greater than dividend
            ```

            We observe that:

            `58 = (2^3 * 5) + (something * 5) + rem // --- (III)`

            Since 5 is multiplied with 2^3, _**we add 2^3 to our answer**_.

            Further operating on equation III:

            `58 - (2^3 * 5) = (something * 5) + rem 58 - (8 * 5) = something * 5 + rem 58 - 40 = something * 5 + rem 18 = something * 5 + rem`

            ```cpp
            class Solution {
            public:
                int findMaxPow2(int dividend, int divisor){
                    int n=0;
                    while((divisor<<(n+1))<=dividend){
                        n++;
                    }
                    return n;
                }
                int divide(int dividend, int divisor) {
                    int ans=0, sign=1;
                    if((dividend<0&&divisor<0)||dividend>0&&divisor>0||dividend==0){
                        sign=1;
                    }
                    else sign=-1;
                    dividend=abs(dividend);
                    divisor=abs(divisor);
                    while(dividend>=0){
                        int cur2 = findMaxPow2(dividend, divisor);
                        if(dividend<(divisor<<cur2)) break;
                        ans+=1<<cur2;
                        dividend-=divisor<<cur2;
                    }
                    return ans*sign;
                }
            };
            ```

        
        - Find two numbers with Odd occurrence

            Find axorb. The rightmostsetbit in axorb would be the bit where a and b differ. So, divide the array into two parts, one with rightmostsetbit set and one with rightmostsetbit unset. Now xor through the parts one by one. First xor would have one number and other xor would have another number.

            ```cpp
            class Solution{
                public:
                vector<long long int> twoOddNum(long long int Arr[], long long int N)  
                {
                    // code here
                    long long int axorb=0;
                    int n=N;
                    for(int i=0;i<n;i++){
                        axorb=axorb^Arr[i];
                    }
                    long long int a=0,b=0, rightmostsetbit=axorb & ~(axorb-1); // !!
                    for(int i=0;i<n;i++){
                        if((Arr[i]&rightmostsetbit)==rightmostsetbit){ // !!!
                            a=(a^Arr[i]);
                        }
                        else{
                            b=(b^Arr[i]);
                        }
                    }
                    if(a<b)swap(a,b);
                    return {a,b};
                }
            };
            ```

        
        - Count total set bits in all numbers from 1 to n

            **find highest power of 2 less than equal to 11 which is 8=2^3 .Now you can observe that from 0-7 all numbers have last binary bit as (0,1,0,1,0,1,0,1) having 8/2=4 set bits similarly observe second last bit of 0-7 (0,0,1,1,0,0,1,1) →8/2=4 set bits similarly last third (0,0,0,0,1,1,1,1)=8/2=4;**

            **so combining all we get 3*(8/2) set bits. If we consider 3=x then generalizing above  expression we get ans= x*(2^(x-1)**

            **Now from 8-11 all numbers have first bit from left as 1 so adding (11-8+1) or (n-(2^x)+1) in ans. In the remaining part we recursively call the same function for (11-8) or (n-(2^x))**

            ```cpp
            int countSetBits(int n)
                {
                    // Your logic here
                    if(n<=1) return n;
                    int x=log2(n);
                    return ((1<<(x-1)))*x+(n-(1<<x)+1)+countSetBits(n-(1<<x));
                }
            ```

        

    - Grids:

        If you are allowed to go **backwards,** you can’t use dp. For example [https://leetcode.com/problems/shortest-path-in-binary-matrix/description/](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/), here you can go backwards too. So no dp, only bfs/djikstra

    
    - Dynamic Programming

        - DP on subsequences

            - Partition into two subsets such that their differences is minimized

                Find total sum of array

                for every cursum=0 to cursum=totalsum, check if cursum can be made. If it could be made, find ans = min(ans, abs(cursum-(totalsum-cursum)))

                Note that this will be only O(totalsum*n) even though we check if the subset can be made for every 0→totalsum, because dp is of totalsum*n and every time, it doesn’t go about calculating everything.

            
            - number of partitions with given difference

                SumA + SumB = totalSum - (1)

                SumB - SumA = k - (2)

                from (1) & (2)

                derive

            

        - DP on strings

            First two things to try - relate to lcs OR use dp on subsequence

            - Longest Common Subsequence

                ```cpp
                class Solution {
                public:
                    int longestCommonSubsequence(string text1, string text2) {
                        int n=text1.length(), m=text2.length();
                        vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
                        for(int i=1;i<=n;i++){
                            for(int j=1;j<=m;j++){
                                if(text1[i-1]==text2[j-1]){
                                    dp[i][j]=1+dp[i-1][j-1];
                                }
                                else{
                                    int shift1=dp[i-1][j];
                                    int shift2=dp[i][j-1];
                                    dp[i][j]=0+max(shift1, shift2);
                                }
                            }
                        }
                        return dp[n][m];
                    }
                };
                ```

            
            - Printing the LCS

                ```cpp
                string st="";
                int i=n, j=m;
                while(j>0&&i>0){
                    if(dp[i][j]==dp[i-1][j]){
                        i--;
                    }
                    else if(dp[i][j]==dp[i][j-1]){
                        j--;
                    }
                    else{              // note that equal case should be at last!!
                        st.push_back(s[i-1]);
                        i--;j--;
                    }
                }
                reverse(st.begin(), st.end());
                ```

            
            - Longest common substring

                Remember to take ans while computing loop too otherwise the answer might get lost before you reach the end.

                ```cpp
                int findLength(vector<int>& nums1, vector<int>& nums2) {
                    int n=nums1.size(), m=nums2.size(), ans=0;
                    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
                    for(int i=1;i<=n;i++){
                        for(int j=1;j<=m;j++){
                            if(nums1[i-1]==nums2[j-1]){
                                dp[i][j]=1+dp[i-1][j-1];
                                ans=max(ans, dp[i][j]); // NOTE
                            }
                            else  dp[i][j]=0;   
                        }
                    }
                    return ans;
                }
                ```

            
            - Shortest common supersequence

                Length of scs: n+m-lcs

                printing the scs: (similar to printing lcs)

                ```cpp
                class Solution {
                public:
                    string shortestCommonSupersequence(string str1, string str2) {
                        int n=str1.length(), m=str2.length();
                        vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
                        for(int i=1;i<=n;i++){
                            for(int j=1;j<=m;j++){
                                if(str1[i-1]==str2[j-1]){
                                    dp[i][j]=1+dp[i-1][j-1];
                                }
                                else{
                                    dp[i][j]=max(dp[i-1][j], dp[i][j-1]);
                                }
                            }
                        }
                        int i=n, j=m;
                        string ans="";
                        while(i>0&&j>0){

                            if(dp[i][j]==dp[i-1][j]){
                                ans.push_back(str1[i-1]);  // Change here
                                i--;
                            }
                            else if(dp[i][j]==dp[i][j-1]){
                                ans.push_back(str2[j-1]);  // Change here
                                j--;
                            }
                            else{
                                ans.push_back(str1[i-1]);
                                i--;
                                j--;
                            }
                        }
                        while(i>0){                 // Change here
                            ans.push_back(str1[i-1]);
                            i--;
                        }
                        while(j>0){                 // Change here
                            ans.push_back(str2[j-1]);
                            j--;
                        }
                        reverse(ans.begin(), ans.end());
                        return ans;
                    }
                };
                ```

            
            - Count distinct subsequence

                every index → 2 options pick/notpick

                subtract number of subsequence ending with the letter.

                ```cpp
                class Solution {
                public:
                    int distinctSubseqII(string s) {
                        vector<int> dp(s.length()+1, 0);
                        int M=1e9+7;
                        vector<int> endC(26, 0);
                        dp[0]=1;
                        for(int i=1;i<=s.length();i++){

                            dp[i]= ( 2 * dp[i-1] ) - endC[s[i-1]-'a'];

                            endC[s[i-1]-'a']=dp[i-1];
                        }
                        return dp[s.length()]-1;
                    }
                };
                ```

            

        - DP on Stocks

            - When buy and sell only once → ez greedy

                ```cpp
                int maxProfit(vector<int>& prices) {
                    int ans=0, curMin=prices[0];
                    for(int i=0;i<prices.size();i++){
                        curMin=min(curMin, prices[i]);
                        ans=max(ans, prices[i]-curMin);
                    }
                    return ans;
                }
                ```

            
            - When buy and sell 2 → ez dp OR ez greedy

                ```cpp
                int recur(vector<int>& prices, int ind, int hold, vector<vector<int>>& dp, int n){
                        if(ind==n) return 0;
                        if(dp[ind][hold]!=-1) return dp[ind][hold];
                        int sell=0, buy=0;
                        if(hold==1)
                        sell=prices[ind]+recur(prices, ind+1, 0, dp, n);
                        int doNothing=recur(prices, ind+1, hold, dp, n);
                        if(hold==0)
                        buy=-prices[ind]+recur(prices, ind+1, 1, dp, n);
                        return dp[ind][hold] = max({sell, doNothing, buy});
                    }
                    int maxProfit(vector<int>& prices) {
                        int n=prices.size();
                        // vector<vector<int>> dp(n+1, vector<int>(2, -1));
                        // return recur(prices, 0, 0, dp, n);
                        int maxprofit=0;
                        for(int i=1;i<n;i++){
                            if(prices[i-1]<prices[i]){
                                maxprofit+=prices[i]-prices[i-1];
                            }
                        }
                        return maxprofit;
                    }
                ```

            
            - When buy and sell only k times → ez dp

                Take a variable initialized at 2*k

                for eg, k=2

                transactionID = 4 → can buy (bought 0 times sold 0 times)

                transactionID = 3 → can sell (bought 1 times sold 0 times)

                transactionID = 2 → can buy (bought 1 times sold 1 times)

                transactionID = 1 → can sell (bought 2 times sold 1 times)

                transactionID = 0 → can’t do anything (bought 2 times sold 2 times)

                ```cpp
                class Solution {
                    // even -> can buy
                    // odd  -> can sell
                public:
                    int recur(vector<int>& prices, vector<vector<int>>& dp, int ind, int event, int n){
                        if(ind==n) return 0;
                        if(event==0) return 0;
                        if(dp[ind][event]!=-1) return dp[ind][event];
                        int sell=0, buy=0, hold=0;
                        if(event%2==1){
                            sell=prices[ind]+recur(prices, dp, ind+1, event-1, n);
                        }
                        if(event%2==0){
                            buy=-prices[ind]+recur(prices, dp, ind+1, event-1, n);
                        }
                        hold=recur(prices, dp, ind+1, event, n);
                        return dp[ind][event] = max({buy, sell, hold});
                    }
                    int maxProfit(int k, vector<int>& prices) {
                        int n=prices.size();
                        // vector<vector<int>> dp(n+1, vector<int>(2*k+1, -1));
                        // return recur(prices, dp, 0, 2*k, n);
                        vector<vector<int>> dp(n+1, vector<int>(2*k+1, 0));
                        for(int i=n-1;i>=0;i--){
                            for(int event=1;event<=2*k;event++){
                                int sell=0, buy=0, hold=0;
                                if(event%2==1){
                                    sell=prices[i]+dp[i+1][event-1];
                                }
                                if(event%2==0){
                                    buy=-prices[i]+dp[i+1][event-1];
                                }
                                hold=dp[i+1][event];
                                dp[i][event] = max({buy, sell, hold});
                            }
                        }
                        return dp[0][2*k];
                    }
                };
                ```

            

        - DP on LIS

            - Basics

                1. Recursion and tabulation basic → simple pick not pick

                    - Code

                        ```cpp
                        int getAns(int arr[], int n,  int ind, int prev_index, vector<vector<int>>& dp){

                            // base condition
                            if(ind == n)
                                return 0;

                            if(dp[ind][prev_index+1]!=-1)
                                return dp[ind][prev_index+1];

                            int notTake = 0 + getAns(arr,n,ind+1,prev_index,dp);

                            int take = 0;

                            if(prev_index == -1 || arr[ind] > arr[prev_index]){
                                take = 1 + getAns(arr,n,ind+1,ind,dp);
                            }

                            return dp[ind][prev_index+1] = max(notTake,take);
                        }

                        
                        int longestIncreasingSubsequence(int arr[], int n){

                            vector<vector<int>> dp(n,vector<int>(n+1,-1));

                            return getAns(arr,n,0,-1,dp);
                        }
                        ```

                    

                1. Optimized O(n^2) time and O(n) space (Used the most in other questions and for printing the LIS)

                    - Details and code

                        Using hash array (watch video maybe)

                        for printing, we use the prev array

                        ```cpp
                        int lengthOfLIS(vector<int>& nums) {
                            int n=nums.size(), maxi=1;
                            vector<int> dp(n, 1);
                            // int ind=0;                      // for printing lis
                            // vector<int> hash(n);
                            // for(int i=0;i<n;i++){
                            //     hash[i]=i;
                            // }
                            for(int i=1;i<n;i++){
                                for(int j=0;j<i;j++){
                                    if(nums[i]>nums[j]){
                                        if(dp[i]<1+dp[j]){
                                            dp[i]=1+dp[j];
                                            // hash[i]=j;       // for printing lis
                                        }
                                    }
                                    if(maxi<dp[i]){
                                        maxi=dp[i];
                                        // ind=i;               // for printing lis
                                    }
                                }
                            }
                            // vector<int> lis;                  // for printing lis
                            // while(hash[ind]!=ind){
                            //     lis.push_back(nums[ind]);
                            //     ind=hash[ind];
                            // }
                            // lis.push_back(nums[ind]);
                            // reverse(lis.begin(), lis.end());
                            // for(auto i: lis){
                            //     cout<<i<<' ';
                            // }
                            return maxi;
                        }
                        ```

                          

                    

                1. Using binary search O(nlogn) time and O(n) space → See video

                    - Code

                        ```cpp
                        // Using binary search
                        int lengthOfLIS(vector<int>& nums){
                            vector<int> cur;
                            int n=nums.size();
                            for(int i=0;i<n;i++){
                                if(cur.empty()) cur.push_back(nums[i]);
                                else{
                                    auto it=lower_bound(cur.begin(), cur.end(), nums[i]);
                                    if(it==cur.end()) cur.push_back(nums[i]);
                                    else cur[it-cur.begin()]=nums[i];
                                }
                            }
                            return cur.size();
                        }
                        ```

                    

            
            - Longest divisible subset and longest word chain

                Same as 2nd LIS method. Minor changes

                Longest word chain:

                ```cpp
                bool checker(string& s1, string& s2){
                        int flag=1;
                        if(s1.length()+1!=s2.length()) return false;
                        cout<<s1<<' '<<s2<<'|';
                        int i1=0, i2=0;
                        while(i2<s2.length()){
                            if(s1[i1]!=s2[i2]){
                                flag--;
                                i2++;
                            }
                            else{
                                i1++;
                                i2++;
                            }
                            if(flag<0) return false;
                        }
                        return true;

                    }
                    static bool comp(string& a, string& b) {
                        return a.length()<b.length();
                    }
                    int longestStrChain(vector<string>& words) {
                        int maxi=1, n=words.size();
                        sort(words.begin(), words.end(), comp);
                        vector<int> dp(n, 1);
                        for(int i=0;i<n;i++){
                            for(int j=0;j<i;j++){
                                if(checker(words[j], words[i])) dp[i]=max(dp[i], 1+dp[j]);
                                maxi=max(maxi, dp[i]);
                            }
                        }
                        return maxi;
                    }
                ```

            
            - Longest Bitonic Subsequence

                Bitonic → Increasing then decreasing

                ~ Max of LIS from start and LIS from end for each index

                If strictly increasing/strictly decreasing not given then just take `nums[i]>=nums[j]` for dp and `nums[i]>nums[j]` for the dp reverse.

                ```cpp
                int LongestBitonicSequence(vector<int>nums)
                {
                    // code here
                      int n=nums.size(), maxi=0;
                    vector<int> dp(n, 1), dpreverse(n, 1);
                    for(int i=1;i<n;i++){
                          for(int j=0;j<i;j++){
                              if(nums[i]>nums[j]){
                                  dp[i]=max(dp[i], 1+dp[j]);
                              }
                          }
                      }
                      for(int i=n-1;i>=0;i--){
                          for(int j=n-1;j>i;j--){
                              if(nums[i]>nums[j]){
                                  dpreverse[i]=max(dpreverse[i], 1+dpreverse[j]);
                              }
                          }
                      }
                      for(int i=0;i<n;i++){
                          maxi=max(maxi, dp[i]+dpreverse[i]-1);
                      }
                      return maxi;
                }
                ```

            

        - Partition

            - Egg drop problem.

                Use binary search dp

                ```jsx
                int recur(int eggs, int floors, vector<vector<int>> &dp){
                    int l=1, r=floors, mini=INT_MAX;
                    if(eggs==1) return floors;
                    if(floors<=1) return floors;
                    if(dp[floors][eggs]!=-1) return dp[floors][eggs];
                    while(l<=r){
                        int mid=(l+r)/2;
                        int breaks=recur(eggs-1, mid-1, dp);
                        int notBreak=recur(eggs, floors-mid, dp);
                        if(breaks>=notBreak){
                            r=mid-1;
                        }
                        else l=mid+1;
                        mini=min(mini, 1+max(breaks, notBreak));
                    }
                    return dp[floors][eggs] = mini;
                }
                int Solution::solve(int eggs, int floors) {
                    vector<vector<int>> dp(floors+1, vector<int>(eggs+1, -1));
                    return recur(eggs, floors, dp);
                }
                ```

            

    
    - Graphs

        - Djikstra sorted with stops rather than distance

            ```jsx
            // priority queue not needed because inserted in increasing order of stops 1, 2, 3...
            // But remember that priority is number of stops and not distance
            ```

            Kind of like BFS. Stop if level>k.

            ```cpp
            int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
                    queue<pair<int, pair<int, int>>> st;
                    st.push({0, {0, src}});
                    vector<int> dist(n, 1e8);
                    dist[src]=0;
                    vector<vector<pair<int,int>>> adj(n);
                    for(auto i: flights){
                        adj[i[0]].push_back({i[1], i[2]});
                    }

                    while(!st.empty()){
                        int v=st.front().second.second;
                        int curdis=st.front().second.first;
                        int stops=st.front().first;
                        st.pop();
                        if(stops>k) continue;
                        for(auto i: adj[v]){
                            if(dist[i.first]>curdis+i.second){
                                dist[i.first]=curdis+i.second;
                                st.push({stops+1, {dist[i.first], i.first}});
                            }
                        }
                    }
                    return dist[dst] == 1e8 ? -1 : dist[dst];
                }
            ```

              

        
        - Useful extra edges

            Here you have to find the min distance from source to destination. You are also given a set of extra edges. You can choose at max one extra edge.

            Run a dijkstra from src once and store the distance of every node from src. Run another dijkstra from dest and store the distance of every node from dest. Now iterate over each extra edge and check if it reduces the minimum distance from src to dest using the two nodes of the edge(they have to be connected)

            ```cpp
            int Solution::solve(int n, vector<vector<int> > &edges, int src, int dest, vector<vector<int> > &extra) {
                vector<int> dis(n+1, INT_MAX);
                dis[src]=0;
                vector<vector<int>> adj[n+1];
                for(auto i: edges){
                    adj[i[0]].push_back({i[1], i[2]});
                    adj[i[1]].push_back({i[0], i[2]});
                }
                int mini=INT_MAX;
                vector<int> distsrc(n+1, 1e9); 
                vector<int> distdest(n+1, 1e9); 
                set<pair<int,int>> st; 

                st.insert({0, src}); 
                distsrc[src] = 0;

                while(!st.empty()) {
                    auto it = *(st.begin()); 
                    int node = it.second; 
                    int dis = it.first; 
                    st.erase(it); 

                    for(auto it : adj[node]) {
                        int adjNode = it[0]; 
                        int edgW = it[1]; 

                        if(dis + edgW < distsrc[adjNode]) {
                            if(distsrc[adjNode] != 1e9) 
                                st.erase({distsrc[adjNode], adjNode}); 
                            distsrc[adjNode] = dis + edgW; 
                            st.insert({distsrc[adjNode], adjNode}); 
                            }
                    }
                }
                mini=min(mini, distsrc[dest]);
                st.clear();
                distdest[dest]=0;
                st.insert({0, dest}); 

                while(!st.empty()) {
                    auto it = *(st.begin()); 
                    int node = it.second; 
                    int dis = it.first; 
                    st.erase(it); 

                    for(auto it : adj[node]) {
                        int adjNode = it[0]; 
                        int edgW = it[1]; 

                        if(dis + edgW < distdest[adjNode]) {
                            if(distdest[adjNode] != 1e9) 
                                st.erase({distdest[adjNode], adjNode}); 
                            distdest[adjNode] = dis + edgW; 
                            st.insert({distdest[adjNode], adjNode}); 
                            }
                    }
                }

                for(auto i: extra){
                    int u=i[0];
                    int v=i[1];
                    int w=i[2];
                    if(distsrc[u]!=1e9&&distdest[v]!=1e9&&mini>distdest[u]+distsrc[v]+w){
                        mini=distdest[u]+distsrc[v]+w;
                    }
                    if(distsrc[u]!=1e9&&distdest[v]!=1e9&&mini>distdest[v]+distsrc[u]+w){
                        mini=distdest[v]+distsrc[u]+w;
                    }
                }
                return mini==1e9?-1:mini;
            }
            ```

        
        - You always confuse how to keep track of visited in bfs

        - Cycle detection in undirected graph

            You keep track of a parent variable and a visited array. If the element visited is not parent, then cycle.

        
        - Cycle detection in directed graph

            - Using path visited

                The previous method won’t work. You need to use a pathVisited array too. While going into a dfs, mark the pathvis and while coming out, unmark it. If pathVis found true on another element, cycle present. You can combine the pathVis array and vis array by using vis[i]=1 for visited and vis[i]=2 for pathvis.

                  

                Note that this shouldn’t be used for finding all cycles/longest cycles/visiting all nodes. This method doesn’t work like normal dfs.

            
            - Using toposort

                If the size of toposort isn’t equal to number of nodes, then the graph has a cycle. (It should have size less than the number of nodes if it has a cycle)

                Note that this doesn’t work with dfs toposort as it pushes even if there’s a cycle so everytime the number of total nodes is equal to nodes in toposort.

            

        - Toposort (Used in course schedule and undirected cycle detection)

            - Using DFS (Don’t use this for cycle detection/course schedule, see cycle detection toposort note)

                Just push into a vector before ending the dfs call, at the end, reverse the vector

                ```cpp
                void dfs(vector<int> adj[], int n, int v, vector<int>& toposort, vector<int>& vis){
                        if(vis[v]) return;
                        vis[v]=1;
                        for(auto i: adj[v]){
                            dfs(adj, n, i, toposort, vis);
                        }
                        toposort.push_back(v);
                    }

                	vector<int> topoSort(int V, vector<int> adj[])
                	{
                	    // code here
                	    vector<int> vis(V, 0), toposort;
                	    for(int i=0;i<V;i++){
                	        if(!vis[i]) dfs(adj, V, i, toposort, vis);
                	    }

                	    reverse(toposort.begin(), toposort.end());
                	    return toposort;
                	}
                ```

            
            - Using BFS(Kahn’s algo) (No need for any visited array)

                Use the indegree. Push all indegree 0 into the queue for bfs. Now, inside bfs, everytime reduce the indegree in the for loop. If indegree becomes 0, push into the queue.

                ```cpp
                vector<int> topoSort(int V, vector<int> adj[]) 
                	{
                	    // code here
                	    vector<int> toposort, indegree(V, 0);
                	   int n=V;
                	   for(int i=0;i<n;i++){
                	       for(auto j: adj[i]){
                	           indegree[j]++;
                	       }
                	   }
                	   queue<int> q;
                	   for(int i=0;i<n;i++){
                	       if(indegree[i]==0) q.push(i);
                	   }
                	   while(!q.empty()){
                	       int v=q.front();
                	       toposort.push_back(v);
                	       q.pop();
                	       for(auto i: adj[v]){
                	           indegree[i]--;
                	           if(indegree[i]==0){
                                    q.push(i);	               
                	           }
                	       }
                	   }
                	   return toposort;
                	}
                ```

            

        - Djikstra

            ```cpp
            vector <int> dijkstra(int V, vector<vector<int>> adj[], int S)
                {
                    // Code here
                    multiset<pair<int, int>> st;
                    st.insert({0, S});
                    vector<int> dis(V, INT_MAX);
                    dis[S]=0;
                    while(!st.empty()){
                        int curv=st.begin()->second;
                        int curdis=st.begin()->first;
                        st.erase(st.begin());
                        for(auto i: adj[curv]){
                            if(dis[i[0]]>curdis+i[1]){
                                dis[i[0]]=curdis+i[1];
                                st.insert({dis[i[0]], i[0]});
                            }
                        }
                    }
                    return dis;
                }
            ```

        
        - path with minimum effort

            Grid with cost as min absolute distance on path → djikstra

        
        - Shortest path in matrix questions

            If somehow, you can limit movement such that you can’t go in opposing directions like up _and_ down or left _and_ right. Then you can use DP.

            For eg, [https://leetcode.com/problems/minimum-path-sum/](https://leetcode.com/problems/minimum-path-sum/)

            But if you have to go all ways, you should use bfs or djikstra

            For eg, [https://leetcode.com/problems/shortest-path-in-binary-matrix/](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

              

        
        - Number of shortest path.

            While using djikstra, keep another vector for ways. Initialize ways[src]=1. Everytime you encounter a shorter path, set ways[j] to number of ways of previous node. Otherwise if you encounter an equal path, increment ways[j] by the number of ways of the previous node.

            For eg, Count number of shortest path to reach n-1th node

            ```cpp
            int countPaths(int n, vector<vector<int>>& roads) {
                    vector<pair<int, int>> adj[n];
                    long long int M=1e9+7;
                    for(auto i: roads){
                        adj[i[0]].push_back({i[1], i[2]});
                        adj[i[1]].push_back({i[0], i[2]});
                    }
                    multiset<pair<long long, long long>> st;
                    vector<long long> dist(n, -1), ways(n, 0);
                    ways[0]=1;
                    dist[0]=0;
                    st.insert({0, 0});
                    while(!st.empty()){
                        long long curdis=st.begin()->first;
                        long long v=st.begin()->second;
                        st.erase(st.begin());
                        for(auto i: adj[v]){
                            if(dist[i.first]>curdis+i.second||dist[i.first]==-1){
                                if(dist[i.first]!=-1){
                                    st.erase({dist[i.first], i.first});
                                }
                                dist[i.first]=curdis+i.second;
                                ways[i.first]=ways[v];
                                st.insert({dist[i.first], i.first});
                            }
                            else if(dist[i.first]==curdis+i.second){
                                ways[i.first]=(ways[i.first]%M+ways[v]%M)%M;
                            }
                        }
                    }
                    return ways[n-1];
                }
            ```

        
        - Shortest path in Directed acyclic graph with non negative weights

            - A bit more time but similar to BFS

                ```cpp
                vector<int> distance(N, INT_MAX);
                        distance[0] = 0;
                        queue<int> q;
                        q.push(0);

                        while(q.size()){
                            int node = q.front();   q.pop(); 

                            for(auto padosi : adj[node]){
                                int v = padosi[0] ;
                                int dist = padosi[1];
                                if(distance[node] + dist < distance[v]){
                                    distance[v] = distance[node] + dist ;
                                    q.push(v);  // add the node again
                                }
                            }
                        }
                ```

            
            - Toposort

                First find the toposort anyhow. Then just one by one relax the edges

                - Only addition to toposort

                    ```cpp
                    for(auto node: toposort){
                            for (auto it: adj[node]) {
                              int v = it.first;
                              int wt = it.second;

                              if (dist[node] + wt < dist[v]) {
                                dist[v] = wt + dist[node];
                              }
                            }
                        }
                    ```

                      

                
                - Whole code

                    ```cpp
                    void dfs(vector<vector<int>> adj[], int n, int v, vector<int>& toposort, vector<int>& vis){
                            if(vis[v]) return;
                            vis[v]=1;
                            for(auto &i: adj[v]){
                                dfs(adj, n, i[0], toposort, vis);
                            }
                            toposort.push_back(v);
                        }
                         vector<int> shortestPath(int N,int M, vector<vector<int>>& edges){
                            // code here
                            vector<vector<int>> adj[N];
                            for(auto e : edges){
                                adj[e[0]].push_back( {e[1], e[2]} );
                            }
                            vector<int> vis(N, 0), toposort, dis(N, INT_MAX);
                    	    dfs(adj, N, 0, toposort, vis);
                    	    reverse(toposort.begin(), toposort.end());

                            dis[0]=0;
                            for(auto node: toposort){
                                for (auto &it: adj[node]) {
                                  int v = it[0];
                                  int wt = it[1];

                                  if (dis[node] + wt < dis[v]) {
                                    dis[v] = wt + dis[node];
                                  }
                                }
                            }
                    	   for(auto &i: dis){
                    	       if(i==INT_MAX) i=-1;
                    	   }
                    	    return dis;
                        }
                    ```

                

                

        
        - Alien dictionary

            Link a character to the other at the first ocurance the character from first string is different from the same length

            ```cpp
            public:
                string findOrder(string dict[], int n, int k) {
                    //code here
                    vector<int> adj[26];
                    for(int i=0;i<n-1;i++){
                        string s1=dict[i];
                        string s2=dict[i+1];
                        int len=min(s1.length(), s2.length());
                        for(int j=0;j<len;j++){
                            if(s1[j]!=s2[j]){
                                adj[s1[j]-'a'].push_back(s2[j]-'a');
                                break;
                            }
                        }
                    }

                    vector<int> vis(k, 0), toposort, indegree(k, 0);
            	   n=k;
            	   for(int i=0;i<26;i++){
            	       for(auto j: adj[i]){
            	           indegree[j]++;
            	       }
            	   }
            	   queue<int> q;
            	   for(int i=0;i<n;i++){
            	       if(indegree[i]==0) q.push(i);
            	   }
            	   while(!q.empty()){
            	       int v=q.front();
            	       toposort.push_back(v);
            	       q.pop();
            	       for(auto i: adj[v]){
            	           indegree[i]--;
            	           if(indegree[i]==0){
                                q.push(i);	               
            	           }
            	       }
            	   }
            	   string st="";
            	   for(auto i: toposort){
            	       st.push_back((char)(i+'a'));
            	   }
            	   //cout<<st<<' ';
            	   return st;
                }
            ```

        
        - Find eventual safe states

            You have to find the nodes which eventually lead to a terminal node.

            Now, we know that toposort uses indegree 0. And we need the outdegree to be 0. So, we reverse all the edges.

            Just take the toposort and only those nodes will be included which don’t form a cycle. Ezpz

        
        - Bellman ford // note isme edge list use hoti na ki adjacency list

            Running the loop n-1 times gets you the minimum distance. Run a loop after that again. If again we find shorter path that means it contains negative cycle

            TC: O(V*E) where E could be n^2 in dense graphs

            ```cpp
            vector<int> bellman_ford(int V, vector<vector<int>>& edges, int S) {
                    // Code here
                    int n=V;
                    vector<int> dist(n, 1e8);
                    dist[S]=0;
                    for(int i=0;i<n-1;i++){
                        for(auto i: edges){
                            int u=i[0];
                            int v=i[1];
                            int wt=i[2];
                            if(dist[u]!=1e8&&dist[v]>dist[u]+wt){
                                dist[v]=dist[u]+wt;
                            }
                        }
                    }
                    for(auto i: edges){
                        int u=i[0];
                        int v=i[1];
                        int wt=i[2];
                        if(dist[u]!=1e8&&dist[v]>dist[u]+wt){
                            return {-1};
                        }
                    }
                    return dist;
                }
            ```

        
        - Floyd Warshall // note isme adjacency matrix use hoti na ki adjacency list

            ```cpp
            vector<vector<int>> dp(n, vector<int>(n, 1e8));
            for(int via=0;via<n;via++){
                for(int i=0;i<n;i++){
                    for(int j=0;j<n;j++){
                        dp[i][j]=min(dp[i][j], dp[i][via]+dp[via][j]);
                    }
                }
            }
            ```

        
        - Prim’s Algo

            ```cpp
            int spanningTree(int V, vector<vector<int>> adj[])
                {
                    // code here
                    int sum=0, n=V;
                    multiset<pair<int, int>> q;
                    vector<int> vis(n, 0);
                    q.insert({0, 0});
                    // vis[0]=1;
                    while(!q.empty()){
                        int v=q.begin()->second;
                        int w=q.begin()->first;
                        if(vis[v]){
                            q.erase(q.begin());
                            continue;
                        }
                        sum+=w;
                        vis[v]=1;
                        q.erase(q.begin());
                        for(auto i: adj[v]){
                            if(!vis[i[0]]){
                                q.insert({i[1], i[0]});
                            }
                        }
                    }
                    return sum;
                }
            ```

        
        - Kruskal Algo

            ```cpp
            vector<int> par, size;
            	int find(int u){
            	    if(par[u]==u) return u;
            	    return par[u]=find(par[u]);
            	}
            	void unions(int a, int b){
            	    a=find(a);
            	    b=find(b);
                    if(a==b) return;
                    if(size[a]>size[b]) swap(a, b);
                    par[a]=b;
                    size[b]+=size[a];
            	}
            	public:
                int spanningTree(int V, vector<vector<int>> adj[])
                {
                    // code here
                   par.resize(V+1, 0);
                    size.resize(V+1, 1);
                    for(int i=0;i<=V;i++){
                        par[i]=i;
                    }
                    vector<pair<int, pair<int, int>>> weight_edge;
                    for (int i = 0; i < V; i++) {
                        for (auto it : adj[i]) {
                            int adjNode = it[0];
                            int wt = it[1];
                            int node = i;

                            weight_edge.push_back({wt, {node, adjNode}});
                        }
                    }
                    sort(weight_edge.begin(), weight_edge.end());
                    int mstwt=0;
                    for(auto i: weight_edge){
                        if(find(i.second.first)==find(i.second.second)){
                            continue;
                        }
                        else{
                            mstwt+=i.first;
                            unions(i.second.first, i.second.second);
                        }
                    }
                    return mstwt;
                }
            ```

        
        - Strongly connected components

            get toposorted nodes. Now reverse the edges of the graph and run dfs from unvisited nodes in toposorted order. Each time you start a dfs from unvisited node, you get a new strongly connected component.

            Question: assign the nodes to their strongly connected components

            ```cpp
            void dfs(ll v, vl &topo){
                vis[v]=1;
                for(auto i: graph[v]){
                    if(!vis[i]) dfs(i, topo);
                }
                topo.push_back(v);
            }

            void dfs2(ll v, vl& ans, ll color){
                vis2[v]=1;
                ans[v]=color;
                for(auto i: graph2[v]){
                    if(!vis2[i])dfs2(i, ans, color);
                }
            }

            int main(){
            	for (ll i = 0; i < m; i++)
                {
                    ll v1, v2;
                    cin>>v1>>v2;
                    graph[v1].push_back(v2);
                    graph2[v2].push_back(v1);
                }
                vl topo;
                for(ll i=1;i<=n;i++){
                    if(!vis[i]) dfs(i, topo);
                }
                reverse(all(topo));
                ll color=0;
                vl ans(n+1);
                for(auto i: topo){
                    if(!vis2[i]){ 
                        color++;
                        dfs2(i, ans, color);
                    }
                }
            }
            ```

              

        
        - Making a large island.

            Given a 2d matrix. Islands of 1s. You can switch a single zero to one to connect islands. You can use DSU to keep track of connected components and size of each components. Iterate over the grid and if 0, check in all four directions for biggest merges.

        
        - Swim in rising water

            ![[prep/DSA Notes/Private & Shared/Untitled 29.png|Untitled 29.png]]

            This question is basically find path with minimized maximum. You have to use binary search to find the maxi and dfs through the nodes below maxi.

        

    - Binary Search

        - Notes

            Binary search is often a topic that's easy to be explained on the abstract  
            level, but when it comes to writing bug free implementations, it's  
            rather difficult.

            Some of the most common problems include:

            1. Infinity loop

            1. Can't decide where to shrink

            1. Do I use lo or hi

            1. When to exit the loop

            1. ...

            In this article, I will be sharing my insights on how to write bug free binary search with just a little pattern.

            _If you are familiar with binary search and just want to see the pattern, you can go directly to the part: The Pattern._

            ## What is binary search?

            Normally, to find the target in a group, such as an array of numbers,  
            the worst case scenario is we need to go through every single element  
            (O(n)). However, when these elements are sorted, we are able to take the  
            privilege of this extra information to bring down the search time to  
            O(log n), that is if we have 100 elements, the worst case scenario would  
            be 10 searches. That is a huge performance improvement.

            The Gif below demonstrates the power of binary search.

            [![](https://assets.leetcode.com/static_assets/posts/1EYkSkQaoduFBhpCVx7nyEA.gif)](https://assets.leetcode.com/static_assets/posts/1EYkSkQaoduFBhpCVx7nyEA.gif)

            The reason behind this huge performance increase is because for each  
            search iterations, we are able to cut the elements we will be looking at  
            in half. Fewer elements to look at = faster search time. And this all  
            comes from the simple fact that in a sorted list, everything to the  
            right of n will be greater or equal to it, and vice versa.

            Before we look at the abstract ideas of binary search, let's see the code first:

            ```
            var search = function(nums, target) {
                let lo = 0, hi = nums.length-1;
                while (lo < hi) {
                    let mid = lo + Math.floor((hi-lo+1)/2);
                    if (target < nums[mid]) {
                        hi = mid - 1
                    } else {
                        lo = mid;
                    }
                }
                return nums[lo]==target?lo:-1;
            };
            ```

            ## The fundamental idea

            **1.** `**lo**` **&** `**hi**`

            We define two variables, let's call them `lo` and `hi`  
            . They will store array indexes and they work like a boundary such that  
            we will only be looking at elements inside the boundary.

            Normally, we would want initialize the boundary to be the entire array.

            ```
            let lo = 0, hi = nums.length-1;
            ```

            **2.** `**mid**`

            The `mid` variable indicates the middle element within the  
            boundary. It separates our boundary into 2 parts. Remember how I said  
            binary search works by keep cutting the elements in half, the `mid` element works like a traffic police, it indicates us which side do we want to cut our boundary to.

            Note when an array has even number of elements, it's your decision to use either the left `mid` (lower `mid`) or the right `mid` (upper mid)

            ```
            let mid = lo + Math.floor((hi - lo) / 2); // left/lower mid

            let mid = lo + Math.floor((hi - lo + 1) / 2); // right/upper mid
            ```

            **3. Comparing the target to** `**mid**`

            By comparing our target to `mid`, we can identify which side of the boundary does the target belong. For example, If our target is greater than `mid`, this means it must exist in the right of `mid`  
            . In this case, there is no reason to even keep a record of all the  
            numbers to its left. And this is the fundamental mechanics of binary  
            search - keep shrinking the boundary.

            ```
            if (target < nums[mid]) {
            	hi = mid - 1
            } else {
            	lo = mid;
            }
            ```

            **4. Keep the loop going**

            Lastly, we use a while loop to keep the search going:

            ```
            while (lo < hi) { ... }
            ```

            The while loop only exits when `lo == hi`, which means  
            there's only one element left. And if we implemented everything  
            correctly, that only element should be our answer(assume if the target  
            is in the array).

            ## The pattern

            It may seem like binary search is such a simple idea, but when you  
            look closely in the code, we are making some serious decisions that can  
            completely change the behavior of our code.

            These decisions include:

            1. Do I use left or right `mid`?

            1. Do I use `<` or `<=` , `>` or `>=`?

            1. How much do I shrink the boundary? is it `mid` or `mid - 1` or even `mid + 1` ?

            1. ...

            And just by messing up one of these decisions, either because you  
            don't understand it completely or by mistake, it's going to break your  
            code.

            To solve these decision problems, I use the following set of rules to  
            always keep me away from trouble, most importantly, it makes my code  
            more consistent and predictable in all edge cases.

            **1. Choice of** `**lo**` **and** `**hi**`**, aka the boundary**

            Normally, we set the initial boundary to the number of elements in the array

            ```
            let lo = 0, hi = nums.length - 1;
            ```

            But this is not always the case.

            We need to remember: the boundary is the range of elements we will be searching from.

            The initial boundary should include **ALL** the elements,  
            meaning all the possible answers should be included. Binary search can  
            be applied to none array problems, such as Math, and this statement is  
            still valid.

            For example, In LeetCode 35, the question asks us to find an index to **insert** into the array.

            It is possible that we insert after the last element of the array, thus the complete range of boundary becomes

            ```
            let lo = 0, hi = nums.length;
            ```

            **2. Calculate** `**mid**`

            Calculating mid can result in overflow when the numbers are extremely big. I ll demonstrate a few ways of calculating `mid` from the worst to the best.

            ```
            let mid = Math.floor((lo + hi) / 2) // worst, very easy to overflow

            let mid = lo + Math.floor((hi - lo) / 2) // much better, but still possible

            let mid = (lo + hi) >>> 1 // the best, but hard to understand
            ```

            When we are dealing with even elements, it is our choice to pick the left `mid` or the right `mid` , and as I ll be explaining in a later section, a bad choice will lead to an infinity loop.

            ```
            let mid = lo + Math.floor((hi - lo) / 2) // left/lower mid

            let mid = lo + Math.floor((hi - lo + 1) / 2) // right/upper mid
            ```

            **3. How do we shrink boundary**

            I always try to keep the logic as simple as possible, that is a single pair of `if...else`. But what kind of logic are we using here? My rule of thumb is always use a logic that you can **exclude** `mid`.

            Let's see an example:

            ```
            if (target < nums[mid]) {
            	hi = mid - 1
            } else {
            	lo = mid;
            }
            ```

            Here, if the target is less than `mid`, there's no way `mid` will be our answer, and we can exclude it very confidently using `hi = mid - 1`. Otherwise, `mid` still has the potential to be the target, thus we include it in the boundary `lo = mid`.

            On the other hand, we can rewrite the logic as:

            ```
            if (target > nums[mid]) {
            	lo = mid + 1; // mid is excluded
            } else {
            	hi = mid; // mid is included
            }
            ```

            **4. while loop**

            To keep the logic simple, I always use

            ```
            while(lo < hi) { ... }
            ```

            Why? Because this way, the only condition the loop exits is `lo == hi`. I know they will be pointing to the same element, and I know that element always exists.

            **5. Avoid infinity loop**

            Remember I said a bad choice of left or right `mid` will lead to an infinity loop? Let's tackle this down.

            Example:

            ```
            let mid = lo + ((hi - lo) / 2); // Bad! We should use right/upper mid!

            if (target < nums[mid]) {
            	hi = mid - 1
            } else {
            	lo = mid;
            }
            ```

            Now, imagine when there are only 2 elements left in the boundary. If the logic fell into the `else`  
            statement, since we are using the left/lower mid, it's simply not doing  
            anything. It just keeps shrinking itself to itself, and the program got  
            stuck.

            We have to keep in mind that, the choice of `mid` and our shrinking logic has to work together in a way that every time, at least 1 element is excluded.

            ```
            let mid = lo + ((hi - lo + 1) / 2); // Bad! We should use left/lower mid!

            if (target > nums[mid]) {
            	lo = mid + 1; // mid is excluded
            } else {
            	hi = mid; // mid is included
            }
            ```

            So when your binary search is stuck, think of the situation when  
            there are only 2 elements left. Did the boundary shrink correctly?

            ## TD;DR

            My rule of thumb when it comes to binary search:

            1. Include **ALL** possible answers when initialize `lo` & `hi`

            1. Don't overflow the `mid` calculation

            1. Shrink boundary using a logic that will **exclude** mid

            1. Avoid infinity loop by picking the correct `mid` and shrinking logic

            1. Always think of the case when there are 2 elements left

            _Because this problem is a failrly easy, the implementions may be_  
            _pretty straight forward and you may wonder why do I need so many rules._  
            _However, binary search problems can get much much more complex, and_  
            _without consistent rules, it's very hard to write predictable code. In_  
            _the end, I would say everybody has their own style of binary serach,_  
            _find the style that works for you!_

        
        - _MY NOTES_

            Use this format (tested for all binary search on answer):

            ```cpp
            // minimizing the answer. Answer stored in r
            // note that since l<r-1, we are searching from l+1 to r
            int l=0, r=1e9;
            while(l<r-1){
                int m = r-(r-l)/2;
                if(check(nums, k, m)) r=m;
                else l=m;
            }
            return r;

            // maximizing the answer. Answer stored in l
            // note that since l<r-1, we are searching from 0 to r-1
            int l=0, r=1e9;
            while(l<r-1){
                int m = r-(r-l)/2;
                if(check(nums, k, m)) l=m;
                else r=m;
            }
            return l;

            // when things involve double, use a for loop. A loop till 64 would suffice for up to 16 decimal places but run till 100 just to be sure
            double l=0, r=1e18;
            for(ll i=0;i<100;i++){
                double mid=(double)(l+r)/2;
                if(good(mid,a)) l=mid;
                else r=mid;
            }
            cout<<setprecision(20)<<l<<"\n";
            ```

        
        - Search in rotated sorted unique array

            Check which side of mid is sorted. If left≤mid then left half is sorted and if right≥mid then right half is sorted. Depending on the half which is sorted, you can check if the target should be on that half or not.

            ```cpp
            int search(vector<int>& nums, int target) {
                    int l=0, r=nums.size()-1;
                    while(l<r-1){
                        int mid=(l+r)/2;
                        if(nums[mid]>=nums[l]){
                            if(nums[mid]>=target&&nums[l]<=target){
                                r=mid;
                            }
                            else l=mid;
                        }
                        else{
                            if(nums[mid]<=target&&nums[r]>=target){
                                l=mid;
                            }
                            else r=mid;
                        }
                    }
                    return nums[r]==target ? r : nums[l]==target ? l : -1;
                }
            ```

        
        - Search in rotated sorted duplicate possible array

            Same as before but first check if nums[l]==nums[mid]==nums[r]. Then we can’t accurately determine which half is sorted. For eg, 3,2,3,3. In this case, decrease the window by one.

            ```cpp
            bool search(vector<int>& nums, int target) {
                    int l=0, r=nums.size()-1;
                    while(l<r-1){
                        int mid=(l+r)/2;
                        if(nums[l]==nums[mid]&&nums[mid]==nums[r]){
                            l++;
                            r--;
                        }
                        else if(nums[l]<=nums[mid]){
                            if(nums[l]<=target&&nums[mid]>=target){
                                r=mid;
                            }
                            else l=mid;
                        }
                        else{
                            if(nums[mid]<=target&&nums[r]>=target){
                                l=mid;
                            }
                            else r=mid;
                        }
                    }
                    cout<<l<<' ';
                    if(nums[l]==target||nums[r]==target) return true;
                    return false;
                }
            ```

        
        - Search the min element in rotated sorted unique array

            Similar concept. Just find which half is sorted and then decide how the window will halve.

            ```cpp
            int findMin(vector<int>& arr) {
                    int l=0, r=arr.size()-1;
                    while(l<r-1){
                        int mid=(l+r)/2;
                        if(arr[l]<arr[mid]&&arr[mid]<arr[r]){
                            return arr[l];
                        }
                        else if(arr[l]<arr[mid]){
                            l=mid;
                        }
                        else if(arr[r]>arr[mid]){
                            r=mid;
                        }
                    }
                    return min(arr[l], arr[r]);
                }
            ```

        
        - Find how many times array is rotated

            Just find the position of min element(previous question)-0.

        
        - Median of two sorted arrays

            ![[prep/DSA Notes/Private & Shared/Untitled 30.png|Untitled 30.png]]

            For it to be a valid cur, l1≤r2 and l2≤r1. Median will be among Max(leftHalf1,leftHalf2) and Min(rightHalf1, rightHalf2)

            ```cpp
            double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
                    int n1=nums1.size(), n2=nums2.size();
                    if(n1>n2) return findMedianSortedArrays(nums2, nums1);
                    int l=0, r=n1;
                    int halfSize=(n1+n2+1)/2;
                    while(l<=r){
                        int mid=(l+r)/2;
                        int cut1=mid;
                        int cut2=halfSize-cut1;
                        int leftHalf1 = (cut1==0) ? INT_MIN : nums1[cut1-1];
                        int leftHalf2 = (cut2==0) ? INT_MIN : nums2[cut2-1];
                        int rightHalf1 = (cut1==n1) ? INT_MAX : nums1[cut1];
                        int rightHalf2 = (cut2==n2) ? INT_MAX : nums2[cut2];
                        if(leftHalf1>rightHalf2){
                            r=cut1-1;
                        }
                        else if(leftHalf2>rightHalf1){
                            l=cut1+1;
                        }
                        else{
                            if((n1+n2)%2==0){
                                return (max(leftHalf1, leftHalf2)+min(rightHalf1, rightHalf2))/2.0;
                            }
                            else 
                                return max(leftHalf1, leftHalf2);
                        }
                    }
                    return 0.0;
                }
            ```

        
        - Kth element of two sorted arrays

            Can be done using heaps nlogk

            Better using binary search: (gfg test case wrong)

            ```cpp
            int kthElement(int nums1[], int nums2[], int n, int m, int k)
                {
                    int n1=n, n2=m;
                    if(n1>n2) return kthElement(nums2, nums1, m, n, k);
                    int l=max(0, k-n2), r=min(k, n1);
                    while(l<=r){
                        int mid=(l+r)/2;
                        int cut1=mid;
                        int cut2=k-cut1;
                        int leftHalf1 = (cut1==0) ? INT_MIN : nums1[cut1-1];
                        int leftHalf2 = (cut2==0) ? INT_MIN : nums2[cut2-1];
                        int rightHalf1 = (cut1==n1) ? INT_MAX : nums1[cut1];
                        int rightHalf2 = (cut2==n2) ? INT_MAX : nums2[cut2];
                        if(leftHalf1>rightHalf2){
                            r=cut1-1;
                        }
                        else if(leftHalf2>rightHalf1){
                            l=cut1+1;
                        }
                        else{
                            return max(leftHalf1, leftHalf2);
                        }
                    }
                    return 1;
                }
            ```

        
        - Find median in 2d array with sorted rows

            This one is super easy nlogm.

            calculate the total number of elements smaller than the mid. It should be exactly n*m/2. Each row is sorted so you can find the number of elements strictly smaller than the current element by lowerbound-begin.

            ```cpp
            bool check(vector<vector<int>>& a, int mid){
                int n=a.size();
                int m=a[0].size();
                int numEl=0;
                for(auto i: a){
                    numEl+=lower_bound(i.begin(), i.end(), mid)-i.begin();
                }
                int numElHalf=(n*m)/2;
                if(numEl>numElHalf) return false;
                return true;
            }
            int Solution::findMedian(vector<vector<int> > &a) {
                int l=0, r=1e9+5;
                while(l<r-1){
                    int mid=r-(r-l)/2;
                    if(check(a, mid))l=mid;
                    else r=mid;
                }
                return l;
            }
            ```

        
        - Search in 2d matrix I (2 ways)

            1. Imagine it as sorted 1d array and convert the 2d index into 1d index

                ```cpp
                bool searchMatrix(vector<vector<int>>& matrix, int target) {
                        int l=0, n=matrix.size(), m=matrix[0].size(), r=m*n;
                        while(l<r-1){
                            int mid=r-(r-l)/2;
                            if(matrix[mid/m][mid%m]<=target) l=mid;
                            else r=mid;
                        }
                        if(matrix[l/m][l%m]==target) return true;
                        return false;
                    }
                ```

            
            1. Imagine it as a BST (left is smaller and down is bigger) start from top right.

                ### This works in search in 2d matrix II

                ```cpp
                bool searchMatrix(vector<vector<int>>& matrix, int target) {
                    int rows = matrix.size(),
                		cols = matrix[0].size(),
                    row = 0, col = cols - 1;

                    while (row < rows && col > -1) {
                        int cur = matrix[row][col];
                        if (cur == target) return true;
                        if (target > cur) row++;
                        else col--;
                    }

                    return false;
                }
                ```

            

    
    - Recursion

        - Recursive pow function

            1. O(log n):

                ```cpp
                double myPow(double x, int n) {
                      if(n == 0)
                          return 1;
                      if(n<0){
                          n = -n;
                          x = 1/x;
                      }
                      return (n%2 == 0) ? pow(x*x, n/2) : x*pow(x*x, n/2);
                  }
                ```

            

        - Sort a stack using recursion

            Using recursion, hold the current number in recursion stack space. O(n^2) time and O(n) auxilliary stack space(recursion)

            ```cpp
            void insert(int x, stack<int>& s){
                if(s.empty()||s.top()<x){
                    s.push(x);
                    return;    
                }
                int nx=s.top();
                s.pop();
                insert(x,s);
                s.push(nx);
            }
            void SortedStack :: sort()
            {
               //Your code here
               if(s.empty()) return;
               int x=s.top();
               s.pop();
               sort();
               insert(x,s);
            }
            ```

        
        - Reverse a stack using recursion

            Same logic as sort

            ```cpp
            class Solution{
            public:
                void insertAtBottom(stack<int>& st, int x){
                    if(st.empty()){
                        st.push(x);
                        return;
                    }
                    int temp=st.top();
                    st.pop();
                    insertAtBottom(st, x);
                    st.push(temp);
                }
                void Reverse(stack<int> &st){
                    if(st.empty()) return;
                    int x=st.top();
                    st.pop();
                    Reverse(st);
                    insertAtBottom(st, x);
                }
            };
            ```

        
        - Combination sum 2

            Must not contain duplicate solutions.

            ```cpp
            class Solution {
                void recur(vector<int>& candidates, vector<vector<int>>& ans, vector<int>& temp, int target, int ind){
                    if(target<0) return;
                    if(target==0){
                        ans.push_back(temp);
                        return;
                    }
                    for(int i = ind; i < candidates.size(); i++){
                        if(i != ind && candidates[i]==candidates[i-1])
                            continue;
                        target -= candidates[i];
                        temp.push_back(candidates[i]);
                        recur(candidates, ans, temp, target, i+1);
                        target += candidates[i];
                        temp.pop_back();
                    }
                }
            public:
                vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
                    vector<vector<int>> ans;
                    vector<int> temp;
                    sort(candidates.begin(), candidates.end());
                    vector<vector<int>> res;
                    recur(candidates, ans, temp, target, 0);
                    sort(ans.begin(), ans.end());
                    for(auto i: ans){
                        if(res.empty()){
                            res.push_back(i);
                        }
                        else{
                            if(i==res.back()) continue;
                            res.push_back(i);
                        }
                    }
                    return res;
                }
            };
            ```

        
        - Combination sum 3 (Use k different numbers from 1-9 to add up to n)

            ```cpp
            class Solution {
            public:
                void recur(vector<vector<int>>& ans, vector<int>& temp, int k, int n, int curnum){
                    if(n==0&&k==0){
                        ans.push_back(temp);
                        return;
                    }
                    if(n<0) return;
                    if(k<0) return;
                    for(int i=curnum+1;i<10;i++){
                        temp.push_back(i);
                        recur(ans, temp, k-1, n-i,i);
                        temp.pop_back();
                    }
                }
                vector<vector<int>> combinationSum3(int k, int n) {
                    vector<vector<int>> ans;
                    vector<int> temp;
                    recur(ans, temp, k, n, 0);
                    return ans;
                }
            };
            ```

        
        - Subset sum 2

            ```cpp
            void recur(vector<int>& nums, int ind, vector<int>& temp, vector<vector<int>>& ans){
                    int n=nums.size();
                    ans.push_back(temp);
                    for(int i=ind;i<n;i++){
                        if(i!=ind&&nums[i]==nums[i-1]) continue;
                        temp.push_back(nums[i]);
                        recur(nums, i+1, temp, ans);
                        temp.pop_back();
                    }
                }
                vector<vector<int>> subsetsWithDup(vector<int>& nums) {
                    vector<vector<int>> ans;
                    vector<int> temp;
                    sort(nums.begin(), nums.end());
                    recur(nums, 0, temp, ans);
                    return ans;
                }
            ```

        
        - Partition string into palindromic partitions

            ```jsx
            class Solution {
                bool isPal(string& s){
                    string st=s;
                    reverse(st.begin(), st.end());
                    return st==s;
                }
                void recur(string& s, int ind, vector<vector<string>>& ans, vector<string>& partitions){
                    int n=s.length();
                    if(ind==n){
                        ans.push_back(partitions);
                        return;
                    }
                    string sub="";
                    for(int i=ind;i<n;i++){
                        // taking a substring from current index to i
                        sub.push_back(s[i]);
                        if(isPal(sub)){
                            // if it is a pallindrome, add it to partition and continue the recursion
                            partitions.push_back(sub);
                            recur(s, i+1, ans, partitions);
                            partitions.pop_back();
                        }
                    }

                }
            public:
                vector<vector<string>> partition(string s) {
                    vector<vector<string>> ans;
                    vector<string> partitions;
                    recur(s, 0, ans, partitions);
                    return ans;
                }
            };
            ```

        
        - N queens

            go column wise. Once you reach nth column, you exit. loop through rows in each col from 1 to n. In each iteration, if it is valid, then recursion.

            You can check valid only by checking in backward, up-back and down-back direction

            ```cpp
            class Solution {
            public:
                bool isValid(vector<string>& board, int row, int col){
                    int r=row, c=col;
                    while(c>=0){
                        if(board[r][c]=='Q') return false;
                        c--;
                    }
                    r=row, c=col;
                    while(c>=0&&r>=0){
                        if(board[r][c]=='Q') return false;
                        r--;
                        c--;
                    }
                    r=row, c=col;
                    while(c>=0&&r<board.size()){
                        if(board[r][c]=='Q') return false;
                        r++;c--;
                    }
                    return true;

                }
                void recur(int n, vector<vector<string>>& ans, vector<string>& board, int col){
                    if(col==n) {
                        ans.push_back(board);
                        return;
                    }
                    for(int row=0;row<n;row++){
                        if(isValid(board, row, col)){
                            board[row][col]='Q';
                            recur(n, ans, board, col+1);
                            board[row][col]='.';
                        }
                    }
                }
                vector<vector<string>> solveNQueens(int n) {
                    vector<vector<string>> ans;
                    vector<string> board(n, string(n, '.'));
                    recur(n, ans, board, 0);
                    for(auto i: board) cout<<i<<'\n';
                    return ans;
                }
            };
            ```

        
        - M coloring

            You don’t need to do dfs/bfs. Given and adjacency matrix, you can just directly check the nodes connected to the node.

            ```cpp
            // Function to determine if graph can be coloured with at most M colours such
                // that no two adjacent vertices of graph are coloured with same colour.
                bool isValid(int node, bool graph[101][101], vector<int>& cols, int n, int col){
                    for(int i=0;i<n;i++){
                        if(graph[node][i]&&cols[i]==col) return false;
                    }
                    return true;
                }
                bool recur(bool graph[101][101], int m, int n, vector<int>& cols, int node){
                    if(node==n) return true;
                    for(int i=1;i<=m;i++){
                        if(isValid(node, graph, cols, n, i)){
                            cols[node]=i;
                            if(recur(graph, m, n, cols, node+1)) return true;
                            cols[node]=-1;
                        }
                    }
                    return false;
                }
                bool graphColoring(bool graph[101][101], int m, int n) {
                    // your code here
                    vector<int> cols(n, -1);
                    return recur(graph, m, n, cols,0);

                }
            ```

        
        - Sudoku solver

            Note that each square of 3x3 can also have each number only once.

            Note this in checker function int row=i-i%3, col=j-j%3; <- this is only for checking the square and not the rows/cols.

            ```cpp
            class Solution {
                bool isvalid(vector<vector<char>>& board, int i, int j, char val){
                    int row=i-i%3, col=j-j%3;
                    for(int x=0;x<9;x++) if(board[x][j]==val) return false;
                    for(int y=0;y<9;y++) if(board[i][y]==val) return false;
                    for(int x=0;x<3;x++){
                        for(int y=0;y<3;y++){
                            if(board[x+row][y+col]==val) return false;
                        }
                    }
                    return true;
                }
            public:
                bool recur(vector<vector<char>>& board, int i, int j){
                    if(i==9) return true;
                    if(j==9) return recur(board, i+1, 0);
                    if(board[i][j]!='.') return recur(board, i, j+1);
                    for(char c='1';c<='9';c++){
                        if(isvalid(board, i,j,c)){
                            board[i][j]=c;
                            if(recur(board, i, j+1)) return true;
                            board[i][j]='.';
                        }
                    }
                    return false;
                }

                void solveSudoku(vector<vector<char>>& board) {
                    recur(board, 0, 0);
                }
            };
            ```

        

    - Mafs

        - all prime factors in O(n)

            ```cpp
            class Solution{
            	public:
            	vector<int>AllPrimeFactors(int N) {
            	    // Code here
            	    vector<int> ans;

            	    for(int i=2;i<=N;i++){
            	        if(N%i==0){
            	            ans.push_back(i);
            	            while(N%i==0)
            	                N=N/i;
            	        }
            	    }
            	    return ans;
            	}
            };
            ```

        
        - all divisors in O(sqrt(n))

            ```cpp
            set<int> st;
            for(int i=1;i*i<=n;i++){
                if(n%i==0){
                    st.insert(i);
                    st.insert(n/i);
                }
            }
            ```

        
        - sieve REMEMBER TO CALL IT ONLY ONCE

            ```cpp
            int seiveOfEratosthenes(int n) {
                    vector<int> sieve(n+10, 1);
                    sieve[0]=sieve[1]=0;
                    for (int p = 2; p * p <= n; p++) {
                    if (sieve[p] == 1) {
                        for (int i = p * p; i <= n; i += p)
                            sieve[i] = 0;
                    }
                }
                }
            ```

        
        - Prime factorization using sieve

            ```cpp
            vector<int>SPF(MAXN);
                void sieve() {
                    for(int i=0;i<MAXN;i++){
                        SPF[i]=i;
                    }
                    for(int i=2;i<MAXN;i+=2){
                        SPF[i]=2;
                    }
                    for(int i=3;i*i<MAXN;i+=2){
                        if(SPF[i]==i){
                            for(int j=i*i;j<MAXN;j+=i){
                                if(SPF[j]==j){
                                    SPF[j]=i;
                                }
                            }
                        }
                    }
                }
                vector<int> findPrimeFactors(int N) {
                    vector<int> pfactors;
                    while(N!=1){
                        pfactors.push_back(SPF[N]);
                        N/=SPF[N];
                    }
                    return pfactors;
                }
            ```

        
        - Nth fibonacci number in log n

            |   |   |
            |---|---|
            |1|1|
            |1|0|

            This matrix when pow(n-1) gives Fibonacci(n) in mat[0][0].

            ```cpp
            void mult(vector<vector<int>>& mat, vector<vector<int>> B){
                int x1=mat[0][0]*B[0][0]+(mat[0][1]*B[1][0]));
                int y1=mat[0][0]*B[0][1]+(mat[0][1]*B[1][1]));
                int x2=mat[1][0]*B[0][0]+(mat[1][1]*B[1][0]));
                int y2=mat[1][0]*B[0][1]+(mat[1][1]*B[1][1]));
                mat={{x1, y1}, {x2, y2}};
            }
            void pow(vector<vector<int>>& mat, int n){
                if(n==0||n==1) return;
                pow(mat, n/2);
                mult(mat, mat);

                vector<vector<int>> extraforodd={{1, 1}, {1, 0}};
                if(n%2==1) mult(mat, extraforodd);
            }
            int Solution::solve(int A) {
                vector<vector<int>> mat={{1, 1}, {1, 0}};
                if(A==1) return 1;
                pow(mat, A-1);
                return mat[0][0];
            }
            ```

        
        - Make the biggest number using array of numbers

            Convert numbers to string and sort them by s1+s2>s2+s1

            ```cpp
            static bool cmp(string& s1, string& s2){
                    return s1+s2>s2+s1;
                }
                string largestNumber(vector<int>& nums) {
                    vector<string> a;
                    for(auto i: nums){
                        a.push_back(to_string(i));
                    }
                    sort(a.begin(), a.end(), cmp);
                    string ans="";
                    if(a[0]=="0") return "0";
                    for(auto i: a){
                        ans+=i;
                    }
                    return ans;
                }
            ```

        
        - Next stage in game of life in place

            The problem with in place was that we had to use the previously updated values in the grid so you can’t overwrite previous values. The game of life had only 0 and 1. So only one bit is used. So we could use the second bit to store the new value. After this, just right shift everything.

            ```cpp
            class Solution {
            public:
                int getcnt(vector<vector<int>>& board, int x, int y){
                    int cnt=0, n=board.size(), m=board[0].size();
                    for(int i=-1;i<=1;i++){
                        for(int j=-1;j<=1;j++){
                            if(x+i<0||x+i>=n||y+j<0||y+j>=m||(i==0&&j==0)) continue;
                            if((board[x+i][y+j]&1)==1) cnt++;
                        }
                    }
                    return cnt;
                }
                void gameOfLife(vector<vector<int>>& board) {
                    int n=board.size(), m=board[0].size();
                    for(int x=0;x<n;x++){
                        for(int y=0;y<m;y++){
                            int cnt=getcnt(board, x, y);

                            if((board[x][y]&1)==1){
                                if(cnt>3) board[x][y]=01;
                                else if(cnt<2) board[x][y]=01;
                                else{
                                    board[x][y]=3;              // 11
                                }
                            }
                            else{
                                if(cnt==3){
                                    board[x][y]=2;              // 10
                                }
                            }
                        }
                    }
                    for(int x=0;x<n;x++){
                        for(int y=0;y<m;y++){
                            board[x][y] = board[x][y]>>1;
                        }
                    }
                }
            };
            ```

        

    - Greedy

        - Fractional Knapsack

            ```cpp
            class Solution
            {
                public:
                static bool cmp(struct Item a, struct Item b)      // NOTE the comparator
                {
                    double r1 = (double)a.value / (double)a.weight;
                    double r2 = (double)b.value / (double)b.weight;
                    return r1 > r2;
                }
                //Function to get the maximum total value in the knapsack.
                double fractionalKnapsack(int W, Item arr[], int n)
                {
                    // Your code here
                    double sum=0;
                    sort(arr, arr+n, cmp);                         // NOTE how comparator is used
                    for(int i=0;i<n;i++){                          // NOTE the loop
                        if(W>=arr[i].weight){
                            W-=arr[i].weight;
                            sum+=arr[i].value;
                        }
                        else{
                            sum+=(double)W*(double)arr[i].value/(double)arr[i].weight;
                            break;
                        }
                    }
                    return sum;
                }

            };
            ```

        
        - Bring sheep together

            given string with …x….x..xxx..x

            x→ sheep and . → empty

            You have to bring the sheep together by minimum shifts

            For this, you can bring all of them to the **median** of the sheep

        
        - N meetings in a room

            Sort on basis of end times first then start times.

            ```cpp
            static bool compare( pair<int,int> &a, pair<int,int> &b){
                    if(a.second<b.second)return true;
                    if(a.second > b.second) return false;
                    return a.first < b.first;
                }
                public:
                //Function to find the maximum number of meetings that can
                //be performed in a meeting room.
                int maxMeetings(int start[], int end[], int n)
                {
                    // Your code here
                    vector<pair<int, int>> st;
                    for(int i=0;i<n;i++){
                        st.push_back({start[i], end[i]});
                    }
                    sort(st.begin(), st.end(), compare);
                    int cnt=0, prev=0;
                    for(auto i: st){
                        if(i.first>prev){
                            prev=i.second;
                            cnt++;
                        }
                    }
                    return cnt;
                }
            ```

        
        - Jump game 2

            To count, use a curEnd variable to mark from where we have to jump absolutely. The curMax variable stores the max step we can go to. Everytime we get to curEnd, increase the count unless we are at the last step.

            ```cpp
            int jump(vector<int>& nums) {
                int curMax=0, cnt=0, curEnd=0;
                for(int i=0;i<nums.size();i++){
                    curMax=max(curMax, i+nums[i]);
                    if(i==curEnd&&i!=nums.size()-1){
                        cnt++;
                        curEnd=curMax;
                    }
                }
                return cnt;
            }
            ```

        
        - Maximum overlapping intervals

            Use a vector<pair<int, char>>. Second would store x→start of interval and y→end of interval. Sort it. While iterating, x→ increase count and y→ decrease count. Max(cnt) during the iteration is the answer

            ```cpp
            int findPlatform(int arr[], int dep[], int n)
                {
                	// Your code here
                	vector<pair<int, char>> vp;
                	for(int i=0;i<n;i++){
                	    vp.push_back({arr[i], 'x'});
                	    vp.push_back({dep[i], 'y'});
                	}
                	int cnt=0, ans=0;
                	sort(vp.begin(), vp.end());
                	for(auto i: vp){
                	    if(i.second=='x'){
                	        cnt++; 
                	    }
                	    else cnt--;
                	    ans=max(ans, cnt);
                	}
                	return ans;
                }
            ```

        
        - Candies (Bigger rating gets more candies than adjacent ones)

            We have to find total candies.

            - O(n) time and O(n) space

                Assign everyone 1 candy. Go right from start considering only left neighbors then go left from end considering only right neighbors. Then sum it all.

                ```cpp
                int candy(vector<int>& ratings) {
                        int sum=0, n=ratings.size();
                        if(n<=1) return n;
                        vector<int> num(n, 1);
                				// go right
                        for(int i=1;i<n;i++){
                            if(ratings[i]>ratings[i-1]){
                                num[i]=num[i-1]+1;
                            }
                        }
                				// go left
                        for(int i=n-2;i>=0;i--){
                            if(ratings[i]>ratings[i+1]){
                                num[i]=max(num[i], num[i+1]+1); // note this
                            }
                        }
                        for(int i=0;i<n;i++){
                            sum+=num[i];
                        }
                        return sum;
                    }
                ```

            
            - O(n) time and O(1) space

                ```cpp
                int candy(vector<int>& ratings) {
                        int n=ratings.size(), sum=n, i=1;
                        while(i<n){
                            // skip the repeating ones
                            if(ratings[i]==ratings[i-1]){
                                i++;
                                continue;
                            }

                            // for increasing slope
                            int peak=0;
                            while(ratings[i]>ratings[i-1]){
                                peak++;
                                sum+=peak;
                                i++;
                                if(i==n) return sum;
                            }

                            // for decreasing slope
                            int valley=0;
                            while(i<n && ratings[i]<ratings[i-1]){
                                valley++;
                                sum+=valley;
                                i++;
                            }
                            // removing the elements which were added twice
                            sum-=min(peak, valley);
                        }
                        return sum;
                    }
                ```

            

        - Job sequencing.

            Sort by profit first. Then if profit same, sort by deadline. Idea is to _try_ to do each job on or just before it’s deadline.

        
        - Minimum number of intervals to remove to make it non overlapping

            Just count the number of overlapping intervals.

            ```cpp
            int eraseOverlapIntervals(vector<vector<int>>& intervals) {
                sort(intervals.begin(), intervals.end());
                int prev=intervals[0][1], cnt=0;
                for(int i=1;i<intervals.size();i++){
                    if(intervals[i][0]<prev){
                        cnt++;
                        prev=min(prev, intervals[i][1]);
                    }
                    else prev=intervals[i][1];
                }
                return cnt;
            }
            ```

        
        - Russian doll envelopes

            You have to fit envelopes into each other such that it must be strictly smaller in height and width than the bigger one.

            You can sort first by height and then in opposite order by width. First was necessary to translate this into a single dimension and second to eliminate envelopes with same height. Then just LIS on width.

            ```cpp
            static bool comp(vector<int>& a, vector<int>& b){
                    if(a[0]<b[0]) return true;
                    else if(a[0]>b[0]) return false;
                    return a[1]>b[1];
                }
                int maxEnvelopes(vector<vector<int>>& envelopes) {
                    sort(envelopes.begin(), envelopes.end(), comp);
                    int n=envelopes.size();
                    for(auto i: envelopes){
                        cout<<i[0]<<' '<<i[1]<<'\n';
                    }
                    vector<int> dp;
                    for(int i=0;i<n;i++){
                        if(dp.empty()){
                            dp.push_back(envelopes[i][1]);
                        }
                        auto it=lower_bound(dp.begin(), dp.end(), envelopes[i][1]);
                        if(it==dp.end()){
                            dp.push_back(envelopes[i][1]);
                        }
                        else{
                            dp[it-dp.begin()]=envelopes[i][1];
                        }
                    }
                    return dp.size();
                }
            ```

        

    - Strings

        ### Note:

        Strings me usually sliding window lagta. Hamesha ye yaad rkhna ki ek hash array of 26 size bana skte. Looping through whole of it takes constant time and space.

        - Isomorphic strings

            Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

            All occurrences of a character must be replaced with another  
            character while preserving the order of characters. No two characters  
            may map to the same character, but a character may map to itself.

            ```cpp
            bool isIsomorphic(string s, string t) {
            	  vector<int> mp1(256, -1), mp2(256, -1);
            	  for(int i=0;i<s.length();i++){
            	      if(mp1[s[i]]!=-1&&mp1[s[i]]!=t[i]) return false;
            	      if(mp2[t[i]]!=-1&&mp2[t[i]]!=s[i]) return false;
            	      mp1[s[i]]=t[i];
            	      mp2[t[i]]=s[i];
            	  }
            	  return true; 
            	}
            ```

        
        - Frequency sort

            ```cpp
            string frequencySort(string s) {
                unordered_map<int, int> mp;
                for(int i=0;i<s.length();i++){
                    mp[s[i]]++;
                }
                priority_queue<pair<int, int>> pq;
                for(auto i: mp){                 // this loop runs only 255 times(characters)
                    pq.push({i.second, i.first});
                }
                string st;
                while(!pq.empty()){
                    st+=string(pq.top().first, pq.top().second); // note this new way
                    pq.pop();
                }
                return st;
            }
            ```

        
        - Next smallest palindrome

            First, try making the current string a palindrome by copying the left half to right half. If the string is smaller or equal to current string, then we have to increase the middle element by 1. Take care of carry for 9.

            ```cpp
            string incrementMid(string& st, int r){
                int carry=0;
                while(r>=0){
                    if(st[r]=='9'){
                        st[r]='0';
                        carry=1;
                    }
                    else{
                        st[r]++;
                        carry=0;
                        break;
                    }
                    r--;
                }
                if(carry==1){
                    st.insert(0, "1");
                }
                int l=0;
                r=st.length()-1;
                while(l<r){
                    st[r]=st[l];
                    l++;
                    r--;
                }
                return st;
            }
            bool check(string& s, string& st){
                for(int i=0;i<s.length();i++){
                    if(s[i]<st[i]) return true;
                    else if(s[i]>st[i]) return false;
                }
                return false;
            }
            string Solution::solve(string s) {
                string st=s;
                int l=0, r=s.length()-1;
                while(l<r){
                    st[r]=st[l];
                    l++;
                    r--;
                }
                if(check(s, st)) return st;
                if(s.length()==1) r=0;
                st=incrementMid(st, r);
                return st;

            }
            ```

        
        - Longest palindromic substring without dp

            At every index, try to find out the longest substring with that index as middle.

            For even, indices are one after another

            For odd length substrings, indices start from same index

            ```jsx
            class Solution {
            public:
                pair<int, int> even(string &s, int ind){
                    int ind2 = ind+1;
                    while(ind>=0&&ind2<s.length()&&s[ind]==s[ind2]){
                        ind--;
                        ind2++;
                    }
                    return {ind+1, ind2-1};
                }
                pair<int, int> odd(string &s, int ind){
                    int ind2=ind;
                    while(ind>=0&&ind2<s.length()&&s[ind]==s[ind2]){
                        ind--;
                        ind2++;
                    }
                    return {ind+1, ind2-1};
                }

                string longestPalindrome(string s) {
                    pair<int, int> range={0,0};
                    for(int i=0;i<s.length();i++){
                        pair<int, int> evenrange = {0,0};
                        if(i!=s.length()-1)
                            evenrange = even(s, i);
                        pair<int,int> oddrange = odd(s, i);
                        if(evenrange.second-evenrange.first>range.second-range.first)
                            range = evenrange;
                        if(oddrange.second-oddrange.first>range.second-range.first)
                            range = oddrange;

                    }
                    string st = "";
                    for(int i=range.first;i<=range.second;i++){
                        st.push_back(s[i]);
                    }
                    return st;
                }
            };
            ```

        
        - Minimum additions to make parenthesis valid

            `left` records the number of `(` we need to add on the left of `S`.

            `right` records the number of `)` we need to add on the right of `S`,

            which equals to the number of current opened parentheses.

            Loop char `c` in the string `S`:

            `if (c == '(')`, we increment `right`,

            `if (c == ')')`, we decrement `right`.

            When `right` is already 0, we increment `left`

            Return `left + right` in the end

            ```cpp
            int minAddToMakeValid(string s) {
                int left=0, right=0;
                for(auto c: s){
                    if(c=='(') right++;
                    else if(right>0) right--;
                    else left++;
                }
                return left+right;
            }
            ```

        
        - Rolling hash in strings/Rabin Karp (Find needle in haystack)

            let us search needle string in haystack string;

            We imagine each character mapped to a→1, b→2 … z→26

            Take smallest prime number greater than the max mapped number (say, 29 or 31)

            Take mod value to be something very large. Do everything in long long int.

            ![[prep/DSA Notes/Private & Shared/Untitled 31.png|Untitled 31.png]]

            Now, we can check if a substring exists in the string by sliding window technique (subtracting highest value, multiplying everything by p and adding new value)

            ```cpp
            class Solution {
            public:
                long long int M = 1e17+7;
                long long int p = 31;
                long long int hashFunction(string& s){
                    long long int p1=p, hash=0;
                    for(int i=0;i<s.length();i++){
                        hash=((hash*p)%M+(s[i]-'a'+1)%M)%M;
                    }
                    return hash;
                }
                int strStr(string haystack, string needle) {
                    long long int hneedle = hashFunction(needle);
                    int n=haystack.size(), m = needle.size();
                    if(n<m) return -1;
                    long long int p1=1, hash=0;
                    cout<<hneedle<<'\n';
                    for(int i=0;i<m;i++){
                        if(i!=0)
                        p1=(p1*p)%M;
                        hash=((hash*p)%M+(haystack[i]-'a'+1)%M)%M;
                    }
                    cout<<hash<<' ';
                    if(hash==hneedle) return 0;
                    for(int i=m;i<n;i++){
                        hash-=(p1*(haystack[i-m]-'a'+1)%M)%M;
                        hash=((hash*p)%M+(haystack[i]-'a'+1)%M)%M;
                        cout<<hash<<' ';
                        if(hash==hneedle) return i-m+1;
                    }
                    return -1;
                }
            };
            ```

        

    - Design

        - Design a file sharing system

            Implement the `FileSharing` class:

            - `FileSharing(int m)` Initializes the object with a file of `m` chunks.

            - `int join(int[] ownedChunks)`: A new user joined the system owning some chunks of the file, the system should assign an id to the user which is the **smallest positive integer** not taken by any other user. Return the assigned id.

            - `void leave(int userID)`: The user with `userID` will leave the system, you cannot take file chunks from them anymore.

            - `int[] request(int userID, int chunkID)`: The user `userID` requested the file chunk with `chunkID`. Return a list of the IDs of all users that own this chunk sorted in ascending order.

            **Example:**

            ```
            Input:
            ["FileSharing","join","join","join","request","request","leave","request","leave","join"]
            [[4],[[1,2]],[[2,3]],[[4]],[1,3],[2,2],[1],[2,1],[2],[[]]]
            Output:
            [null,1,2,3,[2],[1,2],null,[],null,1]
            Explanation:
            FileSharing fileSharing = new FileSharing(4); // We use the system to share a file of 4 chunks.

            fileSharing.join([1, 2]);    // A user who has chunks [1,2] joined the system, assign id = 1 to them and return 1.

            fileSharing.join([2, 3]);    // A user who has chunks [2,3] joined the system, assign id = 2 to them and return 2.

            fileSharing.join([4]);       // A user who has chunk [4] joined the system, assign id = 3 to them and return 3.

            fileSharing.request(1, 3);   // The user with id = 1 requested the third file chunk, as only the user with id = 2 has the file, return [2] . Notice that user 1 now has chunks [1,2,3].

            fileSharing.request(2, 2);   // The user with id = 2 requested the second file chunk, users with ids [1,2] have this chunk, thus we return [1,2].

            fileSharing.leave(1);        // The user with id = 1 left the system, all the file chunks with them are no longer available for other users.

            fileSharing.request(2, 1);   // The user with id = 2 requested the first file chunk, no one in the system has this chunk, we return empty list [].

            fileSharing.leave(2);        // The user with id = 2 left the system.

            fileSharing.join([]);        // A user who doesn't have any chunks joined the system, assign id = 1 to them and return 1. Notice that ids 1 and 2 are free and we can reuse them.
            ```

            Use unordered_map<int, set<int>> for both chunks and users. Use a variable to track currently smallest uid. Keep a set unused for smallest uid which might have been freed.

            ```jsx
            class Download
            {
                public:
                unordered_map<int, unordered_set<int>> users;
                vector<unordered_set<int>> chunks;
                set<int> unused;

                int cur;

                Download(int m)
                {
                    cur = 1;
                    chunks.resize(m);
                    users.clear();
                    unused.clear();
                }
                int join(vector<int> &owned_chunks)
                {
                    int min_id;
                    if (unused.empty())
                    {
                        min_id = cur;
                        for (auto chunk : owned_chunks)
                        {
                            users[min_id].insert(chunk);
                        }
                        cur++;
                    }
                    else
                    {
                        min_id = *unused.begin();
                        for (auto chunk : owned_chunks)
                        {
                            users[min_id].insert(chunk);
                        }
                        unused.erase(unused.begin());

                        return min_id;
                    }
                    for (auto chunk : owned_chunks)
                    {
                        chunks[chunk - 1].insert(min_id);
                    }
                    return min_id;
                }
                public:
                void leave(int id)
                {
                    unused.insert(id);
                    for (auto chunk : users[id])
                    {
                        chunks[chunk-1].erase(id);
                    }
                    users.erase(id);
                }
                public:
                vector<int> request(int userId, int chunkId)
                {
                    vector<int> ids;
                    for (auto i : chunks[chunkId-1])
                    {
                        ids.push_back(i);
                    }
                    chunks[chunkId-1].insert(userId);
                    users[userId].insert(chunkId);
                    return ids;
                }
            };
            ```

        

1. To-do

    1. Recursive Insertion sort

    1. Recursive bubble sort

    1. Find Peak Element (2D Matrix)

    1. Recursive Implementation of atoi()

    1. Expression Add Operators

    1. Min Heap and Max Heap Implementation

    1. Convert min Heap to max Heap

    1. SJF

    1. [Longest substring with at least k repeating characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)

    1. [Wiggle sort 2](https://leetcode.com/problems/wiggle-sort-ii/)

    1. [Merge BSTs](https://leetcode.com/problems/merge-bsts-to-create-single-bst/solutions/)

    1. [Max BST in BT](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)

    1. [Number of NGE’s to the right](https://practice.geeksforgeeks.org/problems/number-of-nges-to-the-right/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-nges-to-the-right)

    1. [Largest BST in BT](https://practice.geeksforgeeks.org/problems/largest-bst/1)

    1. [Check whether a string is rotation of another string](https://leetcode.com/problems/rotate-string/)

      

      

      

      

      

1. Revisions:

    1. [Binary Tree Max path sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/)

    1. [Top view of a binary tree](https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1)

ail written in the corresp

![[Untitled 32.png]]

![[Untitled 33.png]]

2 question reinforcement

1 question agent

1 question game playing game theory

2 question searching

h