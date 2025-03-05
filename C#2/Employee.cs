using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//Create a class `Employee` with properties `Name` and `Salary`. Derive a class `Manager` that has an additional property `Bonus`. Use constructor chaining to initialize the properties from the base class.
namespace OOPSAssignment2
{
    class Employee
    {
        public string Name { get; set; }
        public double Salary { get; set; }
        public Employee(string name, double salary)
        {
            Name = name;
            Salary = salary;
        }
    }
    class Manager : Employee
    {
        public double Bonus { get; set; }
        public Manager(string name, double salary, double bonus) : base(name, salary)
        {
            Bonus = bonus;
        }
    }

}
