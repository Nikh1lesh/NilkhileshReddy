using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{   public class User
    {
        public string Username { get; set; }
        public string Role { get; set; }
        public User(string username, string role)
        {
            Username = username;
            Role = role;
        }
        public virtual void AccessControl()
        {
            Console.WriteLine("Access granted to all features");
        }
    }
    public class Admin : User
    {
        public Admin(string username, string role) : base(username, role)
        {
        }
        public override void AccessControl()
        {
            Console.WriteLine("Access granted to all features");
        }
    }
    public class Customer : User
    {
        public Customer(string username, string role) : base(username, role)
        {
        }
        public override void AccessControl()
        {
            Console.WriteLine("Access granted to limited features");
        }
    }
}
