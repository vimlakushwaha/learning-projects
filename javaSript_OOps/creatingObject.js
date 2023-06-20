// learning javascript classes .. it's woring and functionality

class claculator{
    constructor(num1,num2){
        this.num1 = num1;
        this.num2 = num2;
    }

    add(){
        return this.num1 + this.num2;
    }
    sub(){
        return(this.num1  - this.num2);
    }
}
let calculator = new claculator(300, 100);

console.log("addtion  calciulator : " + calculator.add() + "Subtraction is: " + calculator.sub());