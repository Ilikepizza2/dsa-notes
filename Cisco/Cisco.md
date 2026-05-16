- Intuit

    Turbotax

    Mailchimp

    Creditkarma

    Mint

    Quickbooks - shut down in india

    CEO - Sasan Goodarzi

    95% revenue from US. One of the best workplaces to work for.

    Intuit assist - generative ai financial assistant for all the above products.

- Cisco

    1. AI based fault detection and fault recovery of firewall instances. Extracted usage metrics from logs and fed to fuzzy inference systems to analyze probability of crashes and their reason. Stored crash debug logs(lina (ASA) and snort(FTD)) and then when similar crashes occurred, used vector search to suggest related crashes and how they recovered. Developed and deployed a vector and a static db on the internal cloud using linux.

    1. Developed Fuzzy Inference System for crash predictions.

    1. Created release tracking website to automate processes and reduce manual workloads across 5 teams (across multiple directors)

    1. Created a dashboard to analyze and filter malicious traffic from ftd and fmc devices

    1. Was working on a network limiter on wan devices to enhance testing for worse scenarios.

    Spring:

    1. Created an interface for mass traffic generator.

    1. Created an AI based tool to read a protocol specification document(400 pages), create a knowledge base, create tests based on that, execute them and relate the results with the knowledge base, based on those results create an AI generated dashboard with graphs and tables for analysis and compliance report. Then based on failing cases, generate scripts for validation and patch creation for the firewall. All this on proprietary data and codebase, nothing available on chatgpt or any LLM.

I’m a final year IT undergraduate at IIIT Lucknow. This summer, I interned

wmctrl -r :SELECT: -b add,skip_taskbar

- HR and projects

    - HR

        1. What’s your greatest weaknesses

            1. Less experience so, can misjudge deadlines → Trying to get as much experience as I can (intern and contract work)

            1. Takes on more work than can handle → Slowly trying to focus on one thing at a time.

        

        Strengths -

        1. Leadership - Foss wing lead and Team management in several projects.

        2. Flexibility - Different tech stacks, different environments, different teams, different time zones, different countries.  

        Problem faced and how you overcame that.

        A significant risk I took involved guiding a client through a difficult situation where they faced potential financial and relational setbacks due to a delayed project. Despite the risk of jeopardizing my freelancing license on Fiverr, I chose to confront the issue openly rather than accepting the losses. The project was behind schedule because a developer on my team fell ill, which meant we couldn't meet the original deadline—right before the client’s critical funding round. He initially demanded a full refund, which could have seriously impacted both of us. To reach a solution, I committed 18-hour days, working on both the code and frequent discussions with him. Through relentless focus and transparency, we ultimately reached a compromise, delivering a simplified MVP that allowed him to secure an extended timeline from his investors.

        This experience taught me the value of integrity, resilience, and commitment to finding solutions, even under pressure. It reflects my determination to put clients' best interests first, communicate transparently, and take ownership of challenges, qualities I believe define my professional character.

          
        Why should we hire you?

        Previous intern - so experience. Expert competitive programmer so problem solving. Strength(). Therefore I stand out from the crowd.

          
        What do you expect from this intern?

        Since I have worked at an startup, mai thoda sa ab impactful projects pe kaam krna chahunga. Intuit has experienced pepol and I would like to learnt from them. chatai chatai. LEARN KRNA CHAHUNGA.

    
    - Projects

        - Chatlect

            Aim: To be what [perplexity.ai](http://perplexity.ai) is now. It was started as a passion project between me and an old internet friend. One more friend joined in. To increase the model’s capabilities by getting it access to the internet like google search and pasting url would go through the website and pdf upload. Purely educational chatbot.

              

            What made it unique: When the work was started, it was the most unique thing, just competing to be the first of it’s kind. Jan → chatgpt released. March 14 → gpt4 api released for select users. Work started Apr. No tutorials available. The vector database used also had no documentation just the api reference. One scroll and it’s over. Used serverless functions for compute for theoretically infinite horizontal scalability. Later, slowly tutorials started emerging, I saw things that I implemented were actually correct and industry standards.

              

            Team: One college friend → a few frontend pages and blog to market it, One online friend → gave aws access and put in money for that. Bought the gpt api. Did some devops. Lobbied very hard to microsoft so that we may get azure assistance for the openai api and compute resources. Managed to find someone who would buy the project in the end.

              

            - Technology:

                - Completely on AWS.

                    1. AWS EC2 → self hosted vector database, main chatlect website and the blog (used subdomains ;) ).

                    1. AWS DynamoDB as static database → NoSQL so flexibility + scaling. Why only dynamoDB and not any other nosql → it handles hot partitions automatically earlier it didn't.

                    1. AWS Cloudwatch: for lambda

                    1. AWS Lambda → used to offload api calls to a serverless function. This function could scale horizontally infinitely. Faced a few problems though with the cloudflare api gateway. And low time limit. (later increased to 15 mins)

                    1. AWS S3 for pdf parsing

                
                - Vector database used was chroma → Kind of wrong decision because this was heavy and so costly. Used the openAI embedding generator to generate embeddings. In one chroma document, I pushed the embedding along with the associated text plus some metadata. This metadata contained the sources so, we could make the ai explainable.

                - Used cheerio to scrape google and other websites. Google is very hard to scrape so used ada to clean it (`Ada` is usually the fastest  
                    model and least costly. It's best for less nuanced tasks—for example,  
                    parsing text, reformatting text, and simpler classification tasks.) But it also increased some time so at last, settled on SerpAPI.

                - NextJS and it’s api routes → no backend lol. Somewhat bad design but it’s okay for small project. Allowed to select model on the go from gpt-3.5 or gpt-4.

                - Langchain → used as wrapper for openai api and used this to summarize chat history for prompt injection.

            

            
            Reception: What started off as a passion project, the friend got one company to buy it for very less for today’s standard but still a lot for me as a college student → 1 lakh inr. Coursessor (now capitalmerce) was a very early age startup. Later, I went on to hold an equity there but now I’m out.

              

            What did you learn: This project fueled me to start learning deep learning. Taught me the basics of what drives a product. Learned to work even with less documentation - gained some confidence that I can work on a lot of things that I don’t know given enough time and resources, learned to not care about the money/time to make something that I am proud of. Learned about design patterns, optimizations and various things in ai like vectors, basics of nlp, embedding search algorithms and multi model(not modal) architecture in ai.

              

            Why it failed: When we started, the first thing we struggled with was the long time the responses took. Until we could finish the basic requirements, we couldn’t start with the optimizations. The gpt-4 api(at that time limited to 8k tokens) itself took a lot of time to give response. This biased the initial feedback which I took from my peers towards this only that I couldn’t get feedback on the things I was doing. Later on when we optimized it, we waited for a few more features(pdf upload) before launching it. In that time only, perplexity gained investors and bard launched in may.

        

- Books

    CN - tannenbaum

