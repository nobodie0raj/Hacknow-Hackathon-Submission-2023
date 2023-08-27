# HackNow-Hackathon-Submission-2023
![Black Elegant Personal LinkedIn Banner (2)](https://github.com/IEEE-CS-GHRCE/Hacknow-Hackathon-Submission-2023/assets/139680254/dac49653-9ab8-42ea-bb6d-758d832b29e8)

# Please Fork this Repository
## Github Guidelins
* Repository must be public. 
* Must include readme file in it having summary of your project. 
* Participants to write clear and descriptive Line of code. 
* Stress the importance of documenting the code, including inline comments and high-level documentation Clearly communicate the deadline for submitting your projects.
* Upload all your Project files in This repository
  

# Format of README file
* Team Name : Tech Titans
* Members Name : Rajnand Bhardwaj, Kaustubh Saraf, Kartik Gile, Prince Mathukiya
* Description : [Description]
* Please add Steps : How to Run the Program with Commands.

# Auction DApp - User Guide

Welcome to the Auction DApp project! This guide will help you set up and run the decentralized auction application on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Node.js and npm (Node Package Manager)
- Truffle
- Ganache (or any Ethereum-compatible blockchain network)
- Web3.js

## Steps to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/auction-dapp.git
   cd auction-dapp

2. **Install Dependencies:**

Navigate to the project folder and install the required dependencies:

```bash
npm install
```

3. **Start Ganache:**

Start your local Ethereum blockchain network using Ganache or a similar tool. Make sure it's running on http://127.0.0.1:7545.

3. **Compile and Deploy Smart Contracts:**

Open a new terminal window and run the following commands to compile and deploy the smart contracts:

```bash
truffle compile
truffle migrate
```

4. **Configure Web3.js:**

Open the app.js file in the src directory. Make sure to update the Web3 provider URL to point to your Ganache instance:

```javascript
const web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:7545"));
```

5. **Start the Frontend:**

Open a terminal window and run the following command to start the frontend development server:

```bash
npm run dev
```

6. **Access the Auction DApp:**

Open your web browser and go to http://localhost:3000 to access the Auction DApp. You can participate in auctions, view ongoing/upcoming auctions, and bid on items securely using blockchain technology.

7. **Interact with the Smart Contracts:**

Inside the truffle console, you can interact with the deployed smart contracts:

```bash
truffle console
```
For example, to get the total supply of tokens:

```javascript
let instance = await Token.deployed();
let totalSupply = await instance.totalSupply();
console.log("Total Supply:", totalSupply.toString());
Additional Notes
Ensure that you have Metamask or another Ethereum wallet extension installed in your browser to interact with the DApp.
Make sure to fund your wallet addresses on Ganache to place bids and participate in auctions.
```
# Additional Notes
## Ensure that you have Metamask or another Ethereum wallet extension installed in your browser to interact with the DApp.
Make sure to fund your wallet addresses on Ganache to place bids and participate in auctions.
Enjoy using the Auction DApp!
