import web3
import pyetherbalance as peb

url = 'HTTP://127.0.0.1:7545'
ethbalance = peb.PyEtherBalance(url)


eth_address_pub = ['0xB0da0323e3d10f0faEC5d714d64f282396b8cEB4','0xA6b716d458EE2bEdB4d6aC008f1aCC5a22A0B9E4','0x660e6162E3320bFb2eC0818A8D3DfD79DC40173D']
eth_address_pri = ['0xb805e2337d77cffbb008115c2154987a6b110c50814d542ac95654f85ad5c296','0x279896bfb5b44b4a0f6333e6bfbe5290b10d74c5f5bd4554569bc07d70aacd0f','0xa03104f4bae2f8921b80c6d542c26731eda12a695d452f6f6598dc0586e34506']

Items = {"Gshock":5,"Lambo":10,"If you know you know":69}

Bids = [{'0xB0da0323e3d10f0faEC5d714d64f282396b8cEB4':10,'0xA6b716d458EE2bEdB4d6aC008f1aCC5a22A0B9E4':11},{'0xA6b716d458EE2bEdB4d6aC008f1aCC5a22A0B9E4':25}]
# balance_eth_1 = ethbalance.get_eth_balance(ethereum_address_1)
# print("Wallet Balance 1 : ",balance_eth_1['balance'])

# ethereum_address_2 = '0xA6b716d458EE2bEdB4d6aC008f1aCC5a22A0B9E4' #public key
# balance_eth_2 = ethbalance.get_eth_balance(ethereum_address_2)
# print("Wallet Balance 2 : ",balance_eth_2['balance'])



def checkbal():
    acc = int(input("Enter account serial no. : "))

    bal = ethbalance.get_eth_balance(eth_address_pub[acc])
    print("Wallet id :",acc,"\nBalance :",bal['balance'] )
    return bal['balance']

def add_item():
    item = input("Enter the item name : ")
    base = int(input('enter the base amount : '))
    items[item] = base
    print("New item added successfully")

def bid():
    for i,item,base in enumerate(Items):
        print(f"Item {i} : {item}")
        print(f"base bid : {base}\n")
    
    ch = int(input("Choose one to bid : "))
    
    while True:
        bid_amount = int(input("Enter your bidding amount : "))
        if bid_amount < Items[Items.values()[ch-1]]:
            print("Invalid value, enter higher bid.")
        elif bid_amount > checkbal():
            print("You don't have enough to spend from your wallet, please try again with different account.")
        else:
            print("Bid placed successfully")
            break

def main(){
    while True:
        print("1 - Check balance \n2 - Add Item to Bid \n3 - Bid Amount");
        
        ch = int(input("Choose Option : "))

        if ch == 1:
            # acc = int(input("Enter account serial no. : "))
            checkbal(acc)
        elif ch == 2:
            add_item()
        elif ch == 3:
            
}   