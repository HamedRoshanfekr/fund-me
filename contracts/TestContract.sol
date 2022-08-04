// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract TestContract {
    constructor () {

    }

    function hello() public pure returns (string memory) {
        return "Hello!";
    }

    function howdy (string memory who) public pure returns (string memory) {
        return string(string.concat("Howdy! ", who));
    }
}

