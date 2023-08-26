// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.5.0 <0.7.0;

contract Transfers {

    function transferEth(address payable recipient, uint256 amount) public payable{
        require(amount<=address(this).balance ,"insufficeint balance");
        
        bool succes = recipient.send(amount);
        require(succes,"transfer failed");
}
}