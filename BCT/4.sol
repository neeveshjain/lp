// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        string name;
        uint256 rollNumber;
        uint256 age;
    }

    Student[] public students;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this operation");
        _;
    }

    function addStudent(string memory _name, uint256 _rollNumber, uint256 _age) public onlyOwner {
        Student memory newStudent = Student(_name, _rollNumber, _age);
        students.push(newStudent);
    }

    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    function getStudent(uint256 index) public view returns (string memory, uint256, uint256) {
        require(index < students.length, "Invalid index");
        Student memory student = students[index];
        return (student.name, student.rollNumber, student.age);
    }

    fallback() external {
        revert("Fallback function: This contract does not accept Ether.");
    }
}