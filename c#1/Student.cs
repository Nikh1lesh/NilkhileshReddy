using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace StudentValidation
{
    class Student
    {
        private String name;
        private int id;
        public Student(String name, int id)
        {
            Name = name;
            RollNo = id;
        }
        public String Name
        {
            get { return name; }
            set
            {
                if (value == "")
                {
                    Console.WriteLine("Name cannot be empty");
                }
                name = value;
            }
        }
        public int RollNo
        {
            get { return id; }
            set
            {
                if (value < 0)
                {
                    Console.WriteLine("RollNo cannot be negative");
                }
                id = value;
            }
        }

    }
}