- OOPs

    - Interview definitions

        - Class

            A class can be understood as a template or a blueprint, which contains some values, known as member data or member, and some set of rules, known as behaviors or functions. It doesn’t consume space. eg, car

        
        - Objects

            An object refers to the instance of the class, which contains the instance of the members and behaviors defined in the class template.

            In the real world, an object is an actual entity to which a user interacts, whereas class is just the blueprint for that object. So the objects consume space and have some characteristic behavior. eg, ford car

        
        - Encapsulation

            Process of binding data members and methods of a program together to do a specific job, without revealing unnecessary details.

            eg, capsule, which contains medicinal materials within it

            Encapsulation can also be defined in two different ways:

            1) **Data hiding:** Encapsulation is the process of hiding unwanted information, such as restricting access to any member of an object.

            2) **Data binding:** Encapsulation is the process of binding the data members and the methods together as a whole, as a class.

        
        - Polymorphism

            In OOPs, Polymorphism refers to the process by which some code, data, method, or object behaves differently under different circumstances or contexts. Compile-time polymorphism and Run time polymorphism.

            eg, a person can be a father, a husband, and an employee, all at the same time, and they will act differently in each of these roles

        
        - Inheritance

            Inheritance is the mechanism by which an object or class (referred to as a child) is created using the definition of another object or class (referred to as a parent). Inheritance not only helps to keep the implementation simpler but also helps to  
            facilitate code reuse.

        
        - Abstraction

            Abstraction is the method of hiding unnecessary details from the necessary ones.

            eg, You only need to know how to run a car, and not how the wires are connected inside it

            ![[1000130157.jpg]]

        
        - Constructors

            Used to initialize object variables and sepicify space for them

            Types:

            1. Default constructor: The default constructor is the constructor which doesn’t take any argument. It has no parameters.

            1. Parameterized constructor: The constructors that take some arguments are known as parameterized constructors

            1. Copy constructor: A copy constructor is a member function that initializes an object using another object of the same class.

        
        - Destructors

            Destructors free up the resources and memory occupied by an object. Destructors are automatically called when an object is being destroyed.

        
        - Garbage collection

        - JVM

            The Java source code first compiled into a binary byte code using Java compiler, then this byte code runs on the JVM (Java Virtual Machine), which is a software based interpreter. So Java is considered as both interpreted and compiled.

        
        - Structs vs class

            Instances of structs called structure variable while classes have objects.

            classes used for data abstraction and further inheritance. structs for grouping of data.

            the structure is saved in the stack memory, whereas the class is saved in the heap memory.

        
        - Abstract classes

            The significance of abstract class is that the abstract methods inside it are not implemented and only declared. So as a result, when a subclass inherits the abstract class and needs to use its abstract methods, they need to define and implement them.

        
        - Access specifiers

            Access specifiers, as the name suggests, are a special type of keywords, which are used to control or specify the accessibility of entities like classes, methods, etc. Some of the access specifiers or access modifiers include “private”, “public”, etc. These access specifiers also play a very vital role in achieving Encapsulation - one  
            of the major features of OOPs.

        
        - Exceptions

            Finally block: Note: The finally block will not be executed if the program exits (either by calling System.exit() or by causing a fatal error that causes the process to abort otherwise it is executed even when control statements like return is present in the try block.

            It is executed after try block if no exception occurs otherwise, it is executed after catch block.

              

            Throws keyword: Checked exception can be propagated with throws. Throws is followed by class.

            We can use throws to declare multiple exceptions. It is used to throw checked exceptions like IOException, InterruptedException, etc.

            Throw Keyword: Checked exception cannot be propagated using throw only. Throw is followed by an instance

            It is used to throw unchecked exceptions like ArithmeticException, NullPointerException, ArrayIndexOutOfBoundsException.

        
        - Threads

            Can be implemented using two ways:

            1. By extending java.lang.Thread class. This way you won't be able to extend any other class.

            1. By implementing the Runnable interface. This way you are able to extend any other class.

            Thread LifeCycle -

            1. New: Instance of thread created which is not yet started by involving start(). In this state, the thread is also known as the born thread.

            1. Runnable - After invocation of start() & before it is selected to be run by the scheduler.

            1. Running - After the thread scheduler has selected it.

            1. Non runnable - thread alive and not eligible to run.

            1. Terminated - run() method has exited.

            Methods: getPriority() and setPriority()

              

            - Ways to achieve synchronization:

                - Synchronized method

                    Synchronized method is used to lock an object for any shared resource.

                
                - Synchronized block

                    Synchronized block can be used to perform synchronization on any specific resource of the method. Suppose we have 50 lines of code in our method, but we want to synchronize only 5 lines, in such cases, we can use synchronized block.  
                    If we put all the codes of the method in the synchronized block, it will work same as the synchronized method.

                
                - Static synchronization

                    When there are more objects of a class, It acquires only the lock of the particular instance. To maintain the synchronized behavior, we need a class-level lock rather than an instance level lock which can be achieved by static synchronization.

                

        
        - Interpretation and compilation

            Source code first converted into Byte code using compilation. Then JVM “interprets” this byte code. Last part of JVM is JIT (just in time) compiler which converts bytecode into machine code so hardware itself can execute the native code as opposed to JVM interpret it so it is v fast.

              

            But due to this long process, the execution is slower than C++ which is just compiled

        

        

    1. Static → compile time, constructor → when object created. Another parent instance variable (which sometimes points to parent object but what if it is abstract class??) created with each child class object creation and is accessible through super(). It just refers to the super class things inherited by child class. Super is like surname of a child - it doesn't affect parent.

    1. object is created when we allocate space using new keyword. Constructor needed to initialize the object.

    1. Reflection is a feature in the Java programming language. It allows an executing Java program to examine or "introspect" upon itself, and manipulate internal properties of the program. For example, it's possible for a Java class to obtain the names of all its members and display them.

    1. You can access the parent class method which is over ridden using super.method(). If a constructor does not explicitly invoke a superclass constructor, the Java compiler automatically inserts a call to the no-argument constructor of the superclass. If a subclass constructor invokes a constructor of its superclass, either explicitly or implicitly, you might think that a whole chain of constructors is called, all the way back to the constructor of Object. This, in fact, is the case. It is called _[constructor chaining](https://www.geeksforgeeks.org/constructor-chaining-java-examples/)._

    1. Shallow copy, deep copy

    1. Abstract classes cannot be instantiated. Also their is no need for them to contain abstract methods

    1. in the signature of the `public static void main(String[] args)` method—this special instance named 'args', often referred to simply as 'command line arguments,' captures external runtime information provided upon executing a Java program.

    1. Java doesn’t support operator overloading except for string1+string2. No support is by design since it aims to be simple and easy to understand.

    1. This and super refer to the instance variable and not the object

    ![[prep/DSA Notes/Private & Shared/Untitled.png]]

    1. Static blocks executed before constructors

    1. In the `main` function of Java, if you attempt to call a non-static method on an object of another class, you must first instantiate an object of that class before invoking the non-static method. This is because non-static methods are associated with instances of classes, while static methods operate independently of instances.

    1. Static methods can be extended(like of a static class) but not overriden. they are stored in heap memory. They can be overloaded though.

    1. Heap memory(like static shit) isn’t thread safe as it is accessible to all threads.

        |   |   |
        |---|---|
        |STACK|HEAP|
        |Memory is allocated in a contiguous block.|Memory is allocated in any random order.|
        |Stores reference to object|Stores object|
        |**methods, variables,** and **reference variables** of the objects.|static shit|

    
    1. singleton classes ⇒ classes which create only one object. You declare constructor private so others can’t create new object, only you can. Use static object instance variable to keep track of the instance. (you can use object==null for this)

        - code

            ```java
            class Singleton{
                private static Singleton obj = null;
                private Singleton(){
                    // private constructor
                }
                public static Singleton getInstance(){
                    if(obj == null) return obj = new Singleton();
                    else return obj;
                }
            }

            class HelloWorld {
                public static void main(String[] args) {
                    Singleton obj1 = Singleton.getInstance();
                    Singleton obj2 = Singleton.getInstance();
                    Singleton obj3 = Singleton.getInstance();
                    System.out.println(obj1);
                    System.out.println(obj2);
                    System.out.println(obj3);
                }
            }
            ```

        

    1. @override ← is an annotation(implemented using interfaces). These are used so that we get errors/warnings for illegal overrides. Without it, let’s say, we try to override a static method, we won’t get any warning but the parent method will only get executed and not the child one. This may cause logical errors.

    1. Static/compile time(early binding) polymorphism → overloading, runtime(late binding) polymorphism → overriding(resolved by Dynamic Method Dispatch).

    1. Call to constructor using `this/super` in another constructor must be the first statement

    1. public static void main & static public void main same

    1. Upcasting: Parent obj = new Child(); ← weird shit see [https://www.geeksforgeeks.org/upcasting-in-java-with-examples/](https://www.geeksforgeeks.org/upcasting-in-java-with-examples/)

        - see below

            ```java
            class par{
                int numover = 1;
                int num1=0;
                void fn1(){
                    System.out.print("fn1\n");
                }
                void over(){
                    System.out.print("over: par\n");
                }
            }

            class child extends par{
                int num2=0;
                int numover = 2;
                void fn2(){
                    System.out.print("fn2\n");
                }
                @Override
                void over(){
                    System.out.print("over: child\n");
                }
            }

            class HelloWorld {
                public static void main(String[] args) {
                    child obj = new child();
                    obj.fn1(); // fn1
                    obj.fn2(); // fn2
                    obj.over(); // child
                    System.out.println(obj.numover); // 2
                    System.out.println(obj.num1); // 0

                    
                    par obj2 = new child();
                    obj2.fn1(); // fn1
                    // obj2.fn2(); // error !!!
                    obj2.over(); // child !!!
                    System.out.println(obj2.numover); // 1 !!!!
                    System.out.println(obj2.num1); // 0 

                    // child obj3 = new par(); // error
                }
            }
            ```

        

    1. if main is not static, no function loaded into memory at compile time so the JVM thinks main function not present.

    1. a. blank final variable can be initialized inside an instance-initializer block or inside the  
        constructor. If you have more than one constructor in your class then it must be  
        initialized in all of them, otherwise, a compile-time error will be thrown. You cannot use both constructor and instance initializer block otherwise error that you reinitialize the variable in constructor after the block.  
        b. A blank final static variable can be initialized inside a static block and not in constructor.

    1. Final uses: Usage 1: One is definitely to prevent inheritance, as final classes cannot be extended. Implicitly, all its methods become final too. For eg all Wrapper Classes like Integer, Float, etc. are final classes. We can not extend them. Usage 2: The other use of final with classes is to create an immutable class like the predefined String class. One can not make a class immutable without making it final. Usage 3: Final functions cannot be overridden(forced early binding)

    1. it seems that instance initializer block is firstly invoked but NO. Instance initializer block is invoked at the time of object creation. The java compiler copies the instance initializer block in the constructor after the first statement super(). So firstly, constructor is invoked.

    1. Interface and abstract classes

        ● both abstract classes and interfaces cannot be used to create objects. But abstract classes can be used as reference data type so you can use super() to call it’s constructor  
        ● Interface methods do not have a body - the body is provided by the class that implements it

        ● Interface cannot have constructors while abstract classes can.

        ● Constructors, static methods can’t be abstract. Although you can have a static method in abstract class just like normal classes

        ● On implementation of an interface, you must override all of its methods

        ● An abstract class is not required to have an abstract method in it. But you must override all its abstract methods.  
        ● Interface methods are by default abstract and public

        ● Declare that Child class as abstract so that the next level Child class should provide implementation to the remaining abstract method

        ● Interface attributes are by default public, static and final  
        ● An interface cannot contain a constructor

        ● Interfaces used to achieve multiple inheritance(aise illegal h java me),total abstraction and loose coupling (one interface reference variable having the capability to hold  
        the multiple implementation classes memory).

    
    1. Reading methods

        ● BufferedReader in java.io

        ● Scanner in java.util

        ● reading methods are not synchronized

        ● BufferedReader should be used if we are working with multiple threads.

    
    1. Generic classes → Template classes in C++, Wrapper classes → Integer, Float, etc.

        - Autoboxing and Unboxing

            ```java
            int primitiveInt = 10;
            Integer wrapperInt = primitiveInt; // Autoboxing

            System.out.println("Wrapper Integer: " + wrapperInt);

            // Unboxing: Integer to int
            Integer wrapperInt2 = new Integer(20);
            int primitiveInt2 = wrapperInt2; // Unboxing

            System.out.println("Primitive int: " + primitiveInt2);
            ```

        

    1. Finally executed even if try contains return statement. Only system.exit() ke case me nahi hoga. It executed even if the catch block doesn’t handle the exception occured.

    1. Threads are independent. If there occurs exception in one thread, it doesn't affect other  
        threads.  
        ● It uses a shared memory area. **static variables are always shared by all the threads in the process**  
        ● Note:  
        ○ At a time one thread is executed only.

    - Nested classes

        - Inner classes.

            They can access their parent’s private members but we have to create object twice (once of the parent class and then the child class)

            ```java
            // Online Java Compiler
            // Use this editor to write, compile and run your Java code online

            class Outer{
                int a=5;
                private void par(){
                    System.out.println("Outer class function");
                }
                class Inner{
                    int b = 5;
                    void child(){
                        par();
                        System.out.println("Inner class function");
                    }
                }
            }

            class HelloWorld {
                public static void main(String[] args) {
                    Outer.Inner in = (new Outer()).new Inner();
                    // obj2.par(); ERROR!!!
                    in.child();
                }
            }
            ```

        
        - Static classes

            ```java
            // Online Java Compiler
            // Use this editor to write, compile and run your Java code online

            class Outer{
                int a=5;
                private static void par(){
                    System.out.println("Outer class function");
                }
                static class Inner{
                    int b = 5;
                    static void child(){
                        lol();
                        System.out.println("Inner class function");
                    }
                }
            }

            class HelloWorld {
                public static void main(String[] args) {
                    // Outer.par();
                    // Outer.Inner.par();
                    //  ERROR!!!

                    

                    Outer.Inner.child();
                }
            }
            ```

        
        - Method local inner classes

        - Anonymous inner classes

    
    1. Threads, exceptions are in java.lang

    1. Java synchronized block is more efficient than Java synchronized method.

    1. throws is a keyword in Java that is used in the signature of a method to indicate the compiler that this method might throw one of the listed type exceptions. The caller can either handle it using try catch or propagate upward the call stack. Once it reaches main and it is not handled and yet an exception occurs, it crashes the program. If the exception doesn’t occur, there’s not a problem.

    - Checked vs unchecked exceptions

        Checked:

        These are the exceptions that are checked at compile time. If some code within a method throws a checked exception, then the method must either handle the exception or it must specify the exception using the _[throws](https://www.geeksforgeeks.org/throw-throws-java/)_ [keyword](https://www.geeksforgeeks.org/throw-throws-java/).  
        In checked exceptions, there are two types: fully checked and partially checked exceptions. A fully checked exception is a checked exception where all its child classes are also checked, like IOException, and InterruptedException. A partially checked exception is a checked exception where some of its child classes are unchecked, like an  
        Exception.

        Unchecked:

        These are the exceptions that are not checked at compile time. In C++, all exceptions are unchecked, so it is not forced by the compiler’s to either handle or specify the exception. It is up to the programmers to be civilized and specify or catch the exceptions. In Java, exceptions under _Error_ and _RuntimeException_ classes are unchecked exceptions, everything else under throwable is checked. 

    
    1. finalize() method that is called by the garbage collector on an object when garbage collection determines that there are no more references to the object. This method is used for cleanup operations before an object is garbage collected.

    1. ● The non-static nested classes are also known as inner classes.  
        ● In the Java programming language, you can not make a top-level class static. You can only make nested classes either static or non-static.  
        ● Top-level classes can not be declared as private or protected.

    1. In c++, array created in stack and vector in heap. stack memory much smaller than heap so array can only go upto 1e6 while vector upto 1e7

    1. Virtual functions like abstract functions. Friend functions can access private variables without inheriting them.

- OS

    - Threads

        - Thread is an independent path of execution in a process. It’s like a lightweight process. Threads of the same process share memory space and resources, including the code section, data section, heap, and global variables. They also share the same address space, which means they can communicate with each other more easily than processes can. However, threads do not share their stack, which is used for local and temporary variables as well as return addresses. Each thread has its own program counter though.

        - If a user level thread gets blocked all peer threads get blocked. If one kernel level thread gets blocked, another thread can continue. If one process gets blocked, others can continue.

        - Main use of thread: responsiveness(mouse, keyboard and applications working simultaneously). Even in a single cpu system, this gives concurrency(time slicing). Total time will not be less if not a bit more.

        - If no blocking thread present, number of threads = number of cores give best performance, otherwise there’s a limit which increase performance, after which it decreases again. [https://stackoverflow.com/questions/1718465/optimal-number-of-threads-per-core](https://stackoverflow.com/questions/1718465/optimal-number-of-threads-per-core)

        - Difference between context switching of thread and process

            |   |   |
            |---|---|
            |Thread Context switching|Process context switching|
            |OS saves current state of thread & switches to another thread of same process.|OS saves current state of process & switches to another process by restoring its state|
            |Fast switching|Slow switching|
            |CPU’s cache state is preserved.|CPU’s cache state is flushed.|
            |Doesn’t includes switching of memory address space. (But Program counter, registers & stack are included)|Includes switching of memory address space.|

        

    - Fork and exec

        - Fork

            Creates a new child process. Returns 0 → child, (+ve)→ parent, (-ve) → error in creating child process.

            creates (2^n)-1 child processes and 1 parent process.

            So

            ```cpp
            main(){
            	fork();
            	fork();
            	cout << "hello\n";
            }

            // output: 4 times hello
            ```

              

            ![[prep/DSA Notes/Private & Shared/Untitled 1.png]]

        
        - exec or execv

            The `execv` system call is a functionality of an operating system that runs an executable file in the context of an already existing process, replacing the previous executable.

            It executes the first program normally until it encounters the execv call. After that, it executes the second program.

        

    - Questions

        - PCB and process states

            Process Control Block(PCB) is a data structure to store all information about a process

            Process states: new, running, ready, blocked, suspend ready, suspend blocked, terminated.

            Thread states: running, ready and blocked

        
        - Mutex vs binary semaphore

            |Mutex|Binary semaphore|
            |---|---|
            |locking mechanism|signalling mechanism|
            |cannot be used as semaphore|can be used as mutex|

        
        - System calls

            System call is a mechanism used by user programs to request services from the OS kernel. It is an interface between user level processes and OS.

        
        - Demand paging

            Keep all pages of frames in secondary memory until they are required. Do not load any page in main memory until required.

        
        - Virtual memory

            Virtual memory is a storage allocation scheme in which secondary memory can be addressed as though it were part of the main memory.

        
        - Multiprogramming vs Multitasking vs multithreading vs multiprocessing

            1. **Multiprogramming –** Multiprogramming is known as keeping multiple programs in the main memory at the same time ready for execution.

            1. **Multiprocessing –** A computer using more than one CPU at a time.

            1. **Multitasking –** Multitasking is nothing but multiprogramming with a Round-robin scheduling algorithm.

            1. **Multithreading** is an extension of multitasking.

            ![[prep/DSA Notes/Private & Shared/Untitled 2.png]]

        
        - Spatial locality vs temporal locality

            Spatial: instructions stored near recently executed instruction have high chances of execution

            Temporal: instructions which are recently executed have high chances of execution again

        
        - IPC

            **Different IPC Mechanisms:**

            1. Pipes

            1. Message Queuing

            1. Semaphores

            1. Socket

            1. Shared Memory

            1. Signals

        
        - Overlays

            Unlike pure segmentation and paging approaches, overlays aim specifically to accommodate executables surpassing the capacity of physically installed memory. It does not need any type of support from the OS.

            It can run programs that are bigger in size than physical memory by only keeping only important data and instructions that can be needed at any given time.

        
        - Re-entrency

            Reentrant is simply a function in which various clients can use and shares a single copy of a program during a similar period. This concept is generally associated with OS code and does not deal with concurrency

        
        - Asymmetric clustering

            Asymmetric Clustering is generally a system in which one of the nodes among all nodes is in hot standby mode whereas the rest of all nodes run different applications. It simply uses whole or entire hardware resources therefore it is considered a more reliable system as compared to others.

        
        - Cascading termination

            Cascading termination is a process termination in which if the parent process is exiting or terminating then the children process will also get terminated. It does not allow the child to continue processing as its parent process terminates. It is generally initiated by OS.

        
        - Kernel

            The kernel is basically a computer program usually considered as a central component or module of OS. It is responsible for handling, managing, and controlling all operations of computer systems and hardware. Whenever the system starts, the kernel is loaded first and remains in the main memory. It also acts as an interface between user applications and hardware.

        
        - Time sharing system

            It is a system that allows more than one user to access the resources of a particular system in many locations. In simple words, it performs multiple tasks on a single processor or CPU. As the name suggests, it means to share time into multiple slots in several processes. It also allows different users from different locations to use a particular computer system at the same time therefore it is considered one of the important types of OS.

        
        - Process

            ![[prep/DSA Notes/Private & Shared/Untitled 3.png]]

        
        - Spooling

            Spooling simply stands for Simultaneous peripheral operations online. It is referred to as putting data of various I/O jobs in a buffer. Here, buffer means a special area in memory or hard disk that can be accessible to an I/O device. It is used for mediation between a computer application and a slow peripheral. It is very useful and important because devices access or acquire data at different rates. This operation also uses disk as a very large buffer and is capable of overlapping I/O operations for one task with processor operations for another task.

        

    - Process

        - Schedulers

            1. **Long-term – performance:** Decides how many processes should be made to stay in the ready state. This decides the degree of multiprogramming. Once a decision is taken it lasts for a long time which also indicates that it runs infrequently.  
                Hence it is called a long-term scheduler.

            1. **Short-term – Context switching time:** Short-term scheduler will decide which process is to be executed next and then it will call the dispatcher. A dispatcher is a software that moves the process from ready to run and vice versa. In other words, it is context switching. It runs frequently. Short-term scheduler is also called CPU  
                scheduler.

            1. **Medium-term – Swapping time:** Suspension decision is taken by the medium-term scheduler. The medium-term scheduler is used for [swapping](https://www.geeksforgeeks.org/swapping-in-operating-system/) which is moving the process from main memory to secondary and vice versa. The swapping is done to reduce degree of multiprogramming.

        
        - Orphan process

            Their parents are dead 😟. But they are adopted by init process. Init is the first process of OS

        
        - Process and PCB structure

            ![[prep/DSA Notes/Private & Shared/Untitled 4.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 5.png]]

            Process table is an array of PCB. It maps Pid with its pcb

        
        - Zombie process

            1. A zombie process is a process whose execution is completed but it still has an entry in the process table.

            1. Zombie processes usually occur for child processes, as the parent process still needs to read its child’s exit status. Once this is done using the wait system call, the zombie process is eliminated from the process table. This is known as reaping the zombie process.

            1. It is because parent process may call wait () on child process for a longer time duration and child process got terminated much earlier.

        

    - Critical section/synchronization

        - Conditions for synchronization (good)

            1. Mutual Exclusion

            1. Progress

            1. Bounded wait

            1. No assumptions related to hardware speed

        
        - Busy waiting dekh lo

        - Solutions

            1. Lock variable: if preempted after while loop, then mutual exclusion doesn’t hold

            1. Test and Set instruction: solves lock variable by combining test and set statements into single indivisible instruction.

            1. Turn variable: solves mutual exclusion but progress doesn’t hold

            1. Semaphores: (P, down, wait) (V, up, signal). Counting semaphores can allow multiple processes in critical section. (as many as we predefine)

            1. Mutex: They are like binary semaphores. Only allow one process in critical section

        

    - Deadlock

        Definition - _A **deadlock**_ is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.

        - Livelock

            Livelock is a situation in operating systems where multiple processes repeatedly perform the same interaction in reaction to changes in the other processes without performing any useful work, preventing them from completing the task. It is similar to deadlock, but all processes are running simultaneously and not in a waiting state.

        
        - Conditions for deadlock

            1. Mutual Exclusion

            1. Hold and wait

            1. No preemption

            1. Circular wait

        
        - Deadlock break

            1. Deadlock ignorance(ostrich): both windows and unix

            1. deadlock prevention: by eliminating any one of the 4 causes of deadlock

            1. deadlock avoidance: Resource allocation graph and banker’s algo

            1. deadlock recovery: choosing victim process and killing it.

        

    - Memory Management

        - Partitioning

            - Contiguous

                |Fixed size partitioning|Variable size partitioning|
                |---|---|
                |Internal Fragmentation|No internal fragmentation|
                |less degree of multiprogramming|high multiprogramming|
                |External Fragmentation|External fragmentation here too.  <br>But can be solved through compaction(undesirable)|

                In case of variable size partitioning, once any process de-allocates from RAM, holes are created(which cause external fragmentation btw). To fill these holes with new processes, we can use best fit, worst fit, first fit (from start), next fit(after last allocated hole).

            
            - Non contiguous

                - Paging

                    - Intro

                        - solves external fragmentation. Thodi thodi hi hoti (usually ignored)

                        - process divided into pages. Main memory divided into frames.

                            Obv, page size = frame size

                        
                        - Each process has its own page table

                        - Logical address to physical address resolution done by memory management unit (MMU)

                        - Cpu deals with logical address. logical address = page number + page offset

                        - main memory with physical address. physical address = frame number + frame offset(size).

                        - Total physical address size = min. bits to represent size of main memory

                        - page table entry

                            |   |   |   |   |   |   |
                            |---|---|---|---|---|---|
                            |frame number|valid bit|protection(r/w/x)|reference|caching|dirty|

                        
                        - multi level page table used if the size of page table>size of single frame

                          

                    
                    - Inverted page table

                        Because each process had its own page table, inverted page table was introduced where it was stored that each frame of main memory stored which frame. So the number of entries only equal to the number of frames.

                        Since we can’t look up a page directly, to search for a page, we have to search linearly. So increased lookup time. Each entry of inverted page table contained the page number and its process id.

                          

                    
                    - Thrashing

                        When we keep increasing the number of processes in main memory by only keeping a few pages in RAM i.e. increase multiprogramming, at one point, while executing a process, a lot of time is wasted in servicing the pages which aren’t present in memory. So, the cpu utilization decreases.

                        How to solve?

                        1. Increase ram size

                        1. ask long term scheduler to decrease degree of multiprogramming.

                    
                    - Virtual memory

                        To give the ability to processes with size greater than the size of main memory to execute, we use paging.

                        It has all the pages, so required page + nearby pages are also serviced into the main memory. So the big process is divided into pages to execute in small main memory. That is why hard disk reserves some portion to act as virtual memory.

                    
                    - Translation lookaside buffer(TLB).

                        We use a seperate fast cache like storage to keep a few pages in tlb memory. In case of tlb hit, we directly get the physical address. In case of tlb miss, we have to go through the normal page table to get the physical address of the frame in main memory.

                    

                - Segmentation

                    Instead of dividing process blindly into pages, we segment the process into logical units like one segment for main(), one for recur() etc. This can only be done in small fixed programs. So, used mostly in embedded systems.

                    Each entry in segment table has

                    |Base address|offset|
                    |---|---|

                
                - Segmented paging

                    Segmented paging is a memory management technique that combines the benefits of segmentation and paging. In this approach, the main memory is divided into variable-sized segments, which are further divided into fixed-sized pages.

                    Each segment has a segment table that points to the page table of the segment, and the page table contains the physical addresses of the page frames.

                    Used in modern operating systems

                
                - Page replacement algos

                    1. FIFO: (Belody’s anamoly : 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5)

                    1. Optimal page replacement (replace the page whose nearest page in the future occurs last)

                    1. Most recently used

                    1. Least recently used

                

            - Fragmentation

                - Contiguous fixed size → internal and external

                - Contiguous variable size → external only

                - Paging → External hota h but very thoda. Usually ignored. Internal bhi very thoda hota since padding.

            

    
    - Diks scheduling

        - Diks architecture

            ![[prep/DSA Notes/Private & Shared/Untitled 6.png]]

        
        - Formulas

            - Seek time: time taken by w/r head to reach track

            - Rotational time: time taken for full rotation

            - Rotational latency: Time taken to reach desired sector(half of rotational time)

            $$transferRate = totalData/Speed = numHeads*TrackCapacity*numRotationsPerSecond$$

        
        - Scheduling algos

            - FCFS:

            - Shortest Seek Time First(SSTF)

            - Scan (elevator algorithm):

                ![[prep/DSA Notes/Private & Shared/Untitled 7.png]]

            
            - Look:

                ![[prep/DSA Notes/Private & Shared/Untitled 8.png]]

            
            - C-Scan:

                ![[prep/DSA Notes/Private & Shared/Untitled 9.png]]

            
            - C-Look:

                ![[prep/DSA Notes/Private & Shared/Untitled 10.png]]

            

    
    - File

        - Contiguous allocation

            ![[prep/DSA Notes/Private & Shared/Untitled 11.png]]

            One file stored contiguously. Different files can have gaps between them though.

        
        - Non Contiguous allocation

            - linked list implementation

                ![[prep/DSA Notes/Private & Shared/Untitled 12.png]]

                  

            
            - Indexed file allocation

                A index table(like index of book) is maintained which points to the file location on disk

                ![[prep/DSA Notes/Private & Shared/Untitled 13.png]]

            
            - Inode Unix structure

                Multilevel indexed files.

            

    
    - Linker and loader

        **1. [Linker](https://www.geeksforgeeks.org/linker/):** A linker is special program that combines the object files, generated by compiler/assembler and other pieces of code to originate an executable file has .exe extension. In the object file, linker searches and append all libraries needed for execution of file. It regulates the memory space that will hold the code from each module. It also merges two or more separate object programs and establishes link among them.

        **2. Loader:** It is special program that takes input of executable files from linker, loads it to main memory, and prepares this code for execution by computer. Loader allocates memory space to program. Even it settles down symbolic reference between objects. It is in charge of loading programs and libraries in operating system. The embedded computer systems don’t have loaders. In them, code is executed through ROM. There are following various loading schemes: 

    
    - Kernels

        **monolithic** kernel runs the entire operating system in kernel space, where user and kernel services share the same address space. This design leads to faster execution but increases the risk of system crashes if a component fails. Examples include Unix and Linux.

        **microkernel** separates user and kernel services into different address spaces, enhancing security and modularity. Although slower due to message passing, it offers better fault isolation. Operating systems like Mac OS X and Windows NT utilize microkernels.

        Macrokernel

        Exokernel

        ![[prep/DSA Notes/Private & Shared/Untitled 14.png]]

    
    - Interrupt vectors:

        Interrupt transfers control to the interrupt service routine generally, through the interrupt vector, which contains the addresses of all the service routines

    
    - DMA (direct memory access)

        Device controller transfers blocks of data from buffer storage directly to main memory without CPU intervention

    
    - Python codes for Synchronization problems

        `p.join()` method in threading is used to wait for a thread (in this case, a philosopher) to complete its execution before proceeding further in the main thread.

        - Producer consumer problem

            ```java
            import threading
            import time
            import random

            # Define a shared buffer
            BUFFER_SIZE = 5
            buffer = []
            mutex = threading.Semaphore(1)
            empty = threading.Semaphore(BUFFER_SIZE)
            full = threading.Semaphore(0)

            # Producer function
            def producer():
                while True:
                    item = random.randint(1, 100)
                    empty.acquire()  # Wait if buffer is full
                    mutex.acquire()  # Protect buffer
                    buffer.append(item)
                    print(f"Produced {item}. Buffer: {buffer}")
                    mutex.release()
                    full.release()   # Notify consumers
                    time.sleep(random.random())

            # Consumer function
            def consumer():
                while True:
                    full.acquire()   # Wait if buffer is empty
                    mutex.acquire()  # Protect buffer
                    item = buffer.pop(0)
                    print(f"Consumed {item}. Buffer: {buffer}")
                    mutex.release()
                    empty.release()  # Notify producers
                    time.sleep(random.random())

            # Create producer and consumer threads
            producer_thread = threading.Thread(target=producer)
            consumer_thread = threading.Thread(target=consumer)

            # Start threads
            producer_thread.start()
            consumer_thread.start()
            ```

        
        - Dining philosopher problem

            ```python
            import threading
            import time
            import random
            NUM_PHILOSOPHERS = 5

            class DiningPhilosophers:
                def __init__(self):
                    self.forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

                def get_forks(self, philosopher_id):
                    left_fork = philosopher_id
                    right_fork = (philosopher_id + 1) % NUM_PHILOSOPHERS

                    # Always pick up lower-indexed fork first to prevent deadlock
                    first_fork = min(left_fork, right_fork)
                    second_fork = max(left_fork, right_fork)

                    self.forks[first_fork].acquire()
                    self.forks[second_fork].acquire()
                    time.sleep(random.random())

                def put_forks(self, philosopher_id):
                    left_fork = philosopher_id
                    right_fork = (philosopher_id + 1) % NUM_PHILOSOPHERS

                    self.forks[left_fork].release()
                    self.forks[right_fork].release()
                    time.sleep(random.random())

            def philosopher(philosopher_id, dining):
                while True:
                    print(f'Philosopher {philosopher_id} is thinking.')

                    dining.get_forks(philosopher_id)
                    print(f'Philosopher {philosopher_id} has picked up forks and is eating.')

                    # Simulate eating
                    dining.put_forks(philosopher_id)
                    print(f'Philosopher {philosopher_id} has put down forks and finished eating.')

            if __name__ == "__main__":
                dining = DiningPhilosophers()
                philosophers = [threading.Thread(target=philosopher, args=(i, dining)) for i in range(NUM_PHILOSOPHERS)]

                for p in philosophers:
                    p.start()

                for p in philosophers:
                    p.join()
            ```

        
        - Reader writer problem

            R-R allowed, W-R R-W W-W not allowed.

            ```python
            import threading

            class ReaderWriter:
                def __init__(self):
                    self.mutex = threading.Semaphore(1)  # Controls access to rc (reader count) and db (database)
                    self.db = threading.Semaphore(1)  # Controls access to the database for writers
                    self.rc = 0  # Reader count

                def reader(self):
                    while True:
                        # Reader wants to enter
                        self.mutex.acquire()
                        self.rc += 1
                        if self.rc == 1:  # First reader
                            self.db.acquire()  # Lock the database to prevent writers
                        self.mutex.release() # in W-R conflict, if one reader already blocked, then it hasn't executed this code. So subsequent readers can't aquire lock

                        # Read from the database (simulated)
                        print(f'Reader reading. current readers: {self.rc}\n')
                        # Reader is done reading
                        self.mutex.acquire()
                        self.rc -= 1
                        if self.rc == 0:  # Last reader
                            self.db.release()  # Release the database lock
                        self.mutex.release()
                        print(f'Reader finished reading. current readers: {self.rc}\n')

                        

                def writer(self):
                    while True:
                        # Writer wants to enter
                        self.db.acquire()  # Lock the database to prevent readers and other writers

                        # Write to the database (simulated)
                        print(f'Writer writing, current num of readers: {self.rc}')

                        # Writer is done writing
                        self.db.release()  # Release the database lock

            
            if __name__ == "__main__":
                rw = ReaderWriter()
                num_readers = 3
                num_writers = 2

                readers = [threading.Thread(target=rw.reader) for _ in range(num_readers)]
                writers = [threading.Thread(target=rw.writer) for _ in range(num_writers)]

                for reader in readers:
                    reader.start()

                for writer in writers:
                    writer.start()

                for reader in readers:
                    reader.join()

                for writer in writers:
                    writer.join()
            ```

        

- DBMS

    - Theory

        - Candidate keys → unique, primary key → a candidate key which is also not NULL anywhere. Foreign key(maintains referential integrity) → referenced to another table’s primary key. Multiple foreign keys possible but only single primary key.

            - foreign key

                In referenced table,

                1. Insert → no violation possible

                1. Delete → violation possible

                    1. solution 1: on delete→delete other places(cascade)

                    1. solution 2: on delete→set null(can cause problems if foreign key is also primary key)

                
                1. Updation → violation possible

                In referencing table,

                1. Insert → violation possible if referenced table doesn’t have that key

                1. Deletion → no violation possible

                1. Updation → violation possible

            
            - Super keys:

                Super keys → must have **at least** one candidate key + any number of any key

                  

            

        - NoSQL can be horizontally scaled by sharding but SQL cannot. Also, Insert and read are faster on NoSQL but UPDATE and DELETE are faster on SQL

        - ER Model:

            1. 1: 1 model → tables can be reduced and any one of the both table primary key can be the primary key.

            1. 1: many model → tables can be reduced and the side which has unique keys can be primary key

            1. M:N model → tables cannot be reduced and primary key should have be made by combining both of these primary keys

        
        - Normalization

            This is a way to remove redundancy. This is opposite to combining tables as seen in the ER model.

            Prime attributes: attributes used in candidate key, eg candidate key → {AB, BE} ⇒ prime attributes → { A, B, E }

            1 normal form: **single and atomic.** No duplicate entries for any attribute, mixing data types for a column not allowed. Must have primary key

            2 normal form:

            1st normal form and no non prime attribute should be partially dependent (If AB→C, and AB is candidate key. Then, A→C or B→C is wrong but AB→C should only be correct.

            ![[prep/DSA Notes/Private & Shared/Untitled 15.png]]

            3 normal form:

            2nd normal form, and no transitive dependency (only case should be if non prime → non prime. If prime→prime/prime→nonprime/nonprime→prime, then no problem.

            ![[prep/DSA Notes/Private & Shared/Untitled 16.png]]

            BCNF (Boyce Codd Normal Form)

            Must be in 3rd normal form and **For a functional dependency say P->Q, P should be a super key**

            1,2,3 normal forms always ensure dependency preserving decomposition but BCNF doesn’t.

            ![[prep/DSA Notes/Private & Shared/Untitled 17.png]]

            4 normal form:

            BCNF + no multivalued dependency

            ![[prep/DSA Notes/Private & Shared/Untitled 18.png]]

            5 normal form:

            In 4 NF + only lossless decomposition (tables me tod do jitna tod skte)

            ![[prep/DSA Notes/Private & Shared/Untitled 19.png]]

        
        - Functional dependency

            the relationship between two sets of attributes, where one attribute determines the value of another attribute

        
        - See minimal cover

            finding the smallest possible non-redundant set of functionally dependent pairs while maintaining their semantic integrity

        
        - Joins

            Joining two or more tables where some column is common.

            Join ⇒ cross product + some condition

            - Types of joins

                1. Natural joins:

            

        - Views

            View is logical subset of data from one or more tables

            ```sql
            CREATE OR REPLACE VIEW sale_view
            AS
            SELECT * FROM sales WHERE customer = "Alex";
            ```

        
        - Constraints

            For integrity of data in database

            eg, NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, DEFAULT, CHECK

            - check example:

                ```sql
                CREATE TABLE Persons (
                    ID int NOT NULL,
                    LastName varchar(255) NOT NULL,
                    FirstName varchar(255),
                    Age int,
                    CHECK (Age>=18)
                ); 
                ```

            

        - Base is relaxed version of Acid and is for more available, modern db

            - ACID:

                ATOMICITY: Either the whole transaction takes place completely OR everything is rolled back

                Consistency: The db must be consistent before and after the transaction

                Isolation: Multiple transactions can occur independently without interference

                Durability: Changes of a successful transaction occurs even if the system fails after that. (permanent)

            
            - BASE:

                The acronym BASE stands for Basically Available, Soft State, and Eventual Consistency.

                **Basically Available**

                This property refers to the fact that the database system should always be available to respond to user requests, even if it cannot guarantee immediate access to all data. The database may experience brief periods of unavailability, but it should be designed to minimize downtime and provide quick recovery from failures.

                **Soft State**

                This property refers to the fact that the state of the database can change over time, even without any explicit user intervention. This can happen due to the effects of background processes, updates to data, and other factors. The database should be designed to handle this change gracefully, and ensure that it does not lead to data corruption or loss.

                **Eventual Consistency**

                This property refers to the eventual consistency of data in the database, despite changes over time. In other words, the database should eventually converge to a consistent state, even if it takes some time for all updates to propagate and be reflected in the data. This is in contrast to the immediate consistency required by traditional ACID-compliant databases.

            

        - What happens when you run a query

            ![[prep/DSA Notes/Private & Shared/Untitled 20.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 21.png]]

        
        - Concurrency problems:

            - Transactions

                A transaction in a Database Management System (DBMS) is a logical unit of work that performs a series of operations on the data. These operations can involve inserting, updating, or deleting data in the database. A transaction should be ACID compliant.

                ![[prep/DSA Notes/Private & Shared/Untitled 22.png]]

            
            - Steps of transaction

                ![[prep/DSA Notes/Private & Shared/Untitled 23.png]]

            
            - Types of schedule:

                1. Serial schedule: Transactions occur one by one → eg, ATM

                1. Parallel schedule: Multiple transactions can happen at once → eg, online banking

            
            - Schedules:

                - Recoverable schedule

                    Which can be converted into serial schedule

                
                - Cascading vs cascade less

                    If one fails, every other schedule which was dependent on it also fails ← cascading

                
                - Conflict serializable

                    By shifting the non conflict pairs, if the schedules become equivalent to serial.

                
                - View serializable

                    Non conflict serializable but still equivalent to serial

                
                - Shared exclusive lock

                    shared → read allowed

                    exclusive → write allowed

                    Still not very effective

                
                - 2 phase locking(2pl)

                    Growing phase → locks acquired

                    Shrinking phase → locks released

                
                - timestamp ordering protocol

                    generating unique timestamps for transactions and comparing them against stored timestamps related to data items being manipulated

                

            > [!info] Concurrency problems in DBMS Transactions - GeeksforGeeks  
            > A Computer Science portal for geeks.  
            > [https://www.geeksforgeeks.org/concurrency-problems-in-dbms-transactions/](https://www.geeksforgeeks.org/concurrency-problems-in-dbms-transactions/)  

            ![[prep/DSA Notes/Private & Shared/Untitled 24.png]]

        
        - Indexing

            Gold: https://youtu.be/YuRO9-rOgv4

            ![[prep/DSA Notes/Private & Shared/Untitled 25.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 26.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 27.png]]

            In a database, an index is a data structure that facilitates quick access to specific data within a table.

            Types:

            1. Primary : ordered files and key. Sparse.

            1. Clustered: ordered files and non-key. Sparse

            1. Secondary : unordered files (both key and non key). Dense

            1. Multilevel indexing

        
        - Triggers

            ![[prep/DSA Notes/Private & Shared/Untitled 28.png]]

            ![[prep/DSA Notes/Private & Shared/Untitled 29.png]]

        
        - CAP Theorem

            Consistency, Availability, Partition Tolerance

            In a distributed system, you can only have two out of three guarantees across read/write pairs. One of them must be sacrificed.

        

    - SQL

        [https://www.sql-practice.com/](https://www.sql-practice.com/)

        - Important questions

            1. Show patient_id, diagnosis from admissions. Find patients admitted multiple times for the same diagnosis.

            1. Show unique first names from the patients table which only occurs once in the list.

            1. all

        
        [https://www.w3resource.com/sql-exercises/sql-joins-exercises.php](https://www.w3resource.com/sql-exercises/sql-joins-exercises.php)

        - Important example

            Select all records where the value of the `City` column does NOT start with the letter "a".  
            `SELECT * FROM Customers WHERE CITY NOT LIKE 'a%';`

        
        - Wildcards:

            1. `%` is like *, it means 0, 1, or any number of instances

            1. `_` is like %, it means exactly 1

        
        - Between used with `AND` and not `,`

            Use the `BETWEEN` operator to select all the records where the value of the  
            `ProductName` column is alphabetically between 'Geitost' and 'Pavlova'.

              
            `SELECT * FROM Products WHERE ProductName BETWEEN 'Geitost' AND 'Pavlova' ;`

            Between includes both the ends. ‘Geitost’ and ‘Pavlova’ bhi rhenge

        
        - Joins using `USING` instead of `ON table1.column=table2.column`

            ONLY WHEN USING SAME COLUMN TO JOIN

            ```jsx
            SELECT E.name, B.bonus
            FROM Employee E
            LEFT JOIN Bonus B USING(empId)
            WHERE B.bonus<1000 OR B.bonus IS NULL;
            ```

        
        - If you need to use `count`, etc in `where` clause, use `having`

            The `HAVING` clause can be used with aggregate functions such as `COUNT()`, `SUM()`, `AVG()`, etc., while the `WHERE` clause cannot be used with them

            ```sql
            select distinct first_name 
            from patients 
            group by first_name 
            having count(first_name) = 1;
            ```

        
        - concat

            ```sql
            select concat(
            	upper(last_name),
              ',',
              	lower(first_name)
            ) from patients order by first_name desc;
            ```

        
        - IN

            ```sql
            select patient_id, first_name, last_name from patients 
            where patient_id not in (select patient_id from admissions)
            ```

            ```sql
            attending_doctor_id in (1, 5, 19)
            ```

        
        - limit

            ```sql
            SELECT * FROM patients group by height order by height desc limit n-1, 1;
            ```

            This gives the nth largest height. 1 shows the number of columns to print after n-1.

            That syntax doesn't work on some db. You can use offset

            ```sql
            SELECT * FROM patients group by height order by height desc limit 1 offset n-1
            ```

        
        - Window functions

            - ROW_NUMBER()

                ```sql
                SELECT *, ROW_NUMBER() OVER (order by patient_id) FROM patients;
                ```

                This assigns a row number ordered by patient id as 1,2,3… in case there’s no extra column which has auto increment

            
            - RANK()

                You can use the RANK function to see the order of the candidates. If you RANK using (ORDER BY votes DESC) then the candidate with the most votes has rank 1.

                  
                Show the party and RANK for constituency S14000024 in 2017. List the output by party

                ```sql
                SELECT party, votes,
                       RANK() OVER (ORDER BY votes DESC) as posn
                  FROM ge
                 WHERE constituency = 'E14000539' AND yr = 2017
                ORDER BY votes
                ```

            

        - Custom sort

            - Using `UNION ALL`

                Union all will return results in desired order but there might be duplicates

                Q - Sort the province names in ascending order in such a way that the province 'Ontario' is always on top.

                ```sql
                select p1.province_name from province_names as p1 where province_name = 'Ontario'
                union all
                select p2.province_name from province_names as p2 where province_name is not 'Ontario';
                ```

                Note that this won’t work with `UNION` as it will return everything sorted for some reason.

            
            - Using `CASE`

                ```sql
                SELECT province_name
                FROM province_names
                ORDER BY
                  CASE
                    WHEN province_name = 'Ontario' THEN 1
                    ELSE province_name
                  END
                ```

            

        - MySQL has no full join but it has to be emulated using left and right joins

            ```sql
            SELECT * FROM t1
            LEFT JOIN t2 ON t1.id = t2.id
            UNION
            SELECT * FROM t1
            RIGHT JOIN t2 ON t1.id = t2.id
            ```

        
        - If we have to use aggregate functions(like count, sum, avg,etc) in `where` then instead of where, use `having`

            Example - Show the provinces that has more patients identified as 'M' than 'F'. Must only show full province_name

            ```sql
            select province_name 
            from province_names join patients using(province_id) 
            group by province_id 
            having sum(gender = 'M') > sum(gender = 'F') // note sum me aise kr skte
            ```

        

    - Questions

        # I have to manage the school sql database where I have to make queries on what might be the average score of a student in a subject over the years. What table design should be best

        Based on the requirements you provided—calculating the average scores of a student across multiple years within a particular subject—you can utilize the following table schema:

        ```
        CREATE TABLE Students (
            id INT PRIMARY KEY AUTO_INCREMENT, -- unique identifier for each student
            fullname VARCHAR(50) NOT NULL        -- student's full name
        );

        CREATE TABLE Subjects (
            id INT PRIMARY KEY AUTO_INCREMENT,   -- unique identifier for each subject
            title VARCHAR(50) NOT NULL           -- subject title or code
        );

        CREATE TABLE Grades (
            year INT NOT NULL,                   -- academic year when the mark was given
            student_id INT REFERENCES Students(id),     -- foreign key referencing the Students table
            subject_id INT REFERENCES Subjects(id),      -- foreign key referencing the Subjects table
            mark INT NOT NULL               -- actual numerical mark obtained by the student
        );
        ```

        To retrieve the desired information about a student's average score per subject throughout different years, you could run a query similar to these examples:

        ### Calculate average score per student per subject:

        ```sql
        SELECT s.fullname, su.title, AVG(gr.mark) AS `AvgScore`
        FROM Students s
        JOIN Grades gr ON s.id = gr.student_id
        JOIN Subjects su ON gr.subject_id = su.id
        GROUP BY s.id, su.id;
        ```

        This query groups data firstly by student and secondarily by subject while calculating averages accordingly. You may add additional conditions if needed, e.g., filtering only certain dates or ranges.

        ### Filtering by individual student and displaying detailed breakdown:

        If you wish to view details including every record contributing to the overall average, you can modify the previous query slightly:

        ```sql
        SELECT g.*
        FROM Students stu
        JOIN Grades g ON stu.id = g.student_id
        WHERE stu.id = <specificStudentID> AND YEAR(g.year) >= <startYear> AND YEAR(g.year) <= <endYear>;
        ```

        Replace `<specificStudentID>`, `<startYear>`, and `<endYear>` with appropriate parameters matching your needs.

        ---

        # what if the total marks of the subject might change over the years

        When dealing with changing total marks for a subject over the years, you can adapt the existing table designs to accommodate this scenario. One approach is to introduce a separate lookup table for scoring scales used during various periods. Modifying the original solution presented earlier, here's an updated schema considering varying maximum possible grades:

        ```
        -- New table to hold grading scale definitions
        CREATE TABLE ScaleDefinitions (
            id INT PRIMARY KEY AUTO_INCREMENT,
            periodStartDate DATE NOT NULL,       -- Start date of the scaling period
            maxGrade INT NOT NULL                 -- Maximum achievable grade under this scheme
        );

        -- Update 'Grades' table to include reference to Scales
        ALTER TABLE Grades ADD CONSTRAINT FK_Scale FOREIGN KEY (scaleId) REFERENCES ScaleDefinitions(id);

        -- Adjustment to Grade records insertion process
        INSERT INTO Grades (..., scaleId, ...) VALUES (..., (SELECT id FROM ScaleDefinitions WHERE periodStartDate <= '<currentAcademicYear>' ORDER BY periodStartDate DESC LIMIT 1), ...);
        ```

        With this modification, whenever you calculate the average score for a student in a subject, you simply group by both the subject and the current active scale defined in the `ScaleDefinitions` table. Note that you still maintain historical accuracy because the scale references remain intact even though older ones aren't actively applied anymore.

        The modified query to get the average score accounting for variable total marks looks like this:

        ```sql
        SELECT sd.maxGrade, s.fullname, su.title, ROUND(AVG(gr.mark / CAST(sd.maxGrade AS DECIMAL)), 2) AS AvgPercentage
        FROM Students s
        JOIN Grades gr ON s.id = gr.student_id
        JOIN Subjects su ON gr.subject_id = su.id
        JOIN ScaleDefinitions sd ON gr.scaleId = sd.id
        WHERE sd.periodStartDate <= NOW()         -- Only select currently applicable scales
        AND sd.periodStartDate > (CURRENT_DATE - INTERVAL 1 YEAR)  -- Limit scope to past X years
        GROUP BY s.id, su.id, sd.id;
        ```

        You can adjust the filters depending upon whether you want to limit the search range further than just looking back up until now. Also note that dividing raw marks by the corresponding scale's maximal values gives percentages rather than absolute numbers. Replace `ROUND(..., 2)` with whatever precision suits your reporting purposes.

        ---

        # there is no scale but just total marks column too

        If instead of having distinct "scales" as mentioned previously, we consider it more straightforward to directly store the total number of points available for any specific exam session, then we would need to update our tables again according to such constraints. Here are some modifications based on the initial setup without explicit scales:

        ```
        -- Add new columns into the 'Grades' table
        ALTER TABLE Grades ADD COLUMN outOfTotalMarks INT NOT NULL AFTER mark;

        -- Insert sample data using subquery to fetch latest entry from another hypothetical ExamSessions table
        INSERT INTO Grades (outOfTotalMarks, ...) SELECT MAX(totalPointsAvailable), ... FROM ExamSessions WHERE startDateTime <= '<examSessionEndTime>';
        ```

        Now let us assume that all students take their tests at roughly around the same time frame so they share common `outOfTotalMarks`. In case test schedules vary widely among subjects or classes, create one row per combination of Student-Subject-Exam Session Date Time tuple along with its respective Total Marks value. This way, you will always know how many potential points were attainable regardless of changes made later down the line.

        Here's the adjusted SQL statement to compute the weighted average taking account of dynamic totals:

        ```sql
        SELECT SUM(gr.mark * 1.0 / GREATEST(IFNULL(gr.outOfTotalMarks, 1), 1)) / COUNT(*) AS WeightedAvgMark
        FROM Grades gr
        ... /* Additional JOINS & CONDITIONS */
        GROUP BY s.id, su.id;
        ```

        In this example, `GREATEST(IFNULL(gr.outOfTotalMarks, 1), 1)` ensures division doesn't fail due to null entries nor zero denominators – replacing them respectively either with default minimum nonzero integer ('1') or calculated sum itself (if present). The result represents a normalized percentage representation which accounts for fluctuation in point distribution schemes between sessions.

        ---

        # list all the tables in tabular form and give the final query in sql

        Based on the discussion above, assuming you already created the necessary tables beforehand, below is a summary of those tables in tabular format followed by the final SQL query to obtain the required results:

        **Tables:**

        |   |   |   |   |   |
        |---|---|---|---|---|
        |Table Name|Column Names|Data Type|Constraints|Description|
        |**Students**|ID, FullName|int, varchar(50)|PK, Not Null|Unique identifiers and names of students|
        |**Subjects**|ID, Title|int, varchar(50)|PK, Not Null|Identifier and titles of subjects|
        |**Grades**|Year, Student_ID, Subject_ID, OutOfTotalMarks, Mark|int, int, int, int, int|Foreign Keys, Not Null|Academic year, associated student ID, subject ID, total marks available, achieved mark|

        Final Query (considering dynamically changed total marks):

        ```sql
        SELECT s.FullName, su.Title,
               ROUND(SUM(gr.Mark * 1.0 / GREATEST(IFNULL(gr.OutOfTotalMarks, 1), 1)) / COUNT(*), 2) AS NormalizedWeightedAvgMark
        FROM Students s
        JOIN Grades gr ON s.ID = gr.Student_ID
        JOIN Subjects su ON gr.Subject_ID = su.ID
        GROUP BY s.ID, su.ID;
        ```

        Note: Ensure proper index creation on relevant fields to improve performance especially since joining large datasets together often requires efficient access methods. Additionally, replace placeholders ("...") with other criteria specified in your question context regarding limiting scopes etc.

        ---

        # what would be the primary key in grades table

        Considering the requirement discussed earlier, the most suitable candidate for the primary key in the `Grades` table would likely be a compound (composite) primary key consisting of the combined columns `Year`, `Student_ID`, `Subject_ID`, and potentially `OutOfTotalMarks` (depending on whether you treat each instance of testing differently despite identical combinations of student, subject, and year).

        Using a natural key composed of several columns allows maintaining integrity and avoiding redundancy better compared to adding surrogate autoincremental integers. So, the revised definition of the `Grades` table would look something like this:

        ```
        CREATE TABLE Grades (
            Year INT NOT NULL,
            Student_ID INT NOT NULL,
            Subject_ID INT NOT NULL,
            OutOfTotalMarks INT NOT NULL,
            Mark INT NOT NULL,
            PRIMARY KEY (Year, Student_ID, Subject_ID, OutOfTotalMarks)
        );
        ```

        And finally, adapting the last query shared in response to your prior questions:

        ```sql
        SELECT s.FullName, su.Title,
               ROUND(SUM(gr.Mark * 1.0 / GREATEST(IFNULL(gr.OutOfTotalMarks, 1), 1)) / COUNT(*), 2) AS NormalizedWeightedAvgMark
        FROM Students s
        JOIN Grades gr USING (Student_ID)
        JOIN Subjects su USING (Subject_ID)
        GROUP BY s.ID, su.ID;
        ```

        Remember to substitute real table and column names appropriately!

        ---

        # what would be the query if I have to find avg grade per year. avg grade means marks of all subject / total marks of all subjects

        like:  
        FullName | year | avg_grade

        To find the average grade per year, you can modify the previous query to include the year column in the SELECT clause and group by year. Here's the revised SQL query:

        ```sql
        SELECT s.FullName, YEAR(gr.Year) AS year,
               ROUND(SUM(gr.Mark * 1.0 / GREATEST(IFNULL(gr.OutOfTotalMarks, 1), 1)) / COUNT(*) / COUNT(DISTINCT su.ID), 2) AS AvgGrade
        FROM Students s
        JOIN Grades gr ON s.ID = gr.Student_ID
        JOIN Subjects su ON gr.Subject_ID = su.ID
        GROUP BY YEAR(gr.Year), s.ID;
        ```

        This query calculates the average grade by dividing the sum of marks obtained by the total marks available for all subjects in a year, then normalizing it to a percentage. The `ROUND` function is used to round the result to two decimal places for better readability.

        Note that this query assumes that each student has at least one record in the `Grades` table for each year they are enrolled. If there are cases where a student does not have any records in a given year, you may need to handle those cases separately or adjust the query accordingly.

        [https://www.perplexity.ai/search/I-have-to-5VBwKQZjS_mi03cI4nRIBg](https://www.perplexity.ai/search/I-have-to-5VBwKQZjS_mi03cI4nRIBg)

        - Intuit question

            You have a student table. You have to add a phone number column to the database now. Each student can have multiple phone numbers and each phone number can belong to multiple students. How to do that?

            Query: Find all student name with a phone number = 123

            ```sql
            ''' 
            We can have add phone number in another table:
            ______________________________
            |student_id | phone_number|
            ------------------------------
            |student 1     | 123         |
            |student 1     | 456         |
            |student 2     | 123         |
            |student 3     | 789         |
            ------------------------------

            primary key = combining both student_id and phone_number
            '''
            SELECT name 
            FROM students AS st 
            JOIN phone_table AS pt
            ON st.student_id = pt.student_id
            WHERE phone_number = 123;
            ```

        

- CN

    - Ethernet: 802.2 and 802.3 : CSMA C/D

        Data link layer and physical layer

    
    - Wifi: 802.11 :

        CSMA C/A

        Hidden and exposed terminal problem: RTS and CTS (request to send and clear to send): This is called MACA solution Mutliple access with collision avoidance

    
    - Bluetooth: 802.15.1

    - TCP

        1. Connection Estabilishment - 3 way handshake (Syn - (syn+ack) - ack)

            They also tell their respective window size

            ![[prep/DSA Notes/Private & Shared/Untitled 30.png]]

        
        1. Connection Termination - 4 way handshake

            ![[prep/DSA Notes/Private & Shared/Untitled 31.png]]

            4 way handshake is required because tcp can be imagined as full duplex mode of communication. Now when client requests to finish, the server might not have finished sending data. Once the server finishes sending data, it sends the FIN packet and after ack, the connection is terminated.

        

    - UDP (user datagram protocol)

        Following implementations uses UDP as a transport layer protocol:

        - NTP (Network Time Protocol)

        - DNS (Domain Name Service)

        - BOOTP, DHCP.

          

        - UDP depends on IP and ICMP for error reporting

        - It is a suitable protocol for multicasting as UDP supports packet switching.

    
    - ARP and RARP (reverse address resolution protocol)

        ARP → ip to mac

        RARP → mac to ip

    
    - ICMP (Internet Control Message Protocol)

        Connection-less protocol. Used for error handling and request & reply. Above IP in Network layer. Usually the first packet to be discarded in case of congestion. Ping and traceroute uses ICMP.

    
    - NAT (network address Translation)

        Private to public ip translation. Also does port translation.

    
    - DHCP (Dynamic host config protocol)

        helps allocate ip addresses for an organization

    
    - Circuit vs packet switching

        Circuit - pehle se path banana pada. change routing → recalculate path beforehand

        packet - independently jaate. change routing → automatically update path

    
    - QOS

        - Traffic shaping: Leaky bucket, token bucket - network layer

        - Flow control: Stop and wait, sliding window(go back n arq, selective repeat) - data link layer

        - Congestion control: TCP congestion control → (slow start, congestion avoidance, congestion detection) (additive increase multiplicative decrease) network layer

    
    - Anycast: nearest node from a group of nodes

    - Class-full addressing:

        - 0-127: Class A

        - 128-191: Class B

        - 192-223: Class C

        - 223-239: Class D

        - 240-255: Class E

    
    - A diskless [workstation](https://www.webopedia.com/definitions/workstation/) or PC on a _[local-area network (LAN)](https://www.webopedia.com/definitions/lan/)_ is a [computer](https://www.webopedia.com/definitions/computer/) system that does not have its own [disk](https://www.webopedia.com/definitions/disk/). Instead, it [stores](https://www.webopedia.com/definitions/store/) [files](https://www.webopedia.com/definitions/file/) on a [network](https://www.webopedia.com/definitions/network/) [file server](https://www.webopedia.com/definitions/server/) and boots from network(BOOTP)

    - HTTPS → TLS(Transport layer security) OR SSL(secure socket layer, replaced by TLS now)

- Good links

    > [!info] How to store a password in database? - GeeksforGeeks  
    > A Computer Science portal for geeks.  
    > [https://www.geeksforgeeks.org/store-password-database/](https://www.geeksforgeeks.org/store-password-database/)  

    > [!info] What happens when we turn on computer? - GeeksforGeeks  
    > A Computer Science portal for geeks.  
    > [https://www.geeksforgeeks.org/what-happens-when-we-turn-on-computer/](https://www.geeksforgeeks.org/what-happens-when-we-turn-on-computer/)  

    > [!info] Methods in Interprocess Communication - GeeksforGeeks  
    > A Computer Science portal for geeks.  
    > [https://www.geeksforgeeks.org/methods-in-interprocess-communication/](https://www.geeksforgeeks.org/methods-in-interprocess-communication/)  

    > [!info] What Is A Hypervisor?  
    > Something you will likely hear a lot about when accessing information regarding Virtual Private Servers (VPS) is the term ‘hypervisor’.  
    > [https://www.vps.net/blog/hypervisor/](https://www.vps.net/blog/hypervisor/)  

- temp

    testing

    Questions on Software Engineering( go through important software engineering questions ).  
    sdlc dekhlena  
    agile model and ye sab  
    puzzles vagera b puch skte  
    gfg pe commonly asked waale dekhlena ek bar

    The key questions which a liked by this round are,

    - Dynamic Casting,

    - 0 – 1 sorting question with different approaches,

    - Program to get the PID of any running process with a LINUX system,

    - Different kinds of Scheduling and how to convert one process scheduling method to others,  
        Tell me about yourself.  
        Explain your projects.  
        What difficulties you faced during your project implementations.  
        Do you think it’s better to work in a team? Why?  
        How your friends helped you with your progress.  
        Explain How an E-mail travels in the network  
        Why TCP better than UDP? What is flow control and congestion control? How do networks ensure congestion control?

    What is the difference between Router and Bridge and Gateway?

    What is the difference between router and switch?  
    The interviewer asked me about layers in OSI and IP architecture and complete details of application of each layer along with protocols used in them. Then he asked me about the NIC -how it works and the internal implementation. What happens when you connect a pc over a new network. What is CSMA-CD with example.  
    What do you mean by paging  
    What do you mean by thrashing?  
    What do you mean by TCP/IP  
    What is TCP protocol?  
    How connections in TCP protocol made?  
    Where Will you use Flooding Routing Algorithm?  
    How DNS works.  
    Difference between Collision Domain and Broadcast domain.  
    What is VLAN?  
    What is the Difference between EIRGP and OSPF?  
    Explain any Routing algorithm in detail  
    How VPN work?  
    Questions related to AWS Lambda (again as mentioned in resume).  
    Few questions related to projects.  
    What are your strengths and weaknesses? (a typical HR question)  
    Array vs LinkedList ( Same question again )  
    What is DNS? – I explained to them what DNS is also added what forward DNS and reverse DNS is. They seemed very satisfied.  
    They asked me if I wanted to explain any project which I was fond of. I took about 5 mins to explain one of the important projects in detail.  
    Follow-up questions on the project: Some basic questions regarding the technologies used and database.  
    Gave me a scenario if I had a conflict with a co-worker how would I resolve it?  
    Asked me about my other skills and interests: I spoke about my contributions to the clubs I was part of and my leadership roles there.  
    What is Process? and how process is stored in Memory?

    What are the different components in PCB and explain it’s structure?

    Explain Context switch in CPU Scheduling.

    And some basic questions on Paging concept of Memory Management

- VCs

    1. [https://www.sequoiacap.com/](https://www.sequoiacap.com/arc/)

    1. [https://www.industryventures.com/approach/](https://www.industryventures.com/approach/)

    1. [https://greylock.com/](https://greylock.com/)

    1. [https://atomico.com](https://atomico.com/)

    1. [http://dnacapital.com/en/](http://dnacapital.com/en/)

    1. [https://www.ouiwill.com/](https://www.ouiwill.com/)

    1. [https://www.heartcore.com/](https://www.heartcore.com/)

    1. [https://www.bondcap.com/#landing](https://www.bondcap.com/#landing)

    1. [https://foundersfund.com/](https://foundersfund.com/)

    1. [https://lsvp.com/](https://lsvp.com/)

    1. [https://a16z.com](https://a16z.com/)

    1. [https://www.kleinerperkins.com/](https://www.kleinerperkins.com/)

    1. [https://www.intelcapital.com/](https://www.intelcapital.com/)

    1. [https://www.bvp.com/](https://www.bvp.com/)

    1. [https://www.accel.com/](https://www.accel.com/)

    1. [https://www.benchmark.com/](https://www.benchmark.com/)

    1. [https://www.indexventures.com/](https://www.indexventures.com/)

    1. [https://www.generalcatalyst.com/](https://www.generalcatalyst.com/)

    1. [https://nep.com/](https://nep.com/)

    1. [https://www.menlovc.com/](https://www.menlovc.com/)

    1. [https://www.fractalsoftware.com/](https://www.fractalsoftware.com/)

    1. [https://hivemind.capital/](https://hivemind.capital/)

    1. [https://www.5ycap.com/](https://www.5ycap.com/)

    1. [https://addition.com/](https://addition.com/)

    1. [https://www.canaan.com/](https://www.canaan.com/)

    1. [https://greenoaks.com/](https://greenoaks.com/)

    1. [https://firstmarkcap.com/](https://firstmarkcap.com/)

    1. [https://foundercollective.com/index.html](https://foundercollective.com/index.html)

    1. [https://www.ivp.com/](https://www.ivp.com/)

    1. [https://m13.c](https://m13.co/)[ct](https://updata.com/get-in-touch/)[o/](https://m13.co/) ← isme kiya to mail and launchpad

    1. [https://pear.vc/](https://pear.vc/) ← last date was September 30, 2024

    1. [https://updata.com/](https://updata.com/) ← 5-15 mil $ arr requirement