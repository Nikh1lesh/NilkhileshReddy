using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    class Manager
    {
        public Manager(string Name)
        {
            this.Name = Name;
        }
        public string Name { get; set; }
    }
    class Department
    {
        public Department(string Name, Manager Manager)
        {
            this.Name = Name;
            this.Manager = Manager;
        }
        public string Name { get; set; }
        public Manager Manager { get; set; }

    }

}
