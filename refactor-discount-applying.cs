using System;
using System.Collections.Generic;


// using System;

// public class Solution
// {
//     // Discount percent for an order. It works - nobody has dared touch it since 2019.
//     public int Discount(int total, string tier, bool coupon, bool seasonal)
//     {
//         if (total <= 0)
//         {
//             return -1;
//         }

//         if (tier == "bronze")
//         {
//             var percent = 0;
//             if (total > 500)
//             {
//                 if (total > 1000)
//                 {
//                     percent = percent + 10;
//                 }
//                 else
//                 {
//                     percent = percent + 5;
//                 }
//             }
//             if (coupon)
//             {
//                 percent = percent + 15;
//             }
//             if (seasonal)
//             {
//                 percent = percent + 5;
//             }
//             if (percent > 40)
//             {
//                 percent = 40;
//             }
//             return percent;
//         }
//         else if (tier == "silver")
//         {
//             var percent = 5;
//             if (total > 500)
//             {
//                 if (total > 1000)
//                 {
//                     percent = percent + 10;
//                 }
//                 else
//                 {
//                     percent = percent + 5;
//                 }
//             }
//             if (coupon)
//             {
//                 percent = percent + 15;
//             }
//             if (seasonal)
//             {
//                 percent = percent + 5;
//             }
//             if (percent > 40)
//             {
//                 percent = 40;
//             }
//             return percent;
//         }
//         else if (tier == "gold")
//         {
//             var percent = 10;
//             if (total > 500)
//             {
//                 if (total > 1000)
//                 {
//                     percent = percent + 10;
//                 }
//                 else
//                 {
//                     percent = percent + 5;
//                 }
//             }
//             if (coupon)
//             {
//                 percent = percent + 15;
//             }
//             if (seasonal)
//             {
//                 percent = percent + 5;
//             }
//             if (percent > 40)
//             {
//                 percent = 40;
//             }
//             return percent;
//         }
//         else
//         {
//             return -1;
//         }
//     }
// }


public class Solution
{
    // Discount percent for an order. It works - nobody has dared touch it since 2019.

    public int determineDiscountIfSeasonalOrCoupon(int percent, bool coupon, bool seasonal)
    {

        if (coupon)
        {
            percent = percent + 15;
        }
        if (seasonal)
        {
            percent = percent + 5;
        }
        if (percent > 40)
        {
            percent = 40;
        }

        return percent;
    }

    public int determineDiscountIfTotalIsGreaterThan500(int total, int percent)
    {

        if (total <= 500)
        {
            return percent;
        }

        if (total > 1000)
        {
            return percent + 10;
        }

        return percent + 5;
    }

    public Dictionary<string, int> tiersInitialPercent = new Dictionary<string, int>();
    public void initializeTiersInitialPercent()
    {
        tiersInitialPercent.Add("bronze", 0);
        tiersInitialPercent.Add("silver", 5);
        tiersInitialPercent.Add("gold", 10);
    }

    public int calculateDiscountsForTier(string tier, int total, bool coupon, bool seasonal)
    {

        var percent = tiersInitialPercent.GetValueOrDefault(tier, -1);
        if (percent == -1)
        {
            return -1;
        }
        percent = determineDiscountIfTotalIsGreaterThan500(total, percent);
        percent = determineDiscountIfSeasonalOrCoupon(percent, coupon, seasonal);
        return percent;
    }


    public int Discount(int total, string tier, bool coupon, bool seasonal)
    {
        initializeTiersInitialPercent();

        if (total <= 0)
        {
            return -1;
        }

        return calculateDiscountsForTier(tier, total, coupon, seasonal);
    }
}
