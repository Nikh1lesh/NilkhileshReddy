using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    class Person
    {
        public virtual void getDetails()
        {
            Console.WriteLine("Person details");
        }
    }
    class Student1 : Person
    {
        public string Name { get; set; }
        public int RollNo { get; set; }
        public Student1(string name, int id)
        {
            Name = name;
            RollNo = id;
        }
        public override void getDetails()
        {
            Console.WriteLine("Name: {0} Rollno: {1}", Name, RollNo);
        }
    }
    class Teacher : Person
    {
        public string Name { get; set; }
        public string Subject { get; set; }
        public Teacher(string name, string subject)
        {
            Name = name;
            Subject = subject;
        }
        public override void getDetails()
        {
            Console.WriteLine("Name: {0} Subject: {1}", Name, Subject);
        }
    }

}
