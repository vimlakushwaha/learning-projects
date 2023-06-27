class Person{
    constructor(name,age){
        this.name=name;
        this.age =age;
    }
}
class Employee extends Person{
    constructor(name,age,role,contact){
        super(name,age);
        this.role = role;
        this.contact = contact;
    }
    getDetails(){
        console.log('Name: '+this.name+'\nAge: '+this.age+'\nRole:'+this.age+'\nContact: '+this.contact);
        console.log(`Name: ${this.name}, \nAge: ${this.age}`);
    }
}
obj = new Employee('Beron', 24, 'Technology Analyst', 9001234567);
obj.getDetails();