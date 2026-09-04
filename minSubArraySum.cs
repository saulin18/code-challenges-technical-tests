namespace PrefixSum;
public class Solution
{
    public static int MinSubArrayLen(int target, int[] nums)
    {
        int res = int.MaxValue;
        int windowSum = 0;
        int windowStart = 0;

        for (int windowEnd = 0; windowEnd < nums.Length; windowEnd++)
        {

            windowSum += nums[windowEnd];

            while (windowSum >= target)
            {

                windowSum -= nums[windowStart];
                res = int.Min(res, windowEnd - windowStart + 1);
                windowStart += 1;
            }
        }

        return res == int.MaxValue ? 0 : res;

    }

}
