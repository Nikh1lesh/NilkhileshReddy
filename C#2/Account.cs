using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPSAssignment2
{
    class Account
    {
        public virtual void CalculateInterest()
        {
        }
    }
    sealed class SavingsAccount : Account
    {
        public override void CalculateInterest()
        {
            Console.WriteLine("Savings Account Interest Calculation");
        }
    }
    //class account111 : SavingsAccount
    //{
    //    public override void CalculateInterest()
    //    {
    //        Console.WriteLine("Savings Account Interest Calculation");
    //    }
    //}
}
