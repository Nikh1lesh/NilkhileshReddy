
namespace StudentValidation
{
    class Program
    {
        static void Main(string[] args)
        {
            //1.BankAccount
            //BankAccount b = new BankAccount(100, 1);
            //Console.WriteLine("Balance: " + b.Balance);

            //Console.WriteLine("Account number: " + b.AccountNumber);
            //b.Deposit(50);
            //Console.WriteLine("Current Balance: " + b.GetBalance());
            //b.Withdraw(30);
            //Console.WriteLine("Current Balance: " + b.GetBalance());

            //2. Student 
            //Student s = new Student("John", 1);
            //Console.WriteLine(s.Name);
            //Console.WriteLine(s.RollNo);
            //Student student = new Student("", 1);
            //Console.WriteLine(student.Name);
            //Console.WriteLine(student.RollNo);
            //Student student1 = new Student("John", -1);
            //Console.WriteLine(student1.Name);
            //Console.WriteLine(student1.RollNo);

            //3. Book
            //Book book = new Book();
            //Book book1 = new Book("Title", "author");
            //Book book2 = new Book("Title1", "author1", "isbn");
            //Console.WriteLine(book1.Title);
            //Console.WriteLine(book1.Author);
            //Console.WriteLine(book2.Title);
            //Console.WriteLine(book2.Author);
            //Console.WriteLine(book2.ISBN);

            //4. Shape
            //Circle circle = new Circle(5);
            //Console.WriteLine(circle.Area());
            //Rectangle rectangle = new Rectangle(5, 6);
            //Console.WriteLine(rectangle.Area());

            //5. Vehicle
            //Car car = new Car();
            //car.start();
            //Bike bike = new Bike();
            //bike.start();

            //6. Person
            //Student1 student = new Student1("John", 1);
            //student.getDetails();
            //Teacher teacher = new Teacher("Tom", "Maths");
            //teacher.getDetails();

            //7. Calculator
            //Calculator calculator = new Calculator();
            //Console.WriteLine(calculator.Add(1, 2));
            //Console.WriteLine(calculator.Add(1, 2, 3));
            //Console.WriteLine(calculator.Add(1.1, 2.2));

            //8. IPlayable Interface
            //MusicPlayer musicPlayer = new MusicPlayer();
            //musicPlayer.Play();
            //VideoPlayer videoPlayer = new VideoPlayer();
            //videoPlayer.Play();

            //9. IPrintable and ISerializable
            //Report report = new Report();
            //report.Print();
            //report.Serialize();

            //10. User
            //Admin admin = new Admin("Username", "Admin");
            //Console.WriteLine(admin.Username);
            //Console.WriteLine(admin.Role);
            //admin.AccessControl();
            //Customer customer = new Customer("Username1", "Customer");
            //Console.WriteLine(customer.Username);
            //Console.WriteLine(customer.Role);
            //customer.AccessControl();

            //11. ComplexNumbers operator overloading
            //ComplexNumbers c1 = new ComplexNumbers(1, 2);
            //ComplexNumbers c2 = new ComplexNumbers(3, 4);
            //ComplexNumbers c3 = c1 + c2;
            //Console.WriteLine(c3.Real);
            //Console.WriteLine(c3.Imaginary);

            //12. Manager Deep copy, shallow copy
            //Manager manager = new Manager("John");
            //Department department = new Department("HR", manager);
            //Department department1 = department;
            //Department department2 = new Department(department.Name, department.Manager);
            //Console.WriteLine(department1.Name);
            //Console.WriteLine(department1.Manager.Name);
            //Console.WriteLine(department2.Name);
            //Console.WriteLine(department2.Manager.Name);

            //13. Bank static method and static variable
            //static variables and static methods are used to share data among all objects of a class.

            //Bank bank = new Bank();
            //Console.WriteLine(Bank.InterestRate);
            //Bank.setInterestRate(5);


            //14. Sealed class securitySystem

            //16. Factory Pattern
            //VehicleFactory vehicleFactory = new VehicleFactory();
            //Console.WriteLine("Enter vehicle type: ");
            //string Vehicletype= Console.ReadLine();
            //Vehicle vehicle = vehicleFactory.GetVehicle(Vehicletype);
            //vehicle.start();

            //17. Decorator Pattern
            //FileLogger fileLogger = new FileLogger();
            //fileLogger.Log("MyMessage");
            //fileLogger.timeStamp();
            //fileLogger.errorCategorization();



        }
    }
    
}