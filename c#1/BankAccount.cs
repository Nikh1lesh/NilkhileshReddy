using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    class BankAccount
    {
        private int balance;
        private int accountNumber;
        public BankAccount(int balance, int accountNumber)
        {
            Balance = balance;
            AccountNumber = accountNumber;
        }
        public int Balance { get; private set; }
        public int AccountNumber { get; private set; }
        public void Deposit(int amount)
        {
            if (amount < 0)
            {
              Console.WriteLine("Amount cannot be negative");
            }
            balance += amount;
        }
        public int GetBalance() { return balance; }
        public void Withdraw(int amount)
        {
            if (amount < 0)
            {
                Console.WriteLine("Amount cannot be negative");
            }
            if (balance < amount)
            {
                Console.WriteLine("Insufficient balance");
            }
            balance -= amount;
        }
    }
}
