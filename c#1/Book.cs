using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{
    class Book
    {
        //default constuctor
        public Book() { }
        //constructor with title and author
        public Book(string title, string author)
        {
            Title = title;
            Author = author;
            
        }
        
        public string Title { get; set; }
        public string Author { get; set; }
        //constructor with title, author and ISBN
        public Book(string title, string author, string isbn)
        {
            Title = title;
            Author = author;
            ISBN = isbn;
        }
        public string ISBN { get; set; }

    }
}
