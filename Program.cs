using static Home;
using System;
 namespace  some
{
    class cat
    {

static void main()
{   
     while ( true )//setup a  while   true  loop
    {

    var input = ReadLine(); // take in input 
    
    switch(input)
    {
        case "hello":
            Print("hey there!");
            break;
        case "goodbye":
            Print("goodbye");
            break;
        default:
            Print("invalid option");
            break;

    }
     return ;
    }
}

main(); //call main  foreach  now
    }}