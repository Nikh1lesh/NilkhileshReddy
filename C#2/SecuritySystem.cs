using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPSAssignment2
{
    sealed class SecuritySystem
    {
        public void AuthenticateUser()
        {
            Console.WriteLine("User Authenticated");
        }
    }
    
    //public class SecuritySystemProxy : SecuritySystem
    //{
    //    private SecuritySystem securitySystem;
    //    public void AuthenticateUser()
    //    {
    //        if (securitySystem == null)
    //        {
    //            securitySystem = new SecuritySystem();
    //        }
    //        securitySystem.AuthenticateUser();
    //    }
    //}
}
