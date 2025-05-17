class BankAccount {
    int accountNumber;
    String accountHolder;
    long balance;

    public BankAccount( String accountHolder, long balance) {
        this.accountNumber = (int) Math.floor(Math.random()*10000 );
        this.accountHolder = accountHolder;
        this.balance = balance;

    }

    public void depositMoney(long money){
        balance+=money;
    }

    public void withdrawMoney(long money){
        balance-=money;
    }

    public void displayInformation(){
        System.out.println(" Account Holder Name : "+ accountHolder );
        System.out.println(" Account Number : " + accountNumber);
        System.out.println(" Balance : " + balance);
    }
}


public class Main {

    public static void main(String[] args) {

        BankAccount warner = new BankAccount("David Andrew Warner" , 0);

        warner.depositMoney(89);
        warner.withdrawMoney(1);
        warner.displayInformation();

    }
}



