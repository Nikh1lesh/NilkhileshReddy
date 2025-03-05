using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    
    class Bank
    {
        public static double InterestRate { get; set; }
        public static void setInterestRate(double rate)
        {
            InterestRate = rate;
        }
    }
}
